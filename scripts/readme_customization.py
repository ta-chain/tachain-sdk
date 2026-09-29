"""Make generated SDK READMEs point to buildable source checkouts."""

from pathlib import Path


def replace_section(body: str, start: str, end: str, replacement: str) -> str:
    """Replace a pinned generator section and flag upstream template changes."""
    if body.count(start) != 1 or body.count(end) != 1:
        raise ValueError(f"Generated README section changed: {start.strip()}")
    before, rest = body.split(start, 1)
    _, after = rest.split(end, 1)
    return before + replacement + end + after


def customize_readme(output: Path, language: str, config: dict) -> None:
    owner = config["githubOwner"]
    main_name = config["githubRepository"]
    main_repo = f"https://github.com/{owner}/{main_name}"
    split = config["splitRepositories"]
    repository_name = split.get(language, main_name)
    repository = f"https://github.com/{owner}/{repository_name}"
    checkout_dir = repository_name if language in split else f"{main_name}/generated/{language}"
    version = config["releaseVersion"]
    build = {
        "typescript": "npm install --no-audit --no-fund\nnpm run build",
        "python": "python3 -m pip install .",
        "java": "mvn -B clean install",
        "csharp": "dotnet build src/Tachain.Sdk/Tachain.Sdk.csproj -c Release",
        "go": "go test ./...",
        "php": "composer install --no-interaction --prefer-dist",
        "ruby": "gem build tachain-sdk.gemspec",
        "swift": "swift build",
    }[language]
    readme = output / "README.md"
    body = readme.read_text(encoding="utf-8")

    if language == "python":
        body = replace_section(
            body, "### pip install\n", "### Setuptools\n",
            f"### pip install\n\nInstall the published version:\n\n"
            f"~~~sh\npython3 -m pip install tachain-sdk=={version}\n~~~\n\n"
            "For a source build, use the checkout steps above.\n\n",
        )
    elif language == "go":
        old_import = f'import tachainsdk "github.com/{owner}/{main_name}"'
        if body.count(old_import) != 1:
            raise ValueError("Generated Go README import path changed")
        body = body.replace(old_import, f'import tachainsdk "{config["packages"]["goModule"]}"')
    elif language == "php":
        body = replace_section(
            body, "### Composer\n", "### Manual Installation\n",
            f"### Composer\n\nInstall version {version} from Packagist:\n\n"
            f"~~~sh\ncomposer require {config['packages']['php']}:{version}\n~~~\n\n"
            f"Composer obtains the source from the [standalone PHP repository]({repository}).\n\n",
        )
    elif language == "ruby":
        body = replace_section(
            body, "### Install from Git\n", "### Include the Ruby code directly\n",
            "### Install from Git\n\nClone the source repository and build the gem "
            "from generated/ruby using the commands above.\n\n",
        )
    elif language == "swift":
        if body.count("- Package version: \n") != 1:
            raise ValueError("Generated Swift README version line changed")
        body = body.replace("- Package version: \n", f"- Package version: {version}\n", 1)
        body = replace_section(
            body, "## Installation\n", "## Documentation for API Endpoints\n",
            "## Installation\n\n### Swift Package Manager\n\n"
            f"Add the [standalone Swift repository]({repository}) as a package dependency:\n\n"
            f"~~~swift\n.package(url: \"{repository}.git\", from: \"{version}\")\n~~~\n\n"
            "Add the TachainSDK library product to your target.\n\n",
        )
    elif language == "csharp":
        body = replace_section(
            body, "## Installation\n", '<a id="packaging"></a>\n',
            "## Installation\n\nBuild the .NET 8 project from this SDK directory:\n\n"
            "~~~sh\ndotnet build src/Tachain.Sdk/Tachain.Sdk.csproj -c Release\n~~~\n\n"
            "The DLL is written under src/Tachain.Sdk/bin/Release/net8.0/.\n\n",
        )
        body = replace_section(
            body, "## Packaging\n", '<a id="usage"></a>\n',
            "## Packaging\n\nCreate a local NuGet package from this SDK directory:\n\n"
            "~~~sh\ndotnet pack src/Tachain.Sdk/Tachain.Sdk.csproj -c Release -o out\n~~~\n\n",
        )

    if language in split:
        source_note = (
            f"This package is distributed from its [standalone source repository]({repository}). "
            f"Its generated code is also maintained in the "
            f"[SDK monorepo]({main_repo}/tree/main/generated/{language})."
        )
    else:
        source_note = (
            f"This SDK is in the [generated/{language} directory]"
            f"({main_repo}/tree/main/generated/{language}) of the "
            f"[open-source SDK repository]({main_repo})."
        )
    platform_note = "Run this build on macOS.\n\n" if language == "swift" else ""
    source_block = (
        "## Source repository and local build\n\n"
        f"{source_note}\n\n{platform_note}"
        "~~~sh\n"
        f"git clone {repository}.git\n"
        f"cd {checkout_dir}\n"
        f"{build}\n"
        "~~~\n"
    )
    heading = body.find("\n## ")
    if heading < 0:
        raise ValueError(f"Generated {language} README has no section heading")
    body = body[:heading] + "\n" + source_block + body[heading:]
    if language == "csharp":
        body = body.replace('<a id="frameworks-supported"></a>\n', "", 1)
        body = body.replace(
            "## Frameworks supported",
            '<a id="frameworks-supported"></a>\n## Frameworks supported',
            1,
        )
    readme.write_text(body, encoding="utf-8")
