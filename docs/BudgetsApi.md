# firefly_iii_client.BudgetsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_budget**](BudgetsApi.md#delete_budget) | **DELETE** /api/v1/budgets/{id} | Delete a budget.
[**delete_budget_limit**](BudgetsApi.md#delete_budget_limit) | **DELETE** /api/v1/budgets/limits/{id} | Delete a budget limit.
[**get_budget**](BudgetsApi.md#get_budget) | **GET** /api/v1/budgets/{id} | Get a single budget.
[**get_budget_limit**](BudgetsApi.md#get_budget_limit) | **GET** /api/v1/budgets/limits/{id} | Get single budget limit.
[**get_budget_limits**](BudgetsApi.md#get_budget_limits) | **GET** /api/v1/budgets/{id}/limits | Get all limits
[**get_budgets**](BudgetsApi.md#get_budgets) | **GET** /api/v1/budgets | List all budgets.
[**get_transactions_by_budget**](BudgetsApi.md#get_transactions_by_budget) | **GET** /api/v1/budgets/{id}/transactions | All transactions to a budget.
[**get_transactions_by_budget_limit**](BudgetsApi.md#get_transactions_by_budget_limit) | **GET** /api/v1/budgets/limits/{id}/transactions | List all transactions by a budget limit ID.
[**store_budget**](BudgetsApi.md#store_budget) | **POST** /api/v1/budgets | Store a new budget
[**store_budget_limit**](BudgetsApi.md#store_budget_limit) | **POST** /api/v1/budgets/{id}/limits | Store new budget limit.
[**update_budget**](BudgetsApi.md#update_budget) | **PUT** /api/v1/budgets/{id} | Update existing budget.
[**update_budget_limit**](BudgetsApi.md#update_budget_limit) | **PUT** /api/v1/budgets/limits/{id} | Update existing budget limit.


# **delete_budget**
> delete_budget(id)

Delete a budget.

Delete a budget. Transactions will not be deleted.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the budget.

try:
    # Delete a budget.
    api_instance.delete_budget(id)
except ApiException as e:
    print("Exception when calling BudgetsApi->delete_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the budget. | 

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
**204** | Budget deleted. |  -  |
**404** | No such budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget_limit**
> delete_budget_limit(id)

Delete a budget limit.

Delete a budget limit.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the requested budget limit.

try:
    # Delete a budget limit.
    api_instance.delete_budget_limit(id)
except ApiException as e:
    print("Exception when calling BudgetsApi->delete_budget_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the requested budget limit. | 

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
**204** | Budget limit deleted. |  -  |
**404** | No such budget limit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget**
> BudgetSingle get_budget(id, start_date=start_date, end_date=end_date)

Get a single budget.

Get a single budget. If the start date and end date are submitted as well, the \"spent\" array will be updated accordingly.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the requested budget.
start_date = '2018-09-17' # str | A date formatted YYYY-MM-DD, to get info on how much the user has spent.  (optional)
end_date = '2018-12-31' # str | A date formatted YYYY-MM-DD, to get info on how much the user has spent.  (optional)

try:
    # Get a single budget.
    api_response = api_instance.get_budget(id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the requested budget. | 
 **start_date** | **str**| A date formatted YYYY-MM-DD, to get info on how much the user has spent.  | [optional] 
 **end_date** | **str**| A date formatted YYYY-MM-DD, to get info on how much the user has spent.  | [optional] 

### Return type

[**BudgetSingle**](BudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested budget |  -  |
**404** | Budget not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_limit**
> BudgetLimitSingle get_budget_limit(id)

Get single budget limit.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the requested budget limit.

try:
    # Get single budget limit.
    api_response = api_instance.get_budget_limit(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the requested budget limit. | 

### Return type

[**BudgetLimitSingle**](BudgetLimitSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested budget limit |  -  |
**404** | Budget limit not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_limits**
> BudgetLimitArray get_budget_limits(id, start=start, end=end)

Get all limits

Get all budget limits for this budget and the money spent, and money left. You can limit the list by submitting a date range as well. The \"spent\" array for each budget limit is NOT influenced by the start and end date of your query, but by the start and end date of the budget limit itself. 

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the requested budget.
start = '2018-09-17' # str | A date formatted YYYY-MM-DD.  (optional)
end = '2018-12-31' # str | A date formatted YYYY-MM-DD.  (optional)

try:
    # Get all limits
    api_response = api_instance.get_budget_limits(id, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the requested budget. | 
 **start** | **str**| A date formatted YYYY-MM-DD.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD.  | [optional] 

### Return type

[**BudgetLimitArray**](BudgetLimitArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget limits applicable to this budget. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets**
> BudgetArray get_budgets(page=page, start=start, end=end)

List all budgets.

List all the budgets the user has made. If the start date and end date are submitted as well, the \"spent\" array will be updated accordingly.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)
start = '2018-09-17' # str | A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  (optional)
end = '2018-12-31' # str | A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  (optional)

try:
    # List all budgets.
    api_response = api_instance.get_budgets(page=page, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  | [optional] 

### Return type

[**BudgetArray**](BudgetArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budgets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_budget**
> TransactionArray get_transactions_by_budget(id, limit=limit, page=page, start=start, end=end, type=type)

All transactions to a budget.

Get all transactions linked to a budget, possibly limited by start and end

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the budget.
limit = 5 # int | Limits the number of results on one page. (optional)
page = 1 # int | Page number. The default pagination is 50. (optional)
start = '2018-09-17' # str | A date formatted YYYY-MM-DD.  (optional)
end = '2018-12-31' # str | A date formatted YYYY-MM-DD.  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned (optional)

try:
    # All transactions to a budget.
    api_response = api_instance.get_transactions_by_budget(id, limit=limit, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_transactions_by_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the budget. | 
 **limit** | **int**| Limits the number of results on one page. | [optional] 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD.  | [optional] 
 **type** | **str**| Optional filter on the transaction type(s) returned | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_budget_limit**
> TransactionArray get_transactions_by_budget_limit(id, page=page, type=type)

List all transactions by a budget limit ID.

List all the transactions within one budget limit. The start and end date are dictated by the budget limit.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the requested budget limit.
page = 1 # int | Page number. The default pagination is 50. (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned (optional)

try:
    # List all transactions by a budget limit ID.
    api_response = api_instance.get_transactions_by_budget_limit(id, page=page, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_transactions_by_budget_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the requested budget limit. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **type** | **str**| Optional filter on the transaction type(s) returned | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_budget**
> BudgetSingle store_budget(budget_update)

Store a new budget

Creates a new budget. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
budget_update = firefly_iii_client.BudgetUpdate() # BudgetUpdate | JSON array or key=value pairs with the necessary budget information. See the model for the exact specifications.

try:
    # Store a new budget
    api_response = api_instance.store_budget(budget_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->store_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_update** | [**BudgetUpdate**](BudgetUpdate.md)| JSON array or key&#x3D;value pairs with the necessary budget information. See the model for the exact specifications. | 

### Return type

[**BudgetSingle**](BudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New budget stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_budget_limit**
> BudgetLimitSingle store_budget_limit(id, budget_limit_update)

Store new budget limit.

Store a new budget limit.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the budget.
budget_limit_update = firefly_iii_client.BudgetLimitUpdate() # BudgetLimitUpdate | JSON array or key=value pairs with the necessary budget information. See the model for the exact specifications.

try:
    # Store new budget limit.
    api_response = api_instance.store_budget_limit(id, budget_limit_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->store_budget_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the budget. | 
 **budget_limit_update** | [**BudgetLimitUpdate**](BudgetLimitUpdate.md)| JSON array or key&#x3D;value pairs with the necessary budget information. See the model for the exact specifications. | 

### Return type

[**BudgetLimitSingle**](BudgetLimitSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New budget limit stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget**
> BudgetSingle update_budget(id, budget_update)

Update existing budget.

Update existing budget. This endpoint cannot be used to set budget amount limits.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the budget.
budget_update = firefly_iii_client.BudgetUpdate() # BudgetUpdate | JSON array with updated budget information. See the model for the exact specifications.

try:
    # Update existing budget.
    api_response = api_instance.update_budget(id, budget_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->update_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the budget. | 
 **budget_update** | [**BudgetUpdate**](BudgetUpdate.md)| JSON array with updated budget information. See the model for the exact specifications. | 

### Return type

[**BudgetSingle**](BudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated budget stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_limit**
> BudgetLimitSingle update_budget_limit(id, budget_limit_update)

Update existing budget limit.

Update existing budget limit.

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
api_instance = firefly_iii_client.BudgetsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the requested budget limit. The budget limit MUST be associated to the budget ID.
budget_limit_update = firefly_iii_client.BudgetLimitUpdate() # BudgetLimitUpdate | JSON array with updated budget limit information. See the model for the exact specifications.

try:
    # Update existing budget limit.
    api_response = api_instance.update_budget_limit(id, budget_limit_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->update_budget_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the requested budget limit. The budget limit MUST be associated to the budget ID. | 
 **budget_limit_update** | [**BudgetLimitUpdate**](BudgetLimitUpdate.md)| JSON array with updated budget limit information. See the model for the exact specifications. | 

### Return type

[**BudgetLimitSingle**](BudgetLimitSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated budget limit stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

