# firefly_iii_client.LinksApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_link_type**](LinksApi.md#delete_link_type) | **DELETE** /api/v1/link_types/{id} | Permanently delete link type.
[**delete_transaction_link**](LinksApi.md#delete_transaction_link) | **DELETE** /api/v1/transaction_links/{id} | Permanently delete link between transactions.
[**get_link_type**](LinksApi.md#get_link_type) | **GET** /api/v1/link_types/{id} | Get single a link type.
[**get_link_types**](LinksApi.md#get_link_types) | **GET** /api/v1/link_types | List all types of links.
[**get_transaction_links**](LinksApi.md#get_transaction_links) | **GET** /api/v1/transaction_links | List all transaction links.
[**get_transactions_by_link_type**](LinksApi.md#get_transactions_by_link_type) | **GET** /api/v1/link_types/{id}/transactions | List all transactions under this link type.
[**store_link_type**](LinksApi.md#store_link_type) | **POST** /api/v1/link_types | Create a new link type
[**store_transaction_link**](LinksApi.md#store_transaction_link) | **POST** /api/v1/transaction_links | Create a new link between transactions
[**update_link_type**](LinksApi.md#update_link_type) | **PUT** /api/v1/link_types/{id} | Update existing link type.
[**update_transaction_link**](LinksApi.md#update_transaction_link) | **PUT** /api/v1/transaction_links/{id} | Update an existing link between transactions.


# **delete_link_type**
> delete_link_type(id)

Permanently delete link type.

Will permanently delete a link type. The links between transactions will be removed. The transactions themselves remain. You cannot delete some of the system provided link types, indicated by the editable=false flag when you list it. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the link type.

try:
    # Permanently delete link type.
    api_instance.delete_link_type(id)
except ApiException as e:
    print("Exception when calling LinksApi->delete_link_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the link type. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_link**
> delete_transaction_link(id)

Permanently delete link between transactions.

Will permanently delete link. Transactions remain. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction link.

try:
    # Permanently delete link between transactions.
    api_instance.delete_transaction_link(id)
except ApiException as e:
    print("Exception when calling LinksApi->delete_transaction_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction link. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_type**
> LinkTypeSingle get_link_type(id)

Get single a link type.

Returns a single link type by its ID. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the link type.

try:
    # Get single a link type.
    api_response = api_instance.get_link_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_link_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the link type. | 

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_types**
> LinkTypeArray get_link_types(page=page)

List all types of links.

List all the link types the system has. These include the default ones as well as any new ones. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50 items. (optional)

try:
    # List all types of links.
    api_response = api_instance.get_link_types(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_link_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50 items. | [optional] 

### Return type

[**LinkTypeArray**](LinkTypeArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_links**
> TransactionLinkArray get_transaction_links(page=page)

List all transaction links.

List all the transaction links. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is per 50 items. (optional)

try:
    # List all transaction links.
    api_response = api_instance.get_transaction_links(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_transaction_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**TransactionLinkArray**](TransactionLinkArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_link_type**
> TransactionArray get_transactions_by_link_type(id, page=page, start=start, end=end, type=type)

List all transactions under this link type.

List all transactions under this link type, both the inward and outward transactions. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the link type.
page = 1 # int | Page number. The default pagination is per 50 items. (optional)
start = 2018-09-17 # str | A date formatted YYYY-MM-DD, to limit the results.  (optional)
end = 2018-09-17 # str | A date formatted YYYY-MM-DD, to limit the results.  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned. (optional)

try:
    # List all transactions under this link type.
    api_response = api_instance.get_transactions_by_link_type(id, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_transactions_by_link_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the link type. | 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD, to limit the results.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD, to limit the results.  | [optional] 
 **type** | **str**| Optional filter on the transaction type(s) returned. | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_link_type**
> LinkTypeSingle store_link_type(link_type_update)

Create a new link type

Creates a new link type. The data required can be submitted as a JSON body or as a list of parameters (in key=value pairs, like a webform).

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
link_type_update = firefly_iii_client.LinkTypeUpdate() # LinkTypeUpdate | JSON array with the necessary link type information or key=value pairs. See the model for the exact specifications.

try:
    # Create a new link type
    api_response = api_instance.store_link_type(link_type_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->store_link_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_type_update** | [**LinkTypeUpdate**](LinkTypeUpdate.md)| JSON array with the necessary link type information or key&#x3D;value pairs. See the model for the exact specifications. | 

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_transaction_link**
> TransactionLinkSingle store_transaction_link(transaction_link_update)

Create a new link between transactions

Store a new link between two transactions. For this end point you need the journal_id from a transaction.

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
transaction_link_update = firefly_iii_client.TransactionLinkUpdate() # TransactionLinkUpdate | JSON array with the necessary link type information or key=value pairs. See the model for the exact specifications.

try:
    # Create a new link between transactions
    api_response = api_instance.store_transaction_link(transaction_link_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->store_transaction_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_link_update** | [**TransactionLinkUpdate**](TransactionLinkUpdate.md)| JSON array with the necessary link type information or key&#x3D;value pairs. See the model for the exact specifications. | 

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link_type**
> LinkTypeSingle update_link_type(id, link_type_update)

Update existing link type.

Used to update a single link type. All fields that are not submitted will be cleared (set to NULL). The model will tell you which fields are mandatory. You cannot update some of the system provided link types, indicated by the editable=false flag when you list it. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the link type.
link_type_update = firefly_iii_client.LinkTypeUpdate() # LinkTypeUpdate | JSON array or formdata with updated link type information. See the model for the exact specifications.

try:
    # Update existing link type.
    api_response = api_instance.update_link_type(id, link_type_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->update_link_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the link type. | 
 **link_type_update** | [**LinkTypeUpdate**](LinkTypeUpdate.md)| JSON array or formdata with updated link type information. See the model for the exact specifications. | 

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_link**
> TransactionLinkSingle update_transaction_link(id, transaction_link_update)

Update an existing link between transactions.

Used to update a single existing link. 

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
api_instance = firefly_iii_client.LinksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the transaction link.
transaction_link_update = firefly_iii_client.TransactionLinkUpdate() # TransactionLinkUpdate | JSON array or formdata with updated link type information. See the model for the exact specifications.

try:
    # Update an existing link between transactions.
    api_response = api_instance.update_transaction_link(id, transaction_link_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->update_transaction_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction link. | 
 **transaction_link_update** | [**TransactionLinkUpdate**](TransactionLinkUpdate.md)| JSON array or formdata with updated link type information. See the model for the exact specifications. | 

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

