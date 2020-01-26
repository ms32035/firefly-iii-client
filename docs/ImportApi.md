# firefly_iii_client.ImportApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_import**](ImportApi.md#get_import) | **GET** /api/v1/import/{key} | Show info on a single import
[**list_import**](ImportApi.md#list_import) | **GET** /api/v1/import/list | List al imports
[**list_transaction_by_import**](ImportApi.md#list_transaction_by_import) | **GET** /api/v1/import/{key}/transactions | List all transactions related to the import job. The correlation is made through the tag.


# **get_import**
> ImportJobSingle get_import(key)

Show info on a single import

Show info on single import.

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
api_instance = firefly_iii_client.ImportApi(firefly_iii_client.ApiClient(configuration))
key = 'x2Akaijm2' # str | The job key of an import job.

try:
    # Show info on a single import
    api_response = api_instance.get_import(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The job key of an import job. | 

### Return type

[**ImportJobSingle**](ImportJobSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested import job |  -  |
**404** | Import job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_import**
> ImportJobArray list_import(page=page)

List al imports

List all imports

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
api_instance = firefly_iii_client.ImportApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is per 50 items. (optional)

try:
    # List al imports
    api_response = api_instance.list_import(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->list_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional] 

### Return type

[**ImportJobArray**](ImportJobArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of import jobs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_import**
> TransactionArray list_transaction_by_import(key, page=page, start=start, end=end, type=type)

List all transactions related to the import job. The correlation is made through the tag.

See summary 

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
api_instance = firefly_iii_client.ImportApi(firefly_iii_client.ApiClient(configuration))
key = 'abcde' # str | The key of the import job
page = 1 # int | Page number. The default pagination is 50. (optional)
start = '2013-10-20' # date | A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  (optional)
end = '2013-10-20' # date | A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  (optional)
type = firefly_iii_client.TransactionTypeFilter() # TransactionTypeFilter | Optional filter on the transaction type(s) returned. (optional)

try:
    # List all transactions related to the import job. The correlation is made through the tag.
    api_response = api_instance.list_transaction_by_import(key, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->list_transaction_by_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the import job | 
 **page** | **int**| Page number. The default pagination is 50. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  | [optional] 
 **type** | [**TransactionTypeFilter**](.md)| Optional filter on the transaction type(s) returned. | [optional] 

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

