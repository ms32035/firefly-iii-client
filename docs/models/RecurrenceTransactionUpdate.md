# firefly_iii_client.model.recurrence_transaction_update.RecurrenceTransactionUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | 
**amount** | str,  | str,  | Amount of the transaction. | [optional] 
**bill_id** | None, str,  | NoneClass, str,  | Optional. | [optional] 
**budget_id** | str,  | str,  | The budget ID for this transaction. | [optional] 
**category_id** | str,  | str,  | Category ID for this transaction. | [optional] 
**currency_code** | str,  | str,  | Submit either a currency_id or a currency_code. | [optional] 
**currency_id** | str,  | str,  | Submit either a currency_id or a currency_code. | [optional] 
**description** | str,  | str,  |  | [optional] 
**destination_id** | str,  | str,  | ID of the destination account. Submit either this or destination_name. | [optional] 
**foreign_amount** | None, str,  | NoneClass, str,  | Foreign amount of the transaction. | [optional] 
**foreign_currency_id** | None, str,  | NoneClass, str,  | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**piggy_bank_id** | None, str,  | NoneClass, str,  |  | [optional] 
**source_id** | str,  | str,  | ID of the source account. Submit either this or source_name. | [optional] 
**[tags](#tags)** | list, tuple, None,  | tuple, NoneClass,  | Array of tags. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Array of tags.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Array of tags. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Tag. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

