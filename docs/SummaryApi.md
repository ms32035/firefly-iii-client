# firefly_iii_client.SummaryApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_summary**](SummaryApi.md#get_basic_summary) | **GET** /v1/summary/basic | Returns basic sums of the users data.


# **get_basic_summary**
> Dict[str, BasicSummaryEntry] get_basic_summary(start, end, x_trace_id=x_trace_id, currency_code=currency_code)

Returns basic sums of the users data.

Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is used in Firefly III to populate the dashboard.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.basic_summary_entry import BasicSummaryEntry
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
    api_instance = firefly_iii_client.SummaryApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
    end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    currency_code = 'currency_code_example' # str | A currency code like EUR or USD, to filter the result.  (optional)

    try:
        # Returns basic sums of the users data.
        api_response = api_instance.get_basic_summary(start, end, x_trace_id=x_trace_id, currency_code=currency_code)
        print("The response of SummaryApi->get_basic_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummaryApi->get_basic_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **currency_code** | **str**| A currency code like EUR or USD, to filter the result.  | [optional] 

### Return type

[**Dict[str, BasicSummaryEntry]**](BasicSummaryEntry.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of sums. It depends on the user what you can expect to get back, so please try this out on the demo site. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

