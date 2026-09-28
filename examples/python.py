"""Token example for the generated Python SDK.

Install with `python -m pip install ./generated/python` from the repository root,
then set TAC_BASE_URL and TAC_TOKEN before running this file.
"""

import os

import tachain_sdk
from tachain_sdk.rest import ApiException


def main() -> None:
    base_url = os.environ["TAC_BASE_URL"]
    token = os.environ["TAC_TOKEN"]
    config = tachain_sdk.Configuration(host=base_url, access_token=token)
    with tachain_sdk.ApiClient(config) as client:
        api = tachain_sdk.ApiEnumApi(client)
        print(api.get_v1_enum_get_list(x_credential_type="Token"))


if __name__ == "__main__":
    try:
        main()
    except ApiException as exc:
        raise SystemExit(f"API request failed: HTTP {exc.status}") from exc
