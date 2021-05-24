# firefly_iii_client.AutocompleteApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_ac**](AutocompleteApi.md#get_accounts_ac) | **GET** /api/v1/autocomplete/accounts | Returns all accounts of the user returned in a basic auto-complete array.
[**get_bills_ac**](AutocompleteApi.md#get_bills_ac) | **GET** /api/v1/autocomplete/bills | Returns all bills of the user returned in a basic auto-complete array.
[**get_budgets_ac**](AutocompleteApi.md#get_budgets_ac) | **GET** /api/v1/autocomplete/budgets | Returns all budgets of the user returned in a basic auto-complete array.
[**get_categories_ac**](AutocompleteApi.md#get_categories_ac) | **GET** /api/v1/autocomplete/categories | Returns all categories of the user returned in a basic auto-complete array.
[**get_currencies_ac**](AutocompleteApi.md#get_currencies_ac) | **GET** /api/v1/autocomplete/currencies | Returns all currencies of the user returned in a basic auto-complete array.
[**get_currencies_code_ac**](AutocompleteApi.md#get_currencies_code_ac) | **GET** /api/v1/autocomplete/currencies-with-code | Returns all currencies of the user returned in a basic auto-complete array.
[**get_object_groups_ac**](AutocompleteApi.md#get_object_groups_ac) | **GET** /api/v1/autocomplete/object-groups | Returns all object groups of the user returned in a basic auto-complete array.
[**get_piggies_ac**](AutocompleteApi.md#get_piggies_ac) | **GET** /api/v1/autocomplete/piggy-banks | Returns all piggy banks of the user returned in a basic auto-complete array.
[**get_piggies_balance_ac**](AutocompleteApi.md#get_piggies_balance_ac) | **GET** /api/v1/autocomplete/piggy-banks-with-balance | Returns all piggy banks of the user returned in a basic auto-complete array complemented with balance information.
[**get_recurring_ac**](AutocompleteApi.md#get_recurring_ac) | **GET** /api/v1/autocomplete/recurring | Returns all recurring transactions of the user returned in a basic auto-complete array.
[**get_rule_groups_ac**](AutocompleteApi.md#get_rule_groups_ac) | **GET** /api/v1/autocomplete/rule-groups | Returns all rule groups of the user returned in a basic auto-complete array.
[**get_rules_ac**](AutocompleteApi.md#get_rules_ac) | **GET** /api/v1/autocomplete/rules | Returns all rules of the user returned in a basic auto-complete array.
[**get_tag_ac**](AutocompleteApi.md#get_tag_ac) | **GET** /api/v1/autocomplete/tags | Returns all tags of the user returned in a basic auto-complete array.
[**get_transaction_types_ac**](AutocompleteApi.md#get_transaction_types_ac) | **GET** /api/v1/autocomplete/transaction-types | Returns all transaction types returned in a basic auto-complete array. English only.
[**get_transactions_ac**](AutocompleteApi.md#get_transactions_ac) | **GET** /api/v1/autocomplete/transactions | Returns all transaction descriptions of the user returned in a basic auto-complete array.
[**get_transactions_idac**](AutocompleteApi.md#get_transactions_idac) | **GET** /api/v1/autocomplete/transactions-with-id | Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array.


# **get_accounts_ac**
> AutocompleteAccountArray get_accounts_ac()

Returns all accounts of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.autocomplete_account_array import AutocompleteAccountArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "query-string" # str | The autocomplete search query for accounts. (optional)
    limit = 10 # int | The number of items returned. (optional)
    date = "2020-09-17" # str | If the account is an asset account or a liability, the autocomplete will also return the balance of the account on this date. (optional)
    type = AccountTypeFilter("all") # AccountTypeFilter | Optional filter on the account type(s) used in the autocomplete. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all accounts of the user returned in a basic auto-complete array.
        api_response = api_instance.get_accounts_ac(query=query, limit=limit, date=date, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_accounts_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query for accounts. | [optional]
 **limit** | **int**| The number of items returned. | [optional]
 **date** | **str**| If the account is an asset account or a liability, the autocomplete will also return the balance of the account on this date. | [optional]
 **type** | **AccountTypeFilter**| Optional filter on the account type(s) used in the autocomplete. | [optional]

### Return type

[**AutocompleteAccountArray**](AutocompleteAccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bills_ac**
> AutocompleteBillArray get_bills_ac()

Returns all bills of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_bill_array import AutocompleteBillArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "query-string" # str | The autocomplete search query for bills. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all bills of the user returned in a basic auto-complete array.
        api_response = api_instance.get_bills_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_bills_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query for bills. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteBillArray**](AutocompleteBillArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_ac**
> AutocompleteBudgetArray get_budgets_ac()

Returns all budgets of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_budget_array import AutocompleteBudgetArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all budgets of the user returned in a basic auto-complete array.
        api_response = api_instance.get_budgets_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_budgets_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned | [optional]

### Return type

[**AutocompleteBudgetArray**](AutocompleteBudgetArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budgets with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_ac**
> AutocompleteCategoryArray get_categories_ac()

Returns all categories of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_category_array import AutocompleteCategoryArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all categories of the user returned in a basic auto-complete array.
        api_response = api_instance.get_categories_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_categories_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteCategoryArray**](AutocompleteCategoryArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of categories with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_ac**
> AutocompleteCurrencyArray get_currencies_ac()

Returns all currencies of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_currency_array import AutocompleteCurrencyArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all currencies of the user returned in a basic auto-complete array.
        api_response = api_instance.get_currencies_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_currencies_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteCurrencyArray**](AutocompleteCurrencyArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_code_ac**
> AutocompleteCurrencyCodeArray get_currencies_code_ac()

Returns all currencies of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_currency_code_array import AutocompleteCurrencyCodeArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all currencies of the user returned in a basic auto-complete array.
        api_response = api_instance.get_currencies_code_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_currencies_code_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteCurrencyCodeArray**](AutocompleteCurrencyCodeArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies with very basic information and the currency code between brackets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups_ac**
> AutocompleteObjectGroupArray get_object_groups_ac()

Returns all object groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_object_group_array import AutocompleteObjectGroupArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all object groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_object_groups_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_object_groups_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteObjectGroupArray**](AutocompleteObjectGroupArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of object groups with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_piggies_ac**
> AutocompletePiggyArray get_piggies_ac()

Returns all piggy banks of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_piggy_array import AutocompletePiggyArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all piggy banks of the user returned in a basic auto-complete array.
        api_response = api_instance.get_piggies_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_piggies_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompletePiggyArray**](AutocompletePiggyArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_piggies_balance_ac**
> AutocompletePiggyBalanceArray get_piggies_balance_ac()

Returns all piggy banks of the user returned in a basic auto-complete array complemented with balance information.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_piggy_balance_array import AutocompletePiggyBalanceArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all piggy banks of the user returned in a basic auto-complete array complemented with balance information.
        api_response = api_instance.get_piggies_balance_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_piggies_balance_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompletePiggyBalanceArray**](AutocompletePiggyBalanceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks with very basic balance information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring_ac**
> AutocompleteRecurrenceArray get_recurring_ac()

Returns all recurring transactions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_recurrence_array import AutocompleteRecurrenceArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all recurring transactions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_recurring_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_recurring_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteRecurrenceArray**](AutocompleteRecurrenceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recurring transactions with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_groups_ac**
> AutocompleteRuleGroupArray get_rule_groups_ac()

Returns all rule groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_rule_group_array import AutocompleteRuleGroupArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all rule groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rule_groups_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_rule_groups_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteRuleGroupArray**](AutocompleteRuleGroupArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule groups with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_ac**
> AutocompleteRuleArray get_rules_ac()

Returns all rules of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_rule_array import AutocompleteRuleArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all rules of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rules_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_rules_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteRuleArray**](AutocompleteRuleArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_ac**
> AutocompleteTagArray get_tag_ac()

Returns all tags of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_tag_array import AutocompleteTagArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all tags of the user returned in a basic auto-complete array.
        api_response = api_instance.get_tag_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_tag_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteTagArray**](AutocompleteTagArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tags with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_types_ac**
> AutocompleteTransactionTypeArray get_transaction_types_ac()

Returns all transaction types returned in a basic auto-complete array. English only.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_transaction_type_array import AutocompleteTransactionTypeArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all transaction types returned in a basic auto-complete array. English only.
        api_response = api_instance.get_transaction_types_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_transaction_types_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteTransactionTypeArray**](AutocompleteTransactionTypeArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction types with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_ac**
> AutocompleteTransactionArray get_transactions_ac()

Returns all transaction descriptions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_transaction_array import AutocompleteTransactionArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all transaction descriptions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_transactions_ac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_transactions_ac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteTransactionArray**](AutocompleteTransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction descriptions with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_idac**
> AutocompleteTransactionIDArray get_transactions_idac()

Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import autocomplete_api
from firefly_iii_client.model.autocomplete_transaction_id_array import AutocompleteTransactionIDArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    query = "str" # str | The autocomplete search query. (optional)
    limit = 10 # int | The number of items returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array.
        api_response = api_instance.get_transactions_idac(query=query, limit=limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_transactions_idac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional]
 **limit** | **int**| The number of items returned. | [optional]

### Return type

[**AutocompleteTransactionIDArray**](AutocompleteTransactionIDArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

