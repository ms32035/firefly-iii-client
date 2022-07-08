# firefly_iii_client.BudgetsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_budget**](BudgetsApi.md#delete_budget) | **DELETE** /api/v1/budgets/{id} | Delete a budget.
[**delete_budget_limit**](BudgetsApi.md#delete_budget_limit) | **DELETE** /api/v1/budgets/{id}/limits/{limitId} | Delete a budget limit.
[**get_budget**](BudgetsApi.md#get_budget) | **GET** /api/v1/budgets/{id} | Get a single budget.
[**get_budget_limit**](BudgetsApi.md#get_budget_limit) | **GET** /api/v1/budgets/{id}/limits/{limitId} | Get single budget limit.
[**list_attachment_by_budget**](BudgetsApi.md#list_attachment_by_budget) | **GET** /api/v1/budgets/{id}/attachments | Lists all attachments of a budget.
[**list_budget**](BudgetsApi.md#list_budget) | **GET** /api/v1/budgets | List all budgets.
[**list_budget_limit**](BudgetsApi.md#list_budget_limit) | **GET** /api/v1/budget-limits | Get list of budget limits by date
[**list_budget_limit_by_budget**](BudgetsApi.md#list_budget_limit_by_budget) | **GET** /api/v1/budgets/{id}/limits | Get all limits for a budget.
[**list_transaction_by_budget**](BudgetsApi.md#list_transaction_by_budget) | **GET** /api/v1/budgets/{id}/transactions | All transactions to a budget.
[**list_transaction_by_budget_limit**](BudgetsApi.md#list_transaction_by_budget_limit) | **GET** /api/v1/budgets/{id}/limits/{limitId}/transactions | List all transactions by a budget limit ID.
[**list_transaction_without_budget**](BudgetsApi.md#list_transaction_without_budget) | **GET** /api/v1/budgets/transactions-without-budget | All transactions without a budget.
[**store_budget**](BudgetsApi.md#store_budget) | **POST** /api/v1/budgets | Store a new budget
[**store_budget_limit**](BudgetsApi.md#store_budget_limit) | **POST** /api/v1/budgets/{id}/limits | Store new budget limit.
[**update_budget**](BudgetsApi.md#update_budget) | **PUT** /api/v1/budgets/{id} | Update existing budget.
[**update_budget_limit**](BudgetsApi.md#update_budget_limit) | **PUT** /api/v1/budgets/{id}/limits/{limitId} | Update existing budget limit.


# **delete_budget**
> delete_budget(id)

Delete a budget.

Delete a budget. Transactions will not be deleted.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget.

    # example passing only required values which don't have defaults set
    try:
        # Delete a budget.
        api_instance.delete_budget(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->delete_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. |

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
> delete_budget_limit(id, limit_id)

Delete a budget limit.

Delete a budget limit.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget. The budget limit MUST be associated to the budget ID.
    limit_id = "123" # str | The ID of the budget limit. The budget limit MUST be associated to the budget ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a budget limit.
        api_instance.delete_budget_limit(id, limit_id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->delete_budget_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. The budget limit MUST be associated to the budget ID. |
 **limit_id** | **str**| The ID of the budget limit. The budget limit MUST be associated to the budget ID. |

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
> BudgetSingle get_budget(id)

Get a single budget.

Get a single budget. If the start date and end date are submitted as well, the \"spent\" array will be updated accordingly.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_single import BudgetSingle
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the requested budget.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to get info on how much the user has spent.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to get info on how much the user has spent.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a single budget.
        api_response = api_instance.get_budget(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->get_budget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a single budget.
        api_response = api_instance.get_budget(id, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->get_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the requested budget. |
 **start** | **date**| A date formatted YYYY-MM-DD, to get info on how much the user has spent.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to get info on how much the user has spent.  | [optional]

### Return type

[**BudgetSingle**](BudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested budget |  -  |
**404** | Budget not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_limit**
> BudgetLimitSingle get_budget_limit(id, limit_id)

Get single budget limit.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_limit_single import BudgetLimitSingle
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget. The budget limit MUST be associated to the budget ID.
    limit_id = 1 # int | The ID of the budget limit. The budget limit MUST be associated to the budget ID.

    # example passing only required values which don't have defaults set
    try:
        # Get single budget limit.
        api_response = api_instance.get_budget_limit(id, limit_id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->get_budget_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. The budget limit MUST be associated to the budget ID. |
 **limit_id** | **int**| The ID of the budget limit. The budget limit MUST be associated to the budget ID. |

### Return type

[**BudgetLimitSingle**](BudgetLimitSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested budget limit |  -  |
**404** | Budget limit not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_budget**
> AttachmentArray list_attachment_by_budget(id)

Lists all attachments of a budget.

Lists all attachments.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.attachment_array import AttachmentArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lists all attachments of a budget.
        api_response = api_instance.list_attachment_by_budget(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_attachment_by_budget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all attachments of a budget.
        api_response = api_instance.list_attachment_by_budget(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_attachment_by_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of attachments |  -  |
**404** | No such budget. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budget**
> BudgetArray list_budget()

List all budgets.

List all the budgets the user has made. If the start date and end date are submitted as well, the \"spent\" array will be updated accordingly.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_array import BudgetArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all budgets.
        api_response = api_instance.list_budget(page=page, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  | [optional]

### Return type

[**BudgetArray**](BudgetArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budgets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budget_limit**
> BudgetLimitArray list_budget_limit(start, end)

Get list of budget limits by date

Get all budget limits for for this date range. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_limit_array import BudgetLimitArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. 

    # example passing only required values which don't have defaults set
    try:
        # Get list of budget limits by date
        api_response = api_instance.list_budget_limit(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_budget_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |

### Return type

[**BudgetLimitArray**](BudgetLimitArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget limits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budget_limit_by_budget**
> BudgetLimitArray list_budget_limit_by_budget(id)

Get all limits for a budget.

Get all budget limits for this budget and the money spent, and money left. You can limit the list by submitting a date range as well. The \"spent\" array for each budget limit is NOT influenced by the start and end date of your query, but by the start and end date of the budget limit itself. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_limit_array import BudgetLimitArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the requested budget.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all limits for a budget.
        api_response = api_instance.list_budget_limit_by_budget(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_budget_limit_by_budget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all limits for a budget.
        api_response = api_instance.list_budget_limit_by_budget(id, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_budget_limit_by_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the requested budget. |
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional]

### Return type

[**BudgetLimitArray**](BudgetLimitArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget limits applicable to this budget. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_budget**
> TransactionArray list_transaction_by_budget(id)

All transactions to a budget.

Get all transactions linked to a budget, possibly limited by start and end

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.model.transaction_array import TransactionArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget.
    limit = 5 # int | Limits the number of results on one page. (optional)
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # All transactions to a budget.
        api_response = api_instance.list_transaction_by_budget(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_transaction_by_budget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # All transactions to a budget.
        api_response = api_instance.list_transaction_by_budget(id, limit=limit, page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_transaction_by_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. |
 **limit** | **int**| Limits the number of results on one page. | [optional]
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned | [optional]

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_budget_limit**
> TransactionArray list_transaction_by_budget_limit(id, limit_id)

List all transactions by a budget limit ID.

List all the transactions within one budget limit. The start and end date are dictated by the budget limit.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.model.transaction_array import TransactionArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget. The budget limit MUST be associated to the budget ID.
    limit_id = "123" # str | The ID of the budget limit. The budget limit MUST be associated to the budget ID.
    page = 1 # int | Page number. The default pagination is 50. (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions by a budget limit ID.
        api_response = api_instance.list_transaction_by_budget_limit(id, limit_id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_transaction_by_budget_limit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions by a budget limit ID.
        api_response = api_instance.list_transaction_by_budget_limit(id, limit_id, page=page, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_transaction_by_budget_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. The budget limit MUST be associated to the budget ID. |
 **limit_id** | **str**| The ID of the budget limit. The budget limit MUST be associated to the budget ID. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned | [optional]

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_without_budget**
> TransactionArray list_transaction_without_budget()

All transactions without a budget.

Get all transactions without a budget, possibly limited by start and end

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.model.transaction_array import TransactionArray
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
    api_instance = budgets_api.BudgetsApi(api_client)
    limit = 5 # int | Limits the number of results on one page. (optional)
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # All transactions without a budget.
        api_response = api_instance.list_transaction_without_budget(limit=limit, page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->list_transaction_without_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of results on one page. | [optional]
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned | [optional]

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_budget**
> BudgetSingle store_budget(budget_store)

Store a new budget

Creates a new budget. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_store import BudgetStore
from firefly_iii_client.model.budget_single import BudgetSingle
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
    api_instance = budgets_api.BudgetsApi(api_client)
    budget_store = BudgetStore(
        active=False,
        auto_budget_amount="-1012.12",
        auto_budget_currency_code="EUR",
        auto_budget_currency_id="12",
        auto_budget_period=AutoBudgetPeriod("monthly"),
        auto_budget_type=AutoBudgetType("reset"),
        name="Bills",
        notes="Some notes",
    ) # BudgetStore | JSON array or key=value pairs with the necessary budget information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new budget
        api_response = api_instance.store_budget(budget_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->store_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_store** | [**BudgetStore**](BudgetStore.md)| JSON array or key&#x3D;value pairs with the necessary budget information. See the model for the exact specifications. |

### Return type

[**BudgetSingle**](BudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New budget stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_budget_limit**
> BudgetLimitSingle store_budget_limit(id, budget_limit_store)

Store new budget limit.

Store a new budget limit under this budget.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.budget_limit_store import BudgetLimitStore
from firefly_iii_client.model.budget_limit_single import BudgetLimitSingle
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget.
    budget_limit_store = BudgetLimitStore(
        amount="123.45",
        currency_code="EUR",
        currency_id="5",
        end=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
        start=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
    ) # BudgetLimitStore | JSON array or key=value pairs with the necessary budget information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store new budget limit.
        api_response = api_instance.store_budget_limit(id, budget_limit_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->store_budget_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. |
 **budget_limit_store** | [**BudgetLimitStore**](BudgetLimitStore.md)| JSON array or key&#x3D;value pairs with the necessary budget information. See the model for the exact specifications. |

### Return type

[**BudgetLimitSingle**](BudgetLimitSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


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
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.budget_update import BudgetUpdate
from firefly_iii_client.model.budget_single import BudgetSingle
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget.
    budget_update = BudgetUpdate(
        active=False,
        auto_budget_amount="-1012.12",
        auto_budget_currency_code="EUR",
        auto_budget_currency_id="12",
        auto_budget_period=AutoBudgetPeriod("monthly"),
        auto_budget_type=AutoBudgetType("reset"),
        name="Bills",
        notes="Some notes",
        order=5,
    ) # BudgetUpdate | JSON array with updated budget information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing budget.
        api_response = api_instance.update_budget(id, budget_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->update_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. |
 **budget_update** | [**BudgetUpdate**](BudgetUpdate.md)| JSON array with updated budget information. See the model for the exact specifications. |

### Return type

[**BudgetSingle**](BudgetSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated budget stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_limit**
> BudgetLimitSingle update_budget_limit(id, limit_id, budget_limit)

Update existing budget limit.

Update existing budget limit.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import budgets_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.budget_limit_single import BudgetLimitSingle
from firefly_iii_client.model.budget_limit import BudgetLimit
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
    api_instance = budgets_api.BudgetsApi(api_client)
    id = "123" # str | The ID of the budget. The budget limit MUST be associated to the budget ID.
    limit_id = "123" # str | The ID of the budget limit. The budget limit MUST be associated to the budget ID.
    budget_limit = BudgetLimit(
        amount="123.45",
        currency_code="EUR",
        currency_id="5",
        end=dateutil_parser('2018-09-17T12:46:47+01:00'),
        start=dateutil_parser('2018-09-17T12:46:47+01:00'),
    ) # BudgetLimit | JSON array with updated budget limit information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing budget limit.
        api_response = api_instance.update_budget_limit(id, limit_id, budget_limit)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BudgetsApi->update_budget_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the budget. The budget limit MUST be associated to the budget ID. |
 **limit_id** | **str**| The ID of the budget limit. The budget limit MUST be associated to the budget ID. |
 **budget_limit** | [**BudgetLimit**](BudgetLimit.md)| JSON array with updated budget limit information. See the model for the exact specifications. |

### Return type

[**BudgetLimitSingle**](BudgetLimitSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated budget limit stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

