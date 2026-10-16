"""Regression coverage for malformed upstream exports without losing fields."""

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from normalize_openapi import INTEGRATION_SCHEMA_PREFIX, normalize


def document(schemas, owner):
    return {
        "openapi": "3.0.1",
        "paths": {"/v1/order/Create": {"post": {
            "requestBody": {"content": {"application/json": {"schema": {
                "$ref": "#/components/schemas/" + owner,
            }}}},
            "responses": {"200": {"description": "OK"}},
        }}},
        "components": {"schemas": schemas},
    }


class NormalizeOpenApi(unittest.TestCase):
    def test_repairs_known_array_refs_but_keeps_fields_required_and_examples(self):
        owner = INTEGRATION_SCHEMA_PREFIX + "ApiOrderCreateRequest"
        target = INTEGRATION_SCHEMA_PREFIX + "ApiOrderLineCreateRequest"
        source = document({
            owner: {"type": "object", "required": ["orderLines"], "properties": {
                "orderLines": {"type": "array", "minItems": 1, "items": {"$ref": "#/definitions/321036564"}},
                "remark": {"type": ["string", "null"], "examples": ["first", "second"], "x-required-when": "when applicable"},
            }, "allOf": [{"anyOf": [{"type": "string"}, {"type": "string"}]}], "examples": [{"orderLines": []}]},
            target: {"type": "object", "properties": {"materialCode": {"type": "string"}}},
        }, owner)
        original = copy.deepcopy(source)
        result = normalize(source)
        self.assertEqual(source, original, "Normalization must not mutate the imported source")
        schema = result["components"]["schemas"][owner]
        self.assertEqual(schema["required"], ["orderLines"])
        self.assertEqual(schema["properties"]["orderLines"]["minItems"], 1)
        self.assertEqual(schema["properties"]["orderLines"]["items"]["$ref"], "#/components/schemas/" + target)
        remark = schema["properties"]["remark"]
        self.assertEqual((remark["type"], remark["nullable"]), ("string", True))
        self.assertEqual(remark["example"], "first")
        self.assertEqual(remark["x-export-examples"], ["first", "second"])
        self.assertEqual(remark["x-required-when"], "when applicable")
        self.assertEqual(schema["example"], {"orderLines": []})
        self.assertNotIn("allOf", schema)
        self.assertEqual(schema["x-export-invalid-composition"]["allOf"], original["components"]["schemas"][owner]["allOf"])

    def test_keeps_valid_file_input_one_of_unchanged(self):
        schema = {"type": "object", "properties": {
            "fileId": {"type": "string"}, "fileBase64": {"type": "string"},
        }, "oneOf": [
            {"required": ["fileId"], "not": {"required": ["fileBase64"]}},
            {"required": ["fileBase64"], "not": {"required": ["fileId"]}},
        ]}
        result = normalize(document({"FileRequest": schema}, "FileRequest"))
        self.assertEqual(result["components"]["schemas"]["FileRequest"], schema)

    def test_unknown_dangling_ref_still_fails(self):
        source = document({"Unknown": {"type": "object", "properties": {
            "items": {"type": "array", "items": {"$ref": "#/definitions/unknown"}},
        }}}, "Unknown")
        with self.assertRaisesRegex(ValueError, "External or unsupported reference"):
            normalize(source)


if __name__ == "__main__":
    unittest.main()
