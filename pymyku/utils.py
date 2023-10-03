from __future__ import annotations

import base64
from typing import Any

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from requests import Response
from requests.models import HTTPError

from . import consts


def hash_credential(cred: str) -> str:
    public_key = RSA.import_key(consts.PUBLIC_KEY)
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(bytes(cred.strip(), encoding="utf-8"))
    return base64.b64encode(cipher_text).decode("utf-8")


def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def amend_locals(locals_: dict[str, Any]) -> dict[str, Any]:
    return {
        snake_to_camel(k): v
        for k, v in locals_.items()
        if k != "self" and k != "session" and v is not None
    }


def raise_for_status_with_response(response: Response) -> None:
    """Raises :class:`HTTPError`, if one occurred."""

    http_error_msg = ""
    if isinstance(response.reason, bytes):
        # We attempt to decode utf-8 first because some servers
        # choose to localize their reason strings. If the string
        # isn't utf-8, we fall back to iso-8859-1 for all other
        # encodings. (See PR #3538)
        try:
            reason = response.reason.decode("utf-8")
        except UnicodeDecodeError:
            reason = response.reason.decode("iso-8859-1")
    else:
        reason = response.reason

    client_error_range = (400, 499)
    server_error_range = (500, 599)

    if client_error_range[0] <= response.status_code < client_error_range[1]:
        http_error_msg = (
            f"{response.status_code} Client Error: {reason}"
            "for url {response.url}"
        )

    elif server_error_range[0] <= response.status_code < server_error_range[1]:
        http_error_msg = (
            f"{response.status_code} Server Error: {reason}"
            "for url {response.url}"
        )

    if http_error_msg:
        if response.text:
            http_error_msg += f" with response: {response.text}"

        raise HTTPError(http_error_msg, response=response)
