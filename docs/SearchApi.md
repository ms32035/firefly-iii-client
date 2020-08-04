# firefly_iii_client.SearchApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_accounts**](SearchApi.md#search_accounts) | **GET** /api/v1/search/accounts | Search for accounts
[**search_transactions**](SearchApi.md#search_transactions) | **GET** /api/v1/search/transactions | Search for transactions


# **search_accounts**
> AccountArray search_accounts(query, type, field, page=page)

Search for accounts

Search for accounts

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
api_instance = firefly_iii_client.SearchApi(firefly_iii_client.ApiClient(configuration))
query = 'checking' # str | The query you wish to search for.
type = firefly_iii_client.AccountTypeFilter() # AccountTypeFilter | The type of accounts you wish to limit the search to.
field = firefly_iii_client.AccountSearchFieldFilter() # AccountSearchFieldFilter | The account field(s) you want to search in.
page = 1 # int | Page number. The default pagination is 50 (optional)

try:
    # Search for accounts
    api_response = api_instance.search_accounts(query, type, field, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The query you wish to search for. | 
 **type** | [**AccountTypeFilter**](.md)| The type of accounts you wish to limit the search to. | 
 **field** | [**AccountSearchFieldFilter**](.md)| The account field(s) you want to search in. | 
 **page** | **int**| Page number. The default pagination is 50 | [optional] 

### Return type

[**AccountArray**](AccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transactions**
> TransactionArray search_transactions(query, page=page)

Search for transactions

Search for transactions

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
api_instance = firefly_iii_client.SearchApi(firefly_iii_client.ApiClient(configuration))
query = 'groceries' # str | The query you wish to search for.
page = 1 # int | Page number. The default pagination is 50 (optional)

try:
    # Search for transactions
    api_response = api_instance.search_transactions(query, page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

