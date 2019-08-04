# firefly_iii_client.SummaryApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_summary**](SummaryApi.md#get_basic_summary) | **GET** /api/v1/summary/basic | Returns basic sums of the users data.


# **get_basic_summary**
> list[BasicSummaryEntry] get_basic_summary(start, end)

Returns basic sums of the users data.

Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is in Firefly III to populate the dashboard. 

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
api_instance = firefly_iii_client.SummaryApi(firefly_iii_client.ApiClient(configuration))
start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 

try:
    # Returns basic sums of the users data.
    api_response = api_instance.get_basic_summary(start, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryApi->get_basic_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 

### Return type

[**list[BasicSummaryEntry]**](BasicSummaryEntry.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of sums. It depends on the user what you can expect to get back, so please check out the documentation and try this out on the demo site. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

