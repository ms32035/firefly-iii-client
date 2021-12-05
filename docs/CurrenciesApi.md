# firefly_iii_client.CurrenciesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_currency**](CurrenciesApi.md#default_currency) | **POST** /api/v1/currencies/{code}/default | Make currency default currency.
[**delete_currency**](CurrenciesApi.md#delete_currency) | **DELETE** /api/v1/currencies/{code} | Delete a currency.
[**disable_currency**](CurrenciesApi.md#disable_currency) | **POST** /api/v1/currencies/{code}/disable | Disable a currency.
[**enable_currency**](CurrenciesApi.md#enable_currency) | **POST** /api/v1/currencies/{code}/enable | Enable a single currency.
[**get_currency**](CurrenciesApi.md#get_currency) | **GET** /api/v1/currencies/{code} | Get a single currency.
[**get_default_currency**](CurrenciesApi.md#get_default_currency) | **GET** /api/v1/currencies/default | Get the user&#39;s default currency.
[**list_account_by_currency**](CurrenciesApi.md#list_account_by_currency) | **GET** /api/v1/currencies/{code}/accounts | List all accounts with this currency.
[**list_available_budget_by_currency**](CurrenciesApi.md#list_available_budget_by_currency) | **GET** /api/v1/currencies/{code}/available_budgets | List all available budgets with this currency.
[**list_bill_by_currency**](CurrenciesApi.md#list_bill_by_currency) | **GET** /api/v1/currencies/{code}/bills | List all bills with this currency.
[**list_budget_limit_by_currency**](CurrenciesApi.md#list_budget_limit_by_currency) | **GET** /api/v1/currencies/{code}/budget_limits | List all budget limits with this currency
[**list_currency**](CurrenciesApi.md#list_currency) | **GET** /api/v1/currencies | List all currencies.
[**list_recurrence_by_currency**](CurrenciesApi.md#list_recurrence_by_currency) | **GET** /api/v1/currencies/{code}/recurrences | List all recurring transactions with this currency.
[**list_rule_by_currency**](CurrenciesApi.md#list_rule_by_currency) | **GET** /api/v1/currencies/{code}/rules | List all rules with this currency.
[**list_transaction_by_currency**](CurrenciesApi.md#list_transaction_by_currency) | **GET** /api/v1/currencies/{code}/transactions | List all transactions with this currency.
[**store_currency**](CurrenciesApi.md#store_currency) | **POST** /api/v1/currencies | Store a new currency
[**update_currency**](CurrenciesApi.md#update_currency) | **PUT** /api/v1/currencies/{code} | Update existing currency.


# **default_currency**
> CurrencySingle default_currency(code)

Make currency default currency.

Make this currency the default currency for the user. If the currency is not enabled, it will be enabled as well.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.

    # example passing only required values which don't have defaults set
    try:
        # Make currency default currency.
        api_response = api_instance.default_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->default_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Currency has been made the default currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_currency**
> delete_currency(code)

Delete a currency.

Delete a currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "GBP" # str | The currency code.

    # example passing only required values which don't have defaults set
    try:
        # Delete a currency.
        api_instance.delete_currency(code)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->delete_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |

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
**204** | Currency deleted. |  -  |
**404** | No such currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_currency**
> CurrencySingle disable_currency(code)

Disable a currency.

Disable a currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = 1 # int | The currency code.

    # example passing only required values which don't have defaults set
    try:
        # Disable a currency.
        api_response = api_instance.disable_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->disable_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **int**| The currency code. |

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Currency was disabled. |  -  |
**409** | Currency cannot be disabled, because it is still in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_currency**
> CurrencySingle enable_currency(code)

Enable a single currency.

Enable a single currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.

    # example passing only required values which don't have defaults set
    try:
        # Enable a single currency.
        api_response = api_instance.enable_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->enable_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Currency was enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency**
> CurrencySingle get_currency(code)

Get a single currency.

Get a single currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.

    # example passing only required values which don't have defaults set
    try:
        # Get a single currency.
        api_response = api_instance.get_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency |  -  |
**404** | Currency not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_currency**
> CurrencySingle get_default_currency()

Get the user's default currency.

Get the user's default currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the user's default currency.
        api_response = api_instance.get_default_currency()
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->get_default_currency: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The default currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_by_currency**
> AccountArray list_account_by_currency(code)

List all accounts with this currency.

List all accounts with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.account_array import AccountArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.
    page = 1 # int | Page number. The default pagination is 50. (optional)
    date = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)
    type = AccountTypeFilter("all") # AccountTypeFilter | Optional filter on the account type(s) returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all accounts with this currency.
        api_response = api_instance.list_account_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_account_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all accounts with this currency.
        api_response = api_instance.list_account_by_currency(code, page=page, date=date, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_account_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **date** | **date**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional]
 **type** | **AccountTypeFilter**| Optional filter on the account type(s) returned | [optional]

### Return type

[**AccountArray**](AccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_budget_by_currency**
> AvailableBudgetArray list_available_budget_by_currency(code)

List all available budgets with this currency.

List all available budgets with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.available_budget_array import AvailableBudgetArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "EUR" # str | The currency code.
    page = 1 # int | Page number. The default pagination is 50 (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all available budgets with this currency.
        api_response = api_instance.list_available_budget_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_available_budget_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all available budgets with this currency.
        api_response = api_instance.list_available_budget_by_currency(code, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_available_budget_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination is 50 | [optional]

### Return type

[**AvailableBudgetArray**](AvailableBudgetArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available budgets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bill_by_currency**
> BillArray list_bill_by_currency(code)

List all bills with this currency.

List all bills with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all bills with this currency.
        api_response = api_instance.list_bill_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_bill_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all bills with this currency.
        api_response = api_instance.list_bill_by_currency(code, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_bill_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

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

# **list_budget_limit_by_currency**
> BudgetLimitArray list_budget_limit_by_currency(code)

List all budget limits with this currency

List all budget limits with this currency

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.budget_limit_array import BudgetLimitArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Jan 01 00:00:00 UTC 2018').date() # date | Start date for the budget limit list. (optional)
    end = dateutil_parser('Wed Jan 31 00:00:00 UTC 2018').date() # date | End date for the budget limit list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all budget limits with this currency
        api_response = api_instance.list_budget_limit_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_budget_limit_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all budget limits with this currency
        api_response = api_instance.list_budget_limit_by_currency(code, page=page, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_budget_limit_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| Start date for the budget limit list. | [optional]
 **end** | **date**| End date for the budget limit list. | [optional]

### Return type

[**BudgetLimitArray**](BudgetLimitArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget limits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency**
> CurrencyArray list_currency()

List all currencies.

List all currencies.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.currency_array import CurrencyArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all currencies.
        api_response = api_instance.list_currency(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**CurrencyArray**](CurrencyArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recurrence_by_currency**
> RecurrenceArray list_recurrence_by_currency(code)

List all recurring transactions with this currency.

List all recurring transactions with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.recurrence_array import RecurrenceArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "EUR" # str | The currency code.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all recurring transactions with this currency.
        api_response = api_instance.list_recurrence_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_recurrence_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all recurring transactions with this currency.
        api_response = api_instance.list_recurrence_by_currency(code, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_recurrence_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**RecurrenceArray**](RecurrenceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recurring transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_by_currency**
> RuleArray list_rule_by_currency(code)

List all rules with this currency.

List all rules with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.rule_array import RuleArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.
    page = 1 # int | Page number. The default pagination per 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all rules with this currency.
        api_response = api_instance.list_rule_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_rule_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all rules with this currency.
        api_response = api_instance.list_rule_by_currency(code, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_rule_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination per 50. | [optional]

### Return type

[**RuleArray**](RuleArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_currency**
> TransactionArray list_transaction_by_currency(code)

List all transactions with this currency.

List all transactions with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.model.transaction_array import TransactionArray
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "USD" # str | The currency code.
    page = 1 # int | Page number. The default pagination is per 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the list of transactions.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the list of transactions.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions with this currency.
        api_response = api_instance.list_transaction_by_currency(code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_transaction_by_currency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions with this currency.
        api_response = api_instance.list_transaction_by_currency(code, page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->list_transaction_by_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **page** | **int**| Page number. The default pagination is per 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the list of transactions.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the list of transactions.  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned | [optional]

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_currency**
> CurrencySingle store_currency(currency_store)

Store a new currency

Creates a new currency. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.currency_store import CurrencyStore
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_store = CurrencyStore(
        code="AMS",
        decimal_places=2,
        default=False,
        enabled=True,
        name="Ankh-Morpork dollar",
        symbol="AM$",
    ) # CurrencyStore | JSON array or key=value pairs with the necessary currency information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new currency
        api_response = api_instance.store_currency(currency_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->store_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_store** | [**CurrencyStore**](CurrencyStore.md)| JSON array or key&#x3D;value pairs with the necessary currency information. See the model for the exact specifications. |

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New currency stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency**
> CurrencySingle update_currency(code, currency_update)

Update existing currency.

Update existing currency.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import currencies_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.currency_update import CurrencyUpdate
from firefly_iii_client.model.currency_single import CurrencySingle
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
    api_instance = currencies_api.CurrenciesApi(api_client)
    code = "EUR" # str | The currency code.
    currency_update = CurrencyUpdate(
        code="AMS",
        decimal_places=2,
        default=True,
        enabled=True,
        name="Ankh-Morpork dollar",
        symbol="AM$",
    ) # CurrencyUpdate | JSON array with updated currency information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing currency.
        api_response = api_instance.update_currency(code, currency_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling CurrenciesApi->update_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. |
 **currency_update** | [**CurrencyUpdate**](CurrencyUpdate.md)| JSON array with updated currency information. See the model for the exact specifications. |

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated currency stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

