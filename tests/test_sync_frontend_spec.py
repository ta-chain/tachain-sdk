"""Check frontend synchronization and read-only detection of release drift."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SyncFrontendSpec(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.frontend = Path(self.temp.name)
        (self.frontend / "package.json").write_text("{}\n")
        self.contract = self.frontend / "public/openapi/tactic-chain-public.json"
        self.release = self.frontend / "src/features/integration/sdk/release.json"

    def run_sync(self, check=False):
        command = [sys.executable, str(ROOT / "scripts/sync_frontend_spec.py"),
                   "--frontend-root", str(self.frontend)]
        if check:
            command.append("--check")
        return subprocess.run(command, text=True, capture_output=True)

    def test_sync_creates_both_assets_from_sdk_sources(self):
        self.assertEqual(self.run_sync().returncode, 0)
        self.assertEqual(self.contract.read_bytes(), (ROOT / "openapi/tactic-chain-public.json").read_bytes())
        config = json.loads((ROOT / "sdk.config.json").read_text())
        self.assertEqual(json.loads(self.release.read_text()), {
            "releaseVersion": config["releaseVersion"],
            "generatorVersion": config["generatorVersion"],
        })
        self.assertEqual(self.run_sync(check=True).returncode, 0)

    def test_check_rejects_each_stale_asset_without_rewriting_it(self):
        self.assertEqual(self.run_sync().returncode, 0)
        for target, message in (
            (self.contract, "Frontend contract differs"),
            (self.release, "Frontend SDK release metadata differs"),
        ):
            with self.subTest(asset=target.name):
                target.write_text("{}\n")
                before = {path: path.read_bytes() for path in (self.contract, self.release)}
                result = self.run_sync(check=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertEqual({path: path.read_bytes() for path in before}, before)
                self.assertEqual(self.run_sync().returncode, 0)
                self.assertEqual(self.run_sync(check=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
