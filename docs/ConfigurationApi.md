# firefly_iii_client.ConfigurationApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](ConfigurationApi.md#get_configuration) | **GET** /api/v1/configuration | Get Firefly III system configuration values.
[**get_single_configuration**](ConfigurationApi.md#get_single_configuration) | **GET** /api/v1/configuration/{name} | Get a single Firefly III system configuration value
[**set_configuration**](ConfigurationApi.md#set_configuration) | **PUT** /api/v1/configuration/{name} | Update configuration value


# **get_configuration**
> ConfigurationArray get_configuration()

Get Firefly III system configuration values.

Returns all editable and not-editable configuration values for this Firefly III installation

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import configuration_api
from firefly_iii_client.model.configuration_array import ConfigurationArray
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
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Firefly III system configuration values.
        api_response = api_instance.get_configuration()
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationArray**](ConfigurationArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System configuration values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_configuration**
> ConfigurationSingle get_single_configuration(name)

Get a single Firefly III system configuration value

Returns one configuration variable for this Firefly III installation

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import configuration_api
from firefly_iii_client.model.config_value_filter import ConfigValueFilter
from firefly_iii_client.model.configuration_single import ConfigurationSingle
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    name = ConfigValueFilter("configuration.is_demo_site") # ConfigValueFilter | The name of the configuration value you want to know.

    # example passing only required values which don't have defaults set
    try:
        # Get a single Firefly III system configuration value
        api_response = api_instance.get_single_configuration(name)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->get_single_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **ConfigValueFilter**| The name of the configuration value you want to know. |

### Return type

[**ConfigurationSingle**](ConfigurationSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One system configuration value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration**
> ConfigurationSingle set_configuration(name, configuration_update)

Update configuration value

Set a single configuration value. Not all configuration values can be updated so the list of accepted configuration variables is small.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import configuration_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.configuration_single import ConfigurationSingle
from firefly_iii_client.model.config_value_update_filter import ConfigValueUpdateFilter
from firefly_iii_client.model.configuration_update import ConfigurationUpdate
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    name = ConfigValueUpdateFilter("configuration.is_demo_site") # ConfigValueUpdateFilter | The name of the configuration value you want to update.
    configuration_update = ConfigurationUpdate(
        value=,
    ) # ConfigurationUpdate | JSON array with the necessary account information or key=value pairs. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update configuration value
        api_response = api_instance.set_configuration(name, configuration_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling ConfigurationApi->set_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **ConfigValueUpdateFilter**| The name of the configuration value you want to update. |
 **configuration_update** | [**ConfigurationUpdate**](ConfigurationUpdate.md)| JSON array with the necessary account information or key&#x3D;value pairs. See the model for the exact specifications. |

### Return type

[**ConfigurationSingle**](ConfigurationSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New configuration value stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

