# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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
from azure.core.utils import case_insensitive_dict

from ..._operations._operations import (
    build_get_cat_request,
    build_get_feline_request,
    build_get_horse_request,
    build_get_kitten_request,
    build_get_pet_request,
    build_put_cat_request,
    build_put_feline_request,
    build_put_horse_request,
    build_put_kitten_request,
    build_put_pet_request,
)
from .._vendor import MixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MultipleInheritanceServiceClientOperationsMixin(MixinABC):
    @distributed_trace_async
    async def get_horse(self, **kwargs: Any) -> JSON:
        """Get a horse with name 'Fred' and isAShowHorse true.

        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "isAShowHorse": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_horse_request(
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def put_horse(self, horse: JSON, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Put a horse with name 'General' and isAShowHorse false.

        :param horse: Put a horse with name 'General' and isAShowHorse false. Required.
        :type horse: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                horse = {
                    "isAShowHorse": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """

        ...

    @overload
    async def put_horse(self, horse: IO, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Put a horse with name 'General' and isAShowHorse false.

        :param horse: Put a horse with name 'General' and isAShowHorse false. Required.
        :type horse: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def put_horse(self, horse: Union[JSON, IO], **kwargs: Any) -> str:
        """Put a horse with name 'General' and isAShowHorse false.

        :param horse: Put a horse with name 'General' and isAShowHorse false. Is either a model type or
         a IO type. Required.
        :type horse: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        if isinstance(horse, (IO, bytes)):
            _content = horse
        else:
            _json = horse
            content_type = content_type or "application/json"

        request = build_put_horse_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_pet(self, **kwargs: Any) -> JSON:
        """Get a pet with name 'Peanut'.

        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_pet_request(
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def put_pet(self, pet: JSON, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Put a pet with name 'Butter'.

        :param pet: Put a pet with name 'Butter'. Required.
        :type pet: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                pet = {
                    "name": "str"  # Required.
                }
        """

        ...

    @overload
    async def put_pet(self, pet: IO, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Put a pet with name 'Butter'.

        :param pet: Put a pet with name 'Butter'. Required.
        :type pet: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def put_pet(self, pet: Union[JSON, IO], **kwargs: Any) -> str:
        """Put a pet with name 'Butter'.

        :param pet: Put a pet with name 'Butter'. Is either a model type or a IO type. Required.
        :type pet: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        if isinstance(pet, (IO, bytes)):
            _content = pet
        else:
            _json = pet
            content_type = content_type or "application/json"

        request = build_put_pet_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_feline(self, **kwargs: Any) -> JSON:
        """Get a feline where meows and hisses are true.

        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "hisses": bool,  # Optional.
                    "meows": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_feline_request(
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def put_feline(self, feline: JSON, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Put a feline who hisses and doesn't meow.

        :param feline: Put a feline who hisses and doesn't meow. Required.
        :type feline: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                feline = {
                    "hisses": bool,  # Optional.
                    "meows": bool  # Optional.
                }
        """

        ...

    @overload
    async def put_feline(self, feline: IO, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Put a feline who hisses and doesn't meow.

        :param feline: Put a feline who hisses and doesn't meow. Required.
        :type feline: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def put_feline(self, feline: Union[JSON, IO], **kwargs: Any) -> str:
        """Put a feline who hisses and doesn't meow.

        :param feline: Put a feline who hisses and doesn't meow. Is either a model type or a IO type.
         Required.
        :type feline: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        if isinstance(feline, (IO, bytes)):
            _content = feline
        else:
            _json = feline
            content_type = content_type or "application/json"

        request = build_put_feline_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_cat(self, **kwargs: Any) -> JSON:
        """Get a cat with name 'Whiskers' where likesMilk, meows, and hisses is true.

        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_cat_request(
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def put_cat(self, cat: JSON, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

        :param cat: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.
         Required.
        :type cat: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                cat = {
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """

        ...

    @overload
    async def put_cat(self, cat: IO, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

        :param cat: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.
         Required.
        :type cat: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def put_cat(self, cat: Union[JSON, IO], **kwargs: Any) -> str:
        """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

        :param cat: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true. Is
         either a model type or a IO type. Required.
        :type cat: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        if isinstance(cat, (IO, bytes)):
            _content = cat
        else:
            _json = cat
            content_type = content_type or "application/json"

        request = build_put_cat_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_kitten(self, **kwargs: Any) -> JSON:
        """Get a kitten with name 'Gatito' where likesMilk and meows is true, and hisses and eatsMiceYet
        is false.

        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "eatsMiceYet": bool,  # Optional.
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_kitten_request(
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def put_kitten(self, kitten: JSON, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
        true.

        :param kitten: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
         eatsMiceYet is true. Required.
        :type kitten: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                kitten = {
                    "eatsMiceYet": bool,  # Optional.
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """

        ...

    @overload
    async def put_kitten(self, kitten: IO, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
        true.

        :param kitten: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
         eatsMiceYet is true. Required.
        :type kitten: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def put_kitten(self, kitten: Union[JSON, IO], **kwargs: Any) -> str:
        """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
        true.

        :param kitten: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
         eatsMiceYet is true. Is either a model type or a IO type. Required.
        :type kitten: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = None
        _content = None
        if isinstance(kitten, (IO, bytes)):
            _content = kitten
        else:
            _json = kitten
            content_type = content_type or "application/json"

        request = build_put_kitten_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)
