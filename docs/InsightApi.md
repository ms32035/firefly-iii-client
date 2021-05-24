# firefly_iii_client.InsightApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insight_expense_asset**](InsightApi.md#insight_expense_asset) | **GET** /api/v1/insight/expense/asset | Insight into expenses, grouped by asset account.
[**insight_expense_bill**](InsightApi.md#insight_expense_bill) | **GET** /api/v1/insight/expense/bill | Insight into expenses, grouped by bill.
[**insight_expense_budget**](InsightApi.md#insight_expense_budget) | **GET** /api/v1/insight/expense/budget | Insight into expenses, grouped by budget.
[**insight_expense_category**](InsightApi.md#insight_expense_category) | **GET** /api/v1/insight/expense/category | Insight into expenses, grouped by category.
[**insight_expense_expense**](InsightApi.md#insight_expense_expense) | **GET** /api/v1/insight/expense/expense | Insight into expenses, grouped by expense account.
[**insight_expense_no_bill**](InsightApi.md#insight_expense_no_bill) | **GET** /api/v1/insight/expense/no-bill | Insight into expenses, without bill.
[**insight_expense_no_budget**](InsightApi.md#insight_expense_no_budget) | **GET** /api/v1/insight/expense/no-budget | Insight into expenses, without budget.
[**insight_expense_no_category**](InsightApi.md#insight_expense_no_category) | **GET** /api/v1/insight/expense/no-category | Insight into expenses, without category.
[**insight_expense_no_tag**](InsightApi.md#insight_expense_no_tag) | **GET** /api/v1/insight/expense/no-tag | Insight into expenses, without tag.
[**insight_expense_tag**](InsightApi.md#insight_expense_tag) | **GET** /api/v1/insight/expense/tag | Insight into expenses, grouped by tag.
[**insight_expense_total**](InsightApi.md#insight_expense_total) | **GET** /api/v1/insight/expense/total | Insight into total expenses.
[**insight_income_asset**](InsightApi.md#insight_income_asset) | **GET** /api/v1/insight/income/asset | Insight into income, grouped by asset account.
[**insight_income_category**](InsightApi.md#insight_income_category) | **GET** /api/v1/insight/income/category | Insight into income, grouped by category.
[**insight_income_no_category**](InsightApi.md#insight_income_no_category) | **GET** /api/v1/insight/income/no-category | Insight into income, without category.
[**insight_income_no_tag**](InsightApi.md#insight_income_no_tag) | **GET** /api/v1/insight/income/no-tag | Insight into income, without tag.
[**insight_income_revenue**](InsightApi.md#insight_income_revenue) | **GET** /api/v1/insight/income/revenue | Insight into income, grouped by revenue account.
[**insight_income_tag**](InsightApi.md#insight_income_tag) | **GET** /api/v1/insight/income/tag | Insight into income, grouped by tag.
[**insight_income_total**](InsightApi.md#insight_income_total) | **GET** /api/v1/insight/income/total | Insight into total income.
[**insight_transfer_category**](InsightApi.md#insight_transfer_category) | **GET** /api/v1/insight/transfer/category | Insight into transfers, grouped by category.
[**insight_transfer_no_category**](InsightApi.md#insight_transfer_no_category) | **GET** /api/v1/insight/transfer/no-category | Insight into transfers, without category.
[**insight_transfer_no_tag**](InsightApi.md#insight_transfer_no_tag) | **GET** /api/v1/insight/transfer/no-tag | Insight into expenses, without tag.
[**insight_transfer_tag**](InsightApi.md#insight_transfer_tag) | **GET** /api/v1/insight/transfer/tag | Insight into transfers, grouped by tag.
[**insight_transfer_total**](InsightApi.md#insight_transfer_total) | **GET** /api/v1/insight/transfer/total | Insight into total transfers.
[**insight_transfers**](InsightApi.md#insight_transfers) | **GET** /api/v1/insight/transfer/asset | Insight into transfers, grouped by account.


# **insight_expense_asset**
> InsightGroup insight_expense_asset(start, end)

Insight into expenses, grouped by asset account.

This endpoint gives a summary of the expenses made by the user, grouped by asset account. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, grouped by asset account.
        api_response = api_instance.insight_expense_asset(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, grouped by asset account.
        api_response = api_instance.insight_expense_asset(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of asset accounts and expense details. Each asset account has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_bill**
> InsightGroup insight_expense_bill(start, end)

Insight into expenses, grouped by bill.

This endpoint gives a summary of the expenses made by the user, grouped by (any) bill. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    bills = ["1","2","3"] # [int] | The bills to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, grouped by bill.
        api_response = api_instance.insight_expense_bill(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_bill: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, grouped by bill.
        api_response = api_instance.insight_expense_bill(start, end, bills=bills, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **bills** | **[int]**| The bills to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget and expense details. Each budget has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_budget**
> InsightGroup insight_expense_budget(start, end)

Insight into expenses, grouped by budget.

This endpoint gives a summary of the expenses made by the user, grouped by (any) budget. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    budgets = ["1","2","3"] # [int] | The budgets to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, grouped by budget.
        api_response = api_instance.insight_expense_budget(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_budget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, grouped by budget.
        api_response = api_instance.insight_expense_budget(start, end, budgets=budgets, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **budgets** | **[int]**| The budgets to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budget and expense details. Each budget has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_category**
> InsightGroup insight_expense_category(start, end)

Insight into expenses, grouped by category.

This endpoint gives a summary of the expenses made by the user, grouped by (any) category. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    categories = ["1","2","3"] # [int] | The categories to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, grouped by category.
        api_response = api_instance.insight_expense_category(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, grouped by category.
        api_response = api_instance.insight_expense_category(start, end, categories=categories, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **categories** | **[int]**| The categories to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of category and expense details. Each category has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_expense**
> InsightGroup insight_expense_expense(start, end)

Insight into expenses, grouped by expense account.

This endpoint gives a summary of the expenses made by the user, grouped by expense account. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you add the accounts ID's of expense accounts, only those accounts are included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. You can combine both asset / liability and expense account ID's. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, grouped by expense account.
        api_response = api_instance.insight_expense_expense(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_expense: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, grouped by expense account.
        api_response = api_instance.insight_expense_expense(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_expense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you add the accounts ID&#39;s of expense accounts, only those accounts are included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. You can combine both asset / liability and expense account ID&#39;s. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of expense accounts and expense details. Each expense acccount has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_no_bill**
> InsightTotal insight_expense_no_bill(start, end)

Insight into expenses, without bill.

This endpoint gives a summary of the expenses made by the user, including only expenses with no bill. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, without bill.
        api_response = api_instance.insight_expense_no_bill(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_bill: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, without bill.
        api_response = api_instance.insight_expense_no_bill(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of expense details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_no_budget**
> InsightTotal insight_expense_no_budget(start, end)

Insight into expenses, without budget.

This endpoint gives a summary of the expenses made by the user, including only expenses with no budget. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, without budget.
        api_response = api_instance.insight_expense_no_budget(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_budget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, without budget.
        api_response = api_instance.insight_expense_no_budget(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_budget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of expense details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_no_category**
> InsightTotal insight_expense_no_category(start, end)

Insight into expenses, without category.

This endpoint gives a summary of the expenses made by the user, including only expenses with no category. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, without category.
        api_response = api_instance.insight_expense_no_category(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, without category.
        api_response = api_instance.insight_expense_no_category(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of expense details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_no_tag**
> InsightTotal insight_expense_no_tag(start, end)

Insight into expenses, without tag.

This endpoint gives a summary of the expenses made by the user, including only expenses with no tag. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, without tag.
        api_response = api_instance.insight_expense_no_tag(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, without tag.
        api_response = api_instance.insight_expense_no_tag(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_no_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of expense details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_tag**
> InsightGroup insight_expense_tag(start, end)

Insight into expenses, grouped by tag.

This endpoint gives a summary of the expenses made by the user, grouped by (any) tag. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    tags = ["1","2","3"] # [int] | The tags to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, grouped by tag.
        api_response = api_instance.insight_expense_tag(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, grouped by tag.
        api_response = api_instance.insight_expense_tag(start, end, tags=tags, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **tags** | **[int]**| The tags to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tag and expense details. Each tag has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_expense_total**
> InsightTotal insight_expense_total(start, end)

Insight into total expenses.

This endpoint gives a sum of the total expenses made by the user. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into total expenses.
        api_response = api_instance.insight_expense_total(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_total: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into total expenses.
        api_response = api_instance.insight_expense_total(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_expense_total: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only withdrawals from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sums in different currencies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_asset**
> InsightGroup insight_income_asset(start, end)

Insight into income, grouped by asset account.

This endpoint gives a summary of the income received by the user, grouped by asset account. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into income, grouped by asset account.
        api_response = api_instance.insight_income_asset(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into income, grouped by asset account.
        api_response = api_instance.insight_income_asset(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of asset accounts and income details. Each asset account has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_category**
> InsightGroup insight_income_category(start, end)

Insight into income, grouped by category.

This endpoint gives a summary of the income received by the user, grouped by (any) category. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    categories = ["1","2","3"] # [int] | The categories to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into income, grouped by category.
        api_response = api_instance.insight_income_category(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into income, grouped by category.
        api_response = api_instance.insight_income_category(start, end, categories=categories, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **categories** | **[int]**| The categories to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of category and income details. Each category has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_no_category**
> InsightTotal insight_income_no_category(start, end)

Insight into income, without category.

This endpoint gives a summary of the income received by the user, including only income with no category. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into income, without category.
        api_response = api_instance.insight_income_no_category(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_no_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into income, without category.
        api_response = api_instance.insight_income_no_category(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_no_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of income details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_no_tag**
> InsightTotal insight_income_no_tag(start, end)

Insight into income, without tag.

This endpoint gives a summary of the income received by the user, including only income with no tag. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into income, without tag.
        api_response = api_instance.insight_income_no_tag(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_no_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into income, without tag.
        api_response = api_instance.insight_income_no_tag(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_no_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of income details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_revenue**
> InsightGroup insight_income_revenue(start, end)

Insight into income, grouped by revenue account.

This endpoint gives a summary of the income received by the user, grouped by revenue account. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you add the accounts ID's of revenue accounts, only those accounts are included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. You can combine both asset / liability and deposit account ID's. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into income, grouped by revenue account.
        api_response = api_instance.insight_income_revenue(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_revenue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into income, grouped by revenue account.
        api_response = api_instance.insight_income_revenue(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_revenue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you add the accounts ID&#39;s of revenue accounts, only those accounts are included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. You can combine both asset / liability and deposit account ID&#39;s. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of revenue accounts and income details. Each revenue acccount has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_tag**
> InsightGroup insight_income_tag(start, end)

Insight into income, grouped by tag.

This endpoint gives a summary of the income received by the user, grouped by (any) tag. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    tags = ["1","2","3"] # [int] | The tags to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into income, grouped by tag.
        api_response = api_instance.insight_income_tag(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into income, grouped by tag.
        api_response = api_instance.insight_income_tag(start, end, tags=tags, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **tags** | **[int]**| The tags to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tag and income details. Each tag has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_income_total**
> InsightTotal insight_income_total(start, end)

Insight into total income.

This endpoint gives a sum of the total income received by the user. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into total income.
        api_response = api_instance.insight_income_total(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_total: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into total income.
        api_response = api_instance.insight_income_total(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_income_total: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only deposits to those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sums in different currencies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_transfer_category**
> InsightGroup insight_transfer_category(start, end)

Insight into transfers, grouped by category.

This endpoint gives a summary of the transfers made by the user, grouped by (any) category. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    categories = ["1","2","3"] # [int] | The categories to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into transfers, grouped by category.
        api_response = api_instance.insight_transfer_category(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into transfers, grouped by category.
        api_response = api_instance.insight_transfer_category(start, end, categories=categories, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **categories** | **[int]**| The categories to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of category and transfer details. Each category has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_transfer_no_category**
> InsightTotal insight_transfer_no_category(start, end)

Insight into transfers, without category.

This endpoint gives a summary of the transfers made by the user, including only transfers with no category. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into transfers, without category.
        api_response = api_instance.insight_transfer_no_category(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_no_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into transfers, without category.
        api_response = api_instance.insight_transfer_no_category(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_no_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transfer details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_transfer_no_tag**
> InsightTotal insight_transfer_no_tag(start, end)

Insight into expenses, without tag.

This endpoint gives a summary of the transfers made by the user, including only transfers with no tag. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only transfers from those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into expenses, without tag.
        api_response = api_instance.insight_transfer_no_tag(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_no_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into expenses, without tag.
        api_response = api_instance.insight_transfer_no_tag(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_no_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only transfers from those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transfer details. One row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_transfer_tag**
> InsightGroup insight_transfer_tag(start, end)

Insight into transfers, grouped by tag.

This endpoint gives a summary of the transfers created by the user, grouped by (any) tag. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_group import InsightGroup
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    tags = ["1","2","3"] # [int] | The tags to be included in the results.  (optional)
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into transfers, grouped by tag.
        api_response = api_instance.insight_transfer_tag(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into transfers, grouped by tag.
        api_response = api_instance.insight_transfer_tag(start, end, tags=tags, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **tags** | **[int]**| The tags to be included in the results.  | [optional]
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tag and transfer details. Each tag has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_transfer_total**
> InsightTotal insight_transfer_total(start, end)

Insight into total transfers.

This endpoint gives a sum of the total amount transfers made by the user. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_total import InsightTotal
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into total transfers.
        api_response = api_instance.insight_transfer_total(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_total: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into total transfers.
        api_response = api_instance.insight_transfer_total(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfer_total: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTotal**](InsightTotal.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sums in different currencies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_transfers**
> InsightTransfer insight_transfers(start, end)

Insight into transfers, grouped by account.

This endpoint gives a summary of the transfers made by the user, grouped by asset account or lability. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import insight_api
from firefly_iii_client.model.insight_transfer import InsightTransfer
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
    api_instance = insight_api.InsightApi(api_client)
    start = dateutil_parser('2021-01-01').date() # date | A date formatted YYYY-MM-DD. 
    end = dateutil_parser('2021-01-31').date() # date | A date formatted YYYY-MM-DD. 
    accounts = ["1","2","3"] # [int] | The accounts to be included in the results. If you include ID's of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID's will be ignored.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insight into transfers, grouped by account.
        api_response = api_instance.insight_transfers(start, end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insight into transfers, grouped by account.
        api_response = api_instance.insight_transfers(start, end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling InsightApi->insight_transfers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| A date formatted YYYY-MM-DD.  |
 **end** | **date**| A date formatted YYYY-MM-DD.  |
 **accounts** | **[int]**| The accounts to be included in the results. If you include ID&#39;s of asset accounts or liabilities, only transfers between those asset accounts / liabilities will be included. Other account ID&#39;s will be ignored.  | [optional]

### Return type

[**InsightTransfer**](InsightTransfer.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of asset accounts and transfer details. Each asset account has one row per currency. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

