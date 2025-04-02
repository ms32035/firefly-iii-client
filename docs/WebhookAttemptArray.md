# WebhookAttemptArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookAttemptRead]**](WebhookAttemptRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.webhook_attempt_array import WebhookAttemptArray

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookAttemptArray from a JSON string
webhook_attempt_array_instance = WebhookAttemptArray.from_json(json)
# print the JSON string representation of the object
print(WebhookAttemptArray.to_json())

# convert the object into a dict
webhook_attempt_array_dict = webhook_attempt_array_instance.to_dict()
# create an instance of WebhookAttemptArray from a dict
webhook_attempt_array_from_dict = WebhookAttemptArray.from_dict(webhook_attempt_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


