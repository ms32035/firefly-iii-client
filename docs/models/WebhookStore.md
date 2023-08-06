# firefly_iii_client.model.webhook_store.WebhookStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**delivery** | [**WebhookDelivery**](WebhookDelivery.md) | [**WebhookDelivery**](WebhookDelivery.md) |  | 
**response** | [**WebhookResponse**](WebhookResponse.md) | [**WebhookResponse**](WebhookResponse.md) |  | 
**trigger** | [**WebhookTrigger**](WebhookTrigger.md) | [**WebhookTrigger**](WebhookTrigger.md) |  | 
**title** | str,  | str,  | A title for the webhook for easy recognition. | 
**url** | str,  | str,  | The URL of the webhook. Has to start with &#x60;https&#x60;. | 
**active** | bool,  | BoolClass,  | Boolean to indicate if the webhook is active | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

