# RecurrenceTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | 
**description** | **str** |  | 
**budget_id** | **str** | The budget ID for this transaction. | [optional] 
**budget_name** | **str, none_type** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] [readonly] 
**category_id** | **str** | Category ID for this transaction. | [optional] 
**category_name** | **str** | Category name for this transaction. | [optional] 
**currency_code** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_decimal_places** | **int** | Number of decimals in the currency | [optional] [readonly] 
**currency_id** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**destination_iban** | **str, none_type** |  | [optional] [readonly] 
**destination_id** | **str** | ID of the destination account. Submit either this or destination_name. | [optional] 
**destination_name** | **str** | Name of the destination account. Submit either this or destination_id. | [optional] 
**destination_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**foreign_amount** | **str, none_type** | Foreign amount of the transaction. | [optional] 
**foreign_currency_code** | **str, none_type** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_decimal_places** | **int, none_type** | Number of decimals in the currency | [optional] [readonly] 
**foreign_currency_id** | **str, none_type** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_symbol** | **str, none_type** |  | [optional] [readonly] 
**piggy_bank_id** | **str, none_type** | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | **str, none_type** | Optional. Use either this or the piggy_bank_id | [optional] 
**source_iban** | **str, none_type** |  | [optional] [readonly] 
**source_id** | **str** | ID of the source account. Submit either this or source_name. | [optional] 
**source_name** | **str** | Name of the source account. Submit either this or source_id. | [optional] 
**source_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**tags** | **[str], none_type** | Array of tags. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


