# firefly_iii_client.AboutApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about**](AboutApi.md#get_about) | **GET** /api/v1/about | System information end point.
[**get_cron**](AboutApi.md#get_cron) | **GET** /api/v1/cron/{cliToken} | Cron job endpoint
[**get_current_user**](AboutApi.md#get_current_user) | **GET** /api/v1/about/user | Currently authenticated user endpoint.


# **get_about**
> SystemInfo get_about()

System information end point.

Returns general system information and versions of the (supporting) software. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import about_api
from firefly_iii_client.model.system_info import SystemInfo
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
    api_instance = about_api.AboutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # System information end point.
        api_response = api_instance.get_about()
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AboutApi->get_about: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available system information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cron**
> CronResult get_cron(cli_token)

Cron job endpoint

Firefly III has one endpoint for its various cron related tasks. Send a GET to this endpoint to run the cron. The cron requires the CLI token to be present. The cron job will fire for all users. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import about_api
from firefly_iii_client.model.cron_result import CronResult
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
    api_instance = about_api.AboutApi(api_client)
    cli_token = "d5ea6b5fb774618dd6ad6ba6e0a7f55c" # str | The CLI token of any user in Firefly III, required to run the cron job.
    date = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. This can be used to make the cron job pretend it's running on another day.  (optional)
    force = False # bool | Forces the cron job to fire, regardless of whether it has fired before. This may result in double transactions or weird budgets, so be careful.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cron job endpoint
        api_response = api_instance.get_cron(cli_token)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AboutApi->get_cron: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cron job endpoint
        api_response = api_instance.get_cron(cli_token, date=date, force=force)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AboutApi->get_cron: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_token** | **str**| The CLI token of any user in Firefly III, required to run the cron job. |
 **date** | **date**| A date formatted YYYY-MM-DD. This can be used to make the cron job pretend it&#39;s running on another day.  | [optional]
 **force** | **bool**| Forces the cron job to fire, regardless of whether it has fired before. This may result in double transactions or weird budgets, so be careful.  | [optional]

### Return type

[**CronResult**](CronResult.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of the cron job(s) firing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> UserSingle get_current_user()

Currently authenticated user endpoint.

Returns the currently authenticated user. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import about_api
from firefly_iii_client.model.user_single import UserSingle
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
    api_instance = about_api.AboutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Currently authenticated user endpoint.
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AboutApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSingle**](UserSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

