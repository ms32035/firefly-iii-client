# firefly_iii_client.ObjectGroupsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_object_group**](ObjectGroupsApi.md#delete_object_group) | **DELETE** /api/v1/object_groups/{id} | Delete a object group.
[**get_object_group**](ObjectGroupsApi.md#get_object_group) | **GET** /api/v1/object_groups/{id} | Get a single object group.
[**list_bill_by_object_group**](ObjectGroupsApi.md#list_bill_by_object_group) | **GET** /api/v1/object_groups/{id}/bills | List all bills with this object group.
[**list_object_groups**](ObjectGroupsApi.md#list_object_groups) | **GET** /api/v1/object_groups | List all oject groups.
[**list_piggy_bank_by_object_group**](ObjectGroupsApi.md#list_piggy_bank_by_object_group) | **GET** /api/v1/object_groups/{id}/piggy_banks | List all piggy banks related to the object group.
[**update_object_group**](ObjectGroupsApi.md#update_object_group) | **PUT** /api/v1/object_groups/{id} | Update existing object group.


# **delete_object_group**
> delete_object_group(id)

Delete a object group.

Delete a object group.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import object_groups_api
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_groups_api.ObjectGroupsApi(api_client)
    id = "123" # str | The ID of the object group.

    # example passing only required values which don't have defaults set
    try:
        # Delete a object group.
        api_instance.delete_object_group(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->delete_object_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object group. |

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Object group deleted. |  -  |
**404** | No such object group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group**
> ObjectGroupSingle get_object_group(id)

Get a single object group.

Get a single object group.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import object_groups_api
from firefly_iii_client.model.object_group_single import ObjectGroupSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_groups_api.ObjectGroupsApi(api_client)
    id = "123" # str | The ID of the object group.

    # example passing only required values which don't have defaults set
    try:
        # Get a single object group.
        api_response = api_instance.get_object_group(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->get_object_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object group. |

### Return type

[**ObjectGroupSingle**](ObjectGroupSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested object group |  -  |
**404** | Object group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bill_by_object_group**
> BillArray list_bill_by_object_group(id)

List all bills with this object group.

List all bills with this object group.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import object_groups_api
from firefly_iii_client.model.bill_array import BillArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_groups_api.ObjectGroupsApi(api_client)
    id = "123" # str | The ID of the account.
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all bills with this object group.
        api_response = api_instance.list_bill_by_object_group(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->list_bill_by_object_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all bills with this object group.
        api_response = api_instance.list_bill_by_object_group(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->list_bill_by_object_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the account. |
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]

### Return type

[**BillArray**](BillArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object_groups**
> ObjectGroupArray list_object_groups()

List all oject groups.

List all oject groups.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import object_groups_api
from firefly_iii_client.model.object_group_array import ObjectGroupArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_groups_api.ObjectGroupsApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all oject groups.
        api_response = api_instance.list_object_groups(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->list_object_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**ObjectGroupArray**](ObjectGroupArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of object groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_piggy_bank_by_object_group**
> PiggyBankArray list_piggy_bank_by_object_group(id)

List all piggy banks related to the object group.

This endpoint returns a list of all the piggy banks connected to the object group. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import object_groups_api
from firefly_iii_client.model.piggy_bank_array import PiggyBankArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_groups_api.ObjectGroupsApi(api_client)
    id = "123" # str | The ID of the account.
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all piggy banks related to the object group.
        api_response = api_instance.list_piggy_bank_by_object_group(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->list_piggy_bank_by_object_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all piggy banks related to the object group.
        api_response = api_instance.list_piggy_bank_by_object_group(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->list_piggy_bank_by_object_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the account. |
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]

### Return type

[**PiggyBankArray**](PiggyBankArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group**
> ObjectGroupSingle update_object_group(id, object_group_update)

Update existing object group.

Update existing object group.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import object_groups_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.object_group_update import ObjectGroupUpdate
from firefly_iii_client.model.object_group_single import ObjectGroupSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_groups_api.ObjectGroupsApi(api_client)
    id = "123" # str | The ID of the object group
    object_group_update = ObjectGroupUpdate(
        order=1,
        title="My object group",
    ) # ObjectGroupUpdate | JSON array with updated piggy bank information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing object group.
        api_response = api_instance.update_object_group(id, object_group_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ObjectGroupsApi->update_object_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object group |
 **object_group_update** | [**ObjectGroupUpdate**](ObjectGroupUpdate.md)| JSON array with updated piggy bank information. See the model for the exact specifications. |

### Return type

[**ObjectGroupSingle**](ObjectGroupSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated object group stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

