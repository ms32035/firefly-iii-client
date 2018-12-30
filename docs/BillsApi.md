# firefly_iii_client.BillsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bill**](BillsApi.md#delete_bill) | **DELETE** /api/v1/bills/{id} | Delete a bill.
[**get_attachments_by_bill**](BillsApi.md#get_attachments_by_bill) | **GET** /api/v1/bills/{id}/attachments | List all attachments uploaded to the bill.
[**get_bill**](BillsApi.md#get_bill) | **GET** /api/v1/bills/{id} | Get a single bill.
[**get_bills**](BillsApi.md#get_bills) | **GET** /api/v1/bills | List all bills.
[**get_rules_by_bill**](BillsApi.md#get_rules_by_bill) | **GET** /api/v1/bills/{id}/rules | List all rules associated with the bill.
[**get_transactions_by_bill**](BillsApi.md#get_transactions_by_bill) | **GET** /api/v1/bills/{id}/transactions | List all transactions associated with the  bill.
[**store_bill**](BillsApi.md#store_bill) | **POST** /api/v1/bills | Store a new bill
[**update_bill**](BillsApi.md#update_bill) | **PUT** /api/v1/bills/{id} | Update existing bill.


# **delete_bill**
> delete_bill(id)

Delete a bill.

Delete a bill. This will not delete any associated rules. Will not remove associated transactions. WILL remove all associated attachments.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the bill.

try:
    # Delete a bill.
    api_instance.delete_bill(id)
except ApiException as e:
    print("Exception when calling BillsApi->delete_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the bill. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_by_bill**
> AttachmentArray get_attachments_by_bill(id, page=page)

List all attachments uploaded to the bill.

This endpoint will list all attachments linked to the bill.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the bill.
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all attachments uploaded to the bill.
    api_response = api_instance.get_attachments_by_bill(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_attachments_by_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the bill. | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill**
> BillSingle get_bill(id)

Get a single bill.

Get a single bill.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the bill.

try:
    # Get a single bill.
    api_response = api_instance.get_bill(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the bill. | 

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bills**
> BillArray get_bills(page=page)

List all bills.

This endpoint will list all the user's bills.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all bills.
    api_response = api_instance.get_bills(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_bills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

### Return type

[**BillArray**](BillArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_by_bill**
> RuleArray get_rules_by_bill(id)

List all rules associated with the bill.

This endpoint will list all rules that have an action to set the bill to this bill.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the bill.

try:
    # List all rules associated with the bill.
    api_response = api_instance.get_rules_by_bill(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_rules_by_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the bill. | 

### Return type

[**RuleArray**](RuleArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_bill**
> TransactionArray get_transactions_by_bill(id, start=start, end=end, type=type)

List all transactions associated with the  bill.

This endpoint will list all transactions linked to this bill.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the bill.
start = 2018-09-17 # str | A date formatted YYYY-MM-DD.  (optional)
end = 2018-12-31 # str | A date formatted YYYY-MM-DD.  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned (optional)

try:
    # List all transactions associated with the  bill.
    api_response = api_instance.get_transactions_by_bill(id, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->get_transactions_by_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the bill. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_bill**
> BillSingle store_bill(bill_update)

Store a new bill

Creates a new bill. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
bill_update = firefly_iii_client.BillUpdate() # BillUpdate | JSON array or key=value pairs with the necessary bill information. See the model for the exact specifications.

try:
    # Store a new bill
    api_response = api_instance.store_bill(bill_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->store_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_update** | [**BillUpdate**](BillUpdate.md)| JSON array or key&#x3D;value pairs with the necessary bill information. See the model for the exact specifications. | 

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill**
> BillSingle update_bill(id, bill_update)

Update existing bill.

Update existing bill.

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
api_instance = firefly_iii_client.BillsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the bill.
bill_update = firefly_iii_client.BillUpdate() # BillUpdate | JSON array or key=value pairs with updated bill information. See the model for the exact specifications.

try:
    # Update existing bill.
    api_response = api_instance.update_bill(id, bill_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->update_bill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the bill. | 
 **bill_update** | [**BillUpdate**](BillUpdate.md)| JSON array or key&#x3D;value pairs with updated bill information. See the model for the exact specifications. | 

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

