# firefly_iii_client.ConfigurationApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](ConfigurationApi.md#get_configuration) | **GET** /v1/configuration | Get Firefly III system configuration values.
[**get_single_configuration**](ConfigurationApi.md#get_single_configuration) | **GET** /v1/configuration/{name} | Get a single Firefly III system configuration value
[**set_configuration**](ConfigurationApi.md#set_configuration) | **PUT** /v1/configuration/{name} | Update configuration value


# **get_configuration**
> List[Configuration] get_configuration(x_trace_id=x_trace_id)

Get Firefly III system configuration values.

Returns all editable and not-editable configuration values for this Firefly III installation

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.configuration import Configuration
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
    api_instance = firefly_iii_client.ConfigurationApi(api_client)
    x_trace_id = 'x_trace_id_example' # str | Unique identifier associated with this request. (optional)

    try:
        # Get Firefly III system configuration values.
        api_response = api_instance.get_configuration(x_trace_id=x_trace_id)
        print("The response of ConfigurationApi->get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**List[Configuration]**](Configuration.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-www-form-urlencoded

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System configuration values |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_configuration**
> ConfigurationSingle get_single_configuration(name, x_trace_id=x_trace_id)

Get a single Firefly III system configuration value

Returns one configuration variable for this Firefly III installation

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.config_value_filter import ConfigValueFilter
from firefly_iii_client.models.configuration_single import ConfigurationSingle
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
    api_instance = firefly_iii_client.ConfigurationApi(api_client)
    name = firefly_iii_client.ConfigValueFilter() # ConfigValueFilter | The name of the configuration value you want to know.
    x_trace_id = 'x_trace_id_example' # str | Unique identifier associated with this request. (optional)

    try:
        # Get a single Firefly III system configuration value
        api_response = api_instance.get_single_configuration(name, x_trace_id=x_trace_id)
        print("The response of ConfigurationApi->get_single_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->get_single_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**ConfigValueFilter**](.md)| The name of the configuration value you want to know. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**ConfigurationSingle**](ConfigurationSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One system configuration value |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration**
> ConfigurationSingle set_configuration(name, configuration_update, x_trace_id=x_trace_id)

Update configuration value

Set a single configuration value. Not all configuration values can be updated so the list of accepted configuration variables is small.

### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.config_value_update_filter import ConfigValueUpdateFilter
from firefly_iii_client.models.configuration_single import ConfigurationSingle
from firefly_iii_client.models.configuration_update import ConfigurationUpdate
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
    api_instance = firefly_iii_client.ConfigurationApi(api_client)
    name = firefly_iii_client.ConfigValueUpdateFilter() # ConfigValueUpdateFilter | The name of the configuration value you want to update.
    configuration_update = firefly_iii_client.ConfigurationUpdate() # ConfigurationUpdate | JSON array with the necessary account information or key=value pairs. See the model for the exact specifications.
    x_trace_id = 'x_trace_id_example' # str | Unique identifier associated with this request. (optional)

    try:
        # Update configuration value
        api_response = api_instance.set_configuration(name, configuration_update, x_trace_id=x_trace_id)
        print("The response of ConfigurationApi->set_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->set_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**ConfigValueUpdateFilter**](.md)| The name of the configuration value you want to update. | 
 **configuration_update** | [**ConfigurationUpdate**](ConfigurationUpdate.md)| JSON array with the necessary account information or key&#x3D;value pairs. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**ConfigurationSingle**](ConfigurationSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New configuration value stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

