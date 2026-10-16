"""Exercise generated request-model round trips with real Pydantic models."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "generated/python"))

from tachain_sdk.models.tactic_chain_api_service_controllers_api_integration_v1_api_declaration_file_request import (
    TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationFileRequest as FileRequest,
)
from tachain_sdk.models.tactic_chain_api_service_controllers_api_integration_v1_api_declaration_submit_request import (
    TacticChainApiServiceControllersApiIntegrationV1ApiDeclarationSubmitRequest as SubmitRequest,
)


for payload in ({"fileId": "uploaded-file"}, {"fileBase64": "ZmlsZQ==", "fileName": "invoice.pdf"}):
    assert FileRequest.from_dict(payload).to_dict() == payload, "File input fields must survive from_dict"
    assert json.loads(FileRequest.from_json(json.dumps(payload)).to_json()) == payload

payload = {
    "stageId": "Order", "orderSide": "SO", "uniqueNo": "order-line",
    "documentList": [{"documentTypeCode": "INVOICE", "fileList": [{"fileId": "uploaded-file"}]}],
}
saved = SubmitRequest.from_dict(payload).to_dict()
assert saved["documentList"][0]["fileList"] == [{"fileId": "uploaded-file"}], "Nested submission must keep uploaded FileId"
print("Python FileId/Base64 and nested declaration request round trips passed")
