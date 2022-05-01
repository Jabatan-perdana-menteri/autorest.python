# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_update_pet_with_form_request(
    pet_id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    # Construct URL
    _url = kwargs.pop("template_url", "/formsdataurlencoded/pet/add/{petId}")
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'int'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_partial_constant_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    # Construct URL
    _url = kwargs.pop("template_url", "/formsdataurlencoded/partialConstantBody")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )

# fmt: on
class FormdataurlencodedOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodyformurlencodeddata.BodyFormsDataURLEncoded`'s
        :attr:`formdataurlencoded` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def update_pet_with_form(  # pylint: disable=inconsistent-return-statements
        self,
        pet_id,  # type: int
        pet_type,  # type: Union[str, "_models.PetType"]
        pet_food,  # type: Union[str, "_models.PetFood"]
        pet_age,  # type: int
        name=None,  # type: Optional[str]
        status=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated. Required.
        :type pet_id: int
        :param pet_type: Can take a value of dog, or cat, or fish. Required.
        :type pet_type: str or ~bodyformurlencodeddata.models.PetType
        :param pet_food: Can take a value of meat, or fish, or plant. Required.
        :type pet_food: str or ~bodyformurlencodeddata.models.PetFood
        :param pet_age: How many years is it old?. Required.
        :type pet_age: int
        :param name: Updated name of the pet. Default value is None.
        :type name: str
        :param status: Updated status of the pet. Default value is None.
        :type status: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        # Construct form data
        _data = {
            "pet_type": pet_type,
            "pet_food": pet_food,
            "pet_age": pet_age,
            "name": name,
            "status": status,
        }

        request = build_update_pet_with_form_request(
            pet_id=pet_id,
            content_type=content_type,
            data=_data,
            template_url=self.update_pet_with_form.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    update_pet_with_form.metadata = {"url": "/formsdataurlencoded/pet/add/{petId}"}  # type: ignore

    @distributed_trace
    def partial_constant_body(  # pylint: disable=inconsistent-return-statements
        self,
        service,  # type: str
        access_token,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
        'foo', service: 'bar' } to pass the test.

        :param service: Indicates the name of your Azure container registry. Required.
        :type service: str
        :param access_token: AAD access token, mandatory when grant_type is access_token_refresh_token
         or access_token. Required.
        :type access_token: str
        :keyword grant_type: Constant part of a formdata body. Default value is "access_token". Note
         that overriding this default value may result in unsupported behavior.
        :paramtype grant_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded")
        )  # type: Optional[str]
        grant_type = kwargs.pop("grant_type", "access_token")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        # Construct form data
        _data = {
            "grant_type": grant_type,
            "service": service,
            "access_token": access_token,
        }

        request = build_partial_constant_body_request(
            content_type=content_type,
            data=_data,
            template_url=self.partial_constant_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    partial_constant_body.metadata = {"url": "/formsdataurlencoded/partialConstantBody"}  # type: ignore
