#!/usr/bin/env python3
"""Copy the public SDK contract to the sibling frontend documentation assets."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "openapi" / "tactic-chain-public.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frontend-root", type=Path, default=ROOT.parent / "tactic-chain-frontend")
    parser.add_argument("--check", action="store_true", help="Only compare files; do not write")
    args = parser.parse_args()
    target = args.frontend_root / "public" / "openapi" / "tactic-chain-public.json"
    if not SOURCE.is_file():
        parser.error(f"SDK contract missing: {SOURCE}")
    if not (args.frontend_root / "package.json").is_file():
        parser.error(f"Frontend project not found: {args.frontend_root}")
    if args.check:
        if not target.is_file() or digest(target) != digest(SOURCE):
            parser.error(f"Frontend contract differs: {target}")
        print(f"Frontend contract matches: {target}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    print(f"Synced public OpenAPI contract to {target}")


if __name__ == "__main__":
    main()
