# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_head200_request(**kwargs: Any) -> HttpRequest:
    """Return 200 status code if successful.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=url, headers=header_parameters, **kwargs)


def build_get200_request(**kwargs: Any) -> HttpRequest:
    """Get 200 success.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_options200_request(**kwargs: Any) -> HttpRequest:
    """Options 200 success.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="OPTIONS", url=url, headers=header_parameters, **kwargs)


def build_put200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put boolean value true returning 200 success.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_patch200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Patch true Boolean value in request returning 200.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PATCH", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post bollean value true in request that returns a 200.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_delete200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Delete simple boolean value true returns 200.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_put201_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put true Boolean value in request returns 201.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/201")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post201_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post true Boolean value in request returns 201 (Created).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/201")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_put202_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put true Boolean value in request returns 202 (Accepted).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/202")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_patch202_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Patch true Boolean value in request returns 202.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/202")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PATCH", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post202_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post true Boolean value in request returns 202 (Accepted).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/202")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_delete202_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Delete true Boolean value in request returns 202 (accepted).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/202")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_head204_request(**kwargs: Any) -> HttpRequest:
    """Return 204 status code if successful.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=url, headers=header_parameters, **kwargs)


def build_put204_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put true Boolean value in request returns 204 (no content).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_patch204_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Patch true Boolean value in request returns 204 (no content).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PATCH", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post204_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post true Boolean value in request returns 204 (no content).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_delete204_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Delete true Boolean value in request returns 204 (no content).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Simple boolean value true.
    :paramtype json: Any
    :keyword content: Simple boolean value true.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_head404_request(**kwargs: Any) -> HttpRequest:
    """Return 404 status code.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/404")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=url, headers=header_parameters, **kwargs)
