# firefly_iii_client.ChartsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chart_account_overview**](ChartsApi.md#get_chart_account_overview) | **GET** /api/v1/chart/account/overview | Dashboard chart with asset account balance information.


# **get_chart_account_overview**
> ChartLine get_chart_account_overview(start, end)

Dashboard chart with asset account balance information.

This endpoint returns the data required to generate a chart with basic asset account balance information. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import charts_api
from firefly_iii_client.model.chart_line import ChartLine
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
    api_instance = charts_api.ChartsApi(api_client)
    start = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. 

    # example passing only required values which don't have defaults set
    try:
        # Dashboard chart with asset account balance information.
        api_response = api_instance.get_chart_account_overview(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ChartsApi->get_chart_account_overview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |

### Return type

[**ChartLine**](ChartLine.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Line chart oriented chart information. Check out the model for more details. Each entry is a line (or bar) in the chart. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

