# WebhookArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookRead]**](WebhookRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.webhook_array import WebhookArray

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookArray from a JSON string
webhook_array_instance = WebhookArray.from_json(json)
# print the JSON string representation of the object
print(WebhookArray.to_json())

# convert the object into a dict
webhook_array_dict = webhook_array_instance.to_dict()
# create an instance of WebhookArray from a dict
webhook_array_form_dict = webhook_array.from_dict(webhook_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


