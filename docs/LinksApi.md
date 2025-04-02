# firefly_iii_client.LinksApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_link_type**](LinksApi.md#delete_link_type) | **DELETE** /v1/link-types/{id} | Permanently delete link type.
[**delete_transaction_link**](LinksApi.md#delete_transaction_link) | **DELETE** /v1/transaction-links/{id} | Permanently delete link between transactions.
[**get_link_type**](LinksApi.md#get_link_type) | **GET** /v1/link-types/{id} | Get single a link type.
[**get_transaction_link**](LinksApi.md#get_transaction_link) | **GET** /v1/transaction-links/{id} | Get a single link.
[**list_link_type**](LinksApi.md#list_link_type) | **GET** /v1/link-types | List all types of links.
[**list_transaction_by_link_type**](LinksApi.md#list_transaction_by_link_type) | **GET** /v1/link-types/{id}/transactions | List all transactions under this link type.
[**list_transaction_link**](LinksApi.md#list_transaction_link) | **GET** /v1/transaction-links | List all transaction links.
[**store_link_type**](LinksApi.md#store_link_type) | **POST** /v1/link-types | Create a new link type
[**store_transaction_link**](LinksApi.md#store_transaction_link) | **POST** /v1/transaction-links | Create a new link between transactions
[**update_currency_exchange_rate**](LinksApi.md#update_currency_exchange_rate) | **PUT** /v1/exchange-rates/{id} | Update existing currency exchange rate.
[**update_link_type**](LinksApi.md#update_link_type) | **PUT** /v1/link-types/{id} | Update existing link type.
[**update_transaction_link**](LinksApi.md#update_transaction_link) | **PUT** /v1/transaction-links/{id} | Update an existing link between transactions.


# **delete_link_type**
> delete_link_type(id, x_trace_id=x_trace_id)

Permanently delete link type.

Will permanently delete a link type. The links between transactions will be removed. The transactions themselves remain. You cannot delete some of the system provided link types, indicated by the editable=false flag when you list it.


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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the link type.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Permanently delete link type.
        api_instance.delete_link_type(id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling LinksApi->delete_link_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. | 
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
**204** | Link type deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_link**
> delete_transaction_link(id, x_trace_id=x_trace_id)

Permanently delete link between transactions.

Will permanently delete link. Transactions remain.


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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the transaction link.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Permanently delete link between transactions.
        api_instance.delete_transaction_link(id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling LinksApi->delete_transaction_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction link. | 
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
**204** | Transaction link deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_type**
> LinkTypeSingle get_link_type(id, x_trace_id=x_trace_id)

Get single a link type.

Returns a single link type by its ID.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.link_type_single import LinkTypeSingle
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the link type.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Get single a link type.
        api_response = api_instance.get_link_type(id, x_trace_id=x_trace_id)
        print("The response of LinksApi->get_link_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->get_link_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested link type |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_link**
> TransactionLinkSingle get_transaction_link(id, x_trace_id=x_trace_id)

Get a single link.

Returns a single link by its ID.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.transaction_link_single import TransactionLinkSingle
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the transaction link.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Get a single link.
        api_response = api_instance.get_transaction_link(id, x_trace_id=x_trace_id)
        print("The response of LinksApi->get_transaction_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->get_transaction_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction link. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested link |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_link_type**
> LinkTypeArray list_link_type(x_trace_id=x_trace_id, limit=limit, page=page)

List all types of links.

List all the link types the system has. These include the default ones as well as any new ones.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.link_type_array import LinkTypeArray
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all types of links.
        api_response = api_instance.list_link_type(x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of LinksApi->list_link_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->list_link_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**LinkTypeArray**](LinkTypeArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of link types. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_link_type**
> TransactionArray list_transaction_by_link_type(id, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)

List all transactions under this link type.

List all transactions under this link type, both the inward and outward transactions.


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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the link type.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD, to limit the results.  (optional)
    end = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD, to limit the results.  (optional)
    type = firefly_iii_client.TransactionTypeFilter() # TransactionTypeFilter | Optional filter on the transaction type(s) returned. (optional)

    try:
        # List all transactions under this link type.
        api_response = api_instance.list_transaction_by_link_type(id, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)
        print("The response of LinksApi->list_transaction_by_link_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->list_transaction_by_link_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the results.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the results.  | [optional] 
 **type** | [**TransactionTypeFilter**](.md)| Optional filter on the transaction type(s) returned. | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_link**
> TransactionLinkArray list_transaction_link(x_trace_id=x_trace_id, limit=limit, page=page)

List all transaction links.

List all the transaction links.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.transaction_link_array import TransactionLinkArray
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all transaction links.
        api_response = api_instance.list_transaction_link(x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of LinksApi->list_transaction_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->list_transaction_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**TransactionLinkArray**](TransactionLinkArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction links |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_link_type**
> LinkTypeSingle store_link_type(link_type, x_trace_id=x_trace_id)

Create a new link type

Creates a new link type. The data required can be submitted as a JSON body or as a list of parameters (in key=value pairs, like a webform).

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.link_type import LinkType
from firefly_iii_client.models.link_type_single import LinkTypeSingle
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    link_type = firefly_iii_client.LinkType() # LinkType | JSON array with the necessary link type information or key=value pairs. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Create a new link type
        api_response = api_instance.store_link_type(link_type, x_trace_id=x_trace_id)
        print("The response of LinksApi->store_link_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->store_link_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_type** | [**LinkType**](LinkType.md)| JSON array with the necessary link type information or key&#x3D;value pairs. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New link type stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_transaction_link**
> TransactionLinkSingle store_transaction_link(transaction_link_store, x_trace_id=x_trace_id)

Create a new link between transactions

Store a new link between two transactions. For this end point you need the journal_id from a transaction.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.transaction_link_single import TransactionLinkSingle
from firefly_iii_client.models.transaction_link_store import TransactionLinkStore
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    transaction_link_store = firefly_iii_client.TransactionLinkStore() # TransactionLinkStore | JSON array with the necessary link type information or key=value pairs. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Create a new link between transactions
        api_response = api_instance.store_transaction_link(transaction_link_store, x_trace_id=x_trace_id)
        print("The response of LinksApi->store_transaction_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->store_transaction_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_link_store** | [**TransactionLinkStore**](TransactionLinkStore.md)| JSON array with the necessary link type information or key&#x3D;value pairs. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New transaction link stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency_exchange_rate**
> CurrencyExchangeRateSingle update_currency_exchange_rate(id, currency_exchange_rate_update, x_trace_id=x_trace_id)

Update existing currency exchange rate.

Used to update a single currency exchange rate


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_single import CurrencyExchangeRateSingle
from firefly_iii_client.models.currency_exchange_rate_update import CurrencyExchangeRateUpdate
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the currency exchange rate.
    currency_exchange_rate_update = firefly_iii_client.CurrencyExchangeRateUpdate() # CurrencyExchangeRateUpdate | JSON array or formdata with updated exchange rate information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing currency exchange rate.
        api_response = api_instance.update_currency_exchange_rate(id, currency_exchange_rate_update, x_trace_id=x_trace_id)
        print("The response of LinksApi->update_currency_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->update_currency_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the currency exchange rate. | 
 **currency_exchange_rate_update** | [**CurrencyExchangeRateUpdate**](CurrencyExchangeRateUpdate.md)| JSON array or formdata with updated exchange rate information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencyExchangeRateSingle**](CurrencyExchangeRateSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated exchange rate stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link_type**
> LinkTypeSingle update_link_type(id, link_type_update, x_trace_id=x_trace_id)

Update existing link type.

Used to update a single link type. All fields that are not submitted will be cleared (set to NULL). The model will tell you which fields are mandatory. You cannot update some of the system provided link types, indicated by the editable=false flag when you list it.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.link_type_single import LinkTypeSingle
from firefly_iii_client.models.link_type_update import LinkTypeUpdate
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the link type.
    link_type_update = firefly_iii_client.LinkTypeUpdate() # LinkTypeUpdate | JSON array or formdata with updated link type information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing link type.
        api_response = api_instance.update_link_type(id, link_type_update, x_trace_id=x_trace_id)
        print("The response of LinksApi->update_link_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->update_link_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. | 
 **link_type_update** | [**LinkTypeUpdate**](LinkTypeUpdate.md)| JSON array or formdata with updated link type information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated link type stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_link**
> TransactionLinkSingle update_transaction_link(id, transaction_link_update, x_trace_id=x_trace_id)

Update an existing link between transactions.

Used to update a single existing link.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.transaction_link_single import TransactionLinkSingle
from firefly_iii_client.models.transaction_link_update import TransactionLinkUpdate
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
    api_instance = firefly_iii_client.LinksApi(api_client)
    id = '123' # str | The ID of the transaction link.
    transaction_link_update = firefly_iii_client.TransactionLinkUpdate() # TransactionLinkUpdate | JSON array or formdata with updated link type information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update an existing link between transactions.
        api_response = api_instance.update_transaction_link(id, transaction_link_update, x_trace_id=x_trace_id)
        print("The response of LinksApi->update_transaction_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinksApi->update_transaction_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction link. | 
 **transaction_link_update** | [**TransactionLinkUpdate**](TransactionLinkUpdate.md)| JSON array or formdata with updated link type information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated link type stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

