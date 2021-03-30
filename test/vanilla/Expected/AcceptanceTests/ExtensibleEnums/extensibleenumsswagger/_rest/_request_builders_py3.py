# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_pet_get_by_pet_id_request(pet_id: str, **kwargs: Any) -> HttpRequest:
    """get pet by id.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request_builder into your code flow.

    :param pet_id: Pet id.
    :type pet_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/extensibleenums/pet/{petId}")
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_pet_add_pet_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """add pet.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request_builder into your code flow.

    :keyword json: pet param.
    :paramtype json: Any
    :keyword content: pet param.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/extensibleenums/pet/addPet")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)
