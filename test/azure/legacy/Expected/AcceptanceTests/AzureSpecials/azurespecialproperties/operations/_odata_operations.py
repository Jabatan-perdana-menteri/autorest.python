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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_with_filter_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    filter = kwargs.pop('filter', None)  # type: Optional[str]
    top = kwargs.pop('top', None)  # type: Optional[int]
    orderby = kwargs.pop('orderby', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/odata/filter")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if filter is not None:
        _query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')
    if top is not None:
        _query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    if orderby is not None:
        _query_parameters['$orderby'] = _SERIALIZER.query("orderby", orderby, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class OdataOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azurespecialproperties.AutoRestAzureSpecialParametersTestClient`'s
        :attr:`odata` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_with_filter(  # pylint: disable=inconsistent-return-statements
        self,
        filter=None,  # type: Optional[str]
        top=None,  # type: Optional[int]
        orderby=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Specify filter parameter with value '$filter=id gt 5 and name eq 'foo'&$orderby=id&$top=10'.

        :param filter: The filter parameter with value '$filter=id gt 5 and name eq 'foo''. Default
         value is None.
        :type filter: str
        :param top: The top parameter with value 10. Default value is None.
        :type top: int
        :param orderby: The orderby parameter with value id. Default value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_with_filter_request(
            filter=filter,
            top=top,
            orderby=orderby,
            template_url=self.get_with_filter.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_with_filter.metadata = {"url": "/azurespecials/odata/filter"}  # type: ignore
