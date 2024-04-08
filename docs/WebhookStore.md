# WebhookStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Boolean to indicate if the webhook is active | [optional] 
**delivery** | [**WebhookDelivery**](WebhookDelivery.md) |  | 
**response** | [**WebhookResponse**](WebhookResponse.md) |  | 
**title** | **str** | A title for the webhook for easy recognition. | 
**trigger** | [**WebhookTrigger**](WebhookTrigger.md) |  | 
**url** | **str** | The URL of the webhook. Has to start with &#x60;https&#x60;. | 

## Example

```python
from firefly_iii_client.models.webhook_store import WebhookStore

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStore from a JSON string
webhook_store_instance = WebhookStore.from_json(json)
# print the JSON string representation of the object
print(WebhookStore.to_json())

# convert the object into a dict
webhook_store_dict = webhook_store_instance.to_dict()
# create an instance of WebhookStore from a dict
webhook_store_form_dict = webhook_store.from_dict(webhook_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


