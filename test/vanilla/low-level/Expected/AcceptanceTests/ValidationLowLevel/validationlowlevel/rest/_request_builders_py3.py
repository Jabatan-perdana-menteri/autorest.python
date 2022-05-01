# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from .._vendor import _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()


def build_validation_of_method_parameters_request(
    subscription_id: str, resource_group_name: str, id: int, **kwargs: Any
) -> HttpRequest:
    """Validates input parameters on the method. See swagger for details.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param subscription_id: Subscription ID. Required.
    :type subscription_id: str
    :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
     Required.
    :type resource_group_name: str
    :param id: Required int multiple of 10 from 100 to 1000. Required.
    :type id: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                "child": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "count": 0  # Optional. Count.
                },
                "constChild": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "constProperty2": "constant2"  # Default value is "constant2".
                      Constant string2. Has constant value: "constant2".
                },
                "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                "constString": "constant",  # Default value is "constant". Constant string.
                  Has constant value: "constant".
                "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                  "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                  pass in are None and "constant_string_as_enum". The default value is None.
                "display_names": [
                    "str"  # Optional. Non required array of unique items from 0 to 6
                      elements.
                ],
                "image": "str"  # Optional. Image URL representing the product.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("apiVersion", "1.0.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9\']+"
        ),
        "id": _SERIALIZER.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["apiVersion"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_validation_of_body_request(
    subscription_id: str,
    resource_group_name: str,
    id: int,
    *,
    json: Optional[JSON] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Validates body parameters on the method. See swagger for details.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param subscription_id: Subscription ID. Required.
    :type subscription_id: str
    :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
     Required.
    :type resource_group_name: str
    :param id: Required int multiple of 10 from 100 to 1000. Required.
    :type id: int
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).  Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                "child": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "count": 0  # Optional. Count.
                },
                "constChild": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "constProperty2": "constant2"  # Default value is "constant2".
                      Constant string2. Has constant value: "constant2".
                },
                "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                "constString": "constant",  # Default value is "constant". Constant string.
                  Has constant value: "constant".
                "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                  "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                  pass in are None and "constant_string_as_enum". The default value is None.
                "display_names": [
                    "str"  # Optional. Non required array of unique items from 0 to 6
                      elements.
                ],
                "image": "str"  # Optional. Image URL representing the product.
            }

            # response body for status code(s): 200
            response.json() == {
                "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                "child": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "count": 0  # Optional. Count.
                },
                "constChild": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "constProperty2": "constant2"  # Default value is "constant2".
                      Constant string2. Has constant value: "constant2".
                },
                "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                "constString": "constant",  # Default value is "constant". Constant string.
                  Has constant value: "constant".
                "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                  "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                  pass in are None and "constant_string_as_enum". The default value is None.
                "display_names": [
                    "str"  # Optional. Non required array of unique items from 0 to 6
                      elements.
                ],
                "image": "str"  # Optional. Image URL representing the product.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("apiVersion", "1.0.0"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9]+"
        ),
        "id": _SERIALIZER.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["apiVersion"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, json=json, content=content, **kwargs)


def build_get_with_constant_in_path_request(**kwargs: Any) -> HttpRequest:
    """get_with_constant_in_path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword constant_param:  Default value is "constant". Note that overriding this default value
     may result in unsupported behavior.
    :paramtype constant_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    constant_param = kwargs.pop("constant_param", "constant")  # type: str
    # Construct URL
    _url = "/validation/constantsInPath/{constantParam}/value"
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    return HttpRequest(method="GET", url=_url, **kwargs)


def build_post_with_constant_in_body_request(
    *, json: Optional[JSON] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """post_with_constant_in_body.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword constant_param:  Default value is "constant". Note that overriding this default value
     may result in unsupported behavior.
    :paramtype constant_param: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).  Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                "child": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "count": 0  # Optional. Count.
                },
                "constChild": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "constProperty2": "constant2"  # Default value is "constant2".
                      Constant string2. Has constant value: "constant2".
                },
                "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                "constString": "constant",  # Default value is "constant". Constant string.
                  Has constant value: "constant".
                "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                  "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                  pass in are None and "constant_string_as_enum". The default value is None.
                "display_names": [
                    "str"  # Optional. Non required array of unique items from 0 to 6
                      elements.
                ],
                "image": "str"  # Optional. Image URL representing the product.
            }

            # response body for status code(s): 200
            response.json() == {
                "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                "child": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "count": 0  # Optional. Count.
                },
                "constChild": {
                    "constProperty": "constant",  # Default value is "constant". Constant
                      string. Has constant value: "constant".
                    "constProperty2": "constant2"  # Default value is "constant2".
                      Constant string2. Has constant value: "constant2".
                },
                "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                "constString": "constant",  # Default value is "constant". Constant string.
                  Has constant value: "constant".
                "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                  "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                  pass in are None and "constant_string_as_enum". The default value is None.
                "display_names": [
                    "str"  # Optional. Non required array of unique items from 0 to 6
                      elements.
                ],
                "image": "str"  # Optional. Image URL representing the product.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    constant_param = kwargs.pop("constant_param", "constant")  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/validation/constantsInPath/{constantParam}/value"
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, json=json, content=content, **kwargs)
