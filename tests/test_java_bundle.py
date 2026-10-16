"""Regression fixtures for the contents of a Maven Central deployment ZIP."""

import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from check_java_bundle import check_bundle

CONFIG = {"packages": {"javaGroup": "com.example", "javaArtifact": "sdk"}, "releaseVersion": "1.2.3"}
PREFIX = "com/example/sdk/1.2.3/"
STEM = "sdk-1.2.3"


def pom(group="com.example", artifact="sdk", version="1.2.3"):
    return (f'<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>'
            f'<groupId>{group}</groupId><artifactId>{artifact}</artifactId><version>{version}</version></project>')


class JavaBundle(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.bundle = Path(self.temp.name) / "central-bundle.zip"
        self.files = {PREFIX + STEM + suffix: b"jar" for suffix in (".jar", "-sources.jar", "-javadoc.jar")}
        self.files[PREFIX + STEM + ".pom"] = pom()

    def validate(self):
        with ZipFile(self.bundle, "w") as archive:
            for name, body in self.files.items():
                archive.writestr(name, body)
        check_bundle(self.bundle, CONFIG)

    def test_unsigned_bundle_and_optional_tests_signatures_checksums_are_accepted(self):
        self.validate()
        self.files[PREFIX + STEM + "-tests.jar"] = b"tests"
        self.files[PREFIX + STEM + ".jar.asc"] = b"signature"
        self.files[PREFIX + STEM + ".jar.asc.sha256"] = b"checksum"
        self.files[PREFIX + STEM + ".pom.md5"] = b"checksum"
        self.validate()

    def test_metadata_at_artifact_or_version_root_is_rejected(self):
        for name in ("maven-metadata.xml", "maven-metadata-local.xml", "_remote.repositories"):
            for directory in ("com/example/sdk/", PREFIX):
                with self.subTest(name=name, directory=directory):
                    path = directory + name
                    self.files[path] = b"local metadata"
                    with self.assertRaisesRegex(ValueError, "Local Maven metadata"):
                        self.validate()
                    del self.files[path]

    def test_files_outside_version_directory_are_rejected(self):
        for path in ("com/example/sdk/1.2.2/sdk-1.2.2.jar", "com/example/sdk/.locks/deploy.lock"):
            with self.subTest(path=path):
                self.files[path] = b"unexpected file"
                with self.assertRaisesRegex(ValueError, "outside the configured version directory"):
                    self.validate()
                del self.files[path]

    def test_missing_pom_is_rejected(self):
        del self.files[PREFIX + STEM + ".pom"]
        with self.assertRaisesRegex(ValueError, "Missing required artifacts.*sdk-1.2.3.pom"):
            self.validate()

    def test_wrong_pom_gav_is_rejected(self):
        for replacement in ({"group": "org.other"}, {"artifact": "other-sdk"}, {"version": "9.9.9"}):
            with self.subTest(replacement=replacement):
                self.files[PREFIX + STEM + ".pom"] = pom(**replacement)
                with self.assertRaisesRegex(ValueError, "POM GAV differs"):
                    self.validate()


if __name__ == "__main__":
    unittest.main()
