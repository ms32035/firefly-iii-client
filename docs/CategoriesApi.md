# firefly_iii_client.CategoriesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /api/v1/categories/{id} | Delete a category.
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /api/v1/categories | List all categories.
[**get_category**](CategoriesApi.md#get_category) | **GET** /api/v1/categories/{id} | Get a single category.
[**get_transactions_by_category**](CategoriesApi.md#get_transactions_by_category) | **GET** /api/v1/categories/{id}/transactions | List all transactions in a category.
[**store_category**](CategoriesApi.md#store_category) | **POST** /api/v1/categories | Store a new category
[**update_category**](CategoriesApi.md#update_category) | **PUT** /api/v1/categories/{id} | Update existing category.


# **delete_category**
> delete_category(id)

Delete a category.

Delete a category. Transactions will not be removed.

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
api_instance = firefly_iii_client.CategoriesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the category.

try:
    # Delete a category.
    api_instance.delete_category(id)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the category. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> CategoryArray get_categories(page=page)

List all categories.

List all categories.

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
api_instance = firefly_iii_client.CategoriesApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all categories.
    api_response = api_instance.get_categories(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

### Return type

[**CategoryArray**](CategoryArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> CategorySingle get_category(id)

Get a single category.

Get a single category.

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
api_instance = firefly_iii_client.CategoriesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the category.

try:
    # Get a single category.
    api_response = api_instance.get_category(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the category. | 

### Return type

[**CategorySingle**](CategorySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_category**
> TransactionArray get_transactions_by_category(id, page=page, start=start, end=end, type=type)

List all transactions in a category.

List all transactions in a category, optionally limited to the date ranges specified.

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
api_instance = firefly_iii_client.CategoriesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the category.
page = 1 # int | Page number. The default pagination is per 50. (optional)
start = 2018-09-17 # str | A date formatted YYYY-MM-DD, to limit the result list.  (optional)
end = 2018-12-31 # str | A date formatted YYYY-MM-DD, to limit the result list.  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned (optional)

try:
    # List all transactions in a category.
    api_response = api_instance.get_transactions_by_category(id, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_transactions_by_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the category. | 
 **page** | **int**| Page number. The default pagination is per 50. | [optional] 
 **start** | **str**| A date formatted YYYY-MM-DD, to limit the result list.  | [optional] 
 **end** | **str**| A date formatted YYYY-MM-DD, to limit the result list.  | [optional] 
 **type** | **str**| Optional filter on the transaction type(s) returned | [optional] 

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_category**
> CategorySingle store_category(category_update)

Store a new category

Creates a new category. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.CategoriesApi(firefly_iii_client.ApiClient(configuration))
category_update = firefly_iii_client.CategoryUpdate() # CategoryUpdate | JSON array or key=value pairs with the necessary category information. See the model for the exact specifications.

try:
    # Store a new category
    api_response = api_instance.store_category(category_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->store_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_update** | [**CategoryUpdate**](CategoryUpdate.md)| JSON array or key&#x3D;value pairs with the necessary category information. See the model for the exact specifications. | 

### Return type

[**CategorySingle**](CategorySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> CategorySingle update_category(id, category_update)

Update existing category.

Update existing category.

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
api_instance = firefly_iii_client.CategoriesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the category.
category_update = firefly_iii_client.CategoryUpdate() # CategoryUpdate | JSON array with updated category information. See the model for the exact specifications.

try:
    # Update existing category.
    api_response = api_instance.update_category(id, category_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the category. | 
 **category_update** | [**CategoryUpdate**](CategoryUpdate.md)| JSON array with updated category information. See the model for the exact specifications. | 

### Return type

[**CategorySingle**](CategorySingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

