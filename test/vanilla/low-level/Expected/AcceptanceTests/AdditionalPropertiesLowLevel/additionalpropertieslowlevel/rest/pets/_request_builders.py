# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, TypeVar

    T = TypeVar("T")
    JSONObject = Dict[str, Any]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_create_ap_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONObject
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
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }

            # response body for status code(s): 200
            response.json() == {
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/additionalProperties/true"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_cat_ap_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a CatAPTrue which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONObject
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
                "friendly": bool,  # Optional.
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }

            # response body for status code(s): 200
            response.json() == {
                "friendly": bool,  # Optional.
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/additionalProperties/true-subclass"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_object_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONObject
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
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }

            # response body for status code(s): 200
            response.json() == {
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/additionalProperties/type/object"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_string_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONObject
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
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }

            # response body for status code(s): 200
            response.json() == {
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/additionalProperties/type/string"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_in_properties_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONObject
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
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }

            # response body for status code(s): 200
            response.json() == {
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/additionalProperties/in/properties"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_in_properties_with_ap_string_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONObject
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
                "@odata.location": "str",  # Required.
                "additionalProperties": {
                    "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                },
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }

            # response body for status code(s): 200
            response.json() == {
                "@odata.location": "str",  # Required.
                "additionalProperties": {
                    "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                },
                "id": 0,  # Required.
                "name": "str",  # Optional.
                "status": bool  # Optional.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/additionalProperties/in/properties/with/additionalProperties/string"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )
