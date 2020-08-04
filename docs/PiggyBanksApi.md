# firefly_iii_client.PiggyBanksApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_piggy_bank**](PiggyBanksApi.md#delete_piggy_bank) | **DELETE** /api/v1/piggy_banks/{id} | Delete a piggy bank.
[**get_piggy_bank**](PiggyBanksApi.md#get_piggy_bank) | **GET** /api/v1/piggy_banks/{id} | Get a single piggy bank.
[**list_attachment_by_piggy_bank**](PiggyBanksApi.md#list_attachment_by_piggy_bank) | **GET** /api/v1/piggy_banks/{id}/attachments | Lists all attachments.
[**list_event_by_piggy_bank**](PiggyBanksApi.md#list_event_by_piggy_bank) | **GET** /api/v1/piggy_banks/{id}/events | List all events linked to a piggy bank.
[**list_piggy_bank**](PiggyBanksApi.md#list_piggy_bank) | **GET** /api/v1/piggy_banks | List all piggy banks.
[**store_piggy_bank**](PiggyBanksApi.md#store_piggy_bank) | **POST** /api/v1/piggy_banks | Store a new piggy bank
[**update_piggy_bank**](PiggyBanksApi.md#update_piggy_bank) | **PUT** /api/v1/piggy_banks/{id} | Update existing piggy bank.


# **delete_piggy_bank**
> delete_piggy_bank(id)

Delete a piggy bank.

Delete a piggy bank.

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the piggy bank.

try:
    # Delete a piggy bank.
    api_instance.delete_piggy_bank(id)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->delete_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the piggy bank. | 

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
**204** | Piggy bank deleted. |  -  |
**404** | No such piggy bank |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_piggy_bank**
> PiggyBankSingle get_piggy_bank(id)

Get a single piggy bank.

Get a single piggy bank.

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the piggy bank.

try:
    # Get a single piggy bank.
    api_response = api_instance.get_piggy_bank(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->get_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the piggy bank. | 

### Return type

[**PiggyBankSingle**](PiggyBankSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested piggy bank |  -  |
**404** | Piggy bank not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_piggy_bank**
> AttachmentArray list_attachment_by_piggy_bank(id, page=page)

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the piggy bank.
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # Lists all attachments.
    api_response = api_instance.list_attachment_by_piggy_bank(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->list_attachment_by_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the piggy bank. | 
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
**404** | No such piggy bank. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_by_piggy_bank**
> PiggyBankEventArray list_event_by_piggy_bank(id, page=page)

List all events linked to a piggy bank.

List all events linked to a piggy bank (adding and removing money).

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the piggy bank
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all events linked to a piggy bank.
    api_response = api_instance.list_event_by_piggy_bank(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->list_event_by_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the piggy bank | 
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
**200** | A list of piggy bank related events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_piggy_bank**
> PiggyBankArray list_piggy_bank(page=page)

List all piggy banks.

List all piggy banks.

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all piggy banks.
    api_response = api_instance.list_piggy_bank(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->list_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional] 

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

# **store_piggy_bank**
> PiggyBankSingle store_piggy_bank(piggy_bank)

Store a new piggy bank

Creates a new piggy bank. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
piggy_bank = firefly_iii_client.PiggyBank() # PiggyBank | JSON array or key=value pairs with the necessary piggy bank information. See the model for the exact specifications.

try:
    # Store a new piggy bank
    api_response = api_instance.store_piggy_bank(piggy_bank)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->store_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piggy_bank** | [**PiggyBank**](PiggyBank.md)| JSON array or key&#x3D;value pairs with the necessary piggy bank information. See the model for the exact specifications. | 

### Return type

[**PiggyBankSingle**](PiggyBankSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New piggy bank stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_piggy_bank**
> PiggyBankSingle update_piggy_bank(id, piggy_bank)

Update existing piggy bank.

Update existing piggy bank.

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
api_instance = firefly_iii_client.PiggyBanksApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the piggy bank
piggy_bank = firefly_iii_client.PiggyBank() # PiggyBank | JSON array with updated piggy bank information. See the model for the exact specifications.

try:
    # Update existing piggy bank.
    api_response = api_instance.update_piggy_bank(id, piggy_bank)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PiggyBanksApi->update_piggy_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the piggy bank | 
 **piggy_bank** | [**PiggyBank**](PiggyBank.md)| JSON array with updated piggy bank information. See the model for the exact specifications. | 

### Return type

[**PiggyBankSingle**](PiggyBankSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated piggy bank stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

