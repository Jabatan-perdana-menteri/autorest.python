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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from ..rest import storage_accounts as rest_storage_accounts

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class StorageAccountsOperations(object):
    """StorageAccountsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~storageversiontolerant.models
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

    @distributed_trace
    def check_name_availability(
        self,
        account_name,  # type: "_models.StorageAccountCheckNameAvailabilityParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.CheckNameAvailabilityResult"
        """Checks that account name is valid and is not in use.

        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name:
         ~storageversiontolerant.models.StorageAccountCheckNameAvailabilityParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult, or the result of cls(response)
        :rtype: ~storageversiontolerant.models.CheckNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.CheckNameAvailabilityResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(account_name, "StorageAccountCheckNameAvailabilityParameters")

        request = rest_storage_accounts.build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self.check_name_availability.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability"}  # type: ignore

    def _create_initial(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        parameters,  # type: "_models.StorageAccountCreateParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.StorageAccount"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.StorageAccount"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "StorageAccountCreateParameters")

        request = rest_storage_accounts.build_create_request_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self._create_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("StorageAccount", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace
    def begin_create(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        parameters,  # type: "_models.StorageAccountCreateParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.StorageAccount"]
        """Asynchronously creates a new storage account with the specified parameters. Existing accounts
        cannot be updated with this API and should instead use the Update Storage Account API. If an
        account is already created and subsequent PUT request is issued with exact same set of
        properties, then HTTP 200 would be returned.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to provide for the created account.
        :type parameters: ~storageversiontolerant.models.StorageAccountCreateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either StorageAccount or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~storageversiontolerant.models.StorageAccount]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccount"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_initial(
                resource_group_name=resource_group_name,
                account_name=account_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("StorageAccount", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace
    def delete(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a storage account in Microsoft Azure.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_storage_accounts.build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace
    def get_properties(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageAccount"
        """Returns the properties for the specified storage account including but not limited to name,
        account type, location, and account status. The ListKeys operation should be used to retrieve
        storage keys.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccount, or the result of cls(response)
        :rtype: ~storageversiontolerant.models.StorageAccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccount"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_storage_accounts.build_get_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get_properties.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccount", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_properties.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace
    def update(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        parameters,  # type: "_models.StorageAccountUpdateParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageAccount"
        """Updates the account type or tags for a storage account. It can also be used to add a custom
        domain (note that custom domains cannot be added via the Create operation). Only one custom
        domain is supported per storage account. This API can only be used to update one of tags,
        accountType, or customDomain per call. To update multiple of these properties, call the API
        multiple times with one change per call. This call does not change the storage keys for the
        account. If you want to change storage account keys, use the RegenerateKey operation. The
        location and name of the storage account cannot be changed after creation.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to update on the account. Note that only one property can be
         changed at a time using this API.
        :type parameters: ~storageversiontolerant.models.StorageAccountUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccount, or the result of cls(response)
        :rtype: ~storageversiontolerant.models.StorageAccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccount"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "StorageAccountUpdateParameters")

        request = rest_storage_accounts.build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self.update.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccount", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace
    def list_keys(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageAccountKeys"
        """Lists the access keys for the specified storage account.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountKeys, or the result of cls(response)
        :rtype: ~storageversiontolerant.models.StorageAccountKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccountKeys"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_storage_accounts.build_list_keys_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            template_url=self.list_keys.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccountKeys", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_keys.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys"}  # type: ignore

    @distributed_trace
    def list(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.StorageAccountListResult"]
        """Lists all the storage accounts available under the subscription. Note that storage keys are not
        returned; use the ListKeys operation for this.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StorageAccountListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~storageversiontolerant.models.StorageAccountListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccountListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_storage_accounts.build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = rest_storage_accounts.build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("StorageAccountListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.StorageAccountListResult"]
        """Lists all the storage accounts available under the given resource group. Note that storage keys
        are not returned; use the ListKeys operation for this.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StorageAccountListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~storageversiontolerant.models.StorageAccountListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccountListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_storage_accounts.build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_resource_group.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = rest_storage_accounts.build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("StorageAccountListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts"}  # type: ignore

    @distributed_trace
    def regenerate_key(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        regenerate_key,  # type: "_models.StorageAccountRegenerateKeyParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageAccountKeys"
        """Regenerates the access keys for the specified storage account.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param regenerate_key: Specifies name of the key which should be regenerated.
        :type regenerate_key: ~storageversiontolerant.models.StorageAccountRegenerateKeyParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountKeys, or the result of cls(response)
        :rtype: ~storageversiontolerant.models.StorageAccountKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StorageAccountKeys"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(regenerate_key, "StorageAccountRegenerateKeyParameters")

        request = rest_storage_accounts.build_regenerate_key_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self.regenerate_key.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccountKeys", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regenerate_key.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey"}  # type: ignore
