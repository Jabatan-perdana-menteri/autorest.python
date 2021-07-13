# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
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

from ... import models as _models
from ...rest import http_redirects as rest_http_redirects

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HttpRedirectsOperations:
    """HttpRedirectsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~httpinfrastructureversiontolerant.models
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
    async def head300(self, **kwargs: Any) -> None:
        """Return 300 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_head300_request(
            template_url=self.head300.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 300]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 300:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    head300.metadata = {"url": "/http/redirect/300"}  # type: ignore

    @distributed_trace_async
    async def get300(self, **kwargs: Any) -> Optional[List[str]]:
        """Return 300 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str] or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[List[str]]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_get300_request(
            template_url=self.get300.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 300]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        response_headers = {}
        if response.status_code == 300:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = self._deserialize("[str]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get300.metadata = {"url": "/http/redirect/300"}  # type: ignore

    @distributed_trace_async
    async def head301(self, **kwargs: Any) -> None:
        """Return 301 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_head301_request(
            template_url=self.head301.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 301:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    head301.metadata = {"url": "/http/redirect/301"}  # type: ignore

    @distributed_trace_async
    async def get301(self, **kwargs: Any) -> None:
        """Return 301 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_get301_request(
            template_url=self.get301.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 301:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get301.metadata = {"url": "/http/redirect/301"}  # type: ignore

    @distributed_trace_async
    async def put301(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Put true Boolean value in request returns 301.  This request should not be automatically
        redirected, but should return the received 301 to the caller for evaluation.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_put301_request(
            content_type=content_type,
            json=json,
            template_url=self.put301.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    put301.metadata = {"url": "/http/redirect/301"}  # type: ignore

    @distributed_trace_async
    async def head302(self, **kwargs: Any) -> None:
        """Return 302 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_head302_request(
            template_url=self.head302.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 302:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    head302.metadata = {"url": "/http/redirect/302"}  # type: ignore

    @distributed_trace_async
    async def get302(self, **kwargs: Any) -> None:
        """Return 302 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_get302_request(
            template_url=self.get302.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 302:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get302.metadata = {"url": "/http/redirect/302"}  # type: ignore

    @distributed_trace_async
    async def patch302(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Patch true Boolean value in request returns 302.  This request should not be automatically
        redirected, but should return the received 302 to the caller for evaluation.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_patch302_request(
            content_type=content_type,
            json=json,
            template_url=self.patch302.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    patch302.metadata = {"url": "/http/redirect/302"}  # type: ignore

    @distributed_trace_async
    async def post303(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Post true Boolean value in request returns 303.  This request should be automatically
        redirected usign a get, ultimately returning a 200 status code.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_post303_request(
            content_type=content_type,
            json=json,
            template_url=self.post303.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 303]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 303:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    post303.metadata = {"url": "/http/redirect/303"}  # type: ignore

    @distributed_trace_async
    async def head307(self, **kwargs: Any) -> None:
        """Redirect with 307, resulting in a 200 success.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_head307_request(
            template_url=self.head307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    head307.metadata = {"url": "/http/redirect/307"}  # type: ignore

    @distributed_trace_async
    async def get307(self, **kwargs: Any) -> None:
        """Redirect get with 307, resulting in a 200 success.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_get307_request(
            template_url=self.get307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get307.metadata = {"url": "/http/redirect/307"}  # type: ignore

    @distributed_trace_async
    async def options307(self, **kwargs: Any) -> None:
        """options redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_http_redirects.build_options307_request(
            template_url=self.options307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    options307.metadata = {"url": "/http/redirect/307"}  # type: ignore

    @distributed_trace_async
    async def put307(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Put redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_put307_request(
            content_type=content_type,
            json=json,
            template_url=self.put307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    put307.metadata = {"url": "/http/redirect/307"}  # type: ignore

    @distributed_trace_async
    async def patch307(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Patch redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_patch307_request(
            content_type=content_type,
            json=json,
            template_url=self.patch307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    patch307.metadata = {"url": "/http/redirect/307"}  # type: ignore

    @distributed_trace_async
    async def post307(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Post redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_post307_request(
            content_type=content_type,
            json=json,
            template_url=self.post307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    post307.metadata = {"url": "/http/redirect/307"}  # type: ignore

    @distributed_trace_async
    async def delete307(self, boolean_value: Optional[bool] = True, **kwargs: Any) -> None:
        """Delete redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        if boolean_value is not None:
            json = self._serialize.body(boolean_value, "bool")
        else:
            json = None

        request = rest_http_redirects.build_delete307_request(
            content_type=content_type,
            json=json,
            template_url=self.delete307.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete307.metadata = {"url": "/http/redirect/307"}  # type: ignore
