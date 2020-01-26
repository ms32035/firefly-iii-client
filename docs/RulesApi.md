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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the rule.

try:
    # Delete an rule.
    api_instance.delete_rule(id)
except ApiException as e:
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
> fire_rule(id, start=start, end=end, accounts=accounts)

Fire the rule on your transactions.

Fire the rule group on your transactions. Changes will be made by the rules in the group! Limit the result if you want to.

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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the rule.
start = '2013-10-20' # date | A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  (optional)
end = '2013-10-20' # date | A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  (optional)
accounts = '1,2,3' # str | Limit the testing of the rule to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped.  (optional)

try:
    # Fire the rule on your transactions.
    api_instance.fire_rule(id, start=start, end=end, accounts=accounts)
except ApiException as e:
    print("Exception when calling RulesApi->fire_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule. | 
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the actions will be applied to. Both the start date and the end date must be present.  | [optional] 
 **accounts** | **str**| Limit the testing of the rule to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped.  | [optional] 

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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the object.X

try:
    # Get a single rule.
    api_response = api_instance.get_rule(id)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rule |  -  |
**404** | Rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule**
> RuleArray list_rule(page=page)

List all rules.

List all rules.

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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
page = 1 # int | Page number. The default pagination is 50. (optional)

try:
    # List all rules.
    api_response = api_instance.list_rule(page=page)
    pprint(api_response)
except ApiException as e:
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_rule**
> RuleSingle store_rule(rule)

Store a new rule

Creates a new rule. The data required can be submitted as a JSON body or as a list of parameters.

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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
rule = firefly_iii_client.Rule() # Rule | JSON array or key=value pairs with the necessary rule information. See the model for the exact specifications.

try:
    # Store a new rule
    api_response = api_instance.store_rule(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->store_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**Rule**](Rule.md)| JSON array or key&#x3D;value pairs with the necessary rule information. See the model for the exact specifications. | 

### Return type

[**RuleSingle**](RuleSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New rule stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rule**
> TransactionArray test_rule(id, page=page, start=start, end=end, search_limit=search_limit, triggered_limit=triggered_limit, accounts=accounts)

Test which transactions would be hit by the rule. No changes will be made.

Test which transactions would be hit by the rule. No changes will be made. Limit the result if you want to.

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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the rule.
page = 1 # int | Page number. The default pagination is 50 items. (optional)
start = '2013-10-20' # date | A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  (optional)
end = '2013-10-20' # date | A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  (optional)
search_limit = 56 # int | Maximum number of transactions Firefly III will try. Don't set this too high, or it will take Firefly III very long to run the test. I suggest a max of 200.  (optional)
triggered_limit = 56 # int | Maximum number of transactions the rule can actually trigger on, before Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the user's page size, because browsing to page 2 or 3 of a test result would fire the test again, making any navigation efforts very slow.  (optional)
accounts = '1,2,3' # str | Limit the testing of the rule to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped.  (optional)

try:
    # Test which transactions would be hit by the rule. No changes will be made.
    api_response = api_instance.test_rule(id, page=page, start=start, end=end, search_limit=search_limit, triggered_limit=triggered_limit, accounts=accounts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->test_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the rule. | 
 **page** | **int**| Page number. The default pagination is 50 items. | [optional] 
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  | [optional] 
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the transactions the test will be applied to. Both the start date and the end date must be present.  | [optional] 
 **search_limit** | **int**| Maximum number of transactions Firefly III will try. Don&#39;t set this too high, or it will take Firefly III very long to run the test. I suggest a max of 200.  | [optional] 
 **triggered_limit** | **int**| Maximum number of transactions the rule can actually trigger on, before Firefly III stops. I would suggest setting this to 10 or 15. Don&#39;t go above the user&#39;s page size, because browsing to page 2 or 3 of a test result would fire the test again, making any navigation efforts very slow.  | [optional] 
 **accounts** | **str**| Limit the testing of the rule to these asset accounts. Only asset accounts will be accepted. Other types will be silently dropped.  | [optional] 

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
**200** | A list of transactions that would be changed by the rule. No changes will be made. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> RuleSingle update_rule(id, rule)

Update existing rule.

Update existing rule.

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
api_instance = firefly_iii_client.RulesApi(firefly_iii_client.ApiClient(configuration))
id = 1 # int | The ID of the object.X
rule = firefly_iii_client.Rule() # Rule | JSON array with updated rule information. See the model for the exact specifications.

try:
    # Update existing rule.
    api_response = api_instance.update_rule(id, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the object.X | 
 **rule** | [**Rule**](Rule.md)| JSON array with updated rule information. See the model for the exact specifications. | 

### Return type

[**RuleSingle**](RuleSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated rule stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

