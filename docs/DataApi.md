# firefly_iii_client.DataApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_transactions**](DataApi.md#bulk_update_transactions) | **POST** /api/v1/data/bulk/transactions | Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/firefly-iii/api/specials
[**destroy_data**](DataApi.md#destroy_data) | **DELETE** /api/v1/data/destroy | Endpoint to destroy user data
[**export_accounts**](DataApi.md#export_accounts) | **GET** /api/v1/data/export/accounts | Export account data from Firefly III
[**export_bills**](DataApi.md#export_bills) | **GET** /api/v1/data/export/bills | Export bills from Firefly III
[**export_budgets**](DataApi.md#export_budgets) | **GET** /api/v1/data/export/budgets | Export budgets and budget amount data from Firefly III
[**export_categories**](DataApi.md#export_categories) | **GET** /api/v1/data/export/categories | Export category data from Firefly III
[**export_piggies**](DataApi.md#export_piggies) | **GET** /api/v1/data/export/piggy-banks | Export piggy banks from Firefly III
[**export_recurring**](DataApi.md#export_recurring) | **GET** /api/v1/data/export/recurring | Export recurring transaction data from Firefly III
[**export_rules**](DataApi.md#export_rules) | **GET** /api/v1/data/export/rules | Export rule groups and rule data from Firefly III
[**export_tags**](DataApi.md#export_tags) | **GET** /api/v1/data/export/tags | Export tag data from Firefly III
[**export_transactions**](DataApi.md#export_transactions) | **GET** /api/v1/data/export/transactions | Export transaction data from Firefly III


# **bulk_update_transactions**
> bulk_update_transactions(query)

Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/firefly-iii/api/specials

Allows you to update transactions in bulk. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
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
    api_instance = data_api.DataApi(api_client)
    query = "query_example" # str | The JSON query.

    # example passing only required values which don't have defaults set
    try:
        # Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/firefly-iii/api/specials
        api_instance.bulk_update_transactions(query)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->bulk_update_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The JSON query. |

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
**204** | Empty response when the update was successful. A future improvement is to include the changed transactions. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_data**
> destroy_data(objects)

Endpoint to destroy user data

A call to this endpoint permanently destroys the requested data type. Use it with care and always with user permission. The demo user is incapable of using this endpoint. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.data_destroy_object import DataDestroyObject
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
    api_instance = data_api.DataApi(api_client)
    objects = DataDestroyObject("budgets") # DataDestroyObject | The type of data that you wish to destroy. You can only use one at a time.

    # example passing only required values which don't have defaults set
    try:
        # Endpoint to destroy user data
        api_instance.destroy_data(objects)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->destroy_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objects** | **DataDestroyObject**| The type of data that you wish to destroy. You can only use one at a time. |

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
**204** | Empty response when data has been destroyed. |  -  |
**500** | Internal error, or user is unauthorized to destroy data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_accounts**
> file_type export_accounts()

Export account data from Firefly III

This endpoint allows you to export your accounts from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export account data from Firefly III
        api_response = api_instance.export_accounts(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_bills**
> file_type export_bills()

Export bills from Firefly III

This endpoint allows you to export your bills from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export bills from Firefly III
        api_response = api_instance.export_bills(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_bills: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_budgets**
> file_type export_budgets()

Export budgets and budget amount data from Firefly III

This endpoint allows you to export your budgets and associated budget data from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export budgets and budget amount data from Firefly III
        api_response = api_instance.export_budgets(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_budgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_categories**
> file_type export_categories()

Export category data from Firefly III

This endpoint allows you to export your categories from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export category data from Firefly III
        api_response = api_instance.export_categories(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_piggies**
> file_type export_piggies()

Export piggy banks from Firefly III

This endpoint allows you to export your piggy banks from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export piggy banks from Firefly III
        api_response = api_instance.export_piggies(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_piggies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_recurring**
> file_type export_recurring()

Export recurring transaction data from Firefly III

This endpoint allows you to export your recurring transactions from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export recurring transaction data from Firefly III
        api_response = api_instance.export_recurring(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_recurring: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_rules**
> file_type export_rules()

Export rule groups and rule data from Firefly III

This endpoint allows you to export your rules and rule groups from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export rule groups and rule data from Firefly III
        api_response = api_instance.export_rules(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_tags**
> file_type export_tags()

Export tag data from Firefly III

This endpoint allows you to export your tags from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export tag data from Firefly III
        api_response = api_instance.export_tags(type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_transactions**
> file_type export_transactions(start, end)

Export transaction data from Firefly III

This endpoint allows you to export transactions from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
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
    api_instance = data_api.DataApi(api_client)
    start = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. 
    accounts = "1,2,3" # str | Limit the export of transactions to these accounts only. Only asset accounts will be accepted. Other types will be silently dropped.  (optional)
    type = ExportFileFilter("csv") # ExportFileFilter | The file type the export file (CSV is currently the only option). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export transaction data from Firefly III
        api_response = api_instance.export_transactions(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export transaction data from Firefly III
        api_response = api_instance.export_transactions(start, end, accounts=accounts, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **str**| Limit the export of transactions to these accounts only. Only asset accounts will be accepted. Other types will be silently dropped.  | [optional]
 **type** | **ExportFileFilter**| The file type the export file (CSV is currently the only option). | [optional]

### Return type

**file_type**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported transaction in a file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

