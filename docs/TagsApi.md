# firefly_iii_client.TagsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /api/v1/tags/{tag} | Delete an tag.
[**get_tag**](TagsApi.md#get_tag) | **GET** /api/v1/tags/{tag} | Get a single tag.
[**get_tags**](TagsApi.md#get_tags) | **GET** /api/v1/tags | List all tags.
[**get_transactions_by_tag**](TagsApi.md#get_transactions_by_tag) | **GET** /api/v1/tags/{tag}/transactions | List all transactions with this tag.
[**store_tag**](TagsApi.md#store_tag) | **POST** /api/v1/tags | Store a new tag
[**update_tag**](TagsApi.md#update_tag) | **PUT** /api/v1/tags/{tag} | Update existing tag.


# **delete_tag**
> delete_tag(tag)

Delete an tag.

Delete an tag.

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
api_instance = firefly_iii_client.TagsApi(firefly_iii_client.ApiClient(configuration))
tag = groceries # str | Either the tag itself or the tag ID.

try:
    # Delete an tag.
    api_instance.delete_tag(tag)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagSingle get_tag(tag, page=page)

Get a single tag.

Get a single tag.

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
api_instance = firefly_iii_client.TagsApi(firefly_iii_client.ApiClient(configuration))
tag = groceries # str | Either the tag itself or the tag ID.
page = 56 # int | Page number (optional)

try:
    # Get a single tag.
    api_response = api_instance.get_tag(tag, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. | 
 **page** | **int**| Page number | [optional] 

### Return type

[**TagSingle**](TagSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> TagArray get_tags(page=page)

List all tags.

List all of the user's tags.

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
api_instance = firefly_iii_client.TagsApi(firefly_iii_client.ApiClient(configuration))
page = 56 # int | Page number (optional)

try:
    # List all tags.
    api_response = api_instance.get_tags(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 

### Return type

[**TagArray**](TagArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_tag**
> TransactionArray get_transactions_by_tag(tag, page=page, start=start, end=end, type=type)

List all transactions with this tag.

List all transactions with this tag.

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
api_instance = firefly_iii_client.TagsApi(firefly_iii_client.ApiClient(configuration))
tag = groceries # str | Either the tag itself or the tag ID.
page = 1 # int | Page number. The default pagination is 50. (optional)
start = 2018-09-17 # str | A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  (optional)
end = 2018-09-17 # str | A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned. (optional)

try:
    # List all transactions with this tag.
    api_response = api_instance.get_transactions_by_tag(tag, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_transactions_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_tag**
> TagSingle store_tag(tag_update)

Store a new tag

Creates a new tag. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.TagsApi(firefly_iii_client.ApiClient(configuration))
tag_update = firefly_iii_client.TagUpdate() # TagUpdate | JSON array or key=value pairs with the necessary tag information. See the model for the exact specifications.

try:
    # Store a new tag
    api_response = api_instance.store_tag(tag_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->store_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_update** | [**TagUpdate**](TagUpdate.md)| JSON array or key&#x3D;value pairs with the necessary tag information. See the model for the exact specifications. | 

### Return type

[**TagSingle**](TagSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> TagSingle update_tag(tag, tag_update)

Update existing tag.

Update existing tag.

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
api_instance = firefly_iii_client.TagsApi(firefly_iii_client.ApiClient(configuration))
tag = groceries # str | Either the tag itself or the tag ID.
tag_update = firefly_iii_client.TagUpdate() # TagUpdate | JSON array with updated tag information. See the model for the exact specifications.

try:
    # Update existing tag.
    api_response = api_instance.update_tag(tag, tag_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. | 
 **tag_update** | [**TagUpdate**](TagUpdate.md)| JSON array with updated tag information. See the model for the exact specifications. | 

### Return type

[**TagSingle**](TagSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

