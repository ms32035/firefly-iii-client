# WebhookMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**errored** | **bool** | If this message has errored out. | [optional] 
**message** | **str** | The actual message that is sent or will be sent as JSON string. | [optional] 
**sent** | **bool** | If this message is sent yet. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**uuid** | **str** | Long UUID string for identification of this webhook message. | [optional] 
**webhook_id** | **str** | The ID of the webhook this message belongs to. | [optional] 

## Example

```python
from firefly_iii_client.models.webhook_message import WebhookMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMessage from a JSON string
webhook_message_instance = WebhookMessage.from_json(json)
# print the JSON string representation of the object
print(WebhookMessage.to_json())

# convert the object into a dict
webhook_message_dict = webhook_message_instance.to_dict()
# create an instance of WebhookMessage from a dict
webhook_message_form_dict = webhook_message.from_dict(webhook_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


