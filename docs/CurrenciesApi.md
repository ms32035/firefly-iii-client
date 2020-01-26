# firefly_iii_client.CurrenciesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_currency**](CurrenciesApi.md#default_currency) | **POST** /api/v1/currencies/{code}/default | Make currency default currency.
[**delete_currency**](CurrenciesApi.md#delete_currency) | **DELETE** /api/v1/currencies/{code} | Delete a currency.
[**disable_currency**](CurrenciesApi.md#disable_currency) | **POST** /api/v1/currencies/{code}/disable | Disable a currency.
[**enable_currency**](CurrenciesApi.md#enable_currency) | **POST** /api/v1/currencies/{code}/enable | Enable a single currency.
[**get_currency**](CurrenciesApi.md#get_currency) | **GET** /api/v1/currencies/{code} | Get a single currency.
[**list_account_by_currency**](CurrenciesApi.md#list_account_by_currency) | **GET** /api/v1/currencies/{code}/accounts | List all accounts with this currency.
[**list_available_budget_by_currency**](CurrenciesApi.md#list_available_budget_by_currency) | **GET** /api/v1/currencies/{code}/available_budgets | List all available budgets with this currency.
[**list_bill_by_currency**](CurrenciesApi.md#list_bill_by_currency) | **GET** /api/v1/currencies/{code}/bills | List all bills with this currency.
[**list_budget_limit_by_currency**](CurrenciesApi.md#list_budget_limit_by_currency) | **GET** /api/v1/currencies/{code}/budget_limits | List all budget limits with this currency
[**list_currency**](CurrenciesApi.md#list_currency) | **GET** /api/v1/currencies | List all currencies.
[**list_exchange_rate_by_currency**](CurrenciesApi.md#list_exchange_rate_by_currency) | **GET** /api/v1/currencies/{code}/cer | List all known exchange rates with (from or to) this currency.
[**list_recurrence_by_currency**](CurrenciesApi.md#list_recurrence_by_currency) | **GET** /api/v1/currencies/{code}/recurrences | List all recurring transactions with this currency.
[**list_rule_by_currency**](CurrenciesApi.md#list_rule_by_currency) | **GET** /api/v1/currencies/{code}/rules | List all rules with this currency.
[**list_transaction_by_currency**](CurrenciesApi.md#list_transaction_by_currency) | **GET** /api/v1/currencies/{code}/transactions | List all transactions with this currency.
[**store_currency**](CurrenciesApi.md#store_currency) | **POST** /api/v1/currencies | Store a new currency
[**update_currency**](CurrenciesApi.md#update_currency) | **PUT** /api/v1/currencies/{code} | Update existing currency.


# **default_currency**
> CurrencySingle default_currency(code)

Make currency default currency.

Make this currency the default currency. If the currency is not enabled, it will be enabled as well.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.

try:
    # Make currency default currency.
    api_response = api_instance.default_currency(code)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

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
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'GBP' # str | The currency code.

try:
    # Delete a currency.
    api_instance.delete_currency(code)
except ApiException as e:
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
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 56 # int | The currency code.

try:
    # Disable a currency.
    api_response = api_instance.disable_currency(code)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

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
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.

try:
    # Enable a single currency.
    api_response = api_instance.enable_currency(code)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

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
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.

try:
    # Get a single currency.
    api_response = api_instance.get_currency(code)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency |  -  |
**404** | Currency not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_by_currency**
> AccountArray list_account_by_currency(code, page=page, date=date, type=type)

List all accounts with this currency.

List all accounts with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.
page = 1 # int | Page number. The default pagination is 50. (optional)
date = 'date_example' # str | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)
type = firefly_iii_client.AccountTypeFilter() # AccountTypeFilter | Optional filter on the account type(s) returned (optional)

try:
    # List all accounts with this currency.
    api_response = api_instance.list_account_by_currency(code, page=page, date=date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_account_by_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **date** | **str**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional] 
 **type** | [**AccountTypeFilter**](.md)| Optional filter on the account type(s) returned | [optional] 

### Return type

[**AccountArray**](AccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_budget_by_currency**
> AvailableBudgetArray list_available_budget_by_currency(code, page=page)

List all available budgets with this currency.

List all available budgets with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'EUR' # str | The currency code.
page = 1 # int | Page number. The default pagination is 50 (optional)

try:
    # List all available budgets with this currency.
    api_response = api_instance.list_available_budget_by_currency(code, page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available budgets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bill_by_currency**
> BillArray list_bill_by_currency(code, page=page)

List all bills with this currency.

List all bills with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all bills with this currency.
    api_response = api_instance.list_bill_by_currency(code, page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budget_limit_by_currency**
> BudgetLimitArray list_budget_limit_by_currency(code, page=page, start=start, end=end)

List all budget limits with this currency

List all budget limits with this currency

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.
page = 1 # int | Page number. The default pagination is 50. (optional)
start = '2013-10-20' # date | Start date for the budget limit list. (optional)
end = '2013-10-20' # date | End date for the budget limit list. (optional)

try:
    # List all budget limits with this currency
    api_response = api_instance.list_budget_limit_by_currency(code, page=page, start=start, end=end)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget limits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency**
> CurrencyArray list_currency(page=page)

List all currencies.

List all currencies.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all currencies.
    api_response = api_instance.list_currency(page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exchange_rate_by_currency**
> ExchangeRateArray list_exchange_rate_by_currency(code, page=page, date=date, start=start, end=end)

List all known exchange rates with (from or to) this currency.

List all known exchange rates.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'GBP' # str | The currency code.
page = 1 # int | Page number. The default pagination is 50. (optional)
date = '2013-10-20' # date | The date of which you want to know the exchange rate  (optional)
start = '2013-10-20' # date | Use this instead of the date parameter to search for a range of currency exchange values.  (optional)
end = '2013-10-20' # date | Use this instead of the date parameter to search for a range of currency exchange values.  (optional)

try:
    # List all known exchange rates with (from or to) this currency.
    api_response = api_instance.list_exchange_rate_by_currency(code, page=page, date=date, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_exchange_rate_by_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **date** | **date**| The date of which you want to know the exchange rate  | [optional] 
 **start** | **date**| Use this instead of the date parameter to search for a range of currency exchange values.  | [optional] 
 **end** | **date**| Use this instead of the date parameter to search for a range of currency exchange values.  | [optional] 

### Return type

[**ExchangeRateArray**](ExchangeRateArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of exchange rates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recurrence_by_currency**
> RecurrenceArray list_recurrence_by_currency(code, page=page)

List all recurring transactions with this currency.

List all recurring transactions with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'EUR' # str | The currency code.
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all recurring transactions with this currency.
    api_response = api_instance.list_recurrence_by_currency(code, page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recurring transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_by_currency**
> RuleArray list_rule_by_currency(code, page=page)

List all rules with this currency.

List all rules with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.
page = 1 # int | Page number. The default pagination per 50. (optional)

try:
    # List all rules with this currency.
    api_response = api_instance.list_rule_by_currency(code, page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_currency**
> TransactionArray list_transaction_by_currency(code, page=page, start_date=start_date, end_date=end_date, type=type)

List all transactions with this currency.

List all transactions with this currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'USD' # str | The currency code.
page = 1 # int | Page number. The default pagination is per 50. (optional)
start_date = '2013-10-20' # date | A date formatted YYYY-MM-DD, to limit the list of transactions.  (optional)
end_date = '2013-10-20' # date | A date formatted YYYY-MM-DD, to limit the list of transactions.  (optional)
type = firefly_iii_client.TransactionTypeFilter() # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

try:
    # List all transactions with this currency.
    api_response = api_instance.list_transaction_by_currency(code, page=page, start_date=start_date, end_date=end_date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_transaction_by_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **page** | **int**| Page number. The default pagination is per 50. | [optional] 
 **start_date** | **date**| A date formatted YYYY-MM-DD, to limit the list of transactions.  | [optional] 
 **end_date** | **date**| A date formatted YYYY-MM-DD, to limit the list of transactions.  | [optional] 
 **type** | [**TransactionTypeFilter**](.md)| Optional filter on the transaction type(s) returned | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_currency**
> CurrencySingle store_currency(currency)

Store a new currency

Creates a new currency. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
currency = firefly_iii_client.Currency() # Currency | JSON array or key=value pairs with the necessary currency information. See the model for the exact specifications.

try:
    # Store a new currency
    api_response = api_instance.store_currency(currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->store_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | [**Currency**](Currency.md)| JSON array or key&#x3D;value pairs with the necessary currency information. See the model for the exact specifications. | 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New currency stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency**
> CurrencySingle update_currency(code, currency)

Update existing currency.

Update existing currency.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.CurrenciesApi(firefly_iii_client.ApiClient(configuration))
code = 'EUR' # str | The currency code.
currency = firefly_iii_client.Currency() # Currency | JSON array with updated currency information. See the model for the exact specifications.

try:
    # Update existing currency.
    api_response = api_instance.update_currency(code, currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->update_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code. | 
 **currency** | [**Currency**](Currency.md)| JSON array with updated currency information. See the model for the exact specifications. | 

### Return type

[**CurrencySingle**](CurrencySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated currency stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

