# firefly_iii_client.WebhooksApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete a webhook.
[**delete_webhook_message**](WebhooksApi.md#delete_webhook_message) | **DELETE** /api/v1/webhooks/{id}/messages/{messageId} | Delete a webhook message.
[**delete_webhook_message_attempt**](WebhooksApi.md#delete_webhook_message_attempt) | **DELETE** /api/v1/webhooks/{id}/messages/{messageId}/attempts/{attemptId} | Delete a webhook attempt.
[**get_single_webhook_message**](WebhooksApi.md#get_single_webhook_message) | **GET** /api/v1/webhooks/{id}/messages/{messageId} | Get a single message from a webhook.
[**get_single_webhook_message_attempt**](WebhooksApi.md#get_single_webhook_message_attempt) | **GET** /api/v1/webhooks/{id}/messages/{messageId}/attempts/{attemptId} | Get a single failed attempt from a single webhook message.
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get a single webhook.
[**get_webhook_message_attempts**](WebhooksApi.md#get_webhook_message_attempts) | **GET** /api/v1/webhooks/{id}/messages/{messageId}/attempts | Get all the failed attempts of a single webhook message.
[**get_webhook_messages**](WebhooksApi.md#get_webhook_messages) | **GET** /api/v1/webhooks/{id}/messages | Get all the messages of a single webhook.
[**list_webhook**](WebhooksApi.md#list_webhook) | **GET** /api/v1/webhooks | List all webhooks.
[**store_webhook**](WebhooksApi.md#store_webhook) | **POST** /api/v1/webhooks | Store a new webhook
[**submit_webook**](WebhooksApi.md#submit_webook) | **POST** /api/v1/webhooks/{id}/submit | Submit messages for a webhook.
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /api/v1/webhooks/{id} | Update existing webhook.


# **delete_webhook**
> delete_webhook(id)

Delete a webhook.

Delete a webhook.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a webhook.
        api_instance.delete_webhook(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |

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
**204** | Webhook deleted. |  -  |
**404** | No such webhook. |  -  |
**500** | Error when deleting. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_message**
> delete_webhook_message(id, message_id)

Delete a webhook message.

Delete a webhook message. Any time a webhook is triggered the message is stored before it's sent. You can delete them before or after sending.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.
    message_id = 1 # int | The webhook message ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a webhook message.
        api_instance.delete_webhook_message(id, message_id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->delete_webhook_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |
 **message_id** | **int**| The webhook message ID. |

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
**204** | Webhook message deleted. |  -  |
**404** | No such webhook or webhook message. |  -  |
**500** | Error when deleting. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_message_attempt**
> delete_webhook_message_attempt(id, message_id, attempt_id)

Delete a webhook attempt.

Delete a webhook message attempt. If you delete all attempts for a webhook message, Firefly III will (once again) assume all is well with the webhook message and will try to send it again.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.
    message_id = 1 # int | The webhook message ID.
    attempt_id = 1 # int | The webhook message attempt ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a webhook attempt.
        api_instance.delete_webhook_message_attempt(id, message_id, attempt_id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->delete_webhook_message_attempt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |
 **message_id** | **int**| The webhook message ID. |
 **attempt_id** | **int**| The webhook message attempt ID. |

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
**204** | Webhook message attempt deleted. |  -  |
**404** | No such webhook, webhook message or webhook attempt. |  -  |
**500** | Error when deleting. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_webhook_message**
> WebhookMessageSingle get_single_webhook_message(id, message_id)

Get a single message from a webhook.

When a webhook is triggered it will store the actual content of the webhook in a webhook message. You can view and analyse a single one using this endpoint.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.webhook_message_single import WebhookMessageSingle
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.
    message_id = 1 # int | The webhook message ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a single message from a webhook.
        api_response = api_instance.get_single_webhook_message(id, message_id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_single_webhook_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |
 **message_id** | **int**| The webhook message ID. |

### Return type

[**WebhookMessageSingle**](WebhookMessageSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single webhook message. |  -  |
**404** | Webhook message not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_webhook_message_attempt**
> WebhookAttemptSingle get_single_webhook_message_attempt(id, message_id, attempt_id)

Get a single failed attempt from a single webhook message.

When a webhook message fails to send it will store the failure in an \"attempt\". You can view and analyse these. Webhooks messages that receive too many attempts (failures) will not be fired. You must first clear out old attempts and try again. This endpoint shows you the details of a single attempt. The ID of the attempt must match the corresponding webhook and webhook message.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.webhook_attempt_single import WebhookAttemptSingle
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.
    message_id = 1 # int | The webhook message ID.
    attempt_id = 1 # int | The webhook attempt ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a single failed attempt from a single webhook message.
        api_response = api_instance.get_single_webhook_message_attempt(id, message_id, attempt_id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_single_webhook_message_attempt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |
 **message_id** | **int**| The webhook message ID. |
 **attempt_id** | **int**| The webhook attempt ID. |

### Return type

[**WebhookAttemptSingle**](WebhookAttemptSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single webhook attempt. |  -  |
**404** | Webhook message attempt not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> WebhookSingle get_webhook(id)

Get a single webhook.

Gets all info of a single webhook.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.webhook_single import WebhookSingle
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a single webhook.
        api_response = api_instance.get_webhook(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |

### Return type

[**WebhookSingle**](WebhookSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested webhook. |  -  |
**404** | Webhook not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_message_attempts**
> WebhookAttemptArray get_webhook_message_attempts(id, message_id)

Get all the failed attempts of a single webhook message.

When a webhook message fails to send it will store the failure in an \"attempt\". You can view and analyse these. Webhook messages that receive too many attempts (failures) will not be sent again. You must first clear out old attempts before the message can go out again.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.webhook_attempt_array import WebhookAttemptArray
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.
    message_id = 1 # int | The webhook message ID.
    page = 1 # int | Page number. The default pagination is per 50 items. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all the failed attempts of a single webhook message.
        api_response = api_instance.get_webhook_message_attempts(id, message_id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook_message_attempts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all the failed attempts of a single webhook message.
        api_response = api_instance.get_webhook_message_attempts(id, message_id, page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook_message_attempts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |
 **message_id** | **int**| The webhook message ID. |
 **page** | **int**| Page number. The default pagination is per 50 items. | [optional]

### Return type

[**WebhookAttemptArray**](WebhookAttemptArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of webhook attempts. |  -  |
**404** | Webhook or webhook message not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_messages**
> WebhookMessageArray get_webhook_messages(id)

Get all the messages of a single webhook.

When a webhook is triggered the actual message that will be send is stored in a \"message\". You can view and analyse these messages.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.webhook_message_array import WebhookMessageArray
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.

    # example passing only required values which don't have defaults set
    try:
        # Get all the messages of a single webhook.
        api_response = api_instance.get_webhook_messages(id)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |

### Return type

[**WebhookMessageArray**](WebhookMessageArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of webhook messages. |  -  |
**404** | Webhook not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook**
> WebhookArray list_webhook()

List all webhooks.

List all the user's webhooks.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.webhook_array import WebhookArray
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    page = 1 # int | The page number, if necessary. The default pagination is 50, so 50 webhooks per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all webhooks.
        api_response = api_instance.list_webhook(page=page)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->list_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number, if necessary. The default pagination is 50, so 50 webhooks per page. | [optional]

### Return type

[**WebhookArray**](WebhookArray.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of webhooks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_webhook**
> WebhookSingle store_webhook(webhook_store)

Store a new webhook

Creates a new webhook. The data required can be submitted as a JSON body or as a list of parameters. The webhook will be given a random secret. 

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.webhook_single import WebhookSingle
from firefly_iii_client.model.webhook_store import WebhookStore
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhook_store = WebhookStore(
        active=False,
        delivery="DELIVERY_JSON",
        response="RESPONSE_TRANSACTIONS",
        title="Update magic mirror on new transaction",
        trigger="TRIGGER_DESTROY_TRANSACTION",
        url="https://example.com",
    ) # WebhookStore | JSON array or key=value pairs with the necessary webhook information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new webhook
        api_response = api_instance.store_webhook(webhook_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->store_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_store** | [**WebhookStore**](WebhookStore.md)| JSON array or key&#x3D;value pairs with the necessary webhook information. See the model for the exact specifications. |

### Return type

[**WebhookSingle**](WebhookSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New webhook stored, result in response. |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_webook**
> submit_webook(id)

Submit messages for a webhook.

This endpoint will submit any open messages for this webhook. This is an asynchronous operation, so you can't see the result. Refresh the webhook message and/or the webhook message attempts to see the results. This may take some time if the webhook receiver is slow.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.

    # example passing only required values which don't have defaults set
    try:
        # Submit messages for a webhook.
        api_instance.submit_webook(id)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->submit_webook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |

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
**200** | OK! |  -  |
**204** | No messages to send, so did nothing. |  -  |
**404** | Webhook not found. |  -  |
**500** | Error while sending. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookSingle update_webhook(id, webhook_update)

Update existing webhook.

Update an existing webhook's information. If you wish to reset the secret, submit any value as the \"secret\". Firefly III will take this as a hint and reset the secret of the webhook.

### Example

* OAuth Authentication (firefly_iii_auth):

```python
import time
import firefly_iii_client
from firefly_iii_client.api import webhooks_api
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.webhook_update import WebhookUpdate
from firefly_iii_client.model.webhook_single import WebhookSingle
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = 1 # int | The webhook ID.
    webhook_update = WebhookUpdate(
        active=False,
        delivery="DELIVERY_JSON",
        response="RESPONSE_TRANSACTIONS",
        secret="iMLZLtLx2JHWhK9Dtyuoqyir",
        title="Update magic mirror on new transaction",
        trigger="TRIGGER_DESTROY_TRANSACTION",
        url="https://example.com",
    ) # WebhookUpdate | JSON array with updated webhook information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Update existing webhook.
        api_response = api_instance.update_webhook(id, webhook_update)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID. |
 **webhook_update** | [**WebhookUpdate**](WebhookUpdate.md)| JSON array with updated webhook information. See the model for the exact specifications. |

### Return type

[**WebhookSingle**](WebhookSingle.md)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.api+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated webhook stored, result in response |  -  |
**422** | Validation errors (see body) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

