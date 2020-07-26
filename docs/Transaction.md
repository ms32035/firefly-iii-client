# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_rules** | **bool** | Whether or not to apply rules when submitting transaction. | [optional] 
**created_at** | **datetime** |  | [optional] 
**error_if_duplicate_hash** | **bool** | Break if the submitted transaction exists already. | [optional] 
**group_title** | **str** | Title of the transaction if it has been split in more than one piece. Empty otherwise. | [optional] 
**transactions** | [**list[TransactionSplit]**](TransactionSplit.md) |  | 
**updated_at** | **datetime** |  | [optional] 
**user** | **int** | User ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


