# firefly_iii_client.RulesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule**](RulesApi.md#delete_rule) | **DELETE** /api/v1/rules/{id} | Delete an rule.
[**fire_rule**](RulesApi.md#fire_rule) | **POST** /api/v1/rules/{id}/trigger | Fire the rule on your transactions.
[**get_rule**](RulesApi.md#get_rule) | **GET** /api/v1/rules/{id} | Get a single rule.
[**list_rule**](RulesApi.md#list_rule) | **GET** /api/v1/rules | List all rules.
[**store_rule**](RulesApi.md#store_rule) | **POST** /api/v1/rules | Store a new rule
[**test_rule**](RulesApi.md#test_rule) | **GET** /api/v1/rules/{id}/test | Test which transactions would be hit by the rule. No changes will be made.
[**update_rule**](RulesApi.md#update_rule) | **PUT** /api/v1/rules/{id} | Update existing rule.


# **delete_rule**
> delete_rule(id)

Delete an rule.

Delete an rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
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
    api_instance = rules_api.RulesApi(api_client)
    id = 1 # int | The ID of the rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete an rule.
        api_instance.delete_rule(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->delete_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule. |

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
**204** | Rule deleted. |  -  |
**404** | No such rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fire_rule**
> fire_rule(id)

Fire the rule on your transactions.

Fire the rule group on your transactions. Changes will be made by the rules in the group! Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
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
    api_instance = rules_api.RulesApi(api_client)
    id = 1 # int | The ID of the rule.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. If the start date is not present, it will be set to one year ago. If you use this field, both the start date and the end date must be present.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. If the end date is not present, it will be set to today. If you use this field, both the start date and the end date must be present.  (optional)
    accounts = ["1","2","3"] # [int] | Limit the triggering of the rule to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fire the rule on your transactions.
        api_instance.fire_rule(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->fire_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fire the rule on your transactions.
        api_instance.fire_rule(id, start=start, end=end, accounts=accounts)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->fire_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule. |
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. If the start date is not present, it will be set to one year ago. If you use this field, both the start date and the end date must be present.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. If the end date is not present, it will be set to today. If you use this field, both the start date and the end date must be present.  | [optional]
 **accounts** | **[int]**| Limit the triggering of the rule to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  | [optional]

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

# **get_rule**
> RuleSingle get_rule(id)

Get a single rule.

Get a single rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
from firefly_iii_client.model.rule_single import RuleSingle
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
    api_instance = rules_api.RulesApi(api_client)
    id = 1 # int | The ID of the object.X

    # example passing only required values which don't have defaults set
    try:
        # Get a single rule.
        api_response = api_instance.get_rule(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->get_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the object.X |

### Return type

[**RuleSingle**](RuleSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rule |  -  |
**404** | Rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule**
> RuleArray list_rule()

List all rules.

List all rules.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
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
    api_instance = rules_api.RulesApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all rules.
        api_response = api_instance.list_rule(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->list_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | A list of rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_rule**
> RuleSingle store_rule(rule_store)

Store a new rule

Creates a new rule. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
from firefly_iii_client.model.rule_store import RuleStore
from firefly_iii_client.model.rule_single import RuleSingle
from firefly_iii_client.model.validation_error import ValidationError
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
    api_instance = rules_api.RulesApi(api_client)
    rule_store = RuleStore(
        actions=[
            RuleActionStore(
                active=True,
                order=5,
                stop_processing=False,
                type="set_category",
                value="Daily groceries",
            ),
        ],
        active=True,
        description="First rule description",
        order=5,
        rule_group_id="81",
        rule_group_title="New rule group",
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger="store-journal",
        triggers=[
            RuleTriggerStore(
                active=True,
                order=5,
                stop_processing=False,
                type="user_action",
                value="tag1",
            ),
        ],
    ) # RuleStore | JSON array or key=value pairs with the necessary rule information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new rule
        api_response = api_instance.store_rule(rule_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->store_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_store** | [**RuleStore**](RuleStore.md)| JSON array or key&#x3D;value pairs with the necessary rule information. See the model for the exact specifications. |

### Return type

[**RuleSingle**](RuleSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New rule stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rule**
> TransactionArray test_rule(id)

Test which transactions would be hit by the rule. No changes will be made.

Test which transactions would be hit by the rule. No changes will be made. Limit the result if you want to.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
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
    api_instance = rules_api.RulesApi(api_client)
    id = 1 # int | The ID of the rule.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  (optional)
    accounts = ["1","2","3"] # [int] | Limit the testing of the rule to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Test which transactions would be hit by the rule. No changes will be made.
        api_response = api_instance.test_rule(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test which transactions would be hit by the rule. No changes will be made.
        api_response = api_instance.test_rule(id, start=start, end=end, accounts=accounts)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule. |
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  | [optional]
 **accounts** | **[int]**| Limit the testing of the rule to these asset accounts or liabilities. Only asset accounts and liabilities will be accepted. Other types will be silently dropped.  | [optional]

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
**200** | A list of transactions that would be changed by the rule. No changes will be made. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> RuleSingle update_rule(id, rule_update)

Update existing rule.

Update existing rule.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
from firefly_iii_client.model.rule_single import RuleSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.rule_update import RuleUpdate
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
    api_instance = rules_api.RulesApi(api_client)
    id = 1 # int | The ID of the object.X
    rule_update = RuleUpdate(
        actions=[
            RuleActionUpdate(
                active=True,
                order=5,
                stop_processing=False,
                type="set_category",
                value="Daily groceries",
            ),
        ],
        active=True,
        description="First rule description",
        order=5,
        rule_group_id="81",
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger="store-journal",
        triggers=[
            RuleTriggerUpdate(
                active=True,
                order=5,
                stop_processing=False,
                type="user_action",
                value="tag1",
            ),
        ],
    ) # RuleUpdate | JSON array with updated rule information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing rule.
        api_response = api_instance.update_rule(id, rule_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->update_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the object.X |
 **rule_update** | [**RuleUpdate**](RuleUpdate.md)| JSON array with updated rule information. See the model for the exact specifications. |

### Return type

[**RuleSingle**](RuleSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated rule stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

