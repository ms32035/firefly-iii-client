# firefly_iii_client.AccountsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /api/v1/accounts/{id} | Permanently delete account.
[**get_account**](AccountsApi.md#get_account) | **GET** /api/v1/accounts/{id} | Get single account.
[**list_account**](AccountsApi.md#list_account) | **GET** /api/v1/accounts | List all accounts.
[**list_attachment_by_account**](AccountsApi.md#list_attachment_by_account) | **GET** /api/v1/accounts/{id}/attachments | Lists all attachments.
[**list_piggy_bank_by_account**](AccountsApi.md#list_piggy_bank_by_account) | **GET** /api/v1/accounts/{id}/piggy_banks | List all piggy banks related to the account.
[**list_transaction_by_account**](AccountsApi.md#list_transaction_by_account) | **GET** /api/v1/accounts/{id}/transactions | List all transactions related to the account.
[**store_account**](AccountsApi.md#store_account) | **POST** /api/v1/accounts | Create new account.
[**update_account**](AccountsApi.md#update_account) | **PUT** /api/v1/accounts/{id} | Update existing account.


# **delete_account**
> delete_account(id)

Permanently delete account.

Will permanently delete an account. Any associated transactions and piggy banks are ALSO deleted. Cannot be recovered from. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = 1 # int | The ID of the account.

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete account.
        api_instance.delete_account(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->delete_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. |

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
**204** | Account deleted |  -  |
**404** | No such account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountSingle get_account(id)

Get single account.

Returns a single account by its ID. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.account_single import AccountSingle
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = 1 # int | The ID of the account.
    date = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get single account.
        api_response = api_instance.get_account(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get single account.
        api_response = api_instance.get_account(id, date=date)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. |
 **date** | **date**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional]

### Return type

[**AccountSingle**](AccountSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested account |  -  |
**404** | Account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account**
> AccountArray list_account()

List all accounts.

This endpoint returns a list of all the accounts owned by the authenticated user. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.account_array import AccountArray
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
    api_instance = accounts_api.AccountsApi(api_client)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    date = dateutil_parser('1970-01-01').date() # date | A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account's balance on that day.  (optional)
    type = AccountTypeFilter("all") # AccountTypeFilter | Optional filter on the account type(s) returned (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all accounts.
        api_response = api_instance.list_account(page=page, date=date, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]
 **date** | **date**| A date formatted YYYY-MM-DD. When added to the request, Firefly III will show the account&#39;s balance on that day.  | [optional]
 **type** | **AccountTypeFilter**| Optional filter on the account type(s) returned | [optional]

### Return type

[**AccountArray**](AccountArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_account**
> AttachmentArray list_attachment_by_account(id)

Lists all attachments.

Lists all attachments.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.attachment_array import AttachmentArray
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = 1 # int | The ID of the account.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lists all attachments.
        api_response = api_instance.list_attachment_by_account(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_attachment_by_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all attachments.
        api_response = api_instance.list_attachment_by_account(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_attachment_by_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**AttachmentArray**](AttachmentArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of attachments |  -  |
**404** | No such account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_piggy_bank_by_account**
> PiggyBankArray list_piggy_bank_by_account(id)

List all piggy banks related to the account.

This endpoint returns a list of all the piggy banks connected to the account. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.piggy_bank_array import PiggyBankArray
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = 1 # int | The ID of the account.
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all piggy banks related to the account.
        api_response = api_instance.list_piggy_bank_by_account(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_piggy_bank_by_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all piggy banks related to the account.
        api_response = api_instance.list_piggy_bank_by_account(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_piggy_bank_by_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. |
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]

### Return type

[**PiggyBankArray**](PiggyBankArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy banks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_account**
> TransactionArray list_transaction_by_account(id)

List all transactions related to the account.

This endpoint returns a list of all the transactions connected to the account. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = 1 # int | The ID of the account.
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    limit = 5 # int | Limits the number of results on one page. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions related to the account.
        api_response = api_instance.list_transaction_by_account(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_transaction_by_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions related to the account.
        api_response = api_instance.list_transaction_by_account(id, page=page, limit=limit, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->list_transaction_by_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. |
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]
 **limit** | **int**| Limits the number of results on one page. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned. | [optional]

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
**200** | A list of transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_account**
> AccountSingle store_account(account_store)

Create new account.

Creates a new account. The data required can be submitted as a JSON body or as a list of parameters (in key=value pairs, like a webform).

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.account_single import AccountSingle
from firefly_iii_client.model.account_store import AccountStore
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
    api_instance = accounts_api.AccountsApi(api_client)
    account_store = AccountStore(
        account_number="7009312345678",
        account_role="defaultAsset",
        active=False,
        bic="BOFAUS3N",
        credit_card_type="monthlyFull",
        currency_code="EUR",
        currency_id="12",
        iban="GB98MIDL07009312345678",
        include_net_worth=True,
        interest="5.3",
        interest_period="monthly",
        latitude=51.983333,
        liability_direction="credit",
        liability_type="loan",
        longitude=5.916667,
        monthly_payment_date=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        name="My checking account",
        notes="Some example notes",
        opening_balance="-1012.12",
        opening_balance_date=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        order=1,
        type="asset",
        virtual_balance="123.45",
        zoom_level=6,
    ) # AccountStore | JSON array with the necessary account information or key=value pairs. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Create new account.
        api_response = api_instance.store_account(account_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->store_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_store** | [**AccountStore**](AccountStore.md)| JSON array with the necessary account information or key&#x3D;value pairs. See the model for the exact specifications. |

### Return type

[**AccountSingle**](AccountSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New account stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> AccountSingle update_account(id, account_update)

Update existing account.

Used to update a single account. All fields that are not submitted will be cleared (set to NULL). The model will tell you which fields are mandatory. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import accounts_api
from firefly_iii_client.model.account_single import AccountSingle
from firefly_iii_client.model.account_update import AccountUpdate
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = 1 # int | The ID of the account.
    account_update = AccountUpdate(
        account_number="7009312345678",
        account_role="defaultAsset",
        active=False,
        bic="BOFAUS3N",
        credit_card_type="monthlyFull",
        currency_code="EUR",
        currency_id="12",
        iban="GB98MIDL07009312345678",
        include_net_worth=True,
        interest="5.3",
        interest_period="monthly",
        latitude=51.983333,
        liability_type="loan",
        longitude=5.916667,
        monthly_payment_date=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        name="My checking account",
        notes="Some example notes",
        opening_balance="-1012.12",
        opening_balance_date=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        order=1,
        virtual_balance="123.45",
        zoom_level=6,
    ) # AccountUpdate | JSON array or formdata with updated account information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing account.
        api_response = api_instance.update_account(id, account_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the account. |
 **account_update** | [**AccountUpdate**](AccountUpdate.md)| JSON array or formdata with updated account information. See the model for the exact specifications. |

### Return type

[**AccountSingle**](AccountSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated account stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

