# firefly_iii_client.BillsApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bill**](BillsApi.md#delete_bill) | **DELETE** /v1/bills/{id} | Delete a bill.
[**get_bill**](BillsApi.md#get_bill) | **GET** /v1/bills/{id} | Get a single bill.
[**list_attachment_by_bill**](BillsApi.md#list_attachment_by_bill) | **GET** /v1/bills/{id}/attachments | List all attachments uploaded to the bill.
[**list_bill**](BillsApi.md#list_bill) | **GET** /v1/bills | List all bills.
[**list_rule_by_bill**](BillsApi.md#list_rule_by_bill) | **GET** /v1/bills/{id}/rules | List all rules associated with the bill.
[**list_transaction_by_bill**](BillsApi.md#list_transaction_by_bill) | **GET** /v1/bills/{id}/transactions | List all transactions associated with the  bill.
[**store_bill**](BillsApi.md#store_bill) | **POST** /v1/bills | Store a new bill
[**update_bill**](BillsApi.md#update_bill) | **PUT** /v1/bills/{id} | Update existing bill.


# **delete_bill**
> delete_bill(id, x_trace_id=x_trace_id)

Delete a bill.

Delete a bill. This will not delete any associated rules. Will not remove associated transactions. WILL remove all associated attachments.

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
    api_instance = firefly_iii_client.BillsApi(api_client)
    id = '123' # str | The ID of the bill.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Delete a bill.
        api_instance.delete_bill(id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling BillsApi->delete_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. | 
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
**204** | Bill deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill**
> BillSingle get_bill(id, x_trace_id=x_trace_id, start=start, end=end)

Get a single bill.

Get a single bill.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.bill_single import BillSingle
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
    api_instance = firefly_iii_client.BillsApi(api_client)
    id = '123' # str | The ID of the bill.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    start = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)
    end = 'Mon Dec 31 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)

    try:
        # Get a single bill.
        api_response = api_instance.get_bill(id, x_trace_id=x_trace_id, start=start, end=end)
        print("The response of BillsApi->get_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->get_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional] 

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bill |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_bill**
> AttachmentArray list_attachment_by_bill(id, x_trace_id=x_trace_id, limit=limit, page=page)

List all attachments uploaded to the bill.

This endpoint will list all attachments linked to the bill.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.attachment_array import AttachmentArray
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
    api_instance = firefly_iii_client.BillsApi(api_client)
    id = '123' # str | The ID of the bill.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all attachments uploaded to the bill.
        api_response = api_instance.list_attachment_by_bill(id, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of BillsApi->list_attachment_by_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->list_attachment_by_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of attachments |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bill**
> BillArray list_bill(x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end)

List all bills.

This endpoint will list all the user's bills.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.bill_array import BillArray
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
    api_instance = firefly_iii_client.BillsApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)
    end = 'Mon Dec 31 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)

    try:
        # List all bills.
        api_response = api_instance.list_bill(x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end)
        print("The response of BillsApi->list_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->list_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional] 

### Return type

[**BillArray**](BillArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_by_bill**
> RuleArray list_rule_by_bill(id, x_trace_id=x_trace_id)

List all rules associated with the bill.

This endpoint will list all rules that have an action to set the bill to this bill.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.rule_array import RuleArray
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
    api_instance = firefly_iii_client.BillsApi(api_client)
    id = '123' # str | The ID of the bill.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # List all rules associated with the bill.
        api_response = api_instance.list_rule_by_bill(id, x_trace_id=x_trace_id)
        print("The response of BillsApi->list_rule_by_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->list_rule_by_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**RuleArray**](RuleArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_bill**
> TransactionArray list_transaction_by_bill(id, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)

List all transactions associated with the  bill.

This endpoint will list all transactions linked to this bill.

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
    api_instance = firefly_iii_client.BillsApi(api_client)
    id = '123' # str | The ID of the bill.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD.  (optional)
    end = 'Mon Dec 31 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD.  (optional)
    type = firefly_iii_client.TransactionTypeFilter() # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    try:
        # List all transactions associated with the  bill.
        api_response = api_instance.list_transaction_by_bill(id, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)
        print("The response of BillsApi->list_transaction_by_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->list_transaction_by_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional] 
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

# **store_bill**
> BillSingle store_bill(bill_store, x_trace_id=x_trace_id)

Store a new bill

Creates a new bill. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.bill_single import BillSingle
from firefly_iii_client.models.bill_store import BillStore
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
    api_instance = firefly_iii_client.BillsApi(api_client)
    bill_store = firefly_iii_client.BillStore() # BillStore | JSON array or key=value pairs with the necessary bill information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store a new bill
        api_response = api_instance.store_bill(bill_store, x_trace_id=x_trace_id)
        print("The response of BillsApi->store_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->store_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_store** | [**BillStore**](BillStore.md)| JSON array or key&#x3D;value pairs with the necessary bill information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New bill stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill**
> BillSingle update_bill(id, bill_update, x_trace_id=x_trace_id)

Update existing bill.

Update existing bill.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.bill_single import BillSingle
from firefly_iii_client.models.bill_update import BillUpdate
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
    api_instance = firefly_iii_client.BillsApi(api_client)
    id = '123' # str | The ID of the bill.
    bill_update = firefly_iii_client.BillUpdate() # BillUpdate | JSON array or key=value pairs with updated bill information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing bill.
        api_response = api_instance.update_bill(id, bill_update, x_trace_id=x_trace_id)
        print("The response of BillsApi->update_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->update_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. | 
 **bill_update** | [**BillUpdate**](BillUpdate.md)| JSON array or key&#x3D;value pairs with updated bill information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated bill stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

