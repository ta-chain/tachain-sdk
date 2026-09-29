"""Validate manual release inputs and pass the selected SDKs to publish jobs."""

import json
import os
import re
from pathlib import Path


LANGUAGES = ("typescript", "python", "java", "csharp", "go", "php", "ruby", "swift")
ROOT = Path(__file__).resolve().parents[1]


def select_languages(inputs: dict[str, object]) -> list[str]:
    for name in ("all", *LANGUAGES):
        if type(inputs.get(name)) is not bool:
            raise ValueError(f"Release selection {name} must be a checkbox value")

    selected = [name for name in LANGUAGES if inputs[name]]
    if inputs["all"]:
        if selected:
            raise ValueError("Select either all or individual SDKs, not both")
        return list(LANGUAGES)
    if not selected:
        raise ValueError("Select all or at least one SDK to publish")
    return selected


def main() -> None:
    inputs = json.loads(os.environ["RELEASE_INPUTS"])
    if not isinstance(inputs, dict):
        raise SystemExit("Release inputs must be a JSON object")

    version = inputs.get("version")
    configured = json.loads((ROOT / "sdk.config.json").read_text(encoding="utf-8"))["releaseVersion"]
    if os.environ["RELEASE_REF"] != "refs/heads/main":
        raise SystemExit("Publish only from the main branch")
    if inputs.get("confirm") != "publish":
        raise SystemExit("Enter publish in the confirm field")
    if not isinstance(version, str) or not re.fullmatch(
        r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?", version
    ):
        raise SystemExit("Version must be a semantic version without the v prefix")
    if version != configured:
        raise SystemExit(f"Input version {version} differs from sdk.config.json {configured}")

    try:
        selected = select_languages(inputs)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    split_languages = [name for name in selected if name in ("php", "swift")]
    with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as output:
        output.write(f"languages={json.dumps(selected, separators=(',', ':'))}\n")
        output.write(f"split_languages={json.dumps(split_languages, separators=(',', ':'))}\n")
    print(f"Publishing: {', '.join(selected)}")


if __name__ == "__main__":
    main()
