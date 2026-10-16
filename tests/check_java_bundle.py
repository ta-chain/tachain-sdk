#!/usr/bin/env python3
"""Validate a local Maven Central bundle; unsigned artifacts are accepted."""

import argparse
import json
from pathlib import Path, PurePosixPath
import xml.etree.ElementTree as ET
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "generated/java/target/central-publishing/central-bundle.zip"


def check_bundle(bundle: Path, config: dict) -> None:
    group = config["packages"]["javaGroup"]
    artifact = config["packages"]["javaArtifact"]
    version = config["releaseVersion"]
    prefix = f"{group.replace('.', '/')}/{artifact}/{version}/"
    stem = f"{artifact}-{version}"
    required = {f"{stem}{suffix}" for suffix in (".jar", ".pom", "-sources.jar", "-javadoc.jar")}
    artifacts = required | {f"{stem}-tests.jar"}
    allowed = {
        name + signature + checksum
        for name in artifacts
        for signature in ("", ".asc")
        for checksum in ("", ".md5", ".sha1", ".sha256", ".sha512")
    }
    with ZipFile(bundle) as archive:
        files = [entry.filename for entry in archive.infolist() if not entry.is_dir()]
        for name in files:
            basename = PurePosixPath(name).name
            if basename.startswith("maven-metadata") or basename.startswith("_remote.repositories"):
                raise ValueError(f"Local Maven metadata must not be bundled: {name}")
            if not name.startswith(prefix):
                raise ValueError(f"File outside the configured version directory {prefix}: {name}")
            if name[len(prefix):] not in allowed:
                raise ValueError(f"Unexpected artifact in the version directory: {name}")
        missing = required - {name[len(prefix):] for name in files}
        if missing:
            raise ValueError(f"Missing required artifacts: {', '.join(sorted(missing))}")

        pom = ET.fromstring(archive.read(prefix + stem + ".pom"))
        namespace = pom.tag.split("}", 1)[0] + "}" if pom.tag.startswith("{") else ""
        actual = tuple((pom.findtext(namespace + field) or "").strip()
                       for field in ("groupId", "artifactId", "version"))
        expected = (group, artifact, version)
        if actual != expected:
            raise ValueError(f"POM GAV differs: expected {':'.join(expected)}, got {':'.join(actual)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", nargs="?", type=Path, default=DEFAULT_BUNDLE)
    args = parser.parse_args()
    config = json.loads((ROOT / "sdk.config.json").read_text(encoding="utf-8"))
    try:
        check_bundle(args.bundle, config)
    except (OSError, BadZipFile, ET.ParseError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Java Central bundle matches {config['packages']['javaGroup']}:{config['packages']['javaArtifact']}:{config['releaseVersion']}: {args.bundle}")


if __name__ == "__main__":
    main()
