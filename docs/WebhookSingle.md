# WebhookSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookRead**](WebhookRead.md) |  | 

## Example

```python
from firefly_iii_client.models.webhook_single import WebhookSingle

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSingle from a JSON string
webhook_single_instance = WebhookSingle.from_json(json)
# print the JSON string representation of the object
print(WebhookSingle.to_json())

# convert the object into a dict
webhook_single_dict = webhook_single_instance.to_dict()
# create an instance of WebhookSingle from a dict
webhook_single_from_dict = WebhookSingle.from_dict(webhook_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


