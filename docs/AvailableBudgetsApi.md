# firefly_iii_client.AvailableBudgetsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_available_budget**](AvailableBudgetsApi.md#delete_available_budget) | **DELETE** /api/v1/available_budgets/{id} | Delete an available budget.
[**get_available_budget**](AvailableBudgetsApi.md#get_available_budget) | **GET** /api/v1/available_budgets/{id} | Get a single available budget.
[**list_available_budget**](AvailableBudgetsApi.md#list_available_budget) | **GET** /api/v1/available_budgets | List all available budget amounts.
[**store_available_budget**](AvailableBudgetsApi.md#store_available_budget) | **POST** /api/v1/available_budgets | Store a new available budget
[**update_available_budget**](AvailableBudgetsApi.md#update_available_budget) | **PUT** /api/v1/available_budgets/{id} | Update existing available budget, to change for example the date range of the amount or the amount itself.


# **delete_available_budget**
> delete_available_budget(id)

Delete an available budget.

Delete an available budget. Not much more to say.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import available_budgets_api
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
    api_instance = available_budgets_api.AvailableBudgetsApi(api_client)
    id = "123" # str | The ID of the available budget.

    # example passing only required values which don't have defaults set
    try:
        # Delete an available budget.
        api_instance.delete_available_budget(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AvailableBudgetsApi->delete_available_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the available budget. |

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Available budget deleted. |  -  |
**404** | No such available budget. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_budget**
> AvailableBudgetSingle get_available_budget(id)

Get a single available budget.

Get a single available budget, by ID.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import available_budgets_api
from firefly_iii_client.model.available_budget_single import AvailableBudgetSingle
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
    api_instance = available_budgets_api.AvailableBudgetsApi(api_client)
    id = "123" # str | The ID of the available budget.

    # example passing only required values which don't have defaults set
    try:
        # Get a single available budget.
        api_response = api_instance.get_available_budget(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AvailableBudgetsApi->get_available_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the available budget. |

### Return type

[**AvailableBudgetSingle**](AvailableBudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested available budget |  -  |
**404** | AvailableBudget not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_budget**
> AvailableBudgetArray list_available_budget()

List all available budget amounts.

Firefly III allows users to set the amount that is available to be budgeted in so-called \"available budgets\". For example, the user could have 1200,- available to be divided during the coming month. This amount is used on the /budgets page. This endpoint returns all of these amounts and the periods for which they are set. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import available_budgets_api
from firefly_iii_client.model.available_budget_array import AvailableBudgetArray
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
    api_instance = available_budgets_api.AvailableBudgetsApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all available budget amounts.
        api_response = api_instance.list_available_budget(page=page, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AvailableBudgetsApi->list_available_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional]

### Return type

[**AvailableBudgetArray**](AvailableBudgetArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available budget amounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_available_budget**
> AvailableBudgetSingle store_available_budget(available_budget_store)

Store a new available budget

Creates a new available budget for a specified period. The data required can be submitted as a JSON body or as a list of parameters. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import available_budgets_api
from firefly_iii_client.model.available_budget_single import AvailableBudgetSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.available_budget_store import AvailableBudgetStore
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
    api_instance = available_budgets_api.AvailableBudgetsApi(api_client)
    available_budget_store = AvailableBudgetStore(
        amount="123.45",
        currency_code="EUR",
        currency_id="5",
        end=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
        start=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
    ) # AvailableBudgetStore | JSON array or key=value pairs with the necessary available budget information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new available budget
        api_response = api_instance.store_available_budget(available_budget_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AvailableBudgetsApi->store_available_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_budget_store** | [**AvailableBudgetStore**](AvailableBudgetStore.md)| JSON array or key&#x3D;value pairs with the necessary available budget information. See the model for the exact specifications. |

### Return type

[**AvailableBudgetSingle**](AvailableBudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New available budget stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_available_budget**
> AvailableBudgetSingle update_available_budget(id, available_budget_update)

Update existing available budget, to change for example the date range of the amount or the amount itself.

Update existing available budget.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import available_budgets_api
from firefly_iii_client.model.available_budget_update import AvailableBudgetUpdate
from firefly_iii_client.model.available_budget_single import AvailableBudgetSingle
from firefly_iii_client.model.validation_error import ValidationError
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
    api_instance = available_budgets_api.AvailableBudgetsApi(api_client)
    id = "123" # str | The ID of the object.X
    available_budget_update = AvailableBudgetUpdate(
        amount="123.45",
        currency_code="EUR",
        currency_id="5",
        end=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
        start=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
    ) # AvailableBudgetUpdate | JSON array or form value with updated available budget information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing available budget, to change for example the date range of the amount or the amount itself.
        api_response = api_instance.update_available_budget(id, available_budget_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AvailableBudgetsApi->update_available_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the object.X |
 **available_budget_update** | [**AvailableBudgetUpdate**](AvailableBudgetUpdate.md)| JSON array or form value with updated available budget information. See the model for the exact specifications. |

### Return type

[**AvailableBudgetSingle**](AvailableBudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated available budget stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

