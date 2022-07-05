# firefly_iii_client.BillsApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bill**](BillsApi.md#delete_bill) | **DELETE** /api/v1/bills/{id} | Delete a bill.
[**get_bill**](BillsApi.md#get_bill) | **GET** /api/v1/bills/{id} | Get a single bill.
[**list_attachment_by_bill**](BillsApi.md#list_attachment_by_bill) | **GET** /api/v1/bills/{id}/attachments | List all attachments uploaded to the bill.
[**list_bill**](BillsApi.md#list_bill) | **GET** /api/v1/bills | List all bills.
[**list_rule_by_bill**](BillsApi.md#list_rule_by_bill) | **GET** /api/v1/bills/{id}/rules | List all rules associated with the bill.
[**list_transaction_by_bill**](BillsApi.md#list_transaction_by_bill) | **GET** /api/v1/bills/{id}/transactions | List all transactions associated with the  bill.
[**store_bill**](BillsApi.md#store_bill) | **POST** /api/v1/bills | Store a new bill
[**update_bill**](BillsApi.md#update_bill) | **PUT** /api/v1/bills/{id} | Update existing bill.


# **delete_bill**
> delete_bill(id)

Delete a bill.

Delete a bill. This will not delete any associated rules. Will not remove associated transactions. WILL remove all associated attachments.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
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
    api_instance = bills_api.BillsApi(api_client)
    id = "123" # str | The ID of the bill.

    # example passing only required values which don't have defaults set
    try:
        # Delete a bill.
        api_instance.delete_bill(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->delete_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. |

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
**204** | Bill deleted. |  -  |
**404** | No such bill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill**
> BillSingle get_bill(id)

Get a single bill.

Get a single bill.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
from firefly_iii_client.model.bill_single import BillSingle
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
    api_instance = bills_api.BillsApi(api_client)
    id = "123" # str | The ID of the bill.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a single bill.
        api_response = api_instance.get_bill(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->get_bill: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a single bill.
        api_response = api_instance.get_bill(id, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->get_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. |
 **start** | **date**| A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional]

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bill |  -  |
**404** | Bill not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachment_by_bill**
> AttachmentArray list_attachment_by_bill(id)

List all attachments uploaded to the bill.

This endpoint will list all attachments linked to the bill.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
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
    api_instance = bills_api.BillsApi(api_client)
    id = "123" # str | The ID of the bill.
    page = 1 # int | Page number. The default pagination is 50. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all attachments uploaded to the bill.
        api_response = api_instance.list_attachment_by_bill(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->list_attachment_by_bill: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all attachments uploaded to the bill.
        api_response = api_instance.list_attachment_by_bill(id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->list_attachment_by_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. |
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bill**
> BillArray list_bill()

List all bills.

This endpoint will list all the user's bills.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
from firefly_iii_client.model.bill_array import BillArray
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
    api_instance = bills_api.BillsApi(api_client)
    page = 1 # int | Page number. The default pagination is 50. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all bills.
        api_response = api_instance.list_bill(page=page, start=start, end=end)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->list_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will calculate the appropriate payment and paid dates.  | [optional]

### Return type

[**BillArray**](BillArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of bills |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rule_by_bill**
> RuleArray list_rule_by_bill(id)

List all rules associated with the bill.

This endpoint will list all rules that have an action to set the bill to this bill.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
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
    api_instance = bills_api.BillsApi(api_client)
    id = "123" # str | The ID of the bill.

    # example passing only required values which don't have defaults set
    try:
        # List all rules associated with the bill.
        api_response = api_instance.list_rule_by_bill(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->list_rule_by_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. |

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

# **list_transaction_by_bill**
> TransactionArray list_transaction_by_bill(id)

List all transactions associated with the  bill.

This endpoint will list all transactions linked to this bill.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
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
    api_instance = bills_api.BillsApi(api_client)
    id = "123" # str | The ID of the bill.
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    end = dateutil_parser('Mon Dec 31 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions associated with the  bill.
        api_response = api_instance.list_transaction_by_bill(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->list_transaction_by_bill: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions associated with the  bill.
        api_response = api_instance.list_transaction_by_bill(id, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->list_transaction_by_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. |
 **start** | **date**| A date formatted YYYY-MM-DD.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD.  | [optional]
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

# **store_bill**
> BillSingle store_bill(bill_store)

Store a new bill

Creates a new bill. The data required can be submitted as a JSON body or as a list of parameters.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.bill_store import BillStore
from firefly_iii_client.model.bill_single import BillSingle
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
    api_instance = bills_api.BillsApi(api_client)
    bill_store = BillStore(
        active=True,
        amount_max="123.45",
        amount_min="123.45",
        currency_code="EUR",
        currency_id="5",
        date=dateutil_parser('2018-09-17T12:46:47+01:00'),
        end_date=dateutil_parser('2018-09-17T12:46:47+01:00'),
        extension_date=dateutil_parser('2018-09-17T12:46:47+01:00'),
        name="Rent",
        notes="Some example notes",
        object_group_id="5",
        object_group_title="Example Group",
        repeat_freq=BillRepeatFrequency("monthly"),
        skip=0,
    ) # BillStore | JSON array or key=value pairs with the necessary bill information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new bill
        api_response = api_instance.store_bill(bill_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->store_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_store** | [**BillStore**](BillStore.md)| JSON array or key&#x3D;value pairs with the necessary bill information. See the model for the exact specifications. |

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New bill stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill**
> BillSingle update_bill(id, bill_update)

Update existing bill.

Update existing bill.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import bills_api
from firefly_iii_client.model.bill_update import BillUpdate
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.bill_single import BillSingle
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
    api_instance = bills_api.BillsApi(api_client)
    id = "123" # str | The ID of the bill.
    bill_update = BillUpdate(
        active=True,
        amount_max="123.45",
        amount_min="123.45",
        currency_code="EUR",
        currency_id="5",
        date=dateutil_parser('2018-09-17T12:46:47+01:00'),
        end_date=dateutil_parser('2018-09-17T12:46:47+01:00'),
        extension_date=dateutil_parser('2018-09-17T12:46:47+01:00'),
        name="Rent",
        notes="Some example notes",
        object_group_id="5",
        object_group_title="Example Group",
        repeat_freq=BillRepeatFrequency("monthly"),
        skip=0,
    ) # BillUpdate | JSON array or key=value pairs with updated bill information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing bill.
        api_response = api_instance.update_bill(id, bill_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling BillsApi->update_bill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the bill. |
 **bill_update** | [**BillUpdate**](BillUpdate.md)| JSON array or key&#x3D;value pairs with updated bill information. See the model for the exact specifications. |

### Return type

[**BillSingle**](BillSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated bill stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

