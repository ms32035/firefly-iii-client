# firefly_iii_client.AboutApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about**](AboutApi.md#get_about) | **GET** /v1/about | System information end point.
[**get_cron**](AboutApi.md#get_cron) | **GET** /v1/cron/{cliToken} | Cron job endpoint
[**get_current_user**](AboutApi.md#get_current_user) | **GET** /v1/about/user | Currently authenticated user endpoint.


# **get_about**
> SystemInfo get_about(x_trace_id=x_trace_id)

System information end point.

Returns general system information and versions of the (supporting) software.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.system_info import SystemInfo
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
    api_instance = firefly_iii_client.AboutApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # System information end point.
        api_response = api_instance.get_about(x_trace_id=x_trace_id)
        print("The response of AboutApi->get_about:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AboutApi->get_about: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available system information |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cron**
> CronResult get_cron(cli_token, x_trace_id=x_trace_id, var_date=var_date, force=force)

Cron job endpoint

Firefly III has one endpoint for its various cron related tasks. Send a GET to this endpoint
to run the cron. The cron requires the CLI token to be present. The cron job will fire for all
users.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.cron_result import CronResult
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
    api_instance = firefly_iii_client.AboutApi(api_client)
    cli_token = 'd5ea6b5fb774618dd6ad6ba6e0a7f55c' # str | The CLI token of any user in Firefly III, required to run the cron job.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    var_date = 'Mon Sep 17 00:00:00 UTC 2018' # date | A date formatted YYYY-MM-DD. This can be used to make the cron job pretend it's running on another day.  (optional)
    force = false # bool | Forces the cron job to fire, regardless of whether it has fired before. This may result in double transactions or weird budgets, so be careful.  (optional)

    try:
        # Cron job endpoint
        api_response = api_instance.get_cron(cli_token, x_trace_id=x_trace_id, var_date=var_date, force=force)
        print("The response of AboutApi->get_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AboutApi->get_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_token** | **str**| The CLI token of any user in Firefly III, required to run the cron job. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **var_date** | **date**| A date formatted YYYY-MM-DD. This can be used to make the cron job pretend it&#39;s running on another day.  | [optional] 
 **force** | **bool**| Forces the cron job to fire, regardless of whether it has fired before. This may result in double transactions or weird budgets, so be careful.  | [optional] 

### Return type

[**CronResult**](CronResult.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the cron job(s) firing. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> UserSingle get_current_user(x_trace_id=x_trace_id)

Currently authenticated user endpoint.

Returns the currently authenticated user.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.user_single import UserSingle
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
    api_instance = firefly_iii_client.AboutApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Currently authenticated user endpoint.
        api_response = api_instance.get_current_user(x_trace_id=x_trace_id)
        print("The response of AboutApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AboutApi->get_current_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**UserSingle**](UserSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

