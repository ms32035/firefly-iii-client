# firefly_iii_client.AutocompleteApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_ac**](AutocompleteApi.md#get_accounts_ac) | **GET** /api/v1/autocomplete/accounts | All accounts of the user returned in a basic auto-complete array.
[**get_bills_ac**](AutocompleteApi.md#get_bills_ac) | **GET** /api/v1/autocomplete/bills | All bills of the user returned in a basic auto-complete array.
[**get_budgets_ac**](AutocompleteApi.md#get_budgets_ac) | **GET** /api/v1/autocomplete/budgets | All budgets of the user returned in a basic auto-complete array.
[**get_categories_ac**](AutocompleteApi.md#get_categories_ac) | **GET** /api/v1/autocomplete/categories | All categories of the user returned in a basic auto-complete array.
[**get_currencies_ac**](AutocompleteApi.md#get_currencies_ac) | **GET** /api/v1/autocomplete/currencies | All currencies of the user returned in a basic auto-complete array.
[**get_currencies_code_ac**](AutocompleteApi.md#get_currencies_code_ac) | **GET** /api/v1/autocomplete/currencies-with-code | All currencies of the user returned in a basic auto-complete array.
[**get_object_groups_ac**](AutocompleteApi.md#get_object_groups_ac) | **GET** /api/v1/autocomplete/object-groups | All object groups of the user returned in a basic auto-complete array.
[**get_rule_groups_ac**](AutocompleteApi.md#get_rule_groups_ac) | **GET** /api/v1/autocomplete/rule-groups | All rule groups of the user returned in a basic auto-complete array.
[**get_rules_ac**](AutocompleteApi.md#get_rules_ac) | **GET** /api/v1/autocomplete/rules | All rules of the user returned in a basic auto-complete array.
[**get_tag_ac**](AutocompleteApi.md#get_tag_ac) | **GET** /api/v1/autocomplete/tags | All tags of the user returned in a basic auto-complete array.
[**get_transaction_types_ac**](AutocompleteApi.md#get_transaction_types_ac) | **GET** /api/v1/autocomplete/transaction-types | All transaction types returned in a basic auto-complete array. English only.
[**get_transactions_ac**](AutocompleteApi.md#get_transactions_ac) | **GET** /api/v1/autocomplete/transactions | All transaction descriptions of the user returned in a basic auto-complete array.
[**get_transactions_idac**](AutocompleteApi.md#get_transactions_idac) | **GET** /api/v1/autocomplete/transactions-with-id | All transactions, complemented with their ID, of the user returned in a basic auto-complete array.


# **get_accounts_ac**
> list[AutocompleteAccount] get_accounts_ac(query=query, limit=limit, date=date, type=type)

All accounts of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)
date = '2020-09-17' # str | For asset accounts, returns the balance on this date. (optional)
type = firefly_iii_client.AccountTypeFilter() # AccountTypeFilter | Optional filter on the account type(s) returned (optional)

    try:
        # All accounts of the user returned in a basic auto-complete array.
        api_response = api_instance.get_accounts_ac(query=query, limit=limit, date=date, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_accounts_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 
 **date** | **str**| For asset accounts, returns the balance on this date. | [optional] 
 **type** | [**AccountTypeFilter**](.md)| Optional filter on the account type(s) returned | [optional] 

### Return type

[**list[AutocompleteAccount]**](AutocompleteAccount.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bills_ac**
> list[AutocompleteBill] get_bills_ac(query=query, limit=limit)

All bills of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All bills of the user returned in a basic auto-complete array.
        api_response = api_instance.get_bills_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_bills_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteBill]**](AutocompleteBill.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets_ac**
> list[AutocompleteBudget] get_budgets_ac(query=query, limit=limit)

All budgets of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All budgets of the user returned in a basic auto-complete array.
        api_response = api_instance.get_budgets_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_budgets_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteBudget]**](AutocompleteBudget.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of budgets with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_ac**
> list[AutocompleteCategory] get_categories_ac(query=query, limit=limit)

All categories of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All categories of the user returned in a basic auto-complete array.
        api_response = api_instance.get_categories_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_categories_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteCategory]**](AutocompleteCategory.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of categories with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_ac**
> list[AutocompleteCurrency] get_currencies_ac(query=query, limit=limit)

All currencies of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All currencies of the user returned in a basic auto-complete array.
        api_response = api_instance.get_currencies_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_currencies_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteCurrency]**](AutocompleteCurrency.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_code_ac**
> list[AutocompleteCurrencyCode] get_currencies_code_ac(query=query, limit=limit)

All currencies of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All currencies of the user returned in a basic auto-complete array.
        api_response = api_instance.get_currencies_code_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_currencies_code_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteCurrencyCode]**](AutocompleteCurrencyCode.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of currencies with very basic information and the currency code between brackets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups_ac**
> list[AutocompleteObjectGroup] get_object_groups_ac(query=query, limit=limit)

All object groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All object groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_object_groups_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_object_groups_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteObjectGroup]**](AutocompleteObjectGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of object groups with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_groups_ac**
> list[AutocompleteRuleGroup] get_rule_groups_ac(query=query, limit=limit)

All rule groups of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All rule groups of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rule_groups_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_rule_groups_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteRuleGroup]**](AutocompleteRuleGroup.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule groups with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_ac**
> list[AutocompleteRule] get_rules_ac(query=query, limit=limit)

All rules of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All rules of the user returned in a basic auto-complete array.
        api_response = api_instance.get_rules_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_rules_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteRule]**](AutocompleteRule.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_ac**
> list[AutocompleteTag] get_tag_ac(query=query, limit=limit)

All tags of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All tags of the user returned in a basic auto-complete array.
        api_response = api_instance.get_tag_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_tag_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteTag]**](AutocompleteTag.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tags with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_types_ac**
> list[AutocompleteTransactionType] get_transaction_types_ac(query=query, limit=limit)

All transaction types returned in a basic auto-complete array. English only.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All transaction types returned in a basic auto-complete array. English only.
        api_response = api_instance.get_transaction_types_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_transaction_types_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteTransactionType]**](AutocompleteTransactionType.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction types with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_ac**
> list[AutocompleteTransaction] get_transactions_ac(query=query, limit=limit)

All transaction descriptions of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All transaction descriptions of the user returned in a basic auto-complete array.
        api_response = api_instance.get_transactions_ac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_transactions_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteTransaction]**](AutocompleteTransaction.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction descriptions with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_idac**
> list[AutocompleteTransactionID] get_transactions_idac(query=query, limit=limit)

All transactions, complemented with their ID, of the user returned in a basic auto-complete array.

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
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
    api_instance = firefly_iii_client.AutocompleteApi(api_client)
    query = 'str' # str | The autocomplete search query. (optional)
limit = 10 # int | The autocomplete number of items returned (optional)

    try:
        # All transactions, complemented with their ID, of the user returned in a basic auto-complete array.
        api_response = api_instance.get_transactions_idac(query=query, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->get_transactions_idac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The autocomplete search query. | [optional] 
 **limit** | **int**| The autocomplete number of items returned | [optional] 

### Return type

[**list[AutocompleteTransactionID]**](AutocompleteTransactionID.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions with very basic information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

