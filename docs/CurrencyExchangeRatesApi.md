# firefly_iii_client.CurrencyExchangeRatesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rate**](CurrencyExchangeRatesApi.md#get_exchange_rate) | **GET** /api/v1/cer | Get an exchange rate.


# **get_exchange_rate**
> ExchangeRate get_exchange_rate(_from=_from, to=to, date=date, amount=amount)

Get an exchange rate.

Get an exchange rate. If Firefly III doesn't know the rate it will set the rate to 1.0.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.CurrencyExchangeRatesApi(firefly_iii_client.ApiClient(configuration))
_from = EUR # str | The source currency code. If omitted, defaults to EUR. (optional)
to = USD # str | The destination currency code. If omitted, defaults to USD. (optional)
date = '2013-10-20' # date | The date you want to know the exchange rate on. (optional)
amount = 120.12 # float | The amount in the source currency. If added, Firefly III will calculate the amount in the destination currency. (optional)

try:
    # Get an exchange rate.
    api_response = api_instance.get_exchange_rate(_from=_from, to=to, date=date, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyExchangeRatesApi->get_exchange_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The source currency code. If omitted, defaults to EUR. | [optional] 
 **to** | **str**| The destination currency code. If omitted, defaults to USD. | [optional] 
 **date** | **date**| The date you want to know the exchange rate on. | [optional] 
 **amount** | **float**| The amount in the source currency. If added, Firefly III will calculate the amount in the destination currency. | [optional] 

### Return type

[**ExchangeRate**](ExchangeRate.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

