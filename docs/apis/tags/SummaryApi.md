<a id="__pageTop"></a>
# firefly_iii_client.apis.tags.summary_api.SummaryApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_summary**](#get_basic_summary) | **get** /v1/summary/basic | Returns basic sums of the users data.

# **get_basic_summary**
<a id="get_basic_summary"></a>
> BasicSummary get_basic_summary(startend)

Returns basic sums of the users data.

Returns basic sums of the users data, like the net worth, spent and earned amounts. It is multi-currency, and is used in Firefly III to populate the dashboard. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import summary_api
from firefly_iii_client.model.basic_summary import BasicSummary
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
    api_instance = summary_api.SummaryApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'start': "1970-01-01",
        'end': "1970-01-01",
    }
    header_params = {
    }
    try:
        # Returns basic sums of the users data.
        api_response = api_instance.get_basic_summary(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SummaryApi->get_basic_summary: %s\n" % e)

    # example passing only optional values
    query_params = {
        'start': "1970-01-01",
        'end': "1970-01-01",
        'currency_code': "currency_code_example",
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns basic sums of the users data.
        api_response = api_instance.get_basic_summary(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling SummaryApi->get_basic_summary: %s\n" % e)
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
start | StartSchema | | 
end | EndSchema | | 
currency_code | CurrencyCodeSchema | | optional


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

# CurrencyCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_basic_summary.ApiResponseFor200) | An array of sums. It depends on the user what you can expect to get back, so please try this out on the demo site.
400 | [ApiResponseFor400](#get_basic_summary.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_basic_summary.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_basic_summary.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_basic_summary.ApiResponseFor500) | Internal exception

#### get_basic_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**BasicSummary**](../../models/BasicSummary.md) |  | 


#### get_basic_summary.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_basic_summary.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_basic_summary.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_basic_summary.ApiResponseFor500
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

