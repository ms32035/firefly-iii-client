# firefly_iii_client.ImportApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_import**](ImportApi.md#get_import) | **GET** /api/v1/import/{key} | Show info on a single import
[**get_imports**](ImportApi.md#get_imports) | **GET** /api/v1/import/list | List al imports
[**get_transactions_by_import**](ImportApi.md#get_transactions_by_import) | **GET** /api/v1/import/{key}/transactions | List all transactions related to the import job. The correlation is made through the tag.


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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.ImportApi(firefly_iii_client.ApiClient(configuration))
key = x2Akaijm2 # str | The job key of an import job.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_imports**
> ImportJobArray get_imports(page=page)

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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.ImportApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is per 50 items. (optional)

try:
    # List al imports
    api_response = api_instance.get_imports(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_imports: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_import**
> TransactionArray get_transactions_by_import(key, page=page, start=start, end=end, type=type)

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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = firefly_iii_client.ImportApi(firefly_iii_client.ApiClient(configuration))
key = abcde # str | The key of the import job
page = 1 # int | Page number. The default pagination is 50. (optional)
start = 2018-09-17 # str | A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  (optional)
end = 2018-09-17 # str | A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  (optional)
type = 'type_example' # str | Optional filter on the transaction type(s) returned. (optional)

try:
    # List all transactions related to the import job. The correlation is made through the tag.
    api_response = api_instance.get_transactions_by_import(key, page=page, start=start, end=end, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_transactions_by_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the import job | 
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

