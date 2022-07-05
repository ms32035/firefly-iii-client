# firefly_iii_client.LinksApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_link_type**](LinksApi.md#delete_link_type) | **DELETE** /api/v1/link_types/{id} | Permanently delete link type.
[**delete_transaction_link**](LinksApi.md#delete_transaction_link) | **DELETE** /api/v1/transaction_links/{id} | Permanently delete link between transactions.
[**get_link_type**](LinksApi.md#get_link_type) | **GET** /api/v1/link_types/{id} | Get single a link type.
[**get_transaction_link**](LinksApi.md#get_transaction_link) | **GET** /api/v1/transaction_links/{id} | Get a single link.
[**list_link_type**](LinksApi.md#list_link_type) | **GET** /api/v1/link_types | List all types of links.
[**list_transaction_by_link_type**](LinksApi.md#list_transaction_by_link_type) | **GET** /api/v1/link_types/{id}/transactions | List all transactions under this link type.
[**list_transaction_link**](LinksApi.md#list_transaction_link) | **GET** /api/v1/transaction_links | List all transaction links.
[**store_link_type**](LinksApi.md#store_link_type) | **POST** /api/v1/link_types | Create a new link type
[**store_transaction_link**](LinksApi.md#store_transaction_link) | **POST** /api/v1/transaction_links | Create a new link between transactions
[**update_link_type**](LinksApi.md#update_link_type) | **PUT** /api/v1/link_types/{id} | Update existing link type.
[**update_transaction_link**](LinksApi.md#update_transaction_link) | **PUT** /api/v1/transaction_links/{id} | Update an existing link between transactions.


# **delete_link_type**
> delete_link_type(id)

Permanently delete link type.

Will permanently delete a link type. The links between transactions will be removed. The transactions themselves remain. You cannot delete some of the system provided link types, indicated by the editable=false flag when you list it. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the link type.

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete link type.
        api_instance.delete_link_type(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->delete_link_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. |

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
**204** | Link type deleted |  -  |
**404** | No such link type |  -  |
**500** | Cannot delete this link type. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_link**
> delete_transaction_link(id)

Permanently delete link between transactions.

Will permanently delete link. Transactions remain. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the transaction link.

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete link between transactions.
        api_instance.delete_transaction_link(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->delete_transaction_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction link. |

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
**204** | Transaction link deleted |  -  |
**404** | No such transaction link |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_type**
> LinkTypeSingle get_link_type(id)

Get single a link type.

Returns a single link type by its ID. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.link_type_single import LinkTypeSingle
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the link type.

    # example passing only required values which don't have defaults set
    try:
        # Get single a link type.
        api_response = api_instance.get_link_type(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->get_link_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. |

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested link type |  -  |
**404** | Link type not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_link**
> TransactionLinkSingle get_transaction_link(id)

Get a single link.

Returns a single link by its ID. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.transaction_link_single import TransactionLinkSingle
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the transaction link.

    # example passing only required values which don't have defaults set
    try:
        # Get a single link.
        api_response = api_instance.get_transaction_link(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->get_transaction_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction link. |

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested link |  -  |
**404** | No such transaction link. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_link_type**
> LinkTypeArray list_link_type()

List all types of links.

List all the link types the system has. These include the default ones as well as any new ones. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.link_type_array import LinkTypeArray
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
    api_instance = links_api.LinksApi(api_client)
    page = 1 # int | Page number. The default pagination is 50 items. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all types of links.
        api_response = api_instance.list_link_type(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->list_link_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is 50 items. | [optional]

### Return type

[**LinkTypeArray**](LinkTypeArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of link types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_by_link_type**
> TransactionArray list_transaction_by_link_type(id)

List all transactions under this link type.

List all transactions under this link type, both the inward and outward transactions. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the link type.
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)
    start = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the results.  (optional)
    end = dateutil_parser('Mon Sep 17 00:00:00 UTC 2018').date() # date | A date formatted YYYY-MM-DD, to limit the results.  (optional)
    type = TransactionTypeFilter("all") # TransactionTypeFilter | Optional filter on the transaction type(s) returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all transactions under this link type.
        api_response = api_instance.list_transaction_by_link_type(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->list_transaction_by_link_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transactions under this link type.
        api_response = api_instance.list_transaction_by_link_type(id, page=page, start=start, end=end, type=type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->list_transaction_by_link_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. |
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]
 **start** | **date**| A date formatted YYYY-MM-DD, to limit the results.  | [optional]
 **end** | **date**| A date formatted YYYY-MM-DD, to limit the results.  | [optional]
 **type** | **TransactionTypeFilter**| Optional filter on the transaction type(s) returned. | [optional]

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
**200** | A list of transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_link**
> TransactionLinkArray list_transaction_link()

List all transaction links.

List all the transaction links. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
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
    api_instance = links_api.LinksApi(api_client)
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all transaction links.
        api_response = api_instance.list_transaction_link(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->list_transaction_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]

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
**200** | A list of transaction links |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_link_type**
> LinkTypeSingle store_link_type(link_type)

Create a new link type

Creates a new link type. The data required can be submitted as a JSON body or as a list of parameters (in key=value pairs, like a webform).

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.link_type import LinkType
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.link_type_single import LinkTypeSingle
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
    api_instance = links_api.LinksApi(api_client)
    link_type = LinkType(
        inward="is (partially) paid for by",
        name="Paid",
        outward="(partially) pays for",
    ) # LinkType | JSON array with the necessary link type information or key=value pairs. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Create a new link type
        api_response = api_instance.store_link_type(link_type)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->store_link_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_type** | [**LinkType**](LinkType.md)| JSON array with the necessary link type information or key&#x3D;value pairs. See the model for the exact specifications. |

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New link type stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_transaction_link**
> TransactionLinkSingle store_transaction_link(transaction_link_store)

Create a new link between transactions

Store a new link between two transactions. For this end point you need the journal_id from a transaction.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.transaction_link_store import TransactionLinkStore
from firefly_iii_client.model.transaction_link_single import TransactionLinkSingle
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
    api_instance = links_api.LinksApi(api_client)
    transaction_link_store = TransactionLinkStore(
        inward_id="131",
        link_type_id="5",
        link_type_name="Is paid by",
        notes="Some example notes",
        outward_id="131",
    ) # TransactionLinkStore | JSON array with the necessary link type information or key=value pairs. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Create a new link between transactions
        api_response = api_instance.store_transaction_link(transaction_link_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->store_transaction_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_link_store** | [**TransactionLinkStore**](TransactionLinkStore.md)| JSON array with the necessary link type information or key&#x3D;value pairs. See the model for the exact specifications. |

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New transaction link stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link_type**
> LinkTypeSingle update_link_type(id, link_type_update)

Update existing link type.

Used to update a single link type. All fields that are not submitted will be cleared (set to NULL). The model will tell you which fields are mandatory. You cannot update some of the system provided link types, indicated by the editable=false flag when you list it. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.link_type_update import LinkTypeUpdate
from firefly_iii_client.model.link_type_single import LinkTypeSingle
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the link type.
    link_type_update = LinkTypeUpdate(
        inward="is (partially) paid for by",
        name="Paid",
        outward="(partially) pays for",
    ) # LinkTypeUpdate | JSON array or formdata with updated link type information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing link type.
        api_response = api_instance.update_link_type(id, link_type_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->update_link_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the link type. |
 **link_type_update** | [**LinkTypeUpdate**](LinkTypeUpdate.md)| JSON array or formdata with updated link type information. See the model for the exact specifications. |

### Return type

[**LinkTypeSingle**](LinkTypeSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated link type stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |
**500** | Cannot delete this link type. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_link**
> TransactionLinkSingle update_transaction_link(id, transaction_link_update)

Update an existing link between transactions.

Used to update a single existing link. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import links_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.transaction_link_single import TransactionLinkSingle
from firefly_iii_client.model.transaction_link_update import TransactionLinkUpdate
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
    api_instance = links_api.LinksApi(api_client)
    id = "123" # str | The ID of the transaction link.
    transaction_link_update = TransactionLinkUpdate(
        inward_id="131",
        link_type_id="5",
        link_type_name="Is paid by",
        notes="Some example notes",
        outward_id="131",
    ) # TransactionLinkUpdate | JSON array or formdata with updated link type information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing link between transactions.
        api_response = api_instance.update_transaction_link(id, transaction_link_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling LinksApi->update_transaction_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the transaction link. |
 **transaction_link_update** | [**TransactionLinkUpdate**](TransactionLinkUpdate.md)| JSON array or formdata with updated link type information. See the model for the exact specifications. |

### Return type

[**TransactionLinkSingle**](TransactionLinkSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated link type stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

