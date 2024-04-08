# WebhookMessageSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookMessageRead**](WebhookMessageRead.md) |  | 

## Example

```python
from firefly_iii_client.models.webhook_message_single import WebhookMessageSingle

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMessageSingle from a JSON string
webhook_message_single_instance = WebhookMessageSingle.from_json(json)
# print the JSON string representation of the object
print(WebhookMessageSingle.to_json())

# convert the object into a dict
webhook_message_single_dict = webhook_message_single_instance.to_dict()
# create an instance of WebhookMessageSingle from a dict
webhook_message_single_form_dict = webhook_message_single.from_dict(webhook_message_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


