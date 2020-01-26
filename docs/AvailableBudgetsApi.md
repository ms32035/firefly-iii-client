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
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.AvailableBudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the available budget.

try:
    # Delete an available budget.
    api_instance.delete_available_budget(id)
except ApiException as e:
    print("Exception when calling AvailableBudgetsApi->delete_available_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the available budget. | 

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
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.AvailableBudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the available budget.

try:
    # Get a single available budget.
    api_response = api_instance.get_available_budget(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailableBudgetsApi->get_available_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the available budget. | 

### Return type

[**AvailableBudgetSingle**](AvailableBudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested available budget |  -  |
**404** | AvailableBudget not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_budget**
> AvailableBudgetArray list_available_budget(page=page, start=start, end=end)

List all available budget amounts.

Firefly III allows users to set the amount that is available to be budgeted in so-called \"available budgets\". For example, the user could have 1200,- available to be divided during the coming month. This amount is used on the /budgets page. This endpoint returns all of these amounts and the periods for which they are set. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.AvailableBudgetsApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)
start = '2013-10-20' # date | A date formatted YYYY-MM-DD.  (optional)
end = '2013-10-20' # date | A date formatted YYYY-MM-DD.  (optional)

try:
    # List all available budget amounts.
    api_response = api_instance.list_available_budget(page=page, start=start, end=end)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available budget amounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_available_budget**
> AvailableBudgetSingle store_available_budget(available_budget)

Store a new available budget

Creates a new available budget for a specified period. The data required can be submitted as a JSON body or as a list of parameters. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.AvailableBudgetsApi(firefly_iii_client.ApiClient(configuration))
available_budget = firefly_iii_client.AvailableBudget() # AvailableBudget | JSON array or key=value pairs with the necessary available budget information. See the model for the exact specifications.

try:
    # Store a new available budget
    api_response = api_instance.store_available_budget(available_budget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailableBudgetsApi->store_available_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_budget** | [**AvailableBudget**](AvailableBudget.md)| JSON array or key&#x3D;value pairs with the necessary available budget information. See the model for the exact specifications. | 

### Return type

[**AvailableBudgetSingle**](AvailableBudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New available budget stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_available_budget**
> AvailableBudgetSingle update_available_budget(id, available_budget)

Update existing available budget, to change for example the date range of the amount or the amount itself.

Update existing available budget.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.AvailableBudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the object.X
available_budget = firefly_iii_client.AvailableBudget() # AvailableBudget | JSON array or form value with updated available budget information. See the model for the exact specifications.

try:
    # Update existing available budget, to change for example the date range of the amount or the amount itself.
    api_response = api_instance.update_available_budget(id, available_budget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailableBudgetsApi->update_available_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the object.X | 
 **available_budget** | [**AvailableBudget**](AvailableBudget.md)| JSON array or form value with updated available budget information. See the model for the exact specifications. | 

### Return type

[**AvailableBudgetSingle**](AvailableBudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated available budget stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

