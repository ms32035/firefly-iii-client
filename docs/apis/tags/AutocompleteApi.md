<a id="__pageTop"></a>
# firefly_iii_client.apis.tags.autocomplete_api.AutocompleteApi

All URIs are relative to *https://demo.firefly-iii.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_ac**](#get_accounts_ac) | **get** /v1/autocomplete/accounts | Returns all accounts of the user returned in a basic auto-complete array.
[**get_bills_ac**](#get_bills_ac) | **get** /v1/autocomplete/bills | Returns all bills of the user returned in a basic auto-complete array.
[**get_budgets_ac**](#get_budgets_ac) | **get** /v1/autocomplete/budgets | Returns all budgets of the user returned in a basic auto-complete array.
[**get_categories_ac**](#get_categories_ac) | **get** /v1/autocomplete/categories | Returns all categories of the user returned in a basic auto-complete array.
[**get_currencies_ac**](#get_currencies_ac) | **get** /v1/autocomplete/currencies | Returns all currencies of the user returned in a basic auto-complete array.
[**get_currencies_code_ac**](#get_currencies_code_ac) | **get** /v1/autocomplete/currencies-with-code | Returns all currencies of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.
[**get_object_groups_ac**](#get_object_groups_ac) | **get** /v1/autocomplete/object-groups | Returns all object groups of the user returned in a basic auto-complete array.
[**get_piggies_ac**](#get_piggies_ac) | **get** /v1/autocomplete/piggy-banks | Returns all piggy banks of the user returned in a basic auto-complete array.
[**get_piggies_balance_ac**](#get_piggies_balance_ac) | **get** /v1/autocomplete/piggy-banks-with-balance | Returns all piggy banks of the user returned in a basic auto-complete array complemented with balance information.
[**get_recurring_ac**](#get_recurring_ac) | **get** /v1/autocomplete/recurring | Returns all recurring transactions of the user returned in a basic auto-complete array.
[**get_rule_groups_ac**](#get_rule_groups_ac) | **get** /v1/autocomplete/rule-groups | Returns all rule groups of the user returned in a basic auto-complete array.
[**get_rules_ac**](#get_rules_ac) | **get** /v1/autocomplete/rules | Returns all rules of the user returned in a basic auto-complete array.
[**get_tag_ac**](#get_tag_ac) | **get** /v1/autocomplete/tags | Returns all tags of the user returned in a basic auto-complete array.
[**get_transaction_types_ac**](#get_transaction_types_ac) | **get** /v1/autocomplete/transaction-types | Returns all transaction types returned in a basic auto-complete array. English only.
[**get_transactions_ac**](#get_transactions_ac) | **get** /v1/autocomplete/transactions | Returns all transaction descriptions of the user returned in a basic auto-complete array.
[**get_transactions_idac**](#get_transactions_idac) | **get** /v1/autocomplete/transactions-with-id | Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.

# **get_accounts_ac**
<a id="get_accounts_ac"></a>
> AutocompleteAccountArray get_accounts_ac()

Returns all accounts of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.autocomplete_account_array import AutocompleteAccountArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
        'date': "2020-09-17",
        'types': [
        AccountTypeFilter("all")
    ],
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all accounts of the user returned in a basic auto-complete array.
        api_response = api_instance.get_accounts_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_accounts_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional
date | DateSchema | | optional
types | TypesSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountTypeFilter**]({{complexTypePrefix}}AccountTypeFilter.md) | [**AccountTypeFilter**]({{complexTypePrefix}}AccountTypeFilter.md) | [**AccountTypeFilter**]({{complexTypePrefix}}AccountTypeFilter.md) |  | 

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
200 | [ApiResponseFor200](#get_accounts_ac.ApiResponseFor200) | A list of accounts with very basic information.
400 | [ApiResponseFor400](#get_accounts_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_accounts_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_accounts_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_accounts_ac.ApiResponseFor500) | Internal exception

#### get_accounts_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteAccountArray**](../../models/AutocompleteAccountArray.md) |  | 


#### get_accounts_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_accounts_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_accounts_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_accounts_ac.ApiResponseFor500
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

# **get_bills_ac**
<a id="get_bills_ac"></a>
> AutocompleteBillArray get_bills_ac()

Returns all bills of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.autocomplete_bill_array import AutocompleteBillArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all bills of the user returned in a basic auto-complete array.
        api_response = api_instance.get_bills_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_bills_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_bills_ac.ApiResponseFor200) | A list of bills with very basic information.
400 | [ApiResponseFor400](#get_bills_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_bills_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_bills_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_bills_ac.ApiResponseFor500) | Internal exception

#### get_bills_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteBillArray**](../../models/AutocompleteBillArray.md) |  | 


#### get_bills_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_bills_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_bills_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_bills_ac.ApiResponseFor500
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

# **get_budgets_ac**
<a id="get_budgets_ac"></a>
> AutocompleteBudgetArray get_budgets_ac()

Returns all budgets of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_budget_array import AutocompleteBudgetArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all budgets of the user returned in a basic auto-complete array.
        api_response = api_instance.get_budgets_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_budgets_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_budgets_ac.ApiResponseFor200) | A list of budgets with very basic information.
400 | [ApiResponseFor400](#get_budgets_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_budgets_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_budgets_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_budgets_ac.ApiResponseFor500) | Internal exception

#### get_budgets_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteBudgetArray**](../../models/AutocompleteBudgetArray.md) |  | 


#### get_budgets_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_budgets_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_budgets_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_budgets_ac.ApiResponseFor500
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

# **get_categories_ac**
<a id="get_categories_ac"></a>
> AutocompleteCategoryArray get_categories_ac()

Returns all categories of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_category_array import AutocompleteCategoryArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all categories of the user returned in a basic auto-complete array.
        api_response = api_instance.get_categories_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_categories_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_categories_ac.ApiResponseFor200) | A list of categories with very basic information.
400 | [ApiResponseFor400](#get_categories_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_categories_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_categories_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_categories_ac.ApiResponseFor500) | Internal exception

#### get_categories_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteCategoryArray**](../../models/AutocompleteCategoryArray.md) |  | 


#### get_categories_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_categories_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_categories_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_categories_ac.ApiResponseFor500
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

# **get_currencies_ac**
<a id="get_currencies_ac"></a>
> AutocompleteCurrencyArray get_currencies_ac()

Returns all currencies of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_currency_array import AutocompleteCurrencyArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all currencies of the user returned in a basic auto-complete array.
        api_response = api_instance.get_currencies_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_currencies_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_currencies_ac.ApiResponseFor200) | A list of currencies with very basic information.
400 | [ApiResponseFor400](#get_currencies_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_currencies_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_currencies_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_currencies_ac.ApiResponseFor500) | Internal exception

#### get_currencies_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteCurrencyArray**](../../models/AutocompleteCurrencyArray.md) |  | 


#### get_currencies_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_currencies_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_currencies_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_currencies_ac.ApiResponseFor500
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

# **get_currencies_code_ac**
<a id="get_currencies_code_ac"></a>
> AutocompleteCurrencyCodeArray get_currencies_code_ac()

Returns all currencies of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_currency_code_array import AutocompleteCurrencyCodeArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all currencies of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.
        api_response = api_instance.get_currencies_code_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_currencies_code_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_currencies_code_ac.ApiResponseFor200) | A list of currencies with very basic information and the currency code between brackets. This endpoint is DEPRECATED and I suggest you DO NOT use it.
400 | [ApiResponseFor400](#get_currencies_code_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_currencies_code_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_currencies_code_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_currencies_code_ac.ApiResponseFor500) | Internal exception

#### get_currencies_code_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteCurrencyCodeArray**](../../models/AutocompleteCurrencyCodeArray.md) |  | 


#### get_currencies_code_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_currencies_code_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_currencies_code_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_currencies_code_ac.ApiResponseFor500
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

# **get_object_groups_ac**
<a id="get_object_groups_ac"></a>
> AutocompleteObjectGroupArray get_object_groups_ac()

Returns all object groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_object_group_array import AutocompleteObjectGroupArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all object groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_object_groups_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_object_groups_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_object_groups_ac.ApiResponseFor200) | A list of object groups with very basic information.
400 | [ApiResponseFor400](#get_object_groups_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_object_groups_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_object_groups_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_object_groups_ac.ApiResponseFor500) | Internal exception

#### get_object_groups_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteObjectGroupArray**](../../models/AutocompleteObjectGroupArray.md) |  | 


#### get_object_groups_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_object_groups_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_object_groups_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_object_groups_ac.ApiResponseFor500
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

# **get_piggies_ac**
<a id="get_piggies_ac"></a>
> AutocompletePiggyArray get_piggies_ac()

Returns all piggy banks of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.internal_exception import InternalException
from firefly_iii_client.model.autocomplete_piggy_array import AutocompletePiggyArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all piggy banks of the user returned in a basic auto-complete array.
        api_response = api_instance.get_piggies_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_piggies_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_piggies_ac.ApiResponseFor200) | A list of piggy banks with very basic information.
400 | [ApiResponseFor400](#get_piggies_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_piggies_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_piggies_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_piggies_ac.ApiResponseFor500) | Internal exception

#### get_piggies_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompletePiggyArray**](../../models/AutocompletePiggyArray.md) |  | 


#### get_piggies_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_piggies_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_piggies_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_piggies_ac.ApiResponseFor500
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

# **get_piggies_balance_ac**
<a id="get_piggies_balance_ac"></a>
> AutocompletePiggyBalanceArray get_piggies_balance_ac()

Returns all piggy banks of the user returned in a basic auto-complete array complemented with balance information.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_piggy_balance_array import AutocompletePiggyBalanceArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all piggy banks of the user returned in a basic auto-complete array complemented with balance information.
        api_response = api_instance.get_piggies_balance_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_piggies_balance_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_piggies_balance_ac.ApiResponseFor200) | A list of piggy banks with very basic balance information.
400 | [ApiResponseFor400](#get_piggies_balance_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_piggies_balance_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_piggies_balance_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_piggies_balance_ac.ApiResponseFor500) | Internal exception

#### get_piggies_balance_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompletePiggyBalanceArray**](../../models/AutocompletePiggyBalanceArray.md) |  | 


#### get_piggies_balance_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_piggies_balance_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_piggies_balance_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_piggies_balance_ac.ApiResponseFor500
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

# **get_recurring_ac**
<a id="get_recurring_ac"></a>
> AutocompleteRecurrenceArray get_recurring_ac()

Returns all recurring transactions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_recurrence_array import AutocompleteRecurrenceArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all recurring transactions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_recurring_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_recurring_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_recurring_ac.ApiResponseFor200) | A list of recurring transactions with very basic information.
400 | [ApiResponseFor400](#get_recurring_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_recurring_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_recurring_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_recurring_ac.ApiResponseFor500) | Internal exception

#### get_recurring_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteRecurrenceArray**](../../models/AutocompleteRecurrenceArray.md) |  | 


#### get_recurring_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_recurring_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_recurring_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_recurring_ac.ApiResponseFor500
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

# **get_rule_groups_ac**
<a id="get_rule_groups_ac"></a>
> AutocompleteRuleGroupArray get_rule_groups_ac()

Returns all rule groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_rule_group_array import AutocompleteRuleGroupArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all rule groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rule_groups_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_rule_groups_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_rule_groups_ac.ApiResponseFor200) | A list of rule groups with very basic information.
400 | [ApiResponseFor400](#get_rule_groups_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_rule_groups_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_rule_groups_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_rule_groups_ac.ApiResponseFor500) | Internal exception

#### get_rule_groups_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteRuleGroupArray**](../../models/AutocompleteRuleGroupArray.md) |  | 


#### get_rule_groups_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_rule_groups_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_rule_groups_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_rule_groups_ac.ApiResponseFor500
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

# **get_rules_ac**
<a id="get_rules_ac"></a>
> AutocompleteRuleArray get_rules_ac()

Returns all rules of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_rule_array import AutocompleteRuleArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all rules of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rules_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_rules_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_rules_ac.ApiResponseFor200) | A list of rules with very basic information.
400 | [ApiResponseFor400](#get_rules_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_rules_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_rules_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_rules_ac.ApiResponseFor500) | Internal exception

#### get_rules_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteRuleArray**](../../models/AutocompleteRuleArray.md) |  | 


#### get_rules_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_rules_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_rules_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_rules_ac.ApiResponseFor500
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

# **get_tag_ac**
<a id="get_tag_ac"></a>
> AutocompleteTagArray get_tag_ac()

Returns all tags of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.unauthenticated import Unauthenticated
from firefly_iii_client.model.bad_request import BadRequest
from firefly_iii_client.model.autocomplete_tag_array import AutocompleteTagArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all tags of the user returned in a basic auto-complete array.
        api_response = api_instance.get_tag_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_tag_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_tag_ac.ApiResponseFor200) | A list of tags with very basic information.
400 | [ApiResponseFor400](#get_tag_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_tag_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_tag_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_tag_ac.ApiResponseFor500) | Internal exception

#### get_tag_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteTagArray**](../../models/AutocompleteTagArray.md) |  | 


#### get_tag_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_tag_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_tag_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_tag_ac.ApiResponseFor500
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

# **get_transaction_types_ac**
<a id="get_transaction_types_ac"></a>
> AutocompleteTransactionTypeArray get_transaction_types_ac()

Returns all transaction types returned in a basic auto-complete array. English only.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_transaction_type_array import AutocompleteTransactionTypeArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all transaction types returned in a basic auto-complete array. English only.
        api_response = api_instance.get_transaction_types_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_transaction_types_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_transaction_types_ac.ApiResponseFor200) | A list of transaction types with very basic information.
400 | [ApiResponseFor400](#get_transaction_types_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_transaction_types_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_transaction_types_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_transaction_types_ac.ApiResponseFor500) | Internal exception

#### get_transaction_types_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteTransactionTypeArray**](../../models/AutocompleteTransactionTypeArray.md) |  | 


#### get_transaction_types_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_transaction_types_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_transaction_types_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_transaction_types_ac.ApiResponseFor500
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

# **get_transactions_ac**
<a id="get_transactions_ac"></a>
> AutocompleteTransactionArray get_transactions_ac()

Returns all transaction descriptions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_transaction_array import AutocompleteTransactionArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all transaction descriptions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_transactions_ac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_transactions_ac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_transactions_ac.ApiResponseFor200) | A list of transaction descriptions with very basic information.
400 | [ApiResponseFor400](#get_transactions_ac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_transactions_ac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_transactions_ac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_transactions_ac.ApiResponseFor500) | Internal exception

#### get_transactions_ac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteTransactionArray**](../../models/AutocompleteTransactionArray.md) |  | 


#### get_transactions_ac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_transactions_ac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_transactions_ac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_transactions_ac.ApiResponseFor500
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

# **get_transactions_idac**
<a id="get_transactions_idac"></a>
> AutocompleteTransactionIDArray get_transactions_idac()

Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import firefly_iii_client
from firefly_iii_client.apis.tags import autocomplete_api
from firefly_iii_client.model.autocomplete_transaction_id_array import AutocompleteTransactionIDArray
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
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example passing only optional values
    query_params = {
        'query': "string",
        'limit': 10,
    }
    header_params = {
        'X-Trace-Id': "X-Trace-Id_example",
    }
    try:
        # Returns all transactions, complemented with their ID, of the user returned in a basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT use it.
        api_response = api_instance.get_transactions_idac(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AutocompleteApi->get_transactions_idac: %s\n" % e)
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
query | QuerySchema | | optional
limit | LimitSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

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
200 | [ApiResponseFor200](#get_transactions_idac.ApiResponseFor200) | A list of transactions with very basic information. This endpoint is DEPRECATED and I suggest you DO NOT use it.
400 | [ApiResponseFor400](#get_transactions_idac.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_transactions_idac.ApiResponseFor401) | Unauthenticated
404 | [ApiResponseFor404](#get_transactions_idac.ApiResponseFor404) | Page not found
500 | [ApiResponseFor500](#get_transactions_idac.ApiResponseFor500) | Internal exception

#### get_transactions_idac.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteTransactionIDArray**](../../models/AutocompleteTransactionIDArray.md) |  | 


#### get_transactions_idac.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### get_transactions_idac.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthenticated**](../../models/Unauthenticated.md) |  | 


#### get_transactions_idac.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_transactions_idac.ApiResponseFor500
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

