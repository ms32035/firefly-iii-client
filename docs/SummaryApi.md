# firefly_iii_client.SummaryApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_summary**](SummaryApi.md#get_basic_summary) | **GET** /api/v1/summary/basic | Returns basic sums of the users data.


# **get_basic_summary**
> BasicSummary get_basic_summary(start, end)

Returns basic sums of the users data.

Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is used in Firefly III to populate the dashboard. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import summary_api
from firefly_iii_client.model.basic_summary import BasicSummary
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
    api_instance = summary_api.SummaryApi(api_client)
    start = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. 
    currency_code = "currency_code_example" # str | A currency code like EUR or USD, to filter the result.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns basic sums of the users data.
        api_response = api_instance.get_basic_summary(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SummaryApi->get_basic_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns basic sums of the users data.
        api_response = api_instance.get_basic_summary(start, end, currency_code=currency_code)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SummaryApi->get_basic_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **currency_code** | **str**| A currency code like EUR or USD, to filter the result.  | [optional]

### Return type

[**BasicSummary**](BasicSummary.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of sums. It depends on the user what you can expect to get back, so please try this out on the demo site. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

