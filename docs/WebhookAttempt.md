# WebhookAttempt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**logs** | **str, none_type** | Internal log for this attempt. May contain sensitive user data. | [optional] 
**response** | **str, none_type** | Webhook receiver response for this attempt, if any. May contain sensitive user data. | [optional] 
**status_code** | **int, none_type** | The HTTP status code of the error, if any. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**webhook_message_id** | **str** | The ID of the webhook message this attempt belongs to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


