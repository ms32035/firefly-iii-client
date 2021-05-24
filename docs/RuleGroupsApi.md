# firefly_iii_client.RuleGroupsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule_group**](RuleGroupsApi.md#delete_rule_group) | **DELETE** /api/v1/rule_groups/{id} | Delete a rule group.
[**fire_rule_group**](RuleGroupsApi.md#fire_rule_group) | **POST** /api/v1/rule_groups/{id}/trigger | Fire the rule group on your transactions.
[**get_rule_group**](RuleGroupsApi.md#get_rule_group) | **GET** /api/v1/rule_groups/{id} | Get a single rule group.
[**list_rule_by_group**](RuleGroupsApi.md#list_rule_by_group) | **GET** /api/v1/rule_groups/{id}/rules | List rules in this rule group.
[**list_rule_group**](RuleGroupsApi.md#list_rule_group) | **GET** /api/v1/rule_groups | List all rule groups.
[**store_rule_group**](RuleGroupsApi.md#store_rule_group) | **POST** /api/v1/rule_groups | Store a new rule group.
[**test_rule_group**](RuleGroupsApi.md#test_rule_group) | **GET** /api/v1/rule_groups/{id}/test | Test which transactions would be hit by the rule group. No changes will be made.
[**update_rule_group**](RuleGroupsApi.md#update_rule_group) | **PUT** /api/v1/rule_groups/{id} | Update existing rule group.


# **delete_rule_group**
> delete_rule_group(id)

Delete a rule group.

Delete a rule group.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    id = 1 # int | The ID of the rule group.

    # example passing only required values which don't have defaults set
    try:
        # Delete a rule group.
        api_instance.delete_rule_group(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->delete_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule group. |

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
**204** | Rule group deleted. |  -  |
**404** | No such rule group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fire_rule_group**
> fire_rule_group(id)

Fire the rule group on your transactions.

Fire the rule group on your transactions. Changes will be made by the rules in the rule group! Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    id = 1 # int | The ID of the rule group.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  (optional)
    accounts = ["1","2","3"] # [int] | Limit the triggering of the rule group to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fire the rule group on your transactions.
        api_instance.fire_rule_group(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->fire_rule_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fire the rule group on your transactions.
        api_instance.fire_rule_group(id, start=start, end=end, accounts=accounts)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->fire_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule group. |
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  | [optional]
 **accounts** | **[int]**| Limit the triggering of the rule group to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  | [optional]

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
**204** | The rules in the group are executed. Due to the setup of this function (asynchronous job execution) the result cannot be displayed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_group**
> RuleGroupSingle get_rule_group(id)

Get a single rule group.

Get a single rule group. This does not include the rules. For that, see below.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    id = 1 # int | The ID of the rule group.

    # example passing only required values which don't have defaults set
    try:
        # Get a single rule group.
        api_response = api_instance.get_rule_group(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->get_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule group. |

### Return type

[**RuleGroupSingle**](RuleGroupSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rule group |  -  |
**404** | Rule group not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_by_group**
> RuleArray list_rule_by_group(id)

List rules in this rule group.

List rules in this rule group.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from firefly_iii_client.model.rule_array import RuleArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    id = 1 # int | The ID of the rule group.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List rules in this rule group.
        api_response = api_instance.list_rule_by_group(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->list_rule_by_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List rules in this rule group.
        api_response = api_instance.list_rule_by_group(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->list_rule_by_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule group. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**RuleArray**](RuleArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_group**
> RuleGroupArray list_rule_group()

List all rule groups.

List all rule groups.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from firefly_iii_client.model.rule_group_array import RuleGroupArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    page = 1 # int | Page number. The default pagination is 50 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all rule groups.
        api_response = api_instance.list_rule_group(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->list_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50 | [optional]

### Return type

[**RuleGroupArray**](RuleGroupArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule groups. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_rule_group**
> RuleGroupSingle store_rule_group(rule_group_store)

Store a new rule group.

Creates a new rule group. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.rule_group_store import RuleGroupStore
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    rule_group_store = RuleGroupStore(
        active=True,
        description="Description of this rule group",
        order=4,
        title="Default rule group",
    ) # RuleGroupStore | JSON array or key=value pairs with the necessary rule group information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new rule group.
        api_response = api_instance.store_rule_group(rule_group_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->store_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_group_store** | [**RuleGroupStore**](RuleGroupStore.md)| JSON array or key&#x3D;value pairs with the necessary rule group information. See the model for the exact specifications. |

### Return type

[**RuleGroupSingle**](RuleGroupSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New rule group stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rule_group**
> TransactionArray test_rule_group(id)

Test which transactions would be hit by the rule group. No changes will be made.

Test which transactions would be hit by the rule group. No changes will be made. Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from firefly_iii_client.model.transaction_array import TransactionArray
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    id = 1 # int | The ID of the rule group.
    page = 1 # int | Page number. The default pagination is 50 items. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  (optional)
    search_limit = 1 # int | Maximum number of transactions Firefly III will try. Don't set this too high, or it will take Firefly III very long to run the test. I suggest a max of 200.  (optional)
    triggered_limit = 1 # int | Maximum number of transactions the rule group can actually trigger on, before Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the user's page size, because browsing to page 2 or 3 of a test result would fire the test again, making any navigation efforts very slow.  (optional)
    accounts = ["1","2","3"] # [int] | Limit the testing of the rule group to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Test which transactions would be hit by the rule group. No changes will be made.
        api_response = api_instance.test_rule_group(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->test_rule_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test which transactions would be hit by the rule group. No changes will be made.
        api_response = api_instance.test_rule_group(id, page=page, start=start, end=end, search_limit=search_limit, triggered_limit=triggered_limit, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->test_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule group. |
 **page** | **int**| Page number. The default pagination is 50 items. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  | [optional]
 **search_limit** | **int**| Maximum number of transactions Firefly III will try. Don&#39;t set this too high, or it will take Firefly III very long to run the test. I suggest a max of 200.  | [optional]
 **triggered_limit** | **int**| Maximum number of transactions the rule group can actually trigger on, before Firefly III stops. I would suggest setting this to 10 or 15. Don&#39;t go above the user&#39;s page size, because browsing to page 2 or 3 of a test result would fire the test again, making any navigation efforts very slow.  | [optional]
 **accounts** | **[int]**| Limit the testing of the rule group to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  | [optional]

### Return type

[**TransactionArray**](TransactionArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions that would be changed by any of the rules of the rule group. No changes will be made. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule_group**
> RuleGroupSingle update_rule_group(id, rule_group_update)

Update existing rule group.

Update existing rule group.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rule_groups_api
from firefly_iii_client.model.rule_group_update import RuleGroupUpdate
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rule_groups_api.RuleGroupsApi(api_client)
    id = 1 # int | The ID of the rule group.
    rule_group_update = RuleGroupUpdate(
        active=True,
        description="Description of this rule group",
        order=4,
        title="Default rule group",
    ) # RuleGroupUpdate | JSON array with updated rule group information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing rule group.
        api_response = api_instance.update_rule_group(id, rule_group_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RuleGroupsApi->update_rule_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule group. |
 **rule_group_update** | [**RuleGroupUpdate**](RuleGroupUpdate.md)| JSON array with updated rule group information. See the model for the exact specifications. |

### Return type

[**RuleGroupSingle**](RuleGroupSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated rule group stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

