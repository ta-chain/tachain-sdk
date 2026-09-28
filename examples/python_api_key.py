"""API Key + Secret example using the generated client's signing adapter."""

import os

import tachain_sdk
from tachain_sdk.signature import SignedRESTClient

config = tachain_sdk.Configuration(host=os.environ["TAC_BASE_URL"])
with tachain_sdk.ApiClient(config) as client:
    client.rest_client = SignedRESTClient(
        config,
        os.environ["TAC_API_KEY"],
        os.environ["TAC_API_SECRET"],
    )
    api = tachain_sdk.ApiEnumApi(client)
    print(api.get_v1_enum_get_list(x_credential_type="API Key"))
