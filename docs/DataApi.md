# firefly_iii_client.DataApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_transactions**](DataApi.md#bulk_update_transactions) | **POST** /v1/data/bulk/transactions | Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/references/firefly-iii/api/specials/
[**destroy_data**](DataApi.md#destroy_data) | **DELETE** /v1/data/destroy | Endpoint to destroy user data
[**export_accounts**](DataApi.md#export_accounts) | **GET** /v1/data/export/accounts | Export account data from Firefly III
[**export_bills**](DataApi.md#export_bills) | **GET** /v1/data/export/bills | Export bills from Firefly III
[**export_budgets**](DataApi.md#export_budgets) | **GET** /v1/data/export/budgets | Export budgets and budget amount data from Firefly III
[**export_categories**](DataApi.md#export_categories) | **GET** /v1/data/export/categories | Export category data from Firefly III
[**export_piggies**](DataApi.md#export_piggies) | **GET** /v1/data/export/piggy-banks | Export piggy banks from Firefly III
[**export_recurring**](DataApi.md#export_recurring) | **GET** /v1/data/export/recurring | Export recurring transaction data from Firefly III
[**export_rules**](DataApi.md#export_rules) | **GET** /v1/data/export/rules | Export rule groups and rule data from Firefly III
[**export_tags**](DataApi.md#export_tags) | **GET** /v1/data/export/tags | Export tag data from Firefly III
[**export_transactions**](DataApi.md#export_transactions) | **GET** /v1/data/export/transactions | Export transaction data from Firefly III
[**purge_data**](DataApi.md#purge_data) | **DELETE** /v1/data/purge | Endpoint to purge user data


# **bulk_update_transactions**
> bulk_update_transactions(query, x_trace_id=x_trace_id)

Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/references/firefly-iii/api/specials/

Allows you to update transactions in bulk.


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
    api_instance = firefly_iii_client.DataApi(api_client)
    query = 'query_example' # str | The JSON query.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/references/firefly-iii/api/specials/
        api_instance.bulk_update_transactions(query, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DataApi->bulk_update_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The JSON query. | 
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
**204** | Empty response when the update was successful. A future improvement is to include the changed transactions. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_data**
> destroy_data(objects, x_trace_id=x_trace_id)

Endpoint to destroy user data

A call to this endpoint deletes the requested data type. Use it with care and always with user permission.
The demo user is incapable of using this endpoint.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.data_destroy_object import DataDestroyObject
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
    api_instance = firefly_iii_client.DataApi(api_client)
    objects = firefly_iii_client.DataDestroyObject() # DataDestroyObject | The type of data that you wish to destroy. You can only use one at a time.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Endpoint to destroy user data
        api_instance.destroy_data(objects, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DataApi->destroy_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objects** | [**DataDestroyObject**](.md)| The type of data that you wish to destroy. You can only use one at a time. | 
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
**204** | Empty response when data has been destroyed. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_accounts**
> bytearray export_accounts(x_trace_id=x_trace_id, type=type)

Export account data from Firefly III

This endpoint allows you to export your accounts from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export account data from Firefly III
        api_response = api_instance.export_accounts(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_bills**
> bytearray export_bills(x_trace_id=x_trace_id, type=type)

Export bills from Firefly III

This endpoint allows you to export your bills from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export bills from Firefly III
        api_response = api_instance.export_bills(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_bills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_bills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_budgets**
> bytearray export_budgets(x_trace_id=x_trace_id, type=type)

Export budgets and budget amount data from Firefly III

This endpoint allows you to export your budgets and associated budget data from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export budgets and budget amount data from Firefly III
        api_response = api_instance.export_budgets(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_categories**
> bytearray export_categories(x_trace_id=x_trace_id, type=type)

Export category data from Firefly III

This endpoint allows you to export your categories from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export category data from Firefly III
        api_response = api_instance.export_categories(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_piggies**
> bytearray export_piggies(x_trace_id=x_trace_id, type=type)

Export piggy banks from Firefly III

This endpoint allows you to export your piggy banks from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export piggy banks from Firefly III
        api_response = api_instance.export_piggies(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_piggies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_piggies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_recurring**
> bytearray export_recurring(x_trace_id=x_trace_id, type=type)

Export recurring transaction data from Firefly III

This endpoint allows you to export your recurring transactions from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export recurring transaction data from Firefly III
        api_response = api_instance.export_recurring(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_recurring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_recurring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_rules**
> bytearray export_rules(x_trace_id=x_trace_id, type=type)

Export rule groups and rule data from Firefly III

This endpoint allows you to export your rules and rule groups from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export rule groups and rule data from Firefly III
        api_response = api_instance.export_rules(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_tags**
> bytearray export_tags(x_trace_id=x_trace_id, type=type)

Export tag data from Firefly III

This endpoint allows you to export your tags from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export tag data from Firefly III
        api_response = api_instance.export_tags(x_trace_id=x_trace_id, type=type)
        print("The response of DataApi->export_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_transactions**
> bytearray export_transactions(start, end, x_trace_id=x_trace_id, accounts=accounts, type=type)

Export transaction data from Firefly III

This endpoint allows you to export transactions from Firefly III into a file. Currently supports CSV exports only.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.export_file_filter import ExportFileFilter
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
    api_instance = firefly_iii_client.DataApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
    end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    accounts = '1,2,3' # str | Limit the export of transactions to these accounts only. Only asset accounts will be accepted. Other types will be silently dropped.  (optional)
    type = firefly_iii_client.ExportFileFilter() # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    try:
        # Export transaction data from Firefly III
        api_response = api_instance.export_transactions(start, end, x_trace_id=x_trace_id, accounts=accounts, type=type)
        print("The response of DataApi->export_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->export_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **accounts** | **str**| Limit the export of transactions to these accounts only. Only asset accounts will be accepted. Other types will be silently dropped.  | [optional] 
 **type** | [**ExportFileFilter**](.md)| The file type the export file (CSV is currently the only option). | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_data**
> purge_data(x_trace_id=x_trace_id)

Endpoint to purge user data

A call to this endpoint purges all previously deleted data. Use it with care and always with user permission.
The demo user is incapable of using this endpoint.


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
    api_instance = firefly_iii_client.DataApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Endpoint to purge user data
        api_instance.purge_data(x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DataApi->purge_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | Empty response when data has been purged. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

