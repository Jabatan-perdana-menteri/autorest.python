# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer
from ..._vendor import _format_url_section

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_empty_request(
    key_name: str, subscription_id: str, *, key_version: str = "v1", **kwargs: Any
) -> HttpRequest:
    """Get a 200 to test a valid base uri.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param key_name: The key name with value 'key1'. Required.
    :type key_name: str
    :param subscription_id: The subscription id with value 'test12'. Required.
    :type subscription_id: str
    :keyword key_version: The key version. Default value 'v1'. Default value is "v1".
    :paramtype key_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/customuri/{subscriptionId}/{keyName}"
    path_format_arguments = {
        "keyName": _SERIALIZER.url("key_name", key_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if key_version is not None:
        _params["keyVersion"] = _SERIALIZER.query("key_version", key_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)
