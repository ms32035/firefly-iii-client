# firefly_iii_client.model.recurrence_transaction.RecurrenceTransaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | Amount of the transaction. | 
**description** | str,  | str,  |  | 
**bill_id** | None, str,  | NoneClass, str,  | Optional. Use either this or the bill_name | [optional] 
**bill_name** | None, str,  | NoneClass, str,  | Optional. Use either this or the bill_id | [optional] 
**budget_id** | str,  | str,  | The budget ID for this transaction. | [optional] 
**budget_name** | None, str,  | NoneClass, str,  | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] 
**category_id** | str,  | str,  | Category ID for this transaction. | [optional] 
**category_name** | str,  | str,  | Category name for this transaction. | [optional] 
**currency_code** | str,  | str,  | Submit either a currency_id or a currency_code. | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | Number of decimals in the currency | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  | Submit either a currency_id or a currency_code. | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**destination_iban** | None, str,  | NoneClass, str,  |  | [optional] 
**destination_id** | str,  | str,  | ID of the destination account. Submit either this or destination_name. | [optional] 
**destination_name** | str,  | str,  | Name of the destination account. Submit either this or destination_id. | [optional] 
**destination_type** | [**AccountTypeProperty**](AccountTypeProperty.md) | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**foreign_amount** | None, str,  | NoneClass, str,  | Foreign amount of the transaction. | [optional] 
**foreign_currency_code** | None, str,  | NoneClass, str,  | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_decimal_places** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of decimals in the currency | [optional] value must be a 32 bit integer
**foreign_currency_id** | None, str,  | NoneClass, str,  | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_symbol** | None, str,  | NoneClass, str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**piggy_bank_id** | None, str,  | NoneClass, str,  | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | None, str,  | NoneClass, str,  | Optional. Use either this or the piggy_bank_id | [optional] 
**source_iban** | None, str,  | NoneClass, str,  |  | [optional] 
**source_id** | str,  | str,  | ID of the source account. Submit either this or source_name. | [optional] 
**source_name** | str,  | str,  | Name of the source account. Submit either this or source_id. | [optional] 
**source_type** | [**AccountTypeProperty**](AccountTypeProperty.md) | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
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

