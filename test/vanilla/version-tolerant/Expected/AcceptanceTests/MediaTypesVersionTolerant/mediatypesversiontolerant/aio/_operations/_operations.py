# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union

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

from ..._operations._operations import (
    build_analyze_body_no_accept_header_request,
    build_analyze_body_request,
    build_binary_body_with_three_content_types_request,
    build_binary_body_with_two_content_types_request,
    build_content_type_with_encoding_request,
    build_put_text_and_json_body_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MediaTypesClientOperationsMixin(MixinABC):
    @distributed_trace_async
    async def analyze_body(self, input: Optional[Union[IO, JSONType]] = None, **kwargs: Any) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter.
        :type input: IO or JSONType
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "application/pdf", "image/jpeg", "image/png",
         "image/tiff", "application/json."
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "source": "str"  # Optional. File source path.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            if input is not None:
                _json = input
        elif content_type.split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
            _content = input
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_analyze_body_request(
            content_type=content_type,
            json=_json,
            content=_content,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[Union[IO, JSONType]] = None, **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter.
        :type input: IO or JSONType
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "application/pdf", "image/jpeg", "image/png",
         "image/tiff", "application/json."
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "source": "str"  # Optional. File source path.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            if input is not None:
                _json = input
        elif content_type.split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
            _content = input
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_analyze_body_no_accept_header_request(
            content_type=content_type,
            json=_json,
            content=_content,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def content_type_with_encoding(self, input: Optional[str] = None, **kwargs: Any) -> str:
        """Pass in contentType 'text/plain; charset=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter.
        :type input: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "text/plain; charset=UTF-8")  # type: Optional[str]

        _content = input

        request = build_content_type_with_encoding_request(
            content_type=content_type,
            content=_content,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def binary_body_with_two_content_types(self, message: Union[IO, JSONType], **kwargs: Any) -> str:
        """Binary body with two content types. Pass in of {'hello': 'world'} for the application/json
        content type, and a byte stream of 'hello, world!' for application/octet-stream.

        :param message: The payload body.
        :type message: IO or JSONType
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", None)  # type: Optional[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            _json = message
        elif content_type.split(";")[0] in ["application/octet-stream"]:
            _content = message
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/json', 'application/octet-stream']".format(content_type)
            )

        request = build_binary_body_with_two_content_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def binary_body_with_three_content_types(self, message: Union[IO, str], **kwargs: Any) -> str:
        """Binary body with three content types. Pass in string 'hello, world' with content type
        'text/plain', {'hello': world'} with content type 'application/json' and a byte string for
        'application/octet-stream'.

        :param message: The payload body.
        :type message: IO or str
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "application/json", "application/octet-stream",
         "text/plain."
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            _json = message
        elif content_type.split(";")[0] in ["application/octet-stream", "text/plain"]:
            _content = message
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/json', 'application/octet-stream', 'text/plain']".format(content_type)
            )

        request = build_binary_body_with_three_content_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def put_text_and_json_body(self, message: Union[str, str], **kwargs: Any) -> str:
        """Body that's either text/plain or application/json.

        :param message: The payload body.
        :type message: str or str
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "text/plain", "application/json."
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ["application/json"]:
            _json = message
        elif content_type.split(";")[0] in ["text/plain"]:
            _content = message
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['text/plain', 'application/json']".format(content_type)
            )

        request = build_put_text_and_json_body_request(
            content_type=content_type,
            json=_json,
            content=_content,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
