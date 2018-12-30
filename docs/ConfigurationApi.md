# firefly_iii_client.ConfigurationApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](ConfigurationApi.md#get_configuration) | **GET** /api/v1/configuration | Get Firefly III system configuration.
[**set_configuration**](ConfigurationApi.md#set_configuration) | **POST** /api/v1/configuration/{name} | Update configuration


# **get_configuration**
> Configuration get_configuration()

Get Firefly III system configuration.

Get system configuration

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.ConfigurationApi(firefly_iii_client.ApiClient(configuration))

try:
    # Get Firefly III system configuration.
    api_response = api_instance.get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Configuration**](Configuration.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration**
> Configuration set_configuration(name, configuration_update)

Update configuration

Set a single config value.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.ConfigurationApi(firefly_iii_client.ApiClient(configuration))
name = single_user_mode # str | The configuration value name.
configuration_update = firefly_iii_client.ConfigurationUpdate() # ConfigurationUpdate | JSON array with the necessary account information or key=value pairs. See the model for the exact specifications.

try:
    # Update configuration
    api_response = api_instance.set_configuration(name, configuration_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->set_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The configuration value name. | 
 **configuration_update** | [**ConfigurationUpdate**](ConfigurationUpdate.md)| JSON array with the necessary account information or key&#x3D;value pairs. See the model for the exact specifications. | 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

