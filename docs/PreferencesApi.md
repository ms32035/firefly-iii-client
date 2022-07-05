# firefly_iii_client.PreferencesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_preference**](PreferencesApi.md#get_preference) | **GET** /api/v1/preferences/{name} | Return a single preference.
[**list_preference**](PreferencesApi.md#list_preference) | **GET** /api/v1/preferences | List all users preferences.
[**store_preference**](PreferencesApi.md#store_preference) | **POST** /api/v1/preferences | Store a new preference for this user.
[**update_preference**](PreferencesApi.md#update_preference) | **PUT** /api/v1/preferences/{name} | Update preference


# **get_preference**
> PreferenceSingle get_preference(name)

Return a single preference.

Return a single preference and the value.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import preferences_api
from firefly_iii_client.model.preference_single import PreferenceSingle
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
    api_instance = preferences_api.PreferencesApi(api_client)
    name = "currencyPreference" # str | The name of the preference.

    # example passing only required values which don't have defaults set
    try:
        # Return a single preference.
        api_response = api_instance.get_preference(name)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling PreferencesApi->get_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the preference. |

### Return type

[**PreferenceSingle**](PreferenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single preference. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_preference**
> PreferenceArray list_preference()

List all users preferences.

List all of the preferences of the user.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import preferences_api
from firefly_iii_client.model.preference_array import PreferenceArray
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
    api_instance = preferences_api.PreferencesApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all users preferences.
        api_response = api_instance.list_preference(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling PreferencesApi->list_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**PreferenceArray**](PreferenceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of preferences. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_preference**
> PreferenceSingle store_preference(preference)

Store a new preference for this user.

This endpoint creates a new preference. The name and data are free-format, and entirely up to you. If the preference is not used in Firefly III itself it may not be configurable through the user interface, but you can use this endpoint to persist custom data for your own app.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import preferences_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.preference_single import PreferenceSingle
from firefly_iii_client.model.preference import Preference
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
    api_instance = preferences_api.PreferencesApi(api_client)
    preference = Preference(
        data=PolymorphicProperty(None),
        name="currencyPreference",
    ) # Preference | JSON array with the necessary preference information or key=value pairs. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new preference for this user.
        api_response = api_instance.store_preference(preference)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling PreferencesApi->store_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preference** | [**Preference**](Preference.md)| JSON array with the necessary preference information or key&#x3D;value pairs. See the model for the exact specifications. |

### Return type

[**PreferenceSingle**](PreferenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New account stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_preference**
> PreferenceSingle update_preference(name, preference_update)

Update preference

Update a user's preference.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import preferences_api
from firefly_iii_client.model.preference_update import PreferenceUpdate
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.preference_single import PreferenceSingle
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
    api_instance = preferences_api.PreferencesApi(api_client)
    name = "currencyPreference" # str | The name of the preference. Will always overwrite. Will be created if it does not exist.
    preference_update = PreferenceUpdate(
        data=PolymorphicProperty(None),
    ) # PreferenceUpdate | JSON array or key=value pairs with the necessary preference information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update preference
        api_response = api_instance.update_preference(name, preference_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling PreferencesApi->update_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the preference. Will always overwrite. Will be created if it does not exist. |
 **preference_update** | [**PreferenceUpdate**](PreferenceUpdate.md)| JSON array or key&#x3D;value pairs with the necessary preference information. See the model for the exact specifications. |

### Return type

[**PreferenceSingle**](PreferenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated preference. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

