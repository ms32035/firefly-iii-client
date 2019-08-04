# firefly_iii_client.TransactionsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /api/v1/transactions/{id} | Delete a transaction.
[**get_attachments_by_transactions**](TransactionsApi.md#get_attachments_by_transactions) | **GET** /api/v1/transactions/{id}/attachments | Lists all attachments.
[**get_events_by_transactions**](TransactionsApi.md#get_events_by_transactions) | **GET** /api/v1/transactions/{id}/piggy_bank_events | Lists all piggy bank events.
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /api/v1/transactions/{id} | Get a single transaction.
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /api/v1/transactions | List all the user&#39;s transactions. 
[**store_transaction**](TransactionsApi.md#store_transaction) | **POST** /api/v1/transactions | Store a new transaction
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /api/v1/transactions/{id} | Update existing transaction.


# **delete_transaction**
> delete_transaction(id)

Delete a transaction.

Delete a transaction.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction.

try:
    # Delete a transaction.
    api_instance.delete_transaction(id)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. | 

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
**204** | Transaction deleted. |  -  |
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_by_transactions**
> AttachmentArray get_attachments_by_transactions(id, page=page)

Lists all attachments.

Lists all attachments.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction.
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # Lists all attachments.
    api_response = api_instance.get_attachments_by_transactions(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_attachments_by_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of attachments |  -  |
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_transactions**
> PiggyBankEventArray get_events_by_transactions(id, page=page)

Lists all piggy bank events.

Lists all piggy bank events.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction.
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # Lists all piggy bank events.
    api_response = api_instance.get_events_by_transactions(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_events_by_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

### Return type

[**PiggyBankEventArray**](PiggyBankEventArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy bank events. |  -  |
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionSingle get_transaction(id)

Get a single transaction.

Get a single transaction.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction. Note that this ID is different from the ID you see in the URL of your Firefly III instance.

try:
    # Get a single transaction.
    api_response = api_instance.get_transaction(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. Note that this ID is different from the ID you see in the URL of your Firefly III instance. | 

### Return type

[**TransactionSingle**](TransactionSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transaction. |  -  |
**404** | Transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> TransactionArray get_transactions(page=page, start=start, end=end, type=type)

List all the user's transactions. 

List all the user's transactions.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)
start = '2018-09-17' # str | A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  (optional)
end = '2018-09-17' # str | A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned. (optional)

try:
    # List all the user's transactions. 
    api_response = api_instance.get_transactions(page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  | [optional] 
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
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_transaction**
> TransactionArray store_transaction(transaction_update)

Store a new transaction

Creates a new transaction. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
transaction_update = firefly_iii_client.TransactionUpdate() # TransactionUpdate | JSON array or key=value pairs with the necessary transaction information. See the model for the exact specifications.

try:
    # Store a new transaction
    api_response = api_instance.store_transaction(transaction_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->store_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_update** | [**TransactionUpdate**](TransactionUpdate.md)| JSON array or key&#x3D;value pairs with the necessary transaction information. See the model for the exact specifications. | 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New transaction stored(s), result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionSingle update_transaction(id, transaction_update)

Update existing transaction.

Update an existing transaction.

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
api_instance = firefly_iii_client.TransactionsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction.
transaction_update = firefly_iii_client.TransactionUpdate() # TransactionUpdate | JSON array with updated transaction information. See the model for the exact specifications.

try:
    # Update existing transaction.
    api_response = api_instance.update_transaction(id, transaction_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. | 
 **transaction_update** | [**TransactionUpdate**](TransactionUpdate.md)| JSON array with updated transaction information. See the model for the exact specifications. | 

### Return type

[**TransactionSingle**](TransactionSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated transaction stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

