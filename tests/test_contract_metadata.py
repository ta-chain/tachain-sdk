"""Release gates for the public contract and package coordinates."""

import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from normalize_openapi import normalize, walk_refs


class ContractMetadata(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT / "sdk.config.json").read_text(encoding="utf-8"))
        cls.source = json.loads((ROOT / "source" / "openapi.json").read_text(encoding="utf-8"))
        cls.public = json.loads((ROOT / "openapi" / "tactic-chain-public.json").read_text(encoding="utf-8"))

    def test_only_public_endpoints_in_committed_source(self):
        self.assertTrue(self.source["paths"])
        self.assertTrue(all(path.startswith("/v1/") for path in self.source["paths"]))
        self.assertEqual(set(self.source["paths"]), set(self.public["paths"]))

    def test_auth_and_operation_ids(self):
        names = set()
        for path, item in self.public["paths"].items():
            for method, operation in item.items():
                if method not in {"get", "post", "put", "patch", "delete"}:
                    continue
                name = operation["operationId"]
                self.assertNotIn(name, names)
                names.add(name)
                self.assertEqual(operation["security"], [
                    {"BearerToken": []},
                    {"ApiKey": [], "Timestamp": [], "Signature": []},
                ])
                self.assertTrue(any(p.get("name") == "X-Credential-Type" and p.get("required") for p in operation.get("parameters", [])), f"{method} {path}")
        self.assertEqual(len(names), 45)

    def test_normalized_contract_is_current_and_all_refs_resolve(self):
        self.assertEqual(normalize(self.source), self.public)
        for name, source_schema in self.source["components"].get("schemas", {}).items():
            schema = self.public["components"]["schemas"][name]
            self.assertEqual(set(source_schema.get("properties", {})), set(schema.get("properties", {})), name)
            self.assertEqual(source_schema.get("required", []), schema.get("required", []), name)
        for ref in walk_refs(self.public):
            self.assertTrue(ref.startswith("#/components/"), ref)
            group, name = ref.removeprefix("#/components/").split("/", 1)
            name = name.replace("~1", "/").replace("~0", "~")
            self.assertIn(name, self.public["components"][group], ref)

    def test_new_operations_and_file_upload_are_present(self):
        for resource in ("material", "product", "processRoute"):
            for operation in ("Create", "Update", "Get", "ListPaging", "Delete"):
                self.assertIn(f"/v1/{resource}/{operation}", self.public["paths"])
        for path in ("/v1/reference/Mappings", "/v1/reference/EnumValues", "/v1/order/DeclarationVerification", "/v1/order/ReceiptPending"):
            self.assertIn(path, self.public["paths"])
        upload = self.public["paths"]["/v1/declaration/UploadFile"]["post"]
        schema = upload["requestBody"]["content"]["multipart/form-data"]["schema"]
        self.assertIn("file", schema["required"])
        self.assertEqual(schema["properties"]["file"]["format"], "binary")

    def test_package_coordinates(self):
        packages = self.config["packages"]
        version = self.config["releaseVersion"]
        ts = json.loads((ROOT / "generated/typescript/package.json").read_text())
        self.assertEqual((ts["name"], ts["version"], ts["license"]), (packages["typescript"], version, "MIT"))
        pyproject = (ROOT / "generated/python/pyproject.toml").read_text()
        self.assertIn(f'version = "{version}"', pyproject)
        self.assertIn('license = "MIT"', pyproject)
        pom = ET.parse(ROOT / "generated/java/pom.xml").getroot()
        ns = {"m": "http://maven.apache.org/POM/4.0.0"}
        self.assertEqual(pom.findtext("m:groupId", namespaces=ns), packages["javaGroup"])
        self.assertEqual(pom.findtext("m:artifactId", namespaces=ns), packages["javaArtifact"])
        self.assertEqual(pom.findtext("m:version", namespaces=ns), version)
        csproj = (ROOT / "generated/csharp/src/Tachain.Sdk/Tachain.Sdk.csproj").read_text()
        self.assertIn(f"<PackageId>{packages['csharp']}</PackageId>", csproj)
        self.assertIn(f"<Version>{version}</Version>", csproj)
        self.assertIn(f"module {packages['goModule']}", (ROOT / "generated/go/go.mod").read_text())
        php = json.loads((ROOT / "generated/php/composer.json").read_text())
        self.assertEqual((php["name"], php["license"]), (packages["php"], "MIT"))
        gemspec = (ROOT / f"generated/ruby/{packages['ruby']}.gemspec").read_text()
        self.assertIn(f's.name        = "{packages["ruby"]}"', gemspec)
        self.assertIn('s.license     = "MIT"', gemspec)
        self.assertIn(f'name: "{packages["swift"]}"', (ROOT / "generated/swift/Package.swift").read_text())


if __name__ == "__main__":
    unittest.main()
