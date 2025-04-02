# WebhookAttempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**logs** | **str** | Internal log for this attempt. May contain sensitive user data. | [optional] 
**response** | **str** | Webhook receiver response for this attempt, if any. May contain sensitive user data. | [optional] 
**status_code** | **int** | The HTTP status code of the error, if any. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**webhook_message_id** | **str** | The ID of the webhook message this attempt belongs to. | [optional] 

## Example

```python
from firefly_iii_client.models.webhook_attempt import WebhookAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookAttempt from a JSON string
webhook_attempt_instance = WebhookAttempt.from_json(json)
# print the JSON string representation of the object
print(WebhookAttempt.to_json())

# convert the object into a dict
webhook_attempt_dict = webhook_attempt_instance.to_dict()
# create an instance of WebhookAttempt from a dict
webhook_attempt_from_dict = WebhookAttempt.from_dict(webhook_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


