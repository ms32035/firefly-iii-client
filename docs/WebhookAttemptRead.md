# WebhookAttemptRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**WebhookAttempt**](WebhookAttempt.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.webhook_attempt_read import WebhookAttemptRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookAttemptRead from a JSON string
webhook_attempt_read_instance = WebhookAttemptRead.from_json(json)
# print the JSON string representation of the object
print(WebhookAttemptRead.to_json())

# convert the object into a dict
webhook_attempt_read_dict = webhook_attempt_read_instance.to_dict()
# create an instance of WebhookAttemptRead from a dict
webhook_attempt_read_form_dict = webhook_attempt_read.from_dict(webhook_attempt_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


