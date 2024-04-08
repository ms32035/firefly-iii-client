# WebhookMessageArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookMessageRead]**](WebhookMessageRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.webhook_message_array import WebhookMessageArray

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMessageArray from a JSON string
webhook_message_array_instance = WebhookMessageArray.from_json(json)
# print the JSON string representation of the object
print(WebhookMessageArray.to_json())

# convert the object into a dict
webhook_message_array_dict = webhook_message_array_instance.to_dict()
# create an instance of WebhookMessageArray from a dict
webhook_message_array_form_dict = webhook_message_array.from_dict(webhook_message_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


