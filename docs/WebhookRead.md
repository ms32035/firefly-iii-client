# WebhookRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Webhook**](Webhook.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.webhook_read import WebhookRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRead from a JSON string
webhook_read_instance = WebhookRead.from_json(json)
# print the JSON string representation of the object
print(WebhookRead.to_json())

# convert the object into a dict
webhook_read_dict = webhook_read_instance.to_dict()
# create an instance of WebhookRead from a dict
webhook_read_from_dict = WebhookRead.from_dict(webhook_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


