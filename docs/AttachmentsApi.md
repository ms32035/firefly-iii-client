# firefly_iii_client.AttachmentsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment**](AttachmentsApi.md#delete_attachment) | **DELETE** /api/v1/attachments/{id} | Delete an attachment.
[**download_attachment**](AttachmentsApi.md#download_attachment) | **GET** /api/v1/attachments/{id}/download | Download a single attachment.
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /api/v1/attachments/{id} | Get a single attachment.
[**list_attachment**](AttachmentsApi.md#list_attachment) | **GET** /api/v1/attachments | List all attachments.
[**store_attachment**](AttachmentsApi.md#store_attachment) | **POST** /api/v1/attachments | Store a new attachment.
[**update_attachment**](AttachmentsApi.md#update_attachment) | **PUT** /api/v1/attachments/{id} | Update existing attachment.
[**upload_attachment**](AttachmentsApi.md#upload_attachment) | **POST** /api/v1/attachments/{id}/upload | Upload an attachment.


# **delete_attachment**
> delete_attachment(id)

Delete an attachment.

With this endpoint you delete an attachment, including any stored file data. 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the single.

try:
    # Delete an attachment.
    api_instance.delete_attachment(id)
except ApiException as e:
    print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the single. | 

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
**204** | Attachment deleted. |  -  |
**404** | No such attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> file download_attachment(id)

Download a single attachment.

This endpoint allows you to download the binary content of a transaction. It will be sent to you as a download, using the content type \"application/octet-stream\" and content disposition \"attachment; filename=example.pdf\". 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the attachment.

try:
    # Download a single attachment.
    api_response = api_instance.download_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->download_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the attachment. | 

### Return type

**file**

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested attachment |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentSingle get_attachment(id)

Get a single attachment.

Get a single attachment. This endpoint only returns the available metadata for the attachment. Actual file data is handled in two other endpoints (see below). 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the attachment.

try:
    # Get a single attachment.
    api_response = api_instance.get_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the attachment. | 

### Return type

[**AttachmentSingle**](AttachmentSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested attachment |  -  |
**404** | Attachment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment**
> AttachmentArray list_attachment(page=page)

List all attachments.

This endpoint lists all attachments. 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all attachments.
    api_response = api_instance.list_attachment(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | A list of attachments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_attachment**
> AttachmentSingle store_attachment(attachment)

Store a new attachment.

Creates a new attachment. The data required can be submitted as a JSON body or as a list of parameters. You cannot use this endpoint to upload the actual file data (see below). This endpoint only creates the attachment object. 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
attachment = firefly_iii_client.Attachment() # Attachment | JSON array or key=value pairs with the necessary attachment information. See the model for the exact specifications.

try:
    # Store a new attachment.
    api_response = api_instance.store_attachment(attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->store_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | [**Attachment**](Attachment.md)| JSON array or key&#x3D;value pairs with the necessary attachment information. See the model for the exact specifications. | 

### Return type

[**AttachmentSingle**](AttachmentSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New attachment stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment**
> AttachmentSingle update_attachment(id, attachment)

Update existing attachment.

Update the meta data for an existing attachment. This endpoint does not allow you to upload or download data. For that, see below. 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the attachment.
attachment = firefly_iii_client.Attachment() # Attachment | JSON array with updated attachment information. See the model for the exact specifications.

try:
    # Update existing attachment.
    api_response = api_instance.update_attachment(id, attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->update_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the attachment. | 
 **attachment** | [**Attachment**](Attachment.md)| JSON array with updated attachment information. See the model for the exact specifications. | 

### Return type

[**AttachmentSingle**](AttachmentSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated attachment stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_attachment**
> upload_attachment(id, body=body)

Upload an attachment.

Use this endpoint to upload (and possible overwrite) the file contents of an attachment. Simply put the entire file in the body as binary data. 

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
api_instance = firefly_iii_client.AttachmentsApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the attachment.
body = '/path/to/file' # file |  (optional)

try:
    # Upload an attachment.
    api_instance.upload_attachment(id, body=body)
except ApiException as e:
    print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the attachment. | 
 **body** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Upload was a success |  -  |
**404** | File not found |  -  |
**422** | Upload invalid or empty file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

