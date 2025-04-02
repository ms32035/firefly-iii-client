# firefly_iii_client.AutocompleteApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_ac**](AutocompleteApi.md#get_accounts_ac) | **GET** /v1/autocomplete/accounts | Returns all accounts of the user returned in a basic auto-complete array.
[**get_bills_ac**](AutocompleteApi.md#get_bills_ac) | **GET** /v1/autocomplete/bills | Returns all bills of the user returned in a basic auto-complete array.
[**get_budgets_ac**](AutocompleteApi.md#get_budgets_ac) | **GET** /v1/autocomplete/budgets | Returns all budgets of the user returned in a basic auto-complete array.
[**get_categories_ac**](AutocompleteApi.md#get_categories_ac) | **GET** /v1/autocomplete/categories | Returns all categories of the user returned in a basic auto-complete array.
[**get_currencies_ac**](AutocompleteApi.md#get_currencies_ac) | **GET** /v1/autocomplete/currencies | Returns all currencies of the user returned in a basic auto-complete array.
[**get_currencies_code_ac**](AutocompleteApi.md#get_currencies_code_ac) | **GET** /v1/autocomplete/currencies-with-code | Returns all currencies of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.
[**get_object_groups_ac**](AutocompleteApi.md#get_object_groups_ac) | **GET** /v1/autocomplete/object-groups | Returns all object groups of the user returned in a basic auto-complete array.
[**get_piggies_ac**](AutocompleteApi.md#get_piggies_ac) | **GET** /v1/autocomplete/piggy-banks | Returns all piggy banks of the user returned in a basic auto-complete array.
[**get_piggies_balance_ac**](AutocompleteApi.md#get_piggies_balance_ac) | **GET** /v1/autocomplete/piggy-banks-with-balance | Returns all piggy banks of the user returned in a basic auto-complete array.
[**get_recurring_ac**](AutocompleteApi.md#get_recurring_ac) | **GET** /v1/autocomplete/recurring | Returns all recurring transactions of the user returned in a basic auto-complete array.
[**get_rule_groups_ac**](AutocompleteApi.md#get_rule_groups_ac) | **GET** /v1/autocomplete/rule-groups | Returns all rule groups of the user returned in a basic auto-complete array.
[**get_rules_ac**](AutocompleteApi.md#get_rules_ac) | **GET** /v1/autocomplete/rules | Returns all rules of the user returned in a basic auto-complete array.
[**get_tag_ac**](AutocompleteApi.md#get_tag_ac) | **GET** /v1/autocomplete/tags | Returns all tags of the user returned in a basic auto-complete array.
[**get_transaction_types_ac**](AutocompleteApi.md#get_transaction_types_ac) | **GET** /v1/autocomplete/transaction-types | Returns all transaction types returned in a basic auto-complete array. English only.
[**get_transactions_ac**](AutocompleteApi.md#get_transactions_ac) | **GET** /v1/autocomplete/transactions | Returns all transaction descriptions of the user returned in a basic auto-complete array.
[**get_transactions_idac**](AutocompleteApi.md#get_transactions_idac) | **GET** /v1/autocomplete/transactions-with-id | Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.


# **get_accounts_ac**
> List[AutocompleteAccount] get_accounts_ac(x_trace_id=x_trace_id, query=query, limit=limit, var_date=var_date, types=types)

Returns all accounts of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.account_type_filter import AccountTypeFilter
from firefly_iii_client.models.autocomplete_account import AutocompleteAccount
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)
    var_date = '2020-09-17' # str | If the account is an asset account or a liability, the autocomplete will also return the balance of the account on this date. (optional)
    types = [firefly_iii_client.AccountTypeFilter()] # List[AccountTypeFilter] | Optional filter on the account type(s) used in the autocomplete. (optional)

    try:
        # Returns all accounts of the user returned in a basic auto-complete array.
        api_response = api_instance.get_accounts_ac(x_trace_id=x_trace_id, query=query, limit=limit, var_date=var_date, types=types)
        print("The response of AutocompleteApi->get_accounts_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_accounts_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 
 **var_date** | **str**| If the account is an asset account or a liability, the autocomplete will also return the balance of the account on this date. | [optional] 
 **types** | [**List[AccountTypeFilter]**](AccountTypeFilter.md)| Optional filter on the account type(s) used in the autocomplete. | [optional] 

### Return type

[**List[AutocompleteAccount]**](AutocompleteAccount.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bills_ac**
> List[AutocompleteBill] get_bills_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all bills of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_bill import AutocompleteBill
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all bills of the user returned in a basic auto-complete array.
        api_response = api_instance.get_bills_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_bills_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_bills_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteBill]**](AutocompleteBill.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_ac**
> List[AutocompleteBudget] get_budgets_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all budgets of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_budget import AutocompleteBudget
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all budgets of the user returned in a basic auto-complete array.
        api_response = api_instance.get_budgets_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_budgets_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_budgets_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteBudget]**](AutocompleteBudget.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budgets with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_ac**
> List[AutocompleteCategory] get_categories_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all categories of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_category import AutocompleteCategory
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all categories of the user returned in a basic auto-complete array.
        api_response = api_instance.get_categories_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_categories_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_categories_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteCategory]**](AutocompleteCategory.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of categories with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_ac**
> List[AutocompleteCurrency] get_currencies_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all currencies of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_currency import AutocompleteCurrency
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all currencies of the user returned in a basic auto-complete array.
        api_response = api_instance.get_currencies_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_currencies_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_currencies_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteCurrency]**](AutocompleteCurrency.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_code_ac**
> List[AutocompleteCurrencyCode] get_currencies_code_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all currencies of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_currency_code import AutocompleteCurrencyCode
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all currencies of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.
        api_response = api_instance.get_currencies_code_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_currencies_code_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_currencies_code_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteCurrencyCode]**](AutocompleteCurrencyCode.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies with very basic information and the currency code between brackets. This endpoint is DEPRECATED and I suggest you DO NOT use it. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups_ac**
> List[AutocompleteObjectGroup] get_object_groups_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all object groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_object_group import AutocompleteObjectGroup
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all object groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_object_groups_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_object_groups_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_object_groups_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteObjectGroup]**](AutocompleteObjectGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of object groups with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_piggies_ac**
> List[AutocompletePiggy] get_piggies_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all piggy banks of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_piggy import AutocompletePiggy
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all piggy banks of the user returned in a basic auto-complete array.
        api_response = api_instance.get_piggies_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_piggies_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_piggies_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompletePiggy]**](AutocompletePiggy.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_piggies_balance_ac**
> List[AutocompletePiggyBalance] get_piggies_balance_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all piggy banks of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_piggy_balance import AutocompletePiggyBalance
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all piggy banks of the user returned in a basic auto-complete array.
        api_response = api_instance.get_piggies_balance_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_piggies_balance_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_piggies_balance_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompletePiggyBalance]**](AutocompletePiggyBalance.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks with very basic balance information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring_ac**
> List[AutocompleteRecurrence] get_recurring_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all recurring transactions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_recurrence import AutocompleteRecurrence
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all recurring transactions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_recurring_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_recurring_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_recurring_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteRecurrence]**](AutocompleteRecurrence.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recurring transactions with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_groups_ac**
> List[AutocompleteRuleGroup] get_rule_groups_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all rule groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_rule_group import AutocompleteRuleGroup
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all rule groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rule_groups_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_rule_groups_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_rule_groups_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteRuleGroup]**](AutocompleteRuleGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule groups with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_ac**
> List[AutocompleteRule] get_rules_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all rules of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_rule import AutocompleteRule
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all rules of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rules_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_rules_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_rules_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteRule]**](AutocompleteRule.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_ac**
> List[AutocompleteTag] get_tag_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all tags of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_tag import AutocompleteTag
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all tags of the user returned in a basic auto-complete array.
        api_response = api_instance.get_tag_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_tag_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_tag_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteTag]**](AutocompleteTag.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tags with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_types_ac**
> List[AutocompleteTransactionType] get_transaction_types_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all transaction types returned in a basic auto-complete array. English only.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_transaction_type import AutocompleteTransactionType
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all transaction types returned in a basic auto-complete array. English only.
        api_response = api_instance.get_transaction_types_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_transaction_types_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_transaction_types_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteTransactionType]**](AutocompleteTransactionType.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction types with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_ac**
> List[AutocompleteTransaction] get_transactions_ac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all transaction descriptions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_transaction import AutocompleteTransaction
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all transaction descriptions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_transactions_ac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_transactions_ac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_transactions_ac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteTransaction]**](AutocompleteTransaction.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction descriptions with very basic information. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_idac**
> List[AutocompleteTransactionID] get_transactions_idac(x_trace_id=x_trace_id, query=query, limit=limit)

Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.autocomplete_transaction_id import AutocompleteTransactionID
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    query = 'string' # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    try:
        # Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.
        api_response = api_instance.get_transactions_idac(x_trace_id=x_trace_id, query=query, limit=limit)
        print("The response of AutocompleteApi->get_transactions_idac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get_transactions_idac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The number of items returned. | [optional] 

### Return type

[**List[AutocompleteTransactionID]**](AutocompleteTransactionID.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions with very basic information. This endpoint is DEPRECATED and I suggest you DO NOT use it. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

