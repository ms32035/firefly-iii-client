<a id="__pageTop"></a>
# firefly_iii_client.apis.tags.data_api.DataApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_transactions**](#bulk_update_transactions) | **post** /v1/data/bulk/transactions | Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/firefly-iii/api/specials
[**destroy_data**](#destroy_data) | **delete** /v1/data/destroy | Endpoint to destroy user data
[**export_accounts**](#export_accounts) | **get** /v1/data/export/accounts | Export account data from Firefly III
[**export_bills**](#export_bills) | **get** /v1/data/export/bills | Export bills from Firefly III
[**export_budgets**](#export_budgets) | **get** /v1/data/export/budgets | Export budgets and budget amount data from Firefly III
[**export_categories**](#export_categories) | **get** /v1/data/export/categories | Export category data from Firefly III
[**export_piggies**](#export_piggies) | **get** /v1/data/export/piggy-banks | Export piggy banks from Firefly III
[**export_recurring**](#export_recurring) | **get** /v1/data/export/recurring | Export recurring transaction data from Firefly III
[**export_rules**](#export_rules) | **get** /v1/data/export/rules | Export rule groups and rule data from Firefly III
[**export_tags**](#export_tags) | **get** /v1/data/export/tags | Export tag data from Firefly III
[**export_transactions**](#export_transactions) | **get** /v1/data/export/transactions | Export transaction data from Firefly III
[**purge_data**](#purge_data) | **delete** /v1/data/purge | Endpoint to purge user data

# **bulk_update_transactions**
<a id="bulk_update_transactions"></a>
> bulk_update_transactions(query)

Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/firefly-iii/api/specials

Allows you to update transactions in bulk. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/firefly-iii/api/specials
        api_response = api_instance.bulk_update_transactions(
            query_params=query_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->bulk_update_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | 


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#bulk_update_transactions.ApiResponseFor204) | Empty response when the update was successful. A future improvement is to include the changed transactions.
400 | [ApiResponseFor400](#bulk_update_transactions.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#bulk_update_transactions.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#bulk_update_transactions.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#bulk_update_transactions.ApiResponseFor500) | Internal exception

#### bulk_update_transactions.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### bulk_update_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### bulk_update_transactions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### bulk_update_transactions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### bulk_update_transactions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **destroy_data**
<a id="destroy_data"></a>
> destroy_data(objects)

Endpoint to destroy user data

A call to this endpoint deletes the requested data type. Use it with care and always with user permission. The demo user is incapable of using this endpoint. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.data_destroy_object import DataDestroyObject
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'objects': DataDestroyObject("not_assets_liabilities"),
    }
    header_params = {
    }
    try:
        # Endpoint to destroy user data
        api_response = api_instance.destroy_data(
            query_params=query_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->destroy_data: %s\n" % e)

    # example passing only optional values
    query_params = {
        'objects': DataDestroyObject("not_assets_liabilities"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Endpoint to destroy user data
        api_response = api_instance.destroy_data(
            query_params=query_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->destroy_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
objects | ObjectsSchema | | 


# ObjectsSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**DataDestroyObject**](../../models/DataDestroyObject.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#destroy_data.ApiResponseFor204) | Empty response when data has been destroyed.
400 | [ApiResponseFor400](#destroy_data.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#destroy_data.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#destroy_data.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#destroy_data.ApiResponseFor500) | Internal exception

#### destroy_data.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### destroy_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### destroy_data.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### destroy_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### destroy_data.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_accounts**
<a id="export_accounts"></a>
> file_type export_accounts()

Export account data from Firefly III

This endpoint allows you to export your accounts from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export account data from Firefly III
        api_response = api_instance.export_accounts(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_accounts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_accounts.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_accounts.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_accounts.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_accounts.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_accounts.ApiResponseFor500) | Internal exception

#### export_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_accounts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_accounts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_accounts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_accounts.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_bills**
<a id="export_bills"></a>
> file_type export_bills()

Export bills from Firefly III

This endpoint allows you to export your bills from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export bills from Firefly III
        api_response = api_instance.export_bills(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_bills: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_bills.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_bills.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_bills.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_bills.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_bills.ApiResponseFor500) | Internal exception

#### export_bills.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_bills.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_bills.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_bills.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_bills.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_budgets**
<a id="export_budgets"></a>
> file_type export_budgets()

Export budgets and budget amount data from Firefly III

This endpoint allows you to export your budgets and associated budget data from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export budgets and budget amount data from Firefly III
        api_response = api_instance.export_budgets(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_budgets: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_budgets.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_budgets.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_budgets.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_budgets.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_budgets.ApiResponseFor500) | Internal exception

#### export_budgets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_budgets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_budgets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_budgets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_budgets.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_categories**
<a id="export_categories"></a>
> file_type export_categories()

Export category data from Firefly III

This endpoint allows you to export your categories from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export category data from Firefly III
        api_response = api_instance.export_categories(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_categories: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_categories.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_categories.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_categories.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_categories.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_categories.ApiResponseFor500) | Internal exception

#### export_categories.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_categories.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_categories.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_categories.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_categories.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_piggies**
<a id="export_piggies"></a>
> file_type export_piggies()

Export piggy banks from Firefly III

This endpoint allows you to export your piggy banks from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export piggy banks from Firefly III
        api_response = api_instance.export_piggies(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_piggies: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_piggies.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_piggies.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_piggies.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_piggies.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_piggies.ApiResponseFor500) | Internal exception

#### export_piggies.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_piggies.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_piggies.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_piggies.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_piggies.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_recurring**
<a id="export_recurring"></a>
> file_type export_recurring()

Export recurring transaction data from Firefly III

This endpoint allows you to export your recurring transactions from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export recurring transaction data from Firefly III
        api_response = api_instance.export_recurring(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_recurring: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_recurring.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_recurring.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_recurring.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_recurring.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_recurring.ApiResponseFor500) | Internal exception

#### export_recurring.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_recurring.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_recurring.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_recurring.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_recurring.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_rules**
<a id="export_rules"></a>
> file_type export_rules()

Export rule groups and rule data from Firefly III

This endpoint allows you to export your rules and rule groups from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export rule groups and rule data from Firefly III
        api_response = api_instance.export_rules(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_rules: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_rules.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_rules.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_rules.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_rules.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_rules.ApiResponseFor500) | Internal exception

#### export_rules.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_rules.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_rules.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_rules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_rules.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_tags**
<a id="export_tags"></a>
> file_type export_tags()

Export tag data from Firefly III

This endpoint allows you to export your tags from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    query_params = {
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export tag data from Firefly III
        api_response = api_instance.export_tags(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_tags.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_tags.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_tags.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_tags.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_tags.ApiResponseFor500) | Internal exception

#### export_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_tags.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_tags.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_tags.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_tags.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_transactions**
<a id="export_transactions"></a>
> file_type export_transactions(startend)

Export transaction data from Firefly III

This endpoint allows you to export transactions from Firefly III into a file. Currently supports CSV exports only. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'start': "1970-01-01",
        'end': "1970-01-01",
    }
    header_params = {
    }
    try:
        # Export transaction data from Firefly III
        api_response = api_instance.export_transactions(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_transactions: %s\n" % e)

    # example passing only optional values
    query_params = {
        'start': "1970-01-01",
        'end': "1970-01-01",
        'accounts': "1,2,3",
        'type': ExportFileFilter("csv"),
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Export transaction data from Firefly III
        api_response = api_instance.export_transactions(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->export_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | 
end | EndSchema | | 
accounts | AccountsSchema | | optional
type | TypeSchema | | optional


# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileFilter**](../../models/ExportFileFilter.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_transactions.ApiResponseFor200) | The exported transaction in a file.
400 | [ApiResponseFor400](#export_transactions.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_transactions.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#export_transactions.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#export_transactions.ApiResponseFor500) | Internal exception

#### export_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### export_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### export_transactions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### export_transactions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### export_transactions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **purge_data**
<a id="purge_data"></a>
> purge_data()

Endpoint to purge user data

A call to this endpoint purges all previously deleted data. Use it with care and always with user permission. The demo user is incapable of using this endpoint. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import data_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
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

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org/api",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)

    # example passing only optional values
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Endpoint to purge user data
        api_response = api_instance.purge_data(
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling DataApi->purge_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Trace-Id | XTraceIdSchema | | optional

# XTraceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#purge_data.ApiResponseFor204) | Empty response when data has been purged.
400 | [ApiResponseFor400](#purge_data.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#purge_data.ApiResponseFor401) | Unauthenticated
500 | [ApiResponseFor500](#purge_data.ApiResponseFor500) | Internal exception

#### purge_data.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### purge_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### purge_data.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### purge_data.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalException**](../../models/InternalException.md) |  | 


### Authorization

[firefly_iii_auth](../../../README.md#firefly_iii_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

