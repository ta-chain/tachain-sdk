#!/usr/bin/env python3
"""Extract the public integration API from a full Tactic Chain OpenAPI export."""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path

METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
PUBLIC_PREFIX = "/v1/"
REF_PREFIX = "#/components/"


def walk_refs(value: object) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "$ref" and isinstance(item, str):
                refs.add(item)
            else:
                refs.update(walk_refs(item))
    elif isinstance(value, list):
        for item in value:
            refs.update(walk_refs(item))
    return refs


def fix_invalid_null_type(value: object) -> None:
    """The upstream 3.0 export contains one 3.1-only `type: null` schema."""
    if isinstance(value, dict):
        if value.get("type") == "null":
            del value["type"]
            value["nullable"] = True
        for item in value.values():
            fix_invalid_null_type(item)
    elif isinstance(value, list):
        for item in value:
            fix_invalid_null_type(item)


def operation_id(method: str, path: str) -> str:
    segments = re.findall(r"[A-Za-z0-9]+", path)
    return method.lower() + "".join(segment[:1].upper() + segment[1:] for segment in segments)


def normalize(source: dict) -> dict:
    if not str(source.get("openapi", "")).startswith("3."):
        raise ValueError("An OpenAPI 3 document is required")
    source_paths = source.get("paths")
    if not isinstance(source_paths, dict):
        raise ValueError("Missing paths")

    paths: dict[str, dict] = {}
    ids: set[str] = set()
    for path in sorted(source_paths):
        if not path.startswith(PUBLIC_PREFIX):
            continue
        path_item = source_paths[path]
        if not isinstance(path_item, dict):
            raise ValueError(f"Invalid path item: {path}")
        selected = {key: copy.deepcopy(value) for key, value in path_item.items() if key not in METHODS}
        for method in sorted(METHODS & path_item.keys()):
            operation = copy.deepcopy(path_item[method])
            name = operation_id(method, path)
            if name in ids:
                raise ValueError(f"Duplicate operationId: {name}")
            ids.add(name)
            operation["operationId"] = name
            # Keep a single controller tag, so every generator groups the same way.
            tags = operation.get("tags") or []
            operation["tags"] = [next((tag for tag in tags if not tag.startswith("SwaggerApi/")), path.split("/")[2])]
            operation["security"] = [
                {"BearerToken": []},
                {"ApiKey": [], "Timestamp": [], "Signature": []},
            ]
            parameters = operation.setdefault("parameters", [])
            if not any(p.get("name", "").lower() == "x-credential-type" and p.get("in") == "header" for p in parameters if isinstance(p, dict)):
                parameters.append({
                    "name": "X-Credential-Type",
                    "in": "header",
                    "required": True,
                    "description": "Use 'Token' with bearer authorization, or 'API Key' with signed API key headers. This header is mandatory in the deployed API.",
                    "schema": {"type": "string", "enum": ["Token", "API Key"]},
                })
            selected[method] = operation
        if any(key in selected for key in METHODS):
            paths[path] = selected

    if not paths:
        raise ValueError("No public /v1/ operations were found")

    # Only retain components reachable from public operations. The source export
    # also contains private management API models and unrelated examples.
    components = source.get("components", {})
    retained: dict[str, dict] = {}
    pending = list(walk_refs(paths))
    seen: set[str] = set()
    while pending:
        ref = pending.pop()
        if ref in seen:
            continue
        seen.add(ref)
        if not ref.startswith(REF_PREFIX):
            raise ValueError(f"External or unsupported reference: {ref}")
        parts = ref[len(REF_PREFIX):].split("/", 1)
        if len(parts) != 2 or not all(parts):
            raise ValueError(f"Malformed component reference: {ref}")
        group, name = parts
        name = name.replace("~1", "/").replace("~0", "~")
        item = components.get(group, {}).get(name)
        if item is None:
            raise ValueError(f"Unresolved reference: {ref}")
        retained.setdefault(group, {})[name] = copy.deepcopy(item)
        pending.extend(walk_refs(item))

    retained = {group: {key: value for key, value in sorted(items.items())} for group, items in sorted(retained.items())}
    retained["securitySchemes"] = {
        "BearerToken": {"type": "http", "scheme": "bearer", "description": "Single Token credential. Also send X-Credential-Type: Token."},
        "ApiKey": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
        "Timestamp": {"type": "apiKey", "in": "header", "name": "X-Timestamp", "description": "Current Unix time in seconds."},
        "Signature": {"type": "apiKey", "in": "header", "name": "X-Signature", "description": "Lowercase hex HMAC-SHA256 of apiKey + timestamp + normalized query string, keyed by the API secret."},
    }
    result = {
        "openapi": source["openapi"],
        "info": {
            "title": "Tactic Chain Public API",
            "version": source.get("info", {}).get("version", "1.0.0"),
            "description": "Public integration endpoints. Set your own base URL and credential before calling.",
        },
        "servers": [{"url": "https://api.example.com", "description": "Replace with your Tactic Chain API base URL"}],
        "paths": paths,
        "components": retained,
    }
    fix_invalid_null_type(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Full backend or exported OpenAPI JSON")
    parser.add_argument("--output", type=Path, default=Path("openapi/tactic-chain-public.json"))
    args = parser.parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    public = normalize(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(public, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    operation_count = sum(sum(key in METHODS for key in item) for item in public["paths"].values())
    print(f"Wrote {operation_count} public operations, {len(public['components'].get('schemas', {}))} schemas to {args.output}")


if __name__ == "__main__":
    main()
