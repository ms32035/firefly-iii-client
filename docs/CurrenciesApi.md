# firefly_iii_client.CurrenciesApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_currency**](CurrenciesApi.md#default_currency) | **POST** /v1/currencies/{code}/default | Make currency default currency.
[**delete_currency**](CurrenciesApi.md#delete_currency) | **DELETE** /v1/currencies/{code} | Delete a currency.
[**disable_currency**](CurrenciesApi.md#disable_currency) | **POST** /v1/currencies/{code}/disable | Disable a currency.
[**enable_currency**](CurrenciesApi.md#enable_currency) | **POST** /v1/currencies/{code}/enable | Enable a single currency.
[**get_currency**](CurrenciesApi.md#get_currency) | **GET** /v1/currencies/{code} | Get a single currency.
[**get_native_currency**](CurrenciesApi.md#get_native_currency) | **GET** /v1/currencies/native | Get the native currency of the current administration.
[**list_account_by_currency**](CurrenciesApi.md#list_account_by_currency) | **GET** /v1/currencies/{code}/accounts | List all accounts with this currency.
[**list_available_budget_by_currency**](CurrenciesApi.md#list_available_budget_by_currency) | **GET** /v1/currencies/{code}/available-budgets | List all available budgets with this currency.
[**list_bill_by_currency**](CurrenciesApi.md#list_bill_by_currency) | **GET** /v1/currencies/{code}/bills | List all bills with this currency.
[**list_budget_limit_by_currency**](CurrenciesApi.md#list_budget_limit_by_currency) | **GET** /v1/currencies/{code}/budget-limits | List all budget limits with this currency
[**list_currency**](CurrenciesApi.md#list_currency) | **GET** /v1/currencies | List all currencies.
[**list_recurrence_by_currency**](CurrenciesApi.md#list_recurrence_by_currency) | **GET** /v1/currencies/{code}/recurrences | List all recurring transactions with this currency.
[**list_rule_by_currency**](CurrenciesApi.md#list_rule_by_currency) | **GET** /v1/currencies/{code}/rules | List all rules with this currency.
[**list_transaction_by_currency**](CurrenciesApi.md#list_transaction_by_currency) | **GET** /v1/currencies/{code}/transactions | List all transactions with this currency.
[**store_currency**](CurrenciesApi.md#store_currency) | **POST** /v1/currencies | Store a new currency
[**update_currency**](CurrenciesApi.md#update_currency) | **PUT** /v1/currencies/{code} | Update existing currency.


# **default_currency**
> CurrencySingle default_currency(code, x_trace_id=x_trace_id)

Make currency default currency.

Make this currency the default currency for the user. If the currency is not enabled, it will be enabled as well.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Make currency default currency.
        api_response = api_instance.default_currency(code, x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->default_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->default_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Currency has been made the default currency. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_currency**
> delete_currency(code, x_trace_id=x_trace_id)

Delete a currency.

Delete a currency.

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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'GBP' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Delete a currency.
        api_instance.delete_currency(code, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling CurrenciesApi->delete_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
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
**204** | Currency deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_currency**
> CurrencySingle disable_currency(code, x_trace_id=x_trace_id)

Disable a currency.

Disable a currency.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'GBP' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Disable a currency.
        api_response = api_instance.disable_currency(code, x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->disable_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->disable_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Currency was disabled. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**409** | Currency cannot be disabled, because it is still in use. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_currency**
> CurrencySingle enable_currency(code, x_trace_id=x_trace_id)

Enable a single currency.

Enable a single currency.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Enable a single currency.
        api_response = api_instance.enable_currency(code, x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->enable_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->enable_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Currency was enabled. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency**
> CurrencySingle get_currency(code, x_trace_id=x_trace_id)

Get a single currency.

Get a single currency.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Get a single currency.
        api_response = api_instance.get_currency(code, x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->get_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->get_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_native_currency**
> CurrencySingle get_native_currency(x_trace_id=x_trace_id)

Get the native currency of the current administration.

Get the native currency of the current administration. This replaces what was called "the user's default currency" although they are essentially the same.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Get the native currency of the current administration.
        api_response = api_instance.get_native_currency(x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->get_native_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->get_native_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The native currency |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_by_currency**
> AccountArray list_account_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page, var_date=var_date, type=type)

List all accounts with this currency.

List all accounts with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.account_array import AccountArray
from firefly_iii_client.models.account_type_filter import AccountTypeFilter
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    var_date = '2013-10-20' # date | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)
    type = firefly_iii_client.AccountTypeFilter() # AccountTypeFilter | Optional filter on the account type(s) returned (optional)

    try:
        # List all accounts with this currency.
        api_response = api_instance.list_account_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page, var_date=var_date, type=type)
        print("The response of CurrenciesApi->list_account_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_account_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **var_date** | **date**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional] 
 **type** | [**AccountTypeFilter**](.md)| Optional filter on the account type(s) returned | [optional] 

### Return type

[**AccountArray**](AccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_budget_by_currency**
> AvailableBudgetArray list_available_budget_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)

List all available budgets with this currency.

List all available budgets with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.available_budget_array import AvailableBudgetArray
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'EUR' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all available budgets with this currency.
        api_response = api_instance.list_available_budget_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrenciesApi->list_available_budget_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_available_budget_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**AvailableBudgetArray**](AvailableBudgetArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available budgets |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bill_by_currency**
> BillArray list_bill_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)

List all bills with this currency.

List all bills with this currency.

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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all bills with this currency.
        api_response = api_instance.list_bill_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrenciesApi->list_bill_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_bill_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

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
**200** | A list of bills. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budget_limit_by_currency**
> BudgetLimitArray list_budget_limit_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end)

List all budget limits with this currency

List all budget limits with this currency

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.budget_limit_array import BudgetLimitArray
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = 'Mon Jan 01 00:00:00 UTC 2018' # date | Start date for the budget limit list. (optional)
    end = 'Wed Jan 31 00:00:00 UTC 2018' # date | End date for the budget limit list. (optional)

    try:
        # List all budget limits with this currency
        api_response = api_instance.list_budget_limit_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end)
        print("The response of CurrenciesApi->list_budget_limit_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_budget_limit_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **date**| Start date for the budget limit list. | [optional] 
 **end** | **date**| End date for the budget limit list. | [optional] 

### Return type

[**BudgetLimitArray**](BudgetLimitArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget limits. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency**
> CurrencyArray list_currency(x_trace_id=x_trace_id, limit=limit, page=page)

List all currencies.

List all currencies.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_array import CurrencyArray
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all currencies.
        api_response = api_instance.list_currency(x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrenciesApi->list_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**CurrencyArray**](CurrencyArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recurrence_by_currency**
> RecurrenceArray list_recurrence_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)

List all recurring transactions with this currency.

List all recurring transactions with this currency.

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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'EUR' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all recurring transactions with this currency.
        api_response = api_instance.list_recurrence_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrenciesApi->list_recurrence_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_recurrence_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
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
**200** | A list of recurring transactions |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_by_currency**
> RuleArray list_rule_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)

List all rules with this currency.

List all rules with this currency.

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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all rules with this currency.
        api_response = api_instance.list_rule_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrenciesApi->list_rule_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_rule_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

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

# **list_transaction_by_currency**
> TransactionArray list_transaction_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)

List all transactions with this currency.

List all transactions with this currency.

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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'USD' # str | The currency code.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD, to limit the list of transactions.  (optional)
    end = 'Mon Dec 31 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD, to limit the list of transactions.  (optional)
    type = firefly_iii_client.TransactionTypeFilter() # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    try:
        # List all transactions with this currency.
        api_response = api_instance.list_transaction_by_currency(code, x_trace_id=x_trace_id, limit=limit, page=page, start=start, end=end, type=type)
        print("The response of CurrenciesApi->list_transaction_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->list_transaction_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the list of transactions.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the list of transactions.  | [optional] 
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
**200** | A list of transactions. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_currency**
> CurrencySingle store_currency(currency_store, x_trace_id=x_trace_id)

Store a new currency

Creates a new currency. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
from firefly_iii_client.models.currency_store import CurrencyStore
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    currency_store = firefly_iii_client.CurrencyStore() # CurrencyStore | JSON array or key=value pairs with the necessary currency information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store a new currency
        api_response = api_instance.store_currency(currency_store, x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->store_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->store_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_store** | [**CurrencyStore**](CurrencyStore.md)| JSON array or key&#x3D;value pairs with the necessary currency information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New currency stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency**
> CurrencySingle update_currency(code, currency_update, x_trace_id=x_trace_id)

Update existing currency.

Update existing currency.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_single import CurrencySingle
from firefly_iii_client.models.currency_update import CurrencyUpdate
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
    api_instance = firefly_iii_client.CurrenciesApi(api_client)
    code = 'EUR' # str | The currency code.
    currency_update = firefly_iii_client.CurrencyUpdate() # CurrencyUpdate | JSON array with updated currency information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing currency.
        api_response = api_instance.update_currency(code, currency_update, x_trace_id=x_trace_id)
        print("The response of CurrenciesApi->update_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrenciesApi->update_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **currency_update** | [**CurrencyUpdate**](CurrencyUpdate.md)| JSON array with updated currency information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated currency stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

