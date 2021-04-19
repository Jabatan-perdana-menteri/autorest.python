# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import _rest, models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """PetsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~additionalproperties.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_ap_true(self, create_parameters: "_models.PetAPTrue", **kwargs: Any) -> "_models.PetAPTrue":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPTrue"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(create_parameters, "PetAPTrue")
        content = json.dumps(content)

        request = _rest.pets.build_create_ap_true_request(
            content=content, content_type=content_type, template_url=self.create_ap_true.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_true.metadata = {"url": "/additionalProperties/true"}  # type: ignore

    @distributed_trace_async
    async def create_cat_ap_true(self, create_parameters: "_models.CatAPTrue", **kwargs: Any) -> "_models.CatAPTrue":
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue, or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.CatAPTrue"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(create_parameters, "CatAPTrue")
        content = json.dumps(content)

        request = _rest.pets.build_create_cat_ap_true_request(
            content=content, content_type=content_type, template_url=self.create_cat_ap_true.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CatAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_cat_ap_true.metadata = {"url": "/additionalProperties/true-subclass"}  # type: ignore

    @distributed_trace_async
    async def create_ap_object(self, create_parameters: "_models.PetAPObject", **kwargs: Any) -> "_models.PetAPObject":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPObject"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(create_parameters, "PetAPObject")
        content = json.dumps(content)

        request = _rest.pets.build_create_ap_object_request(
            content=content, content_type=content_type, template_url=self.create_ap_object.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPObject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_object.metadata = {"url": "/additionalProperties/type/object"}  # type: ignore

    @distributed_trace_async
    async def create_ap_string(self, create_parameters: "_models.PetAPString", **kwargs: Any) -> "_models.PetAPString":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPString
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPString"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(create_parameters, "PetAPString")
        content = json.dumps(content)

        request = _rest.pets.build_create_ap_string_request(
            content=content, content_type=content_type, template_url=self.create_ap_string.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_string.metadata = {"url": "/additionalProperties/type/string"}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties(
        self, create_parameters: "_models.PetAPInProperties", **kwargs: Any
    ) -> "_models.PetAPInProperties":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPInProperties"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(create_parameters, "PetAPInProperties")
        content = json.dumps(content)

        request = _rest.pets.build_create_ap_in_properties_request(
            content=content,
            content_type=content_type,
            template_url=self.create_ap_in_properties.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties.metadata = {"url": "/additionalProperties/in/properties"}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: "_models.PetAPInPropertiesWithAPString", **kwargs: Any
    ) -> "_models.PetAPInPropertiesWithAPString":
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAPInPropertiesWithAPString"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        content = self._serialize.body(create_parameters, "PetAPInPropertiesWithAPString")
        content = json.dumps(content)

        request = _rest.pets.build_create_ap_in_properties_with_ap_string_request(
            content=content,
            content_type=content_type,
            template_url=self.create_ap_in_properties_with_ap_string.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInPropertiesWithAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties_with_ap_string.metadata = {"url": "/additionalProperties/in/properties/with/additionalProperties/string"}  # type: ignore
