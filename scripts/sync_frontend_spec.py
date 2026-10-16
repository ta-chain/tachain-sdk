#!/usr/bin/env python3
"""Sync the public SDK contract and release metadata to the sibling frontend."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "openapi" / "tactic-chain-public.json"
CONFIG = ROOT / "sdk.config.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frontend-root", type=Path, default=ROOT.parent / "tactic-chain-frontend")
    parser.add_argument("--check", action="store_true", help="Only compare files; do not write")
    args = parser.parse_args()
    target = args.frontend_root / "public" / "openapi" / "tactic-chain-public.json"
    release_target = args.frontend_root / "src" / "features" / "integration" / "sdk" / "release.json"
    if not SOURCE.is_file():
        parser.error(f"SDK contract missing: {SOURCE}")
    if not (args.frontend_root / "package.json").is_file():
        parser.error(f"Frontend project not found: {args.frontend_root}")
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    release = {key: config[key] for key in ("releaseVersion", "generatorVersion")}
    if args.check:
        if not target.is_file() or digest(target) != digest(SOURCE):
            parser.error(f"Frontend contract differs: {target}")
        try:
            current_release = json.loads(release_target.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            parser.error(f"Frontend SDK release metadata missing or invalid: {release_target}")
        if current_release != release:
            parser.error(f"Frontend SDK release metadata differs: {release_target}")
        print(f"Frontend contract matches: {target}")
        print(f"Frontend SDK release metadata matches: {release_target}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    release_target.parent.mkdir(parents=True, exist_ok=True)
    release_target.write_text(json.dumps(release, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Synced public OpenAPI contract to {target}")
    print(f"Synced SDK release metadata to {release_target}")


if __name__ == "__main__":
    main()
