"""API Key + Secret signing for the generated urllib3 client."""

from __future__ import annotations

import hashlib
import hmac
import time
from typing import Callable
from urllib.parse import parse_qsl, urlsplit

from tachain_sdk.rest import RESTClientObject


def normalize_query(url: str) -> str:
    """Match SignatureHelper.NormalizeQueryString on the final request URL."""
    values: dict[str, tuple[str, list[str]]] = {}
    for key, value in parse_qsl(urlsplit(url).query, keep_blank_values=True):
        folded = key.lower()
        if folded not in values:
            values[folded] = (key, [])
        values[folded][1].append(value)
    def ordinal(value: str) -> bytes:
        # .NET StringComparer.Ordinal compares UTF-16 code units, not scalars.
        return value.encode("utf-16-be", errors="surrogatepass")
    return "&".join(
        f"{key}={value}"
        for key, group in sorted(values.values(), key=lambda item: ordinal(item[0]))
        for value in sorted(group, key=ordinal)
    )


def compute_signature(api_key: str, api_secret: str, timestamp: str, url: str) -> str:
    message = (api_key + timestamp + normalize_query(url)).encode("utf-8")
    return hmac.new(api_secret.encode("utf-8"), message, hashlib.sha256).hexdigest()


class SignedRESTClient(RESTClientObject):
    """Assign to `api_client.rest_client` after constructing ApiClient."""

    def __init__(
        self,
        configuration,
        api_key: str,
        api_secret: str,
        clock: Callable[[], float] = time.time,
    ) -> None:
        super().__init__(configuration)
        self.api_key = api_key
        self.api_secret = api_secret
        self.clock = clock

    def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
        timestamp = str(int(self.clock()))
        signed_headers = dict(headers or {})
        signed_headers.pop("Authorization", None)
        signed_headers.update({
            "X-Credential-Type": "API Key",
            "X-API-Key": self.api_key,
            "X-Timestamp": timestamp,
            "X-Signature": compute_signature(self.api_key, self.api_secret, timestamp, url),
        })
        return super().request(
            method, url, headers=signed_headers, body=body,
            post_params=post_params, _request_timeout=_request_timeout,
        )
