# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin:

    def _test_paging_request(
        self,
        **kwargs: Any
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._test_paging_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        return self._client.get(url, query_parameters, header_parameters)
    _test_paging_request.metadata = {'url': '/multiapi/paging'}  # type: ignore

    def test_paging(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.PagingResult"]:
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.multiapi.sample.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagingResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            if not next_link:
                request = self._test_paging_request(**kwargs)

            else:
                request = self._test_paging_request(**kwargs)

                # little hacky, but this code will soon be replaced with code that won't need the hack
                request.method = "get"
                request.url = self._client.format_url(next_link)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PagingResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    test_paging.metadata = {'url': '/multiapi/paging'}  # type: ignore

    def _test_different_calls_request(
        self,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        greeting_in_french: Optional[str] = None,
        **kwargs: Any
    ) -> HttpRequest:
        api_version = "3.0.0"
        accept = "application/json"

        # Construct URL
        url = self._test_different_calls_request.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['greetingInEnglish'] = self._serialize.header("greeting_in_english", greeting_in_english, 'str')
        if greeting_in_chinese is not None:
            header_parameters['greetingInChinese'] = self._serialize.header("greeting_in_chinese", greeting_in_chinese, 'str')
        if greeting_in_french is not None:
            header_parameters['greetingInFrench'] = self._serialize.header("greeting_in_french", greeting_in_french, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        return self._client.get(url, query_parameters, header_parameters)
    _test_different_calls_request.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

    async def test_different_calls(
        self,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        greeting_in_french: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test.
        :type greeting_in_chinese: str
        :param greeting_in_french: pass in 'bonjour' to pass test.
        :type greeting_in_french: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        request = self._test_different_calls_request(
            greeting_in_english=greeting_in_english,
            greeting_in_chinese=greeting_in_chinese,
            greeting_in_french=greeting_in_french,
            **kwargs
        )
        kwargs.pop('content_type', None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

