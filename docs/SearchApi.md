# firefly_iii_client.SearchApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_accounts**](SearchApi.md#search_accounts) | **GET** /api/v1/search/accounts | Search for accounts
[**search_transactions**](SearchApi.md#search_transactions) | **GET** /api/v1/search/transactions | Search for transactions


# **search_accounts**
> AccountArray search_accounts(query, field)

Search for accounts

Search for accounts

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import search_api
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.account_array import AccountArray
from firefly_iii_client.model.account_search_field_filter import AccountSearchFieldFilter
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
    api_instance = search_api.SearchApi(api_client)
    query = "checking" # str | The query you wish to search for.
    field = AccountSearchFieldFilter("all") # AccountSearchFieldFilter | The account field(s) you want to search in.
    page = 1 # int | Page number. The default pagination is 50 (optional)
    type = AccountTypeFilter("all") # AccountTypeFilter | The type of accounts you wish to limit the search to. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for accounts
        api_response = api_instance.search_accounts(query, field)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SearchApi->search_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for accounts
        api_response = api_instance.search_accounts(query, field, page=page, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SearchApi->search_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The query you wish to search for. |
 **field** | **AccountSearchFieldFilter**| The account field(s) you want to search in. |
 **page** | **int**| Page number. The default pagination is 50 | [optional]
 **type** | **AccountTypeFilter**| The type of accounts you wish to limit the search to. | [optional]

### Return type

[**AccountArray**](AccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transactions**
> TransactionArray search_transactions(query)

Search for transactions

Searches through the users transactions.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import search_api
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
    api_instance = search_api.SearchApi(api_client)
    query = "groceries" # str | The query you wish to search for.
    page = 1 # int | Page number. The default pagination is 50 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for transactions
        api_response = api_instance.search_transactions(query)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SearchApi->search_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for transactions
        api_response = api_instance.search_transactions(query, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SearchApi->search_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The query you wish to search for. |
 **page** | **int**| Page number. The default pagination is 50 | [optional]

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

