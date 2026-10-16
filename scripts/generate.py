#!/usr/bin/env python3
"""Pin OpenAPI Generator, normalize the source spec, and generate SDKs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
import uuid
import zipfile
from pathlib import Path

if __package__:
    from .readme_customization import customize_readme
else:
    from readme_customization import customize_readme

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "sdk.config.json").read_text(encoding="utf-8"))
VERSION = CONFIG["generatorVersion"]
JAR = ROOT / ".cache" / f"openapi-generator-cli-{VERSION}.jar"
SPEC = ROOT / "openapi" / "tactic-chain-public.json"
SOURCE = ROOT / "source" / "openapi.json"
GENERATED = ROOT / "generated"
LANGUAGES = ("typescript", "python", "java", "csharp", "go", "php", "ruby", "swift")
JAR_SHA256 = "41ce4f6b07f196676439d710759fa1ced7a08066d06ff1bf314681470289efae"


def run(args: list[str]) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def ensure_jar() -> None:
    if not JAR.is_file():
        JAR.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://repo.maven.apache.org/maven2/org/openapitools/openapi-generator-cli/{VERSION}/openapi-generator-cli-{VERSION}.jar"
        with tempfile.NamedTemporaryFile(dir=JAR.parent, delete=False) as temp:
            temp_path = Path(temp.name)
            with urllib.request.urlopen(url, timeout=60) as response:
                shutil.copyfileobj(response, temp)
        temp_path.replace(JAR)
    if hashlib.sha256(JAR.read_bytes()).hexdigest() != JAR_SHA256:
        raise RuntimeError(f"OpenAPI Generator checksum mismatch: {JAR}")


def settings(language: str) -> tuple[str, dict[str, str]]:
    packages = CONFIG["packages"]
    version = CONFIG["releaseVersion"]
    common = {"hideGenerationTimestamp": "true", "licenseName": "MIT"}
    if language == "typescript":
        return "typescript-fetch", {**common, "npmName": packages["typescript"], "npmVersion": version, "dateLibrary": "string"}
    if language == "python":
        return "python", {**common, "packageName": "tachain_sdk", "projectName": packages["python"], "packageVersion": version}
    if language == "java":
        return "java", {**common, "groupId": packages["javaGroup"], "artifactId": packages["javaArtifact"], "artifactVersion": version, "apiPackage": "com.tachain.sdk.api", "modelPackage": "com.tachain.sdk.model", "invokerPackage": "com.tachain.sdk.client", "library": "okhttp-gson"}
    if language == "csharp":
        return "csharp", {**common, "packageName": packages["csharp"], "packageVersion": version, "targetFramework": "net8.0", "library": "httpclient"}
    if language == "go":
        return "go", {**common, "packageName": "tachainsdk", "packageVersion": version, "withGoMod": "true"}
    if language == "php":
        return "php", {**common, "composerPackageName": packages["php"], "packageName": "TachainSdk", "invokerPackage": "TachainSdk", "artifactVersion": version, "artifactUrl": f"https://github.com/{CONFIG['githubOwner']}/{CONFIG['splitRepositories']['php']}"}
    if language == "ruby":
        return "ruby", {**common, "gemName": packages["ruby"], "gemVersion": version, "moduleName": "TachainSdk"}
    if language == "swift":
        return "swift5", {**common, "projectName": packages["swift"], "useSPMFileStructure": "true", "useClasses": "true", "podVersion": version}
    raise ValueError(language)


def short_model_name(name: str) -> str:
    """Keep RubyGems file paths within its 100-byte filename limit."""
    if name.isdigit():
        return name
    name = re.sub(r"TacticChainApiServiceVersion.*$", "", name)
    name = re.sub(r"SystemPrivateCoreLibVersion.*$", "", name)
    for fragment in (
        "TacticChainApiService", "ViewModelsCommon", "ControllersApiIntegrationV1",
        "ViewModels", "DataEntities", "Models", "Helper",
    ):
        name = name.replace(fragment, "")
    name = name.replace("ApiResponse1", "ApiResponse")
    name = name.replace("PagedResponse1", "PagedResponse")
    name = name.replace("SystemString", "String")
    return name


def customize_java_pom(path: Path, repository: str) -> None:
    namespace = "http://maven.apache.org/POM/4.0.0"
    xsi = "http://www.w3.org/2001/XMLSchema-instance"
    ET.register_namespace("", namespace)
    ET.register_namespace("xsi", xsi)
    q = lambda name: f"{{{namespace}}}{name}"
    tree = ET.parse(path)
    root = tree.getroot()
    root.find(q("url")).text = repository
    root.find(f"{q('scm')}/{q('connection')}").text = f"scm:git:https://github.com/{CONFIG['githubOwner']}/{CONFIG['githubRepository']}.git"
    root.find(f"{q('scm')}/{q('developerConnection')}").text = f"scm:git:ssh://git@github.com/{CONFIG['githubOwner']}/{CONFIG['githubRepository']}.git"
    root.find(f"{q('scm')}/{q('url')}").text = repository
    license_node = root.find(f"{q('licenses')}/{q('license')}")
    license_node.find(q("name")).text = "MIT"
    license_node.find(q("url")).text = "https://opensource.org/license/mit"
    developers = root.find(q("developers"))
    for child in list(developers):
        developers.remove(child)
    developer = ET.SubElement(developers, q("developer"))
    ET.SubElement(developer, q("name")).text = "Tactic Chain contributors"
    ET.SubElement(developer, q("organization")).text = "Tactic Chain"
    ET.SubElement(developer, q("organizationUrl")).text = repository
    plugins = root.find(f"{q('build')}/{q('plugins')}")
    central = ET.SubElement(plugins, q("plugin"))
    ET.SubElement(central, q("groupId")).text = "org.sonatype.central"
    ET.SubElement(central, q("artifactId")).text = "central-publishing-maven-plugin"
    ET.SubElement(central, q("version")).text = "0.9.0"
    ET.SubElement(central, q("extensions")).text = "true"
    config = ET.SubElement(central, q("configuration"))
    ET.SubElement(config, q("publishingServerId")).text = "central"
    ET.SubElement(config, q("autoPublish")).text = "true"
    ET.indent(tree, space="    ")
    tree.write(path, encoding="utf-8", xml_declaration=True)


def customize(output: Path, language: str) -> None:
    repository = f"https://github.com/{CONFIG['githubOwner']}/{CONFIG['githubRepository']}"
    shutil.copyfile(ROOT / "LICENSE", output / "LICENSE")
    if language == "typescript":
        shutil.copyfile(ROOT / "helpers" / "typescript" / "signature.ts", output / "src" / "signature.ts")
        index = output / "src" / "index.ts"
        index.write_text(index.read_text(encoding="utf-8") + "\nexport * from './signature';\n", encoding="utf-8")
        package = output / "package.json"
        metadata = json.loads(package.read_text(encoding="utf-8"))
        metadata["author"] = "Tactic Chain contributors"
        metadata["license"] = "MIT"
        package.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif language == "python":
        shutil.copyfile(ROOT / "helpers" / "python" / "signature.py", output / "tachain_sdk" / "signature.py")
        pyproject = output / "pyproject.toml"
        body = pyproject.read_text(encoding="utf-8")
        body = body.replace('{name = "OpenAPI Generator Community",email = "team@openapitools.org"}', '{name = "Tactic Chain contributors"}')
        body = body.replace("Repository = \"https://github.com/GIT_USER_ID/GIT_REPO_ID\"", f"Repository = \"{repository}\"")
        body = body.replace('readme = "README.md"', 'readme = "README.md"\nlicense = "MIT"')
        pyproject.write_text(body, encoding="utf-8")
        setup = output / "setup.py"
        body = setup.read_text(encoding="utf-8")
        body = body.replace('author="OpenAPI Generator community",', 'author="Tactic Chain contributors",')
        body = body.replace('author_email="team@openapitools.org",', '')
        body = body.replace('url="",', f'url="{repository}",')
        setup.write_text(body, encoding="utf-8")
    elif language == "java":
        shutil.copyfile(ROOT / "helpers" / "java" / "SignatureInterceptor.java", output / "src" / "main" / "java" / "com" / "tachain" / "sdk" / "client" / "SignatureInterceptor.java")
        test_dir = output / "src" / "test" / "java" / "com" / "tachain" / "sdk" / "client"
        test_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "helpers" / "java" / "SignatureInterceptorTest.java", test_dir / "SignatureInterceptorTest.java")
        customize_java_pom(output / "pom.xml", repository)
    elif language == "csharp":
        shutil.copyfile(ROOT / "helpers" / "csharp" / "SignatureHandler.cs", output / "src" / "Tachain.Sdk" / "Client" / "SignatureHandler.cs")
        project = output / "src" / "Tachain.Sdk" / "Tachain.Sdk.csproj"
        body = project.read_text(encoding="utf-8")
        body = body.replace("<Authors>OpenAPI</Authors>", "<Authors>Tactic Chain contributors</Authors>")
        body = body.replace("<Company>OpenAPI</Company>", "<Company>Tactic Chain</Company>")
        body = body.replace("<AssemblyTitle>OpenAPI Library</AssemblyTitle>", "<AssemblyTitle>Tactic Chain SDK</AssemblyTitle>")
        body = body.replace("<Description>A library generated from a OpenAPI doc</Description>", "<Description>Tactic Chain public integration API client</Description>")
        body = body.replace("<Copyright>No Copyright</Copyright>", "<Copyright>Copyright 2026 Tactic Chain contributors</Copyright>")
        body = body.replace("<RepositoryUrl>https://github.com/GIT_USER_ID/GIT_REPO_ID.git</RepositoryUrl>", f"<RepositoryUrl>{repository}.git</RepositoryUrl>")
        body = body.replace("<RepositoryType>git</RepositoryType>", "<RepositoryType>git</RepositoryType>\n    <PackageLicenseExpression>MIT</PackageLicenseExpression>")
        body = body.replace("<PackageLicenseExpression>MIT</PackageLicenseExpression>", "<PackageLicenseExpression>MIT</PackageLicenseExpression>\n    <PackageReadmeFile>README.md</PackageReadmeFile>")
        body = body.replace("</Project>", "  <ItemGroup>\n    <None Include=\"../../README.md\" Pack=\"true\" PackagePath=\"/\" />\n  </ItemGroup>\n</Project>")
        project.write_text(body, encoding="utf-8")
        solution = output / "Tachain.Sdk.sln"
        text = solution.read_text(encoding="utf-8")
        fixed = {"FAE04EC0-301F-11D3-BF4B-00C04F79EFBC"}
        mapping: dict[str, str] = {}
        def stable_guid(match: re.Match[str]) -> str:
            original = match.group(1)
            if original in fixed:
                return match.group(0)
            if original not in mapping:
                mapping[original] = str(uuid.uuid5(uuid.NAMESPACE_URL, f"tachain-sdk/csharp/{len(mapping)}")).upper()
            return "{" + mapping[original] + "}"
        solution.write_text(re.sub(r"\{([A-F0-9-]{36})\}", stable_guid, text), encoding="utf-8")
    elif language == "go":
        shutil.copyfile(ROOT / "helpers" / "go" / "signature_transport.go", output / "signature_transport.go")
        shutil.copyfile(ROOT / "helpers" / "go" / "signature_transport_test.go", output / "signature_transport_test.go")
        module = CONFIG["packages"]["goModule"]
        go_mod = output / "go.mod"
        body = go_mod.read_text(encoding="utf-8")
        body = body.replace("module github.com/GIT_USER_ID/GIT_REPO_ID", f"module {module}")
        body = body.replace(f"module {repository.removeprefix('https://')}", f"module {module}")
        go_mod.write_text(body, encoding="utf-8")
    elif language == "php":
        auth = output / "lib" / "Auth"
        auth.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "helpers" / "php" / "SignatureMiddleware.php", auth / "SignatureMiddleware.php")
        composer = output / "composer.json"
        metadata = json.loads(composer.read_text(encoding="utf-8"))
        metadata.pop("version", None)  # Packagist reads versions from split-repo tags.
        metadata["homepage"] = f"https://github.com/{CONFIG['githubOwner']}/{CONFIG['splitRepositories']['php']}"
        metadata["license"] = "MIT"
        metadata["authors"] = [{"name": "Tactic Chain contributors"}]
        composer.write_text(json.dumps(metadata, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    elif language == "ruby":
        shutil.copyfile(ROOT / "helpers" / "ruby" / "signed_api_client.rb", output / "lib" / "tachain-sdk" / "signed_api_client.rb")
        entry = output / "lib" / "tachain-sdk.rb"
        entry.write_text(entry.read_text(encoding="utf-8") + "\nrequire 'tachain-sdk/signed_api_client'\n", encoding="utf-8")
        gemspec = output / f"{CONFIG['packages']['ruby']}.gemspec"
        body = gemspec.read_text(encoding="utf-8")
        body = body.replace('s.authors     = ["OpenAPI-Generator"]', 's.authors     = ["Tactic Chain contributors"]')
        body = body.replace('s.homepage    = "https://openapi-generator.tech"', f's.homepage    = "{repository}"')
        body = body.replace('s.license     = "Unlicense"', 's.license     = "MIT"')
        gemspec.write_text(body, encoding="utf-8")
    elif language == "swift":
        shutil.copyfile(ROOT / "helpers" / "swift" / "SignatureRequestBuilder.swift", output / "Sources" / "TachainSDK" / "SignatureRequestBuilder.swift")
        swift_tests = output / "Tests" / "TachainSDKTests"
        swift_tests.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "helpers" / "swift" / "SignatureRequestBuilderTests.swift", swift_tests / "SignatureRequestBuilderTests.swift")
        package = output / "Package.swift"
        package_text = package.read_text(encoding="utf-8")
        package_text = package_text.replace(
            '        .target(\n            name: "TachainSDK",\n            dependencies: ["AnyCodable", ],\n            path: "Sources/TachainSDK"\n        ),',
            '        .target(\n            name: "TachainSDK",\n            dependencies: ["AnyCodable", ],\n            path: "Sources/TachainSDK"\n        ),\n        .testTarget(name: "TachainSDKTests", dependencies: ["TachainSDK"], path: "Tests/TachainSDKTests"),',
        )
        package.write_text(package_text, encoding="utf-8")
        # This package targets SPM. Other generator outputs carry unrelated
        # upstream CocoaPods/Carthage metadata and are not release artifacts.
        for pattern in ("*.podspec", "Cartfile", "git_push.sh"):
            for path in output.glob(pattern):
                path.unlink()
    customize_readme(output, language, CONFIG)


def generate(language: str) -> None:
    generator, options = settings(language)
    with tempfile.TemporaryDirectory(prefix=f"sdk-{language}-") as temp_name:
        temp = Path(temp_name)
        output = temp / "output"
        config_file = temp / "config.json"
        config_file.write_text(json.dumps(options), encoding="utf-8")
        command = ["java", "-jar", str(JAR), "generate", "-i", str(SPEC), "-g", generator, "-o", str(output), "-c", str(config_file), "--git-user-id", CONFIG["githubOwner"], "--git-repo-id", CONFIG["githubRepository"], "--global-property", "apiDocs=false,modelDocs=false,apiTests=false,modelTests=false"]
        if language == "python":
            # Generator 7.25.0 leaves allVars empty on object models with
            # required-only oneOf branches, even though vars contains the
            # declared fields. Its from_dict then silently discards fileId.
            # Override the pinned template, using vars only when allVars is
            # empty; keep the public oneOf contract and generated code intact.
            templates = temp / "templates"
            templates.mkdir()
            with zipfile.ZipFile(JAR) as archive:
                template = archive.read("python/model_generic.mustache").decode("utf-8")
            pattern = re.compile(r"{{#allVars}}(.*?){{/allVars}}", re.DOTALL)
            template, count = pattern.subn(
                lambda match: match.group(0) + "{{^allVars}}{{#vars}}" + match.group(1) + "{{/vars}}{{/allVars}}",
                template,
            )
            if count != 7:
                raise ValueError("Pinned Python model template changed; review composed-model serialization")
            from_dict = "        _obj = cls.model_validate({"
            if template.count(from_dict) != 1:
                raise ValueError("Pinned Python from_dict template changed")
            template = template.replace(from_dict, (
                "{{^allVars}}\n"
                "        # Composed-model fallback: keep omitted nullable fields absent.\n"
                "        return cls.model_validate(obj)\n"
                "{{/allVars}}\n" + from_dict
            ))
            (templates / "model_generic.mustache").write_text(template, encoding="utf-8")
            command += ["--template-dir", str(templates)]
        if language == "ruby":
            schema_names = json.loads(SPEC.read_text(encoding="utf-8"))["components"]["schemas"]
            aliases = {name: short_model_name(name) for name in schema_names}
            if len(set(aliases.values())) != len(aliases):
                raise ValueError("Ruby model aliases are not unique")
            mappings = ",".join(f"{name}={alias}" for name, alias in aliases.items() if name != alias)
            command += ["--model-name-mappings", mappings]
        run(command)
        if not any(output.iterdir()):
            raise RuntimeError(f"Generator produced no files for {language}")
        customize(output, language)
        destination = GENERATED / language
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(output, destination)
        print(f"Generated {language}: {sum(p.is_file() for p in destination.rglob('*'))} files")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("languages", nargs="*", help="Omit to generate all eight languages")
    parser.add_argument("--source", type=Path, default=SOURCE, help="Full OpenAPI export; defaults to source/openapi.json")
    args = parser.parse_args()
    invalid = set(args.languages) - set(LANGUAGES)
    if invalid:
        parser.error(f"Unknown languages: {', '.join(sorted(invalid))}")
    source = args.source.resolve()
    if not source.is_file():
        parser.error(f"Source OpenAPI file does not exist: {source}")
    run([sys.executable, str(ROOT / "scripts" / "normalize_openapi.py"), "--input", str(source), "--output", str(SPEC)])
    ensure_jar()
    run(["java", "-jar", str(JAR), "validate", "-i", str(SPEC)])
    for language in args.languages or LANGUAGES:
        generate(language)


if __name__ == "__main__":
    main()
