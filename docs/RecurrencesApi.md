# firefly_iii_client.RecurrencesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recurrence**](RecurrencesApi.md#delete_recurrence) | **DELETE** /api/v1/recurrences/{id} | Delete a recurring transaction.
[**get_recurrence**](RecurrencesApi.md#get_recurrence) | **GET** /api/v1/recurrences/{id} | Get a single recurring transaction.
[**get_recurring**](RecurrencesApi.md#get_recurring) | **GET** /api/v1/recurrences | List all recurring transactions.
[**get_transactions_by_recurrence**](RecurrencesApi.md#get_transactions_by_recurrence) | **GET** /api/v1/recurrences/{id}/transactions | List all transactions created by a recurring transaction.
[**store_recurrence**](RecurrencesApi.md#store_recurrence) | **POST** /api/v1/recurrences | Store a new recurring transaction
[**trigger_recurrence**](RecurrencesApi.md#trigger_recurrence) | **POST** /api/v1/recurrences/trigger | Trigger the creation of recurring transactions (like a cron job).
[**update_recurrence**](RecurrencesApi.md#update_recurrence) | **PUT** /api/v1/recurrences/{id} | Update existing recurring transaction.


# **delete_recurrence**
> delete_recurrence(id)

Delete a recurring transaction.

Delete a recurring transaction. Transactions created will not be deleted.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the recurring transaction.

try:
    # Delete a recurring transaction.
    api_instance.delete_recurrence(id)
except ApiException as e:
    print("Exception when calling RecurrencesApi->delete_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurrence**
> RecurrenceSingle get_recurrence(id)

Get a single recurring transaction.

Get a single recurring transaction.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the recurring transaction.

try:
    # Get a single recurring transaction.
    api_response = api_instance.get_recurrence(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrencesApi->get_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. | 

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring**
> RecurrenceArray get_recurring(page=page)

List all recurring transactions.

List all recurring transactions.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all recurring transactions.
    api_response = api_instance.get_recurring(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrencesApi->get_recurring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

### Return type

[**RecurrenceArray**](RecurrenceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_recurrence**
> TransactionArray get_transactions_by_recurrence(id, page=page, start=start, end=end, type=type)

List all transactions created by a recurring transaction.

List all transactions created by a recurring transaction, optionally limited to the date ranges specified.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the recurring transaction.
page = 1 # int | Page number. The default pagination is 50. (optional)
start = 2018-09-17 # str | A date formatted YYYY-MM-DD. Both the start and end date must be present.  (optional)
end = 2018-09-17 # str | A date formatted YYYY-MM-DD. Both the start and end date must be present.  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned (optional)

try:
    # List all transactions created by a recurring transaction.
    api_response = api_instance.get_transactions_by_recurrence(id, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrencesApi->get_transactions_by_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD. Both the start and end date must be present.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD. Both the start and end date must be present.  | [optional] 
 **type** | **str**| Optional filter on the transaction type(s) returned | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_recurrence**
> RecurrenceSingle store_recurrence(recurrence_update)

Store a new recurring transaction

Creates a new recurring transaction. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))
recurrence_update = firefly_iii_client.RecurrenceUpdate() # RecurrenceUpdate | JSON array or key=value pairs with the necessary recurring transaction information. See the model for the exact specifications.

try:
    # Store a new recurring transaction
    api_response = api_instance.store_recurrence(recurrence_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrencesApi->store_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurrence_update** | [**RecurrenceUpdate**](RecurrenceUpdate.md)| JSON array or key&#x3D;value pairs with the necessary recurring transaction information. See the model for the exact specifications. | 

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_recurrence**
> trigger_recurrence()

Trigger the creation of recurring transactions (like a cron job).

Triggers the recurring transactions, like a cron job would. If the schedule does not call for a new transaction to be created, nothing will happen. 

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))

try:
    # Trigger the creation of recurring transactions (like a cron job).
    api_instance.trigger_recurrence()
except ApiException as e:
    print("Exception when calling RecurrencesApi->trigger_recurrence: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recurrence**
> RecurrenceSingle update_recurrence(id, recurrence_update)

Update existing recurring transaction.

Update existing recurring transaction.

### Example

* OAuth Authentication (firefly_iii_auth): 
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.RecurrencesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the recurring transaction.
recurrence_update = firefly_iii_client.RecurrenceUpdate() # RecurrenceUpdate | JSON array with updated recurring transaction information. See the model for the exact specifications.

try:
    # Update existing recurring transaction.
    api_response = api_instance.update_recurrence(id, recurrence_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrencesApi->update_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. | 
 **recurrence_update** | [**RecurrenceUpdate**](RecurrenceUpdate.md)| JSON array with updated recurring transaction information. See the model for the exact specifications. | 

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

