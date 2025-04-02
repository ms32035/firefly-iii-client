# firefly_iii_client.ChartsApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chart_account_overview**](ChartsApi.md#get_chart_account_overview) | **GET** /v1/chart/account/overview | Dashboard chart with asset account balance information.


# **get_chart_account_overview**
> List[ChartDataSet] get_chart_account_overview(start, end, x_trace_id=x_trace_id)

Dashboard chart with asset account balance information.

This endpoint returns the data required to generate a chart with basic asset account balance information.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.chart_data_set import ChartDataSet
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
    api_instance = firefly_iii_client.ChartsApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
    end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Dashboard chart with asset account balance information.
        api_response = api_instance.get_chart_account_overview(start, end, x_trace_id=x_trace_id)
        print("The response of ChartsApi->get_chart_account_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChartsApi->get_chart_account_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**List[ChartDataSet]**](ChartDataSet.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Line chart oriented chart information. Check out the model for more details. Each entry is a line (or bar) in the chart. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

