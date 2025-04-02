# firefly_iii_client.AttachmentsApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment**](AttachmentsApi.md#delete_attachment) | **DELETE** /v1/attachments/{id} | Delete an attachment.
[**download_attachment**](AttachmentsApi.md#download_attachment) | **GET** /v1/attachments/{id}/download | Download a single attachment.
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /v1/attachments/{id} | Get a single attachment.
[**list_attachment**](AttachmentsApi.md#list_attachment) | **GET** /v1/attachments | List all attachments.
[**store_attachment**](AttachmentsApi.md#store_attachment) | **POST** /v1/attachments | Store a new attachment.
[**update_attachment**](AttachmentsApi.md#update_attachment) | **PUT** /v1/attachments/{id} | Update existing attachment.
[**upload_attachment**](AttachmentsApi.md#upload_attachment) | **POST** /v1/attachments/{id}/upload | Upload an attachment.


# **delete_attachment**
> delete_attachment(id, x_trace_id=x_trace_id)

Delete an attachment.

With this endpoint you delete an attachment, including any stored file data.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    id = '123' # str | The ID of the single attachment.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Delete an attachment.
        api_instance.delete_attachment(id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the single attachment. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Attachment deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> bytearray download_attachment(id, x_trace_id=x_trace_id)

Download a single attachment.

This endpoint allows you to download the binary content of a transaction. It will be sent to you as a download, using the content type "application/octet-stream" and content disposition "attachment; filename=example.pdf".


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    id = '123' # str | The ID of the attachment.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Download a single attachment.
        api_response = api_instance.download_attachment(id, x_trace_id=x_trace_id)
        print("The response of AttachmentsApi->download_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->download_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the attachment. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

**bytearray**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested attachment |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentSingle get_attachment(id, x_trace_id=x_trace_id)

Get a single attachment.

Get a single attachment. This endpoint only returns the available metadata for the attachment. Actual file data is handled in two other endpoints (see below).


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.attachment_single import AttachmentSingle
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    id = '123' # str | The ID of the attachment.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Get a single attachment.
        api_response = api_instance.get_attachment(id, x_trace_id=x_trace_id)
        print("The response of AttachmentsApi->get_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the attachment. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**AttachmentSingle**](AttachmentSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested attachment |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment**
> AttachmentArray list_attachment(x_trace_id=x_trace_id, limit=limit, page=page)

List all attachments.

This endpoint lists all attachments.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.attachment_array import AttachmentArray
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    limit = 10 # int | Number of items per page. The default pagination is per 50 items. (optional)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    try:
        # List all attachments.
        api_response = api_instance.list_attachment(x_trace_id=x_trace_id, limit=limit, page=page)
        print("The response of AttachmentsApi->list_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->list_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **limit** | **int**| Number of items per page. The default pagination is per 50 items. | [optional] 
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of attachments. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_attachment**
> AttachmentSingle store_attachment(attachment_store, x_trace_id=x_trace_id)

Store a new attachment.

Creates a new attachment. The data required can be submitted as a JSON body or as a list of parameters. You cannot use this endpoint to upload the actual file data (see below). This endpoint only creates the attachment object.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.attachment_single import AttachmentSingle
from firefly_iii_client.models.attachment_store import AttachmentStore
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    attachment_store = firefly_iii_client.AttachmentStore() # AttachmentStore | JSON array or key=value pairs with the necessary attachment information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Store a new attachment.
        api_response = api_instance.store_attachment(attachment_store, x_trace_id=x_trace_id)
        print("The response of AttachmentsApi->store_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->store_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_store** | [**AttachmentStore**](AttachmentStore.md)| JSON array or key&#x3D;value pairs with the necessary attachment information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**AttachmentSingle**](AttachmentSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New attachment stored, result in response. |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment**
> AttachmentSingle update_attachment(id, attachment_update, x_trace_id=x_trace_id)

Update existing attachment.

Update the meta data for an existing attachment. This endpoint does not allow you to upload or download data. For that, see below.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.models.attachment_single import AttachmentSingle
from firefly_iii_client.models.attachment_update import AttachmentUpdate
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    id = '123' # str | The ID of the attachment.
    attachment_update = firefly_iii_client.AttachmentUpdate() # AttachmentUpdate | JSON array with updated attachment information. See the model for the exact specifications.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)

    try:
        # Update existing attachment.
        api_response = api_instance.update_attachment(id, attachment_update, x_trace_id=x_trace_id)
        print("The response of AttachmentsApi->update_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->update_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the attachment. | 
 **attachment_update** | [**AttachmentUpdate**](AttachmentUpdate.md)| JSON array with updated attachment information. See the model for the exact specifications. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 

### Return type

[**AttachmentSingle**](AttachmentSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated attachment stored, result in response |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_attachment**
> upload_attachment(id, x_trace_id=x_trace_id, body=body)

Upload an attachment.

Use this endpoint to upload (and possible overwrite) the file contents of an attachment. Simply put the entire file in the body as binary data.


### Example

* OAuth Authentication (firefly_iii_auth):
* Bearer Authentication (local_bearer_auth):

```python
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.firefly-iii.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: local_bearer_auth
configuration = firefly_iii_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = firefly_iii_client.AttachmentsApi(api_client)
    id = '123' # str | The ID of the attachment.
    x_trace_id = '40c71bbb-c676-4f24-83cf-cc725d7d7a00' # str | Unique identifier associated with this request. (optional)
    body = None # bytearray |  (optional)

    try:
        # Upload an attachment.
        api_instance.upload_attachment(id, x_trace_id=x_trace_id, body=body)
    except Exception as e:
        print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the attachment. | 
 **x_trace_id** | **str**| Unique identifier associated with this request. | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth), [local_bearer_auth](../README.md#local_bearer_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Upload was a success |  -  |
**400** | Bad request |  -  |
**401** | Unauthenticated |  -  |
**404** | Page not found |  -  |
**422** | Validation error. The body will have the exact details. |  -  |
**500** | Internal exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

