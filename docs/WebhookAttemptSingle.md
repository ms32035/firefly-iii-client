# WebhookAttemptSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookAttemptRead**](WebhookAttemptRead.md) |  | 

## Example

```python
from firefly_iii_client.models.webhook_attempt_single import WebhookAttemptSingle

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookAttemptSingle from a JSON string
webhook_attempt_single_instance = WebhookAttemptSingle.from_json(json)
# print the JSON string representation of the object
print(WebhookAttemptSingle.to_json())

# convert the object into a dict
webhook_attempt_single_dict = webhook_attempt_single_instance.to_dict()
# create an instance of WebhookAttemptSingle from a dict
webhook_attempt_single_form_dict = webhook_attempt_single.from_dict(webhook_attempt_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


