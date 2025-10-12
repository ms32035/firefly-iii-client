# firefly_iii_client.CurrencyExchangeRatesApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_specific_currency_exchange_rate**](CurrencyExchangeRatesApi.md#delete_specific_currency_exchange_rate) | **DELETE** /v1/exchange-rates/{id} | Delete a specific currency exchange rate.
[**delete_specific_currency_exchange_rate_on_date**](CurrencyExchangeRatesApi.md#delete_specific_currency_exchange_rate_on_date) | **DELETE** /v1/exchange-rates/{from}/{to}/{date} | Delete the currency exchange rate from &#39;from&#39; to &#39;to&#39; on the specified date.
[**delete_specific_currency_exchange_rates**](CurrencyExchangeRatesApi.md#delete_specific_currency_exchange_rates) | **DELETE** /v1/exchange-rates/{from}/{to} | Deletes ALL currency exchange rates from &#39;from&#39; to &#39;to&#39;.
[**list_currency_exchange_rates**](CurrencyExchangeRatesApi.md#list_currency_exchange_rates) | **GET** /v1/exchange-rates | List all exchange rates that Firefly III knows.
[**list_specific_currency_exchange_rate**](CurrencyExchangeRatesApi.md#list_specific_currency_exchange_rate) | **GET** /v1/exchange-rates/{id} | List a single specific exchange rate.
[**list_specific_currency_exchange_rate_on_date**](CurrencyExchangeRatesApi.md#list_specific_currency_exchange_rate_on_date) | **GET** /v1/exchange-rates/{from}/{to}/{date} | List the exchange rate for the from and to-currency on the requested date.
[**list_specific_currency_exchange_rates**](CurrencyExchangeRatesApi.md#list_specific_currency_exchange_rates) | **GET** /v1/exchange-rates/{from}/{to} | List all exchange rates from/to the mentioned currencies.
[**store_currency_exchange_rate**](CurrencyExchangeRatesApi.md#store_currency_exchange_rate) | **POST** /v1/exchange-rates | Store a new currency exchange rate.
[**store_currency_exchange_rates_by_date**](CurrencyExchangeRatesApi.md#store_currency_exchange_rates_by_date) | **POST** /v1/exchange-rates/by-date/{date} | Store new currency exchange rates under this date
[**store_currency_exchange_rates_by_pair**](CurrencyExchangeRatesApi.md#store_currency_exchange_rates_by_pair) | **POST** /v1/exchange-rates/by-currencies/{from}/{to} | Store new currency exchange rates under this from/to pair.
[**update_currency_exchange_rate**](CurrencyExchangeRatesApi.md#update_currency_exchange_rate) | **PUT** /v1/exchange-rates/{id} | Update existing currency exchange rate.
[**update_currency_exchange_rate_by_date**](CurrencyExchangeRatesApi.md#update_currency_exchange_rate_by_date) | **PUT** /v1/exchange-rates/{from}/{to}/{date} | Update existing currency exchange rate.


# **delete_specific_currency_exchange_rate**
> delete_specific_currency_exchange_rate(id, x_trace_id=x_trace_id)

Delete a specific currency exchange rate.

Delete a specific currency exchange rate by its internal ID.

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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    id = '123' # str | The ID of the requested currency exchange rate.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Delete a specific currency exchange rate.
        api_instance.delete_specific_currency_exchange_rate(id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->delete_specific_currency_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the requested currency exchange rate. | 
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
**204** | Currency exchange rate deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_specific_currency_exchange_rate_on_date**
> delete_specific_currency_exchange_rate_on_date(var_from, to, var_date, x_trace_id=x_trace_id)

Delete the currency exchange rate from 'from' to 'to' on the specified date.

Delete the currency exchange rate from 'from' to 'to' on the specified date.  It's important to know that the reverse exchange rate (from 'to' to 'from') will not be deleted and Firefly III will still be able to infer the correct exchange rate from the reverse one.

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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_from = 'EUR' # str | The currency code of the 'from' currency.
    to = 'USD' # str | The currency code of the 'to' currency.
    var_date = '2025-10-01' # str | 
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Delete the currency exchange rate from 'from' to 'to' on the specified date.
        api_instance.delete_specific_currency_exchange_rate_on_date(var_from, to, var_date, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->delete_specific_currency_exchange_rate_on_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency code of the &#39;from&#39; currency. | 
 **to** | **str**| The currency code of the &#39;to&#39; currency. | 
 **var_date** | **str**|  | 
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
**204** | Currency exchange rate(s) deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_specific_currency_exchange_rates**
> delete_specific_currency_exchange_rates(var_from, to, x_trace_id=x_trace_id)

Deletes ALL currency exchange rates from 'from' to 'to'.

Deletes ALL currency exchange rates from 'from' to 'to'. It's important to know that the reverse exchange rates (from 'to' to 'from') will not be deleted and Firefly III will still be able to infer the correct exchange rate from the reverse one.

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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_from = 'EUR' # str | The currency code of the 'from' currency.
    to = 'USD' # str | The currency code of the 'to' currency.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Deletes ALL currency exchange rates from 'from' to 'to'.
        api_instance.delete_specific_currency_exchange_rates(var_from, to, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->delete_specific_currency_exchange_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency code of the &#39;from&#39; currency. | 
 **to** | **str**| The currency code of the &#39;to&#39; currency. | 
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
**204** | Currency exchange rate(s) deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency_exchange_rates**
> CurrencyExchangeRateArray list_currency_exchange_rates(x_trace_id=x_trace_id, limit=limit, page=page)

List all exchange rates that Firefly III knows.

List exchange rates that Firefly III knows.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_array import CurrencyExchangeRateArray
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all exchange rates that Firefly III knows.
        api_response = api_instance.list_currency_exchange_rates(x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrencyExchangeRatesApi->list_currency_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->list_currency_exchange_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**CurrencyExchangeRateArray**](CurrencyExchangeRateArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all available currency exchange rates. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_specific_currency_exchange_rate**
> CurrencyExchangeRateSingle list_specific_currency_exchange_rate(id, x_trace_id=x_trace_id, limit=limit, page=page)

List a single specific exchange rate.

List a single specific exchange rate by its ID.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_single import CurrencyExchangeRateSingle
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    id = '123' # str | The ID of the requested currency exchange rate.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List a single specific exchange rate.
        api_response = api_instance.list_specific_currency_exchange_rate(id, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrencyExchangeRatesApi->list_specific_currency_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->list_specific_currency_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the requested currency exchange rate. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**CurrencyExchangeRateSingle**](CurrencyExchangeRateSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exchange rate requested. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_specific_currency_exchange_rate_on_date**
> CurrencyExchangeRateArray list_specific_currency_exchange_rate_on_date(var_from, to, var_date, x_trace_id=x_trace_id, limit=limit, page=page)

List the exchange rate for the from and to-currency on the requested date.

List the exchange rate for the from and to-currency on the requested date.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_array import CurrencyExchangeRateArray
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_from = 'EUR' # str | The currency code of the 'from' currency.
    to = 'USD' # str | The currency code of the 'to' currency.
    var_date = '2025-10-01' # str | 
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List the exchange rate for the from and to-currency on the requested date.
        api_response = api_instance.list_specific_currency_exchange_rate_on_date(var_from, to, var_date, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrencyExchangeRatesApi->list_specific_currency_exchange_rate_on_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->list_specific_currency_exchange_rate_on_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency code of the &#39;from&#39; currency. | 
 **to** | **str**| The currency code of the &#39;to&#39; currency. | 
 **var_date** | **str**|  | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**CurrencyExchangeRateArray**](CurrencyExchangeRateArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currency exchange rates. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_specific_currency_exchange_rates**
> CurrencyExchangeRateArray list_specific_currency_exchange_rates(var_from, to, x_trace_id=x_trace_id, limit=limit, page=page)

List all exchange rates from/to the mentioned currencies.

List all exchange rates from/to the mentioned currencies.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_array import CurrencyExchangeRateArray
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_from = 'EUR' # str | The currency code of the 'from' currency.
    to = 'USD' # str | The currency code of the 'to' currency.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all exchange rates from/to the mentioned currencies.
        api_response = api_instance.list_specific_currency_exchange_rates(var_from, to, x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of CurrencyExchangeRatesApi->list_specific_currency_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->list_specific_currency_exchange_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency code of the &#39;from&#39; currency. | 
 **to** | **str**| The currency code of the &#39;to&#39; currency. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**CurrencyExchangeRateArray**](CurrencyExchangeRateArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currency exchange rates. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_currency_exchange_rate**
> CurrencyExchangeRateSingle store_currency_exchange_rate(currency_exchange_rate_store, x_trace_id=x_trace_id)

Store a new currency exchange rate.

Stores a new exchange rate. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_single import CurrencyExchangeRateSingle
from firefly_iii_client.models.currency_exchange_rate_store import CurrencyExchangeRateStore
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    currency_exchange_rate_store = firefly_iii_client.CurrencyExchangeRateStore() # CurrencyExchangeRateStore | JSON array or key=value pairs with the necessary exchange rate information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store a new currency exchange rate.
        api_response = api_instance.store_currency_exchange_rate(currency_exchange_rate_store, x_trace_id=x_trace_id)
        print("The response of CurrencyExchangeRatesApi->store_currency_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->store_currency_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_exchange_rate_store** | [**CurrencyExchangeRateStore**](CurrencyExchangeRateStore.md)| JSON array or key&#x3D;value pairs with the necessary exchange rate information. See the model for the exact specifications. | 
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
**200** | New exchange stored, result in response. If a rate already exists for this currency pair and date, it will be updated. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_currency_exchange_rates_by_date**
> CurrencyExchangeRateArray store_currency_exchange_rates_by_date(var_date, currency_exchange_rate_store_by_date, x_trace_id=x_trace_id)

Store new currency exchange rates under this date

Stores a new set of exchange rates. The date is fixed (in the URL parameter) and the data required can be submitted as a JSON body.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_array import CurrencyExchangeRateArray
from firefly_iii_client.models.currency_exchange_rate_store_by_date import CurrencyExchangeRateStoreByDate
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_date = '2025-10-01' # str | 
    currency_exchange_rate_store_by_date = firefly_iii_client.CurrencyExchangeRateStoreByDate() # CurrencyExchangeRateStoreByDate | JSON array with the necessary currency exchange rate information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store new currency exchange rates under this date
        api_response = api_instance.store_currency_exchange_rates_by_date(var_date, currency_exchange_rate_store_by_date, x_trace_id=x_trace_id)
        print("The response of CurrencyExchangeRatesApi->store_currency_exchange_rates_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->store_currency_exchange_rates_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**|  | 
 **currency_exchange_rate_store_by_date** | [**CurrencyExchangeRateStoreByDate**](CurrencyExchangeRateStoreByDate.md)| JSON array with the necessary currency exchange rate information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencyExchangeRateArray**](CurrencyExchangeRateArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New exchange rates stored, result in response. If a rate already existed for any submitted entry, it will be updated. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_currency_exchange_rates_by_pair**
> CurrencyExchangeRateArray store_currency_exchange_rates_by_pair(var_from, to, request_body, x_trace_id=x_trace_id)

Store new currency exchange rates under this from/to pair.

Stores a new set of exchange rates for this pair. The date is variable, and the data required can be submitted as a JSON body.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_array import CurrencyExchangeRateArray
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_from = 'EUR' # str | The currency code of the 'from' currency.
    to = 'USD' # str | The currency code of the 'to' currency.
    request_body = {'key': 'request_body_example'} # Dict[str, str] | JSON array with the necessary currency exchange rate information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store new currency exchange rates under this from/to pair.
        api_response = api_instance.store_currency_exchange_rates_by_pair(var_from, to, request_body, x_trace_id=x_trace_id)
        print("The response of CurrencyExchangeRatesApi->store_currency_exchange_rates_by_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->store_currency_exchange_rates_by_pair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency code of the &#39;from&#39; currency. | 
 **to** | **str**| The currency code of the &#39;to&#39; currency. | 
 **request_body** | [**Dict[str, str]**](str.md)| JSON array with the necessary currency exchange rate information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**CurrencyExchangeRateArray**](CurrencyExchangeRateArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New exchange rates stored, result in response. If a rate already existed for any submitted entry, it will be updated. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency_exchange_rate**
> CurrencyExchangeRateSingle update_currency_exchange_rate(id, currency_exchange_rate_update, x_trace_id=x_trace_id)

Update existing currency exchange rate.

Used to update a single currency exchange rate by its ID. Including the from/to currency is optional.


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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    id = '123' # str | The ID of the currency exchange rate.
    currency_exchange_rate_update = firefly_iii_client.CurrencyExchangeRateUpdate() # CurrencyExchangeRateUpdate | JSON array or form-data with updated exchange rate information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing currency exchange rate.
        api_response = api_instance.update_currency_exchange_rate(id, currency_exchange_rate_update, x_trace_id=x_trace_id)
        print("The response of CurrencyExchangeRatesApi->update_currency_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->update_currency_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the currency exchange rate. | 
 **currency_exchange_rate_update** | [**CurrencyExchangeRateUpdate**](CurrencyExchangeRateUpdate.md)| JSON array or form-data with updated exchange rate information. See the model for the exact specifications. | 
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

# **update_currency_exchange_rate_by_date**
> CurrencyExchangeRateSingle update_currency_exchange_rate_by_date(var_from, to, var_date, currency_exchange_rate_update_no_date, x_trace_id=x_trace_id)

Update existing currency exchange rate.

Used to update a single currency exchange rate by its currency codes and date


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.currency_exchange_rate_single import CurrencyExchangeRateSingle
from firefly_iii_client.models.currency_exchange_rate_update_no_date import CurrencyExchangeRateUpdateNoDate
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
    api_instance = firefly_iii_client.CurrencyExchangeRatesApi(api_client)
    var_from = 'EUR' # str | The currency code of the 'from' currency.
    to = 'USD' # str | The currency code of the 'to' currency.
    var_date = '2025-10-01' # str | 
    currency_exchange_rate_update_no_date = firefly_iii_client.CurrencyExchangeRateUpdateNoDate() # CurrencyExchangeRateUpdateNoDate | JSON array or form-data with updated exchange rate information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing currency exchange rate.
        api_response = api_instance.update_currency_exchange_rate_by_date(var_from, to, var_date, currency_exchange_rate_update_no_date, x_trace_id=x_trace_id)
        print("The response of CurrencyExchangeRatesApi->update_currency_exchange_rate_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyExchangeRatesApi->update_currency_exchange_rate_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The currency code of the &#39;from&#39; currency. | 
 **to** | **str**| The currency code of the &#39;to&#39; currency. | 
 **var_date** | **str**|  | 
 **currency_exchange_rate_update_no_date** | [**CurrencyExchangeRateUpdateNoDate**](CurrencyExchangeRateUpdateNoDate.md)| JSON array or form-data with updated exchange rate information. See the model for the exact specifications. | 
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

