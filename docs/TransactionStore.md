# TransactionStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**[TransactionSplitStore]**](TransactionSplitStore.md) |  | 
**apply_rules** | **bool** | Whether or not to apply rules when submitting transaction. | [optional] 
**error_if_duplicate_hash** | **bool** | Break if the submitted transaction exists already. | [optional] 
**fire_webhooks** | **bool** | Whether or not to fire the webhooks that are related to this event. | [optional]  if omitted the server will use the default value of True
**group_title** | **str, none_type** | Title of the transaction if it has been split in more than one piece. Empty otherwise. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


