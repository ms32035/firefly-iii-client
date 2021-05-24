# firefly_iii_client.TagsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /api/v1/tags/{tag} | Delete an tag.
[**get_tag**](TagsApi.md#get_tag) | **GET** /api/v1/tags/{tag} | Get a single tag.
[**list_attachment_by_tag**](TagsApi.md#list_attachment_by_tag) | **GET** /api/v1/tags/{tag}/attachments | Lists all attachments.
[**list_tag**](TagsApi.md#list_tag) | **GET** /api/v1/tags | List all tags.
[**list_transaction_by_tag**](TagsApi.md#list_transaction_by_tag) | **GET** /api/v1/tags/{tag}/transactions | List all transactions with this tag.
[**store_tag**](TagsApi.md#store_tag) | **POST** /api/v1/tags | Store a new tag
[**update_tag**](TagsApi.md#update_tag) | **PUT** /api/v1/tags/{tag} | Update existing tag.


# **delete_tag**
> delete_tag(tag)

Delete an tag.

Delete an tag.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    tag = "groceries" # str | Either the tag itself or the tag ID. If you use the tag itself, and it contains international (non-ASCII) characters, your milage may vary.

    # example passing only required values which don't have defaults set
    try:
        # Delete an tag.
        api_instance.delete_tag(tag)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. If you use the tag itself, and it contains international (non-ASCII) characters, your milage may vary. |

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
**204** | Tag deleted. |  -  |
**404** | No such tag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagSingle get_tag(tag)

Get a single tag.

Get a single tag.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
from firefly_iii_client.model.tag_single import TagSingle
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
    api_instance = tags_api.TagsApi(api_client)
    tag = "groceries" # str | Either the tag itself or the tag ID. If you use the tag itself, and it contains international (non-ASCII) characters, your milage may vary.
    page = 1 # int | Page number (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a single tag.
        api_response = api_instance.get_tag(tag)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a single tag.
        api_response = api_instance.get_tag(tag, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. If you use the tag itself, and it contains international (non-ASCII) characters, your milage may vary. |
 **page** | **int**| Page number | [optional]

### Return type

[**TagSingle**](TagSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested tag |  -  |
**404** | Tag not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_tag**
> AttachmentArray list_attachment_by_tag(tag)

Lists all attachments.

Lists all attachments.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
from firefly_iii_client.model.attachment_array import AttachmentArray
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
    api_instance = tags_api.TagsApi(api_client)
    tag = "groceries" # str | Either the tag itself or the tag ID.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lists all attachments.
        api_response = api_instance.list_attachment_by_tag(tag)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->list_attachment_by_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all attachments.
        api_response = api_instance.list_attachment_by_tag(tag, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->list_attachment_by_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of attachments |  -  |
**404** | No such tag. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tag**
> TagArray list_tag()

List all tags.

List all of the user's tags.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
from firefly_iii_client.model.tag_array import TagArray
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
    api_instance = tags_api.TagsApi(api_client)
    page = 1 # int | Page number (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all tags.
        api_response = api_instance.list_tag(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->list_tag: %s\n" % e)
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
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tags |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_tag**
> TransactionArray list_transaction_by_tag(tag)

List all transactions with this tag.

List all transactions with this tag.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
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
    api_instance = tags_api.TagsApi(api_client)
    tag = "groceries" # str | Either the tag itself or the tag ID.
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions with this tag.
        api_response = api_instance.list_transaction_by_tag(tag)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->list_transaction_by_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions with this tag.
        api_response = api_instance.list_transaction_by_tag(tag, page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->list_transaction_by_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned. | [optional]

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

# **store_tag**
> TagSingle store_tag(tag_model_store)

Store a new tag

Creates a new tag. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
from firefly_iii_client.model.tag_single import TagSingle
from firefly_iii_client.model.tag_model_store import TagModelStore
from firefly_iii_client.model.validation_error import ValidationError
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
    api_instance = tags_api.TagsApi(api_client)
    tag_model_store = TagModelStore(
        date=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        description="Tag for expensive stuff",
        latitude=51.983333,
        longitude=5.916667,
        tag="expensive",
        zoom_level=6,
    ) # TagModelStore | JSON array or key=value pairs with the necessary tag information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new tag
        api_response = api_instance.store_tag(tag_model_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->store_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_model_store** | [**TagModelStore**](TagModelStore.md)| JSON array or key&#x3D;value pairs with the necessary tag information. See the model for the exact specifications. |

### Return type

[**TagSingle**](TagSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New tag stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> TagSingle update_tag(tag, tag_model_update)

Update existing tag.

Update existing tag.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import tags_api
from firefly_iii_client.model.tag_single import TagSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.tag_model_update import TagModelUpdate
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
    api_instance = tags_api.TagsApi(api_client)
    tag = "groceries" # str | Either the tag itself or the tag ID. If you use the tag itself, and it contains international (non-ASCII) characters, your milage may vary.
    tag_model_update = TagModelUpdate(
        date=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        description="Tag for expensive stuff",
        latitude=51.983333,
        longitude=5.916667,
        tag="expensive",
        zoom_level=6,
    ) # TagModelUpdate | JSON array with updated tag information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing tag.
        api_response = api_instance.update_tag(tag, tag_model_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TagsApi->update_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Either the tag itself or the tag ID. If you use the tag itself, and it contains international (non-ASCII) characters, your milage may vary. |
 **tag_model_update** | [**TagModelUpdate**](TagModelUpdate.md)| JSON array with updated tag information. See the model for the exact specifications. |

### Return type

[**TagSingle**](TagSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated tag stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

