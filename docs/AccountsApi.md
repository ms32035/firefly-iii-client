# firefly_iii_client.AccountsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /api/v1/accounts/{id} | Permanently delete account.
[**get_account**](AccountsApi.md#get_account) | **GET** /api/v1/accounts/{id} | Get single account.
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /api/v1/accounts | List all accounts.
[**get_piggies_by_account**](AccountsApi.md#get_piggies_by_account) | **GET** /api/v1/accounts/{id}/piggy_banks | List all piggy banks related to the account.
[**get_transactions_by_account**](AccountsApi.md#get_transactions_by_account) | **GET** /api/v1/accounts/{id}/transactions | List all transactions related to the account.
[**store_account**](AccountsApi.md#store_account) | **POST** /api/v1/accounts | Create new account.
[**update_account**](AccountsApi.md#update_account) | **PUT** /api/v1/accounts/{id} | Update existing account.


# **delete_account**
> delete_account(id)

Permanently delete account.

Will permanently delete an account. Any associated transactions and piggy banks are ALSO deleted. Cannot be recovered from. 

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the account.

try:
    # Permanently delete account.
    api_instance.delete_account(id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. | 

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
**204** | Account deleted |  -  |
**404** | No such account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountSingle get_account(id, date=date)

Get single account.

Returns a single account by its ID. 

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the account.
date = 'date_example' # str | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)

try:
    # Get single account.
    api_response = api_instance.get_account(id, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. | 
 **date** | **str**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional] 

### Return type

[**AccountSingle**](AccountSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested account |  -  |
**404** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountArray get_accounts(page=page, date=date, type=type)

List all accounts.

This endpoint returns a list of all the accounts owned by the authenticated user. 

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is per 50 items. (optional)
date = '2013-10-20' # date | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)
type = 'type_example' # str | Optional filter on the account type(s) returned (optional)

try:
    # List all accounts.
    api_response = api_instance.get_accounts(page=page, date=date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **date** | **date**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional] 
 **type** | **str**| Optional filter on the account type(s) returned | [optional] 

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
**200** | A list of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_piggies_by_account**
> PiggyBankArray get_piggies_by_account(id, page=page)

List all piggy banks related to the account.

This endpoint returns a list of all the piggy banks connected to the account. 

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the account.
page = 56 # int | Page number. The default pagination is per 50 items. (optional)

try:
    # List all piggy banks related to the account.
    api_response = api_instance.get_piggies_by_account(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_piggies_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. | 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**PiggyBankArray**](PiggyBankArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_account**
> TransactionArray get_transactions_by_account(id, page=page, limit=limit, start=start, end=end, type=type)

List all transactions related to the account.

This endpoint returns a list of all the transactions connected to the account. 

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the account.
page = 1 # int | Page number. The default pagination is per 50 items. (optional)
limit = 5 # int | Limits the number of results on one page. (optional)
start = '2018-09-17' # str | A date formatted YYYY-MM-DD.  (optional)
end = '2018-09-17' # str | A date formatted YYYY-MM-DD.  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned. (optional)

try:
    # List all transactions related to the account.
    api_response = api_instance.get_transactions_by_account(id, page=page, limit=limit, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_transactions_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. | 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **limit** | **int**| Limits the number of results on one page. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD.  | [optional] 
 **type** | **str**| Optional filter on the transaction type(s) returned. | [optional] 

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
**200** | A list of transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_account**
> AccountSingle store_account(account_update)

Create new account.

Creates a new account. The data required can be submitted as a JSON body or as a list of parameters (in key=value pairs, like a webform).

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
account_update = firefly_iii_client.AccountUpdate() # AccountUpdate | JSON array with the necessary account information or key=value pairs. See the model for the exact specifications.

try:
    # Create new account.
    api_response = api_instance.store_account(account_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->store_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_update** | [**AccountUpdate**](AccountUpdate.md)| JSON array with the necessary account information or key&#x3D;value pairs. See the model for the exact specifications. | 

### Return type

[**AccountSingle**](AccountSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New account stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> AccountSingle update_account(id, account_update)

Update existing account.

Used to update a single account. All fields that are not submitted will be cleared (set to NULL). The model will tell you which fields are mandatory. 

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
api_instance = firefly_iii_client.AccountsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the account.
account_update = firefly_iii_client.AccountUpdate() # AccountUpdate | JSON array or formdata with updated account information. See the model for the exact specifications.

try:
    # Update existing account.
    api_response = api_instance.update_account(id, account_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. | 
 **account_update** | [**AccountUpdate**](AccountUpdate.md)| JSON array or formdata with updated account information. See the model for the exact specifications. | 

### Return type

[**AccountSingle**](AccountSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated account stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

