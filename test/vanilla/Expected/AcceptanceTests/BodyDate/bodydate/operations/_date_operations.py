# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
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
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class DateOperations(object):
    """DateOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodydate.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _get_null_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_null_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_null_request.metadata = {"url": "/date/null"}  # type: ignore

    @distributed_trace
    def get_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[datetime.date]
        """Get null date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date or None, or the result of cls(response)
        :rtype: ~datetime.date or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[datetime.date]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_null_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/date/null"}  # type: ignore

    def _get_invalid_date_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_invalid_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_invalid_date_request.metadata = {"url": "/date/invaliddate"}  # type: ignore

    @distributed_trace
    def get_invalid_date(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.date
        """Get invalid date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_invalid_date_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid_date.metadata = {"url": "/date/invaliddate"}  # type: ignore

    def _get_overflow_date_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_overflow_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_overflow_date_request.metadata = {"url": "/date/overflowdate"}  # type: ignore

    @distributed_trace
    def get_overflow_date(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.date
        """Get overflow date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_overflow_date_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_overflow_date.metadata = {"url": "/date/overflowdate"}  # type: ignore

    def _get_underflow_date_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_underflow_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_underflow_date_request.metadata = {"url": "/date/underflowdate"}  # type: ignore

    @distributed_trace
    def get_underflow_date(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.date
        """Get underflow date value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_underflow_date_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_underflow_date.metadata = {"url": "/date/underflowdate"}  # type: ignore

    def _put_max_date_request(
        self,
        body,  # type: datetime.date
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_max_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "date")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_max_date_request.metadata = {"url": "/date/max"}  # type: ignore

    @distributed_trace
    def put_max_date(
        self,
        date_body,  # type: datetime.date
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put max date value 9999-12-31.

        :param date_body: date body.
        :type date_body: ~datetime.date
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_max_date_request(body=date_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_max_date.metadata = {"url": "/date/max"}  # type: ignore

    def _get_max_date_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_max_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_max_date_request.metadata = {"url": "/date/max"}  # type: ignore

    @distributed_trace
    def get_max_date(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.date
        """Get max date value 9999-12-31.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_max_date_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_max_date.metadata = {"url": "/date/max"}  # type: ignore

    def _put_min_date_request(
        self,
        body,  # type: datetime.date
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_min_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "date")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_min_date_request.metadata = {"url": "/date/min"}  # type: ignore

    @distributed_trace
    def put_min_date(
        self,
        date_body,  # type: datetime.date
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put min date value 0000-01-01.

        :param date_body: date body.
        :type date_body: ~datetime.date
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_min_date_request(body=date_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_min_date.metadata = {"url": "/date/min"}  # type: ignore

    def _get_min_date_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_min_date_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_min_date_request.metadata = {"url": "/date/min"}  # type: ignore

    @distributed_trace
    def get_min_date(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> datetime.date
        """Get min date value 0000-01-01.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: date, or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.date]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_min_date_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("date", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_min_date.metadata = {"url": "/date/min"}  # type: ignore
