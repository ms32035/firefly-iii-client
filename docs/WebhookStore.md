# WebhookStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Indicator for what Firefly III will deliver to the webhook URL. | 
**title** | **str** | A title for the webhook for easy recognition. | 
**trigger** | **str** | The trigger for the webhook. | 
**url** | **str** | The URL of the webhook. Has to start with &#x60;https&#x60;. | 
**delivery** | **str** | Format of the delivered response. | defaults to "DELIVERY_JSON"
**active** | **bool** | Boolean to indicate if the webhook is active | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


