# firefly_iii_client.RecurrencesApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recurrence**](RecurrencesApi.md#delete_recurrence) | **DELETE** /api/v1/recurrences/{id} | Delete a recurring transaction.
[**get_recurrence**](RecurrencesApi.md#get_recurrence) | **GET** /api/v1/recurrences/{id} | Get a single recurring transaction.
[**list_recurrence**](RecurrencesApi.md#list_recurrence) | **GET** /api/v1/recurrences | List all recurring transactions.
[**list_transaction_by_recurrence**](RecurrencesApi.md#list_transaction_by_recurrence) | **GET** /api/v1/recurrences/{id}/transactions | List all transactions created by a recurring transaction.
[**store_recurrence**](RecurrencesApi.md#store_recurrence) | **POST** /api/v1/recurrences | Store a new recurring transaction
[**update_recurrence**](RecurrencesApi.md#update_recurrence) | **PUT** /api/v1/recurrences/{id} | Update existing recurring transaction.


# **delete_recurrence**
> delete_recurrence(id)

Delete a recurring transaction.

Delete a recurring transaction. Transactions created by the recurring transaction will not be deleted.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import recurrences_api
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
    api_instance = recurrences_api.RecurrencesApi(api_client)
    id = 1 # int | The ID of the recurring transaction.

    # example passing only required values which don't have defaults set
    try:
        # Delete a recurring transaction.
        api_instance.delete_recurrence(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->delete_recurrence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. |

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
**204** | Recurring transaction deleted. |  -  |
**404** | No such recurring transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurrence**
> RecurrenceSingle get_recurrence(id)

Get a single recurring transaction.

Get a single recurring transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import recurrences_api
from firefly_iii_client.model.recurrence_single import RecurrenceSingle
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
    api_instance = recurrences_api.RecurrencesApi(api_client)
    id = 1 # int | The ID of the recurring transaction.

    # example passing only required values which don't have defaults set
    try:
        # Get a single recurring transaction.
        api_response = api_instance.get_recurrence(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->get_recurrence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. |

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested recurring transaction |  -  |
**404** | Recurring transaction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recurrence**
> RecurrenceArray list_recurrence()

List all recurring transactions.

List all recurring transactions.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import recurrences_api
from firefly_iii_client.model.recurrence_array import RecurrenceArray
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
    api_instance = recurrences_api.RecurrencesApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all recurring transactions.
        api_response = api_instance.list_recurrence(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->list_recurrence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]

### Return type

[**RecurrenceArray**](RecurrenceArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recurring transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_recurrence**
> TransactionArray list_transaction_by_recurrence(id)

List all transactions created by a recurring transaction.

List all transactions created by a recurring transaction, optionally limited to the date ranges specified.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import recurrences_api
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
    api_instance = recurrences_api.RecurrencesApi(api_client)
    id = 1 # int | The ID of the recurring transaction.
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. Both the start and end date must be present.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. Both the start and end date must be present.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions created by a recurring transaction.
        api_response = api_instance.list_transaction_by_recurrence(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->list_transaction_by_recurrence: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions created by a recurring transaction.
        api_response = api_instance.list_transaction_by_recurrence(id, page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->list_transaction_by_recurrence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. |
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD. Both the start and end date must be present.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD. Both the start and end date must be present.  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned | [optional]

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

# **store_recurrence**
> RecurrenceSingle store_recurrence(recurrence_store)

Store a new recurring transaction

Creates a new recurring transaction. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import recurrences_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.recurrence_single import RecurrenceSingle
from firefly_iii_client.model.recurrence_store import RecurrenceStore
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
    api_instance = recurrences_api.RecurrencesApi(api_client)
    recurrence_store = RecurrenceStore(
        active=True,
        apply_rules=True,
        description="Recurring transaction for the monthly rent",
        first_date=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
        notes="Some notes",
        nr_of_repetitions=5,
        repeat_until=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        repetitions=[
            RecurrenceRepetitionStore(
                moment="3",
                skip=0,
                type="weekly",
                weekend=1,
            ),
        ],
        title="Rent",
        transactions=[
            RecurrenceTransactionStore(
                amount="123.45",
                budget_id="4",
                category_id="211",
                currency_code="EUR",
                currency_id="3",
                description="Rent for the current month",
                destination_id="258",
                foreign_amount="123.45",
                foreign_currency_code="GBP",
                foreign_currency_id="17",
                piggy_bank_id="123",
                source_id="913",
                tags=[
                    "",
                ],
            ),
        ],
        type="withdrawal",
    ) # RecurrenceStore | JSON array or key=value pairs with the necessary recurring transaction information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new recurring transaction
        api_response = api_instance.store_recurrence(recurrence_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->store_recurrence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurrence_store** | [**RecurrenceStore**](RecurrenceStore.md)| JSON array or key&#x3D;value pairs with the necessary recurring transaction information. See the model for the exact specifications. |

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New recurring transaction stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recurrence**
> RecurrenceSingle update_recurrence(id, recurrence_update)

Update existing recurring transaction.

Update existing recurring transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import recurrences_api
from firefly_iii_client.model.recurrence_update import RecurrenceUpdate
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.recurrence_single import RecurrenceSingle
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
    api_instance = recurrences_api.RecurrencesApi(api_client)
    id = 1 # int | The ID of the recurring transaction.
    recurrence_update = RecurrenceUpdate(
        active=True,
        apply_rules=True,
        description="Recurring transaction for the monthly rent",
        first_date=dateutil_parser('Sun Sep 17 00:00:00 UTC 2017').date(),
        notes="Some notes",
        nr_of_repetitions=5,
        repeat_until=dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date(),
        repetitions=[
            RecurrenceRepetitionUpdate(
                moment="3",
                skip=0,
                type="weekly",
                weekend=1,
            ),
        ],
        title="Rent",
        transactions=[
            RecurrenceTransactionUpdate(
                amount="123.45",
                budget_id="4",
                category_id="211",
                currency_code="EUR",
                currency_id="3",
                description="Rent for the current month",
                destination_id="258",
                foreign_amount="123.45",
                foreign_currency_id="17",
                piggy_bank_id="123",
                source_id="913",
                tags=[
                    "",
                ],
            ),
        ],
    ) # RecurrenceUpdate | JSON array with updated recurring transaction information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing recurring transaction.
        api_response = api_instance.update_recurrence(id, recurrence_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RecurrencesApi->update_recurrence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the recurring transaction. |
 **recurrence_update** | [**RecurrenceUpdate**](RecurrenceUpdate.md)| JSON array with updated recurring transaction information. See the model for the exact specifications. |

### Return type

[**RecurrenceSingle**](RecurrenceSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated recurring transaction stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

