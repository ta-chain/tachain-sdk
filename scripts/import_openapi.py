#!/usr/bin/env python3
"""Import a full export while keeping only public API material in this repo."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from normalize_openapi import PUBLIC_PREFIX, normalize


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path, help="Full upstream OpenAPI JSON; kept outside this repo")
    parser.add_argument("--output", type=Path, default=Path("source/openapi.json"))
    args = parser.parse_args()
    raw = json.loads(args.export.read_text(encoding="utf-8"))
    public = normalize(raw)
    source = copy.deepcopy(raw)
    source["paths"] = {
        path: item for path, item in raw["paths"].items()
        if path.startswith(PUBLIC_PREFIX)
    }
    source["components"] = {
        group: {
            name: copy.deepcopy(raw["components"][group][name])
            for name in items
        }
        for group, items in public["components"].items()
        if group != "securitySchemes"
    }
    selected_tags = {
        tag for item in source["paths"].values()
        for operation in item.values() if isinstance(operation, dict)
        for tag in operation.get("tags", [])
    }
    if "tags" in source:
        source["tags"] = [tag for tag in raw["tags"] if tag.get("name") in selected_tags]
    # The normalized public contract must remain byte-identical after filtering.
    if normalize(source) != public:
        raise ValueError("Filtered source changed the public contract")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(source['paths'])} public paths and {len(source['components'].get('schemas', {}))} schemas to {args.output}")


if __name__ == "__main__":
    main()
