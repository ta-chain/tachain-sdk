"""Check the maintained Python signing helper against backend vectors."""

import importlib.util
import json
import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The pure signing functions can be tested before installing generated client deps.
stub_package = types.ModuleType("tachain_sdk")
stub_package.__path__ = []
stub_rest = types.ModuleType("tachain_sdk.rest")
stub_rest.RESTClientObject = type("RESTClientObject", (), {})
sys.modules["tachain_sdk"] = stub_package
sys.modules["tachain_sdk.rest"] = stub_rest
spec = importlib.util.spec_from_file_location("signature", ROOT / "helpers" / "python" / "signature.py")
signature = importlib.util.module_from_spec(spec)
spec.loader.exec_module(signature)


class SignatureVectors(unittest.TestCase):
    def test_backend_vectors(self):
        for name in ("signature-vector.json", "signature-unicode-vector.json", "signature-case-vector.json"):
            vector = json.loads((ROOT / "tests" / name).read_text(encoding="utf-8"))
            with self.subTest(name=name):
                self.assertEqual(signature.normalize_query(vector["url"]), vector["normalizedQuery"])
                self.assertEqual(
                    signature.compute_signature(vector["apiKey"], vector["apiSecret"], vector["timestamp"], vector["url"]),
                    vector["signature"],
                )


if __name__ == "__main__":
    unittest.main()
