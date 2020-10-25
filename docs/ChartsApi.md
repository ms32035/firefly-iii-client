# firefly_iii_client.ChartsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chart_ab_overview**](ChartsApi.md#get_chart_ab_overview) | **GET** /api/v1/chart/ab/overview/{id} | Dashboard chart with an overview of the available budget.
[**get_chart_account_expense**](ChartsApi.md#get_chart_account_expense) | **GET** /api/v1/chart/account/expense | Dashboard chart with expense account balance information.
[**get_chart_account_overview**](ChartsApi.md#get_chart_account_overview) | **GET** /api/v1/chart/account/overview | Dashboard chart with asset account balance information.
[**get_chart_account_revenue**](ChartsApi.md#get_chart_account_revenue) | **GET** /api/v1/chart/account/revenue | Dashboard chart with revenue account balance information.
[**get_chart_category_overview**](ChartsApi.md#get_chart_category_overview) | **GET** /api/v1/chart/category/overview | Dashboard chart with an overview of the users categories.


# **get_chart_ab_overview**
> list[ChartDataSet] get_chart_ab_overview(id, start, end)

Dashboard chart with an overview of the available budget.

This endpoint returns the data required to generate a pie chart for the available budget. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.ChartsApi(api_client)
    id = 1 # int | The ID of the available budget.
start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 

    try:
        # Dashboard chart with an overview of the available budget.
        api_response = api_instance.get_chart_ab_overview(id, start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartsApi->get_chart_ab_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the available budget. | 
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 

### Return type

[**list[ChartDataSet]**](ChartDataSet.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pie chart oriented chart information. Check out the model for more details. Each entry is a piece of the pie in the chart. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_account_expense**
> list[ChartDataSet] get_chart_account_expense(start, end)

Dashboard chart with expense account balance information.

This endpoint returns the data required to generate a chart that shows the user how much they've spent on their expense accounts. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.ChartsApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 

    try:
        # Dashboard chart with expense account balance information.
        api_response = api_instance.get_chart_account_expense(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartsApi->get_chart_account_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 

### Return type

[**list[ChartDataSet]**](ChartDataSet.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bar chart oriented chart information. Check out the model for more details. Each entry is a line (or bar) in the chart. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_account_overview**
> list[ChartDataSet] get_chart_account_overview(start, end)

Dashboard chart with asset account balance information.

This endpoint returns the data required to generate a chart with basic asset account balance information. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.ChartsApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 

    try:
        # Dashboard chart with asset account balance information.
        api_response = api_instance.get_chart_account_overview(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartsApi->get_chart_account_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 

### Return type

[**list[ChartDataSet]**](ChartDataSet.md)

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

# **get_chart_account_revenue**
> list[ChartDataSet] get_chart_account_revenue(start, end)

Dashboard chart with revenue account balance information.

This endpoint returns the data required to generate a chart that shows the user how much they've earned from their revenue accounts. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.ChartsApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 

    try:
        # Dashboard chart with revenue account balance information.
        api_response = api_instance.get_chart_account_revenue(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartsApi->get_chart_account_revenue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 

### Return type

[**list[ChartDataSet]**](ChartDataSet.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bar chart oriented chart information. Check out the model for more details. Each entry is a line (or bar) in the chart. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_category_overview**
> list[ChartDataSet] get_chart_category_overview(start, end)

Dashboard chart with an overview of the users categories.

This endpoint returns the data required to generate a bar chart for the expenses and incomes on the users categories. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.ChartsApi(api_client)
    start = '2013-10-20' # date | A date formatted YYYY-MM-DD. 
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. 

    try:
        # Dashboard chart with an overview of the users categories.
        api_response = api_instance.get_chart_category_overview(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartsApi->get_chart_category_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  | 
 **end** | **date**| A date formatted YYYY-MM-DD.  | 

### Return type

[**list[ChartDataSet]**](ChartDataSet.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bar chart oriented chart information. Check out the model for more details. Each entry is a set of bars in the chart. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

