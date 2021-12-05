# firefly_iii_client.TransactionsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /api/v1/transactions/{id} | Delete a transaction.
[**delete_transaction_journal**](TransactionsApi.md#delete_transaction_journal) | **DELETE** /api/v1/transaction-journals/{id} | Delete split from transaction
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /api/v1/transactions/{id} | Get a single transaction.
[**get_transaction_by_journal**](TransactionsApi.md#get_transaction_by_journal) | **GET** /api/v1/transaction-journals/{id} | Get a single transaction, based on one of the underlying transaction journals (transaction splits).
[**list_attachment_by_transaction**](TransactionsApi.md#list_attachment_by_transaction) | **GET** /api/v1/transactions/{id}/attachments | Lists all attachments.
[**list_event_by_transaction**](TransactionsApi.md#list_event_by_transaction) | **GET** /api/v1/transactions/{id}/piggy_bank_events | Lists all piggy bank events.
[**list_links_by_journal**](TransactionsApi.md#list_links_by_journal) | **GET** /api/v1/transaction-journals/{id}/links | Lists all the transaction links for an individual journal (individual split).
[**list_transaction**](TransactionsApi.md#list_transaction) | **GET** /api/v1/transactions | List all the user&#39;s transactions. 
[**store_transaction**](TransactionsApi.md#store_transaction) | **POST** /api/v1/transactions | Store a new transaction
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /api/v1/transactions/{id} | Update existing transaction.


# **delete_transaction**
> delete_transaction(id)

Delete a transaction.

Delete a transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction.

    # example passing only required values which don't have defaults set
    try:
        # Delete a transaction.
        api_instance.delete_transaction(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. |

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
**204** | Transaction deleted. |  -  |
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_journal**
> delete_transaction_journal(id)

Delete split from transaction

Delete an individual journal (split) from a transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction journal (the split) you wish to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete split from transaction
        api_instance.delete_transaction_journal(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->delete_transaction_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction journal (the split) you wish to delete. |

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
**204** | Transaction journal (split) deleted. |  -  |
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionSingle get_transaction(id)

Get a single transaction.

Get a single transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.transaction_single import TransactionSingle
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction.

    # example passing only required values which don't have defaults set
    try:
        # Get a single transaction.
        api_response = api_instance.get_transaction(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. |

### Return type

[**TransactionSingle**](TransactionSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transaction. |  -  |
**404** | Transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_journal**
> TransactionSingle get_transaction_by_journal(id)

Get a single transaction, based on one of the underlying transaction journals (transaction splits).

Get a single transaction by underlying journal (split).

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.transaction_single import TransactionSingle
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction journal (split).

    # example passing only required values which don't have defaults set
    try:
        # Get a single transaction, based on one of the underlying transaction journals (transaction splits).
        api_response = api_instance.get_transaction_by_journal(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_by_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction journal (split). |

### Return type

[**TransactionSingle**](TransactionSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transaction. |  -  |
**404** | Transaction not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_transaction**
> AttachmentArray list_attachment_by_transaction(id)

Lists all attachments.

Lists all attachments.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lists all attachments.
        api_response = api_instance.list_attachment_by_transaction(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_attachment_by_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all attachments.
        api_response = api_instance.list_attachment_by_transaction(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_attachment_by_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. |
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
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_by_transaction**
> PiggyBankEventArray list_event_by_transaction(id)

Lists all piggy bank events.

Lists all piggy bank events.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.piggy_bank_event_array import PiggyBankEventArray
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lists all piggy bank events.
        api_response = api_instance.list_event_by_transaction(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_event_by_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all piggy bank events.
        api_response = api_instance.list_event_by_transaction(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_event_by_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**PiggyBankEventArray**](PiggyBankEventArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of piggy bank events. |  -  |
**404** | No such transaction. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_links_by_journal**
> TransactionLinkArray list_links_by_journal(id)

Lists all the transaction links for an individual journal (individual split).

Lists all the transaction links for an individual journal (a split). Don't use the group ID, you need the actual underlying journal (the split).

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.transaction_link_array import TransactionLinkArray
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction journal / the split.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lists all the transaction links for an individual journal (individual split).
        api_response = api_instance.list_links_by_journal(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_links_by_journal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all the transaction links for an individual journal (individual split).
        api_response = api_instance.list_links_by_journal(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_links_by_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction journal / the split. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**TransactionLinkArray**](TransactionLinkArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction links. |  -  |
**404** | No such transaction journal (transaction split). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction**
> TransactionArray list_transaction()

List all the user's transactions. 

List all the user's transactions.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
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
    api_instance = transactions_api.TransactionsApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all the user's transactions. 
        api_response = api_instance.list_transaction(page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->list_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive).  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive).  | [optional]
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
**200** | A list of transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_transaction**
> TransactionSingle store_transaction(transaction_store)

Store a new transaction

Creates a new transaction. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.transaction_single import TransactionSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.transaction_store import TransactionStore
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
    api_instance = transactions_api.TransactionsApi(api_client)
    transaction_store = TransactionStore(
        apply_rules=False,
        error_if_duplicate_hash=False,
        fire_webhooks=True,
        group_title="Split transaction title.",
        transactions=[
            TransactionSplitStore(
                amount="123.45",
                bill_id="112",
                bill_name="Monthly rent",
                book_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                budget_id="4",
                bunq_payment_id="bunq_payment_id_example",
                category_id="43",
                category_name="Groceries",
                currency_code="EUR",
                currency_id="12",
                date=dateutil_parser('2018-09-17T12:46:47+01:00'),
                description="Vegetables",
                destination_id="2",
                destination_name="Buy and Large",
                due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                external_id="external_id_example",
                foreign_amount="123.45",
                foreign_currency_code="USD",
                foreign_currency_id="17",
                interest_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                internal_reference="internal_reference_example",
                invoice_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                notes="Some example notes",
                order=0,
                payment_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                piggy_bank_id=1,
                piggy_bank_name="piggy_bank_name_example",
                process_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                reconciled=False,
                sepa_batch_id="sepa_batch_id_example",
                sepa_cc="sepa_cc_example",
                sepa_ci="sepa_ci_example",
                sepa_country="sepa_country_example",
                sepa_ct_id="sepa_ct_id_example",
                sepa_ct_op="sepa_ct_op_example",
                sepa_db="sepa_db_example",
                sepa_ep="sepa_ep_example",
                source_id="2",
                source_name="Checking account",
                tags=[
                    "",
                ],
                type="withdrawal",
            ),
        ],
    ) # TransactionStore | JSON array or key=value pairs with the necessary transaction information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new transaction
        api_response = api_instance.store_transaction(transaction_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->store_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_store** | [**TransactionStore**](TransactionStore.md)| JSON array or key&#x3D;value pairs with the necessary transaction information. See the model for the exact specifications. |

### Return type

[**TransactionSingle**](TransactionSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New transaction stored(s), result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionSingle update_transaction(id, transaction_update)

Update existing transaction.

Update an existing transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import transactions_api
from firefly_iii_client.model.transaction_single import TransactionSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.transaction_update import TransactionUpdate
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
    api_instance = transactions_api.TransactionsApi(api_client)
    id = 1 # int | The ID of the transaction.
    transaction_update = TransactionUpdate(
        apply_rules=False,
        fire_webhooks=True,
        group_title="Split transaction title.",
        transactions=[
            TransactionSplitUpdate(
                amount="123.45",
                bill_id="111",
                bill_name="Monthly rent",
                book_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                budget_id="4",
                bunq_payment_id="bunq_payment_id_example",
                category_id="43",
                category_name="Groceries",
                currency_code="EUR",
                currency_id="12",
                date=dateutil_parser('2018-09-17T12:46:47+01:00'),
                description="Vegetables",
                destination_iban="NL02ABNA0123456789",
                destination_id="2",
                destination_name="Buy and Large",
                due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                external_id="external_id_example",
                foreign_amount="123.45",
                foreign_currency_code="USD",
                foreign_currency_id="17",
                interest_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                internal_reference="internal_reference_example",
                invoice_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                notes="Some example notes",
                order=0,
                payment_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                process_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                reconciled=False,
                sepa_batch_id="sepa_batch_id_example",
                sepa_cc="sepa_cc_example",
                sepa_ci="sepa_ci_example",
                sepa_country="sepa_country_example",
                sepa_ct_id="sepa_ct_id_example",
                sepa_ct_op="sepa_ct_op_example",
                sepa_db="sepa_db_example",
                sepa_ep="sepa_ep_example",
                source_iban="NL02ABNA0123456789",
                source_id="2",
                source_name="Checking account",
                tags=[
                    "",
                ],
            ),
        ],
    ) # TransactionUpdate | JSON array with updated transaction information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing transaction.
        api_response = api_instance.update_transaction(id, transaction_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the transaction. |
 **transaction_update** | [**TransactionUpdate**](TransactionUpdate.md)| JSON array with updated transaction information. See the model for the exact specifications. |

### Return type

[**TransactionSingle**](TransactionSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated transaction stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

