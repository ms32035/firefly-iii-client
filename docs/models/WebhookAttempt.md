# firefly_iii_client.model.webhook_attempt.WebhookAttempt

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**logs** | None, str,  | NoneClass, str,  | Internal log for this attempt. May contain sensitive user data. | [optional] 
**response** | None, str,  | NoneClass, str,  | Webhook receiver response for this attempt, if any. May contain sensitive user data. | [optional] 
**status_code** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The HTTP status code of the error, if any. | [optional] value must be a 32 bit integer
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**webhook_message_id** | str,  | str,  | The ID of the webhook message this attempt belongs to. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

