<a id="__pageTop"></a>
# firefly_iii_client.apis.tags.rule_groups_api.RuleGroupsApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule_group**](#delete_rule_group) | **delete** /v1/rule-groups/{id} | Delete a rule group.
[**fire_rule_group**](#fire_rule_group) | **post** /v1/rule-groups/{id}/trigger | Fire the rule group on your transactions.
[**get_rule_group**](#get_rule_group) | **get** /v1/rule-groups/{id} | Get a single rule group.
[**list_rule_by_group**](#list_rule_by_group) | **get** /v1/rule-groups/{id}/rules | List rules in this rule group.
[**list_rule_group**](#list_rule_group) | **get** /v1/rule-groups | List all rule groups.
[**store_rule_group**](#store_rule_group) | **post** /v1/rule-groups | Store a new rule group.
[**test_rule_group**](#test_rule_group) | **get** /v1/rule-groups/{id}/test | Test which transactions would be hit by the rule group. No changes will be made.
[**update_rule_group**](#update_rule_group) | **put** /v1/rule-groups/{id} | Update existing rule group.

# **delete_rule_group**
<a id="delete_rule_group"></a>
> delete_rule_group(id)

Delete a rule group.

Delete a rule group.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # Delete a rule group.
        api_response = api_instance.delete_rule_group(
            path_params=path_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->delete_rule_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Delete a rule group.
        api_response = api_instance.delete_rule_group(
            path_params=path_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->delete_rule_group: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_rule_group.ApiResponseFor204) | Rule group deleted.
400 | [ApiResponseFor400](#delete_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#delete_rule_group.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#delete_rule_group.ApiResponseFor500) | Internal exception

#### delete_rule_group.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### delete_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### delete_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_rule_group.ApiResponseFor500
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

# **fire_rule_group**
<a id="fire_rule_group"></a>
> fire_rule_group(id)

Fire the rule group on your transactions.

Fire the rule group on your transactions. Changes will be made by the rules in the rule group! Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Fire the rule group on your transactions.
        api_response = api_instance.fire_rule_group(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->fire_rule_group: %s\n" % e)

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
        # Fire the rule group on your transactions.
        api_response = api_instance.fire_rule_group(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->fire_rule_group: %s\n" % e)
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
204 | [ApiResponseFor204](#fire_rule_group.ApiResponseFor204) | The rules in the group are executed. Due to the setup of this function (asynchronous job execution) the result cannot be displayed.
400 | [ApiResponseFor400](#fire_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#fire_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#fire_rule_group.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#fire_rule_group.ApiResponseFor500) | Internal exception

#### fire_rule_group.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### fire_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### fire_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### fire_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### fire_rule_group.ApiResponseFor500
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

# **get_rule_group**
<a id="get_rule_group"></a>
> RuleGroupSingle get_rule_group(id)

Get a single rule group.

Get a single rule group. This does not include the rules. For that, see below.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # Get a single rule group.
        api_response = api_instance.get_rule_group(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->get_rule_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Get a single rule group.
        api_response = api_instance.get_rule_group(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->get_rule_group: %s\n" % e)
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
200 | [ApiResponseFor200](#get_rule_group.ApiResponseFor200) | The requested rule group
400 | [ApiResponseFor400](#get_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_rule_group.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_rule_group.ApiResponseFor500) | Internal exception

#### get_rule_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleGroupSingle**](../../models/RuleGroupSingle.md) |  | 


#### get_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_rule_group.ApiResponseFor500
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

# **list_rule_by_group**
<a id="list_rule_by_group"></a>
> RuleArray list_rule_by_group(id)

List rules in this rule group.

List rules in this rule group.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # List rules in this rule group.
        api_response = api_instance.list_rule_by_group(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->list_rule_by_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    query_params = {
        'page': 1,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # List rules in this rule group.
        api_response = api_instance.list_rule_by_group(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->list_rule_by_group: %s\n" % e)
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
200 | [ApiResponseFor200](#list_rule_by_group.ApiResponseFor200) | A list of rules.
400 | [ApiResponseFor400](#list_rule_by_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_rule_by_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#list_rule_by_group.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#list_rule_by_group.ApiResponseFor500) | Internal exception

#### list_rule_by_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleArray**](../../models/RuleArray.md) |  | 


#### list_rule_by_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### list_rule_by_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### list_rule_by_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### list_rule_by_group.ApiResponseFor500
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

# **list_rule_group**
<a id="list_rule_group"></a>
> RuleGroupArray list_rule_group()

List all rule groups.

List all rule groups.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.rule_group_array import RuleGroupArray
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # List all rule groups.
        api_response = api_instance.list_rule_group(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->list_rule_group: %s\n" % e)
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
200 | [ApiResponseFor200](#list_rule_group.ApiResponseFor200) | A list of rule groups.
400 | [ApiResponseFor400](#list_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#list_rule_group.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#list_rule_group.ApiResponseFor500) | Internal exception

#### list_rule_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleGroupArray**](../../models/RuleGroupArray.md) |  | 


#### list_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### list_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### list_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### list_rule_group.ApiResponseFor500
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

# **store_rule_group**
<a id="store_rule_group"></a>
> RuleGroupSingle store_rule_group(rule_group_store)

Store a new rule group.

Creates a new rule group. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.rule_group_store import RuleGroupStore
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = RuleGroupStore(
        active=True,
        description="Description of this rule group",
        order=4,
        title="Default rule group",
    )
    try:
        # Store a new rule group.
        api_response = api_instance.store_rule_group(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->store_rule_group: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    body = RuleGroupStore(
        active=True,
        description="Description of this rule group",
        order=4,
        title="Default rule group",
    )
    try:
        # Store a new rule group.
        api_response = api_instance.store_rule_group(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->store_rule_group: %s\n" % e)
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
[**RuleGroupStore**](../../models/RuleGroupStore.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleGroupStore**](../../models/RuleGroupStore.md) |  | 


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
200 | [ApiResponseFor200](#store_rule_group.ApiResponseFor200) | New rule group stored, result in response.
400 | [ApiResponseFor400](#store_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#store_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#store_rule_group.ApiResponseFor404) | Page not found
422 | [ApiResponseFor422](#store_rule_group.ApiResponseFor422) | Validation error. The body will have the exact details.
500 | [ApiResponseFor500](#store_rule_group.ApiResponseFor500) | Internal exception

#### store_rule_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleGroupSingle**](../../models/RuleGroupSingle.md) |  | 


#### store_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### store_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### store_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### store_rule_group.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


#### store_rule_group.ApiResponseFor500
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

# **test_rule_group**
<a id="test_rule_group"></a>
> TransactionArray test_rule_group(id)

Test which transactions would be hit by the rule group. No changes will be made.

Test which transactions would be hit by the rule group. No changes will be made. Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Test which transactions would be hit by the rule group. No changes will be made.
        api_response = api_instance.test_rule_group(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->test_rule_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    query_params = {
        'page': 1,
        'start': "Mon Sep 17 00:00:00 UTC 2018",
        'end': "Mon Sep 17 00:00:00 UTC 2018",
        'search_limit': 1,
        'triggered_limit': 1,
        'accounts[]': ["1","2","3"],
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Test which transactions would be hit by the rule group. No changes will be made.
        api_response = api_instance.test_rule_group(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->test_rule_group: %s\n" % e)
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
page | PageSchema | | optional
start | StartSchema | | optional
end | EndSchema | | optional
search_limit | SearchLimitSchema | | optional
triggered_limit | TriggeredLimitSchema | | optional
accounts[] | AccountsSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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

# SearchLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TriggeredLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#test_rule_group.ApiResponseFor200) | A list of transactions that would be changed by any of the rules of the rule group. No changes will be made.
400 | [ApiResponseFor400](#test_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#test_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#test_rule_group.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#test_rule_group.ApiResponseFor500) | Internal exception

#### test_rule_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionArray**](../../models/TransactionArray.md) |  | 


#### test_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### test_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### test_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### test_rule_group.ApiResponseFor500
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

# **update_rule_group**
<a id="update_rule_group"></a>
> RuleGroupSingle update_rule_group(idrule_group_update)

Update existing rule group.

Update existing rule group.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import rule_groups_api
from firefly_iii_client.model.rule_group_update import RuleGroupUpdate
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.not_found import NotFound
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
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
    api_instance = rule_groups_api.RuleGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    body = RuleGroupUpdate(
        active=True,
        description="Description of this rule group",
        order=4,
        title="Default rule group",
    )
    try:
        # Update existing rule group.
        api_response = api_instance.update_rule_group(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->update_rule_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    body = RuleGroupUpdate(
        active=True,
        description="Description of this rule group",
        order=4,
        title="Default rule group",
    )
    try:
        # Update existing rule group.
        api_response = api_instance.update_rule_group(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->update_rule_group: %s\n" % e)
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
[**RuleGroupUpdate**](../../models/RuleGroupUpdate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleGroupUpdate**](../../models/RuleGroupUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_rule_group.ApiResponseFor200) | Updated rule group stored, result in response
400 | [ApiResponseFor400](#update_rule_group.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_rule_group.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#update_rule_group.ApiResponseFor404) | Page not found
422 | [ApiResponseFor422](#update_rule_group.ApiResponseFor422) | Validation error. The body will have the exact details.
500 | [ApiResponseFor500](#update_rule_group.ApiResponseFor500) | Internal exception

#### update_rule_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleGroupSingle**](../../models/RuleGroupSingle.md) |  | 


#### update_rule_group.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### update_rule_group.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### update_rule_group.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### update_rule_group.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationError**](../../models/ValidationError.md) |  | 


#### update_rule_group.ApiResponseFor500
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

