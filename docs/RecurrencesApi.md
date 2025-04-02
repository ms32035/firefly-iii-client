# firefly_iii_client.RecurrencesApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recurrence**](RecurrencesApi.md#delete_recurrence) | **DELETE** /v1/recurrences/{id} | Delete a recurring transaction.
[**get_recurrence**](RecurrencesApi.md#get_recurrence) | **GET** /v1/recurrences/{id} | Get a single recurring transaction.
[**list_recurrence**](RecurrencesApi.md#list_recurrence) | **GET** /v1/recurrences | List all recurring transactions.
[**list_transaction_by_recurrence**](RecurrencesApi.md#list_transaction_by_recurrence) | **GET** /v1/recurrences/{id}/transactions | List all transactions created by a recurring transaction.
[**store_recurrence**](RecurrencesApi.md#store_recurrence) | **POST** /v1/recurrences | Store a new recurring transaction
[**update_recurrence**](RecurrencesApi.md#update_recurrence) | **PUT** /v1/recurrences/{id} | Update existing recurring transaction.


# **delete_recurrence**
> delete_recurrence(id, x_trace_id=x_trace_id)

Delete a recurring transaction.

Delete a recurring transaction. Transactions created by the recurring transaction will not be deleted.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.RecurrencesApi(api_client)
    id = '123' # str | The ID of the recurring transaction.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Delete a recurring transaction.
        api_instance.delete_recurrence(id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling RecurrencesApi->delete_recurrence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the recurring transaction. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Recurring transaction deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurrence**
> RecurrenceSingle get_recurrence(id, x_trace_id=x_trace_id)

Get a single recurring transaction.

Get a single recurring transaction.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.recurrence_single import RecurrenceSingle
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.RecurrencesApi(api_client)
    id = '123' # str | The ID of the recurring transaction.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Get a single recurring transaction.
        api_response = api_instance.get_recurrence(id, x_trace_id=x_trace_id)
        print("The response of RecurrencesApi->get_recurrence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurrencesApi->get_recurrence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the recurring transaction. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested recurring transaction |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recurrence**
> RecurrenceArray list_recurrence(x_trace_id=x_trace_id, limit=limit, page=page)

List all recurring transactions.

List all recurring transactions.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.recurrence_array import RecurrenceArray
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.RecurrencesApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all recurring transactions.
        api_response = api_instance.list_recurrence(x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of RecurrencesApi->list_recurrence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurrencesApi->list_recurrence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**RecurrenceArray**](RecurrenceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recurring transactions. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_recurrence**
> TransactionArray list_transaction_by_recurrence(id, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)

List all transactions created by a recurring transaction.

List all transactions created by a recurring transaction, optionally limited to the date ranges specified.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.transaction_array import TransactionArray
from firefly_iii_client.models.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.RecurrencesApi(api_client)
    id = '123' # str | The ID of the recurring transaction.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. Both the start and end date must be present.  (optional)
    end = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. Both the start and end date must be present.  (optional)
    type = firefly_iii_client.TransactionTypeFilter() # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    try:
        # List all transactions created by a recurring transaction.
        api_response = api_instance.list_transaction_by_recurrence(id, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)
        print("The response of RecurrencesApi->list_transaction_by_recurrence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurrencesApi->list_transaction_by_recurrence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the recurring transaction. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD. Both the start and end date must be present.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD. Both the start and end date must be present.  | [optional] 
 **type** | [**TransactionTypeFilter**](.md)| Optional filter on the transaction type(s) returned | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_recurrence**
> RecurrenceSingle store_recurrence(recurrence_store, x_trace_id=x_trace_id)

Store a new recurring transaction

Creates a new recurring transaction. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.recurrence_single import RecurrenceSingle
from firefly_iii_client.models.recurrence_store import RecurrenceStore
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.RecurrencesApi(api_client)
    recurrence_store = firefly_iii_client.RecurrenceStore() # RecurrenceStore | JSON array or key=value pairs with the necessary recurring transaction information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store a new recurring transaction
        api_response = api_instance.store_recurrence(recurrence_store, x_trace_id=x_trace_id)
        print("The response of RecurrencesApi->store_recurrence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurrencesApi->store_recurrence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurrence_store** | [**RecurrenceStore**](RecurrenceStore.md)| JSON array or key&#x3D;value pairs with the necessary recurring transaction information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New recurring transaction stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recurrence**
> RecurrenceSingle update_recurrence(id, recurrence_update, x_trace_id=x_trace_id)

Update existing recurring transaction.

Update existing recurring transaction.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.recurrence_single import RecurrenceSingle
from firefly_iii_client.models.recurrence_update import RecurrenceUpdate
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.RecurrencesApi(api_client)
    id = '123' # str | The ID of the recurring transaction.
    recurrence_update = firefly_iii_client.RecurrenceUpdate() # RecurrenceUpdate | JSON array with updated recurring transaction information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing recurring transaction.
        api_response = api_instance.update_recurrence(id, recurrence_update, x_trace_id=x_trace_id)
        print("The response of RecurrencesApi->update_recurrence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurrencesApi->update_recurrence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the recurring transaction. | 
 **recurrence_update** | [**RecurrenceUpdate**](RecurrenceUpdate.md)| JSON array with updated recurring transaction information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated recurring transaction stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

