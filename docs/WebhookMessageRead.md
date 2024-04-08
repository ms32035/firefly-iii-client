# WebhookMessageRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**WebhookMessage**](WebhookMessage.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.webhook_message_read import WebhookMessageRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMessageRead from a JSON string
webhook_message_read_instance = WebhookMessageRead.from_json(json)
# print the JSON string representation of the object
print(WebhookMessageRead.to_json())

# convert the object into a dict
webhook_message_read_dict = webhook_message_read_instance.to_dict()
# create an instance of WebhookMessageRead from a dict
webhook_message_read_form_dict = webhook_message_read.from_dict(webhook_message_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


