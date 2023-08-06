<a id="__pageTop"></a>
# firefly_iii_client.apis.tags.rules_api.RulesApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule**](#delete_rule) | **delete** /v1/rules/{id} | Delete an rule.
[**fire_rule**](#fire_rule) | **post** /v1/rules/{id}/trigger | Fire the rule on your transactions.
[**get_rule**](#get_rule) | **get** /v1/rules/{id} | Get a single rule.
[**list_rule**](#list_rule) | **get** /v1/rules | List all rules.
[**store_rule**](#store_rule) | **post** /v1/rules | Store a new rule
[**test_rule**](#test_rule) | **get** /v1/rules/{id}/test | Test which transactions would be hit by the rule. No changes will be made.
[**update_rule**](#update_rule) | **put** /v1/rules/{id} | Update existing rule.

# **delete_rule**
<a id="delete_rule"></a>
> delete_rule(id)

Delete an rule.

Delete an rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # Delete an rule.
        api_response = api_instance.delete_rule(
            path_params=path_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->delete_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Delete an rule.
        api_response = api_instance.delete_rule(
            path_params=path_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->delete_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_rule.ApiResponseFor204) | Rule deleted.
400 | [ApiResponseFor400](#delete_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#delete_rule.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#delete_rule.ApiResponseFor500) | Internal exception

#### delete_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### delete_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### delete_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_rule.ApiResponseFor500
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

# **fire_rule**
<a id="fire_rule"></a>
> fire_rule(id)

Fire the rule on your transactions.

Fire the rule group on your transactions. Changes will be made by the rules in the group! Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Fire the rule on your transactions.
        api_response = api_instance.fire_rule(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->fire_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    query_params = {
        'start': "Mon Sep 17 00:00:00 UTC 2018",
        'end': "Mon Sep 17 00:00:00 UTC 2018",
        'accounts[]': ["1","2","3"],
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Fire the rule on your transactions.
        api_response = api_instance.fire_rule(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->fire_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | optional
end | EndSchema | | optional
accounts[] | AccountsSchema | | optional


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
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#fire_rule.ApiResponseFor204) | The rules in the group are executed. Due to the setup of this function (asynchronous job execution) the result cannot be displayed.
400 | [ApiResponseFor400](#fire_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#fire_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#fire_rule.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#fire_rule.ApiResponseFor500) | Internal exception

#### fire_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### fire_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### fire_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### fire_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### fire_rule.ApiResponseFor500
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

# **get_rule**
<a id="get_rule"></a>
> RuleSingle get_rule(id)

Get a single rule.

Get a single rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
from firefly_iii_client.model.rule_single import RuleSingle
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # Get a single rule.
        api_response = api_instance.get_rule(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->get_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Get a single rule.
        api_response = api_instance.get_rule(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->get_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_rule.ApiResponseFor200) | The requested rule
400 | [ApiResponseFor400](#get_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_rule.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_rule.ApiResponseFor500) | Internal exception

#### get_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleSingle**](../../models/RuleSingle.md) |  | 


#### get_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_rule.ApiResponseFor500
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

# **list_rule**
<a id="list_rule"></a>
> RuleArray list_rule()

List all rules.

List all rules.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.rule_array import RuleArray
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # List all rules.
        api_response = api_instance.list_rule(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->list_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#list_rule.ApiResponseFor200) | A list of rules
400 | [ApiResponseFor400](#list_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#list_rule.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#list_rule.ApiResponseFor500) | Internal exception

#### list_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleArray**](../../models/RuleArray.md) |  | 


#### list_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### list_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### list_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### list_rule.ApiResponseFor500
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

# **store_rule**
<a id="store_rule"></a>
> RuleSingle store_rule(rule_store)

Store a new rule

Creates a new rule. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
from firefly_iii_client.model.rule_store import RuleStore
from firefly_iii_client.model.rule_single import RuleSingle
from firefly_iii_client.model.validation_error import ValidationError
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = RuleStore(
        actions=[
            RuleActionStore(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleActionKeyword("set_category"),
                value="Daily groceries",
            )
        ],
        active=True,
        description="First rule description",
        order=5,
        rule_group_id="81",
        rule_group_title="New rule group",
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger=RuleTriggerType("store-journal"),
        triggers=[
            RuleTriggerStore(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleTriggerKeyword("user_action"),
                value="tag1",
            )
        ],
    )
    try:
        # Store a new rule
        api_response = api_instance.store_rule(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->store_rule: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    body = RuleStore(
        actions=[
            RuleActionStore(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleActionKeyword("set_category"),
                value="Daily groceries",
            )
        ],
        active=True,
        description="First rule description",
        order=5,
        rule_group_id="81",
        rule_group_title="New rule group",
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger=RuleTriggerType("store-journal"),
        triggers=[
            RuleTriggerStore(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleTriggerKeyword("user_action"),
                value="tag1",
            )
        ],
    )
    try:
        # Store a new rule
        api_response = api_instance.store_rule(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->store_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleStore**](../../models/RuleStore.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleStore**](../../models/RuleStore.md) |  | 


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
200 | [ApiResponseFor200](#store_rule.ApiResponseFor200) | New rule stored, result in response.
400 | [ApiResponseFor400](#store_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#store_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#store_rule.ApiResponseFor404) | Page not found
422 | [ApiResponseFor422](#store_rule.ApiResponseFor422) | Validation error. The body will have the exact details.
500 | [ApiResponseFor500](#store_rule.ApiResponseFor500) | Internal exception

#### store_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleSingle**](../../models/RuleSingle.md) |  | 


#### store_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### store_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### store_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### store_rule.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


#### store_rule.ApiResponseFor500
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

# **test_rule**
<a id="test_rule"></a>
> TransactionArray test_rule(id)

Test which transactions would be hit by the rule. No changes will be made.

Test which transactions would be hit by the rule. No changes will be made. Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
from firefly_iii_client.model.transaction_array import TransactionArray
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Test which transactions would be hit by the rule. No changes will be made.
        api_response = api_instance.test_rule(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    query_params = {
        'start': "Mon Sep 17 00:00:00 UTC 2018",
        'end': "Mon Sep 17 00:00:00 UTC 2018",
        'accounts[]': ["1","2","3"],
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Test which transactions would be hit by the rule. No changes will be made.
        api_response = api_instance.test_rule(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start | StartSchema | | optional
end | EndSchema | | optional
accounts[] | AccountsSchema | | optional


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
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#test_rule.ApiResponseFor200) | A list of transactions that would be changed by the rule. No changes will be made.
400 | [ApiResponseFor400](#test_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#test_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#test_rule.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#test_rule.ApiResponseFor500) | Internal exception

#### test_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionArray**](../../models/TransactionArray.md) |  | 


#### test_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### test_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### test_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### test_rule.ApiResponseFor500
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

# **update_rule**
<a id="update_rule"></a>
> RuleSingle update_rule(idrule_update)

Update existing rule.

Update existing rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rules_api
from firefly_iii_client.model.rule_single import RuleSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.rule_update import RuleUpdate
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
    api_instance = rules_api.RulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    body = RuleUpdate(
        actions=[
            RuleActionUpdate(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleActionKeyword("set_category"),
                value="Daily groceries",
            )
        ],
        active=True,
        description="First rule description",
        order=5,
        rule_group_id="81",
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger=RuleTriggerType("store-journal"),
        triggers=[
            RuleTriggerUpdate(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleTriggerKeyword("user_action"),
                value="tag1",
            )
        ],
    )
    try:
        # Update existing rule.
        api_response = api_instance.update_rule(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->update_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    body = RuleUpdate(
        actions=[
            RuleActionUpdate(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleActionKeyword("set_category"),
                value="Daily groceries",
            )
        ],
        active=True,
        description="First rule description",
        order=5,
        rule_group_id="81",
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger=RuleTriggerType("store-journal"),
        triggers=[
            RuleTriggerUpdate(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleTriggerKeyword("user_action"),
                value="tag1",
            )
        ],
    )
    try:
        # Update existing rule.
        api_response = api_instance.update_rule(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->update_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleUpdate**](../../models/RuleUpdate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleUpdate**](../../models/RuleUpdate.md) |  | 


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_rule.ApiResponseFor200) | Updated rule stored, result in response
400 | [ApiResponseFor400](#update_rule.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_rule.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#update_rule.ApiResponseFor404) | Page not found
422 | [ApiResponseFor422](#update_rule.ApiResponseFor422) | Validation error. The body will have the exact details.
500 | [ApiResponseFor500](#update_rule.ApiResponseFor500) | Internal exception

#### update_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleSingle**](../../models/RuleSingle.md) |  | 


#### update_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### update_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### update_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### update_rule.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


#### update_rule.ApiResponseFor500
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

