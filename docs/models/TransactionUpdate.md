# firefly_iii_client.model.transaction_update.TransactionUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apply_rules** | bool,  | BoolClass,  | Whether or not to apply rules when submitting transaction. | [optional] 
**fire_webhooks** | bool,  | BoolClass,  | Whether or not to fire the webhooks that are related to this event. | [optional] if omitted the server will use the default value of True
**group_title** | None, str,  | NoneClass, str,  | Title of the transaction if it has been split in more than one piece. Empty otherwise. | [optional] 
**[transactions](#transactions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionSplitUpdate**](TransactionSplitUpdate.md) | [**TransactionSplitUpdate**](TransactionSplitUpdate.md) | [**TransactionSplitUpdate**](TransactionSplitUpdate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

