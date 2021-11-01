# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

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
from msrest import Serializer

from .._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_formdataurlencoded_update_pet_with_form_request(
    pet_id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/formsdataurlencoded/pet/add/{petId}')
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'int'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_formdataurlencoded_partial_constant_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    content = kwargs.pop('content', "access_token")  # type: str

    # Construct URL
    url = kwargs.pop("template_url", '/formsdataurlencoded/partialConstantBody')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class FormdataurlencodedOperations(object):
    """FormdataurlencodedOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def update_pet_with_form(
        self,
        pet_id,  # type: int
        data,  # type: Dict[str, Any]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated.
        :type pet_id: int
        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    name: "str",  # Optional. Updated name of the pet.
                    pet_age: 0,  # How many years is it old?.
                    pet_food: "str",  # Can take a value of meat, or fish, or plant. Possible values are: "meat", "fish", and "plant".
                    pet_type: "str",  # Can take a value of dog, or cat, or fish. Possible values are: "dog", "cat", and "fish".
                    status: "str"  # Optional. Updated status of the pet.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_formdataurlencoded_update_pet_with_form_request(
            pet_id=pet_id,
            content_type=content_type,
            data=data,
            template_url=self.update_pet_with_form.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    update_pet_with_form.metadata = {"url": "/formsdataurlencoded/pet/add/{petId}"}  # type: ignore

    @distributed_trace
    def partial_constant_body(
        self,
        data,  # type: Dict[str, Any]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test a partially constant formdata body.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    access_token: "str",  # AAD access token, mandatory when grant_type is access_token_refresh_token or access_token.
                    grant_type: "access_token",  # Default value is "access_token". Constant part of a formdata body. The default value is "access_token". Note that overriding this default value may result in unsupported behavior.
                    service: "str"  # Indicates the name of your Azure container registry.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_formdataurlencoded_partial_constant_body_request(
            content_type=content_type,
            content=data,
            template_url=self.partial_constant_body.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    partial_constant_body.metadata = {"url": "/formsdataurlencoded/partialConstantBody"}  # type: ignore
