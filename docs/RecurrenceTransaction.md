# RecurrenceTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the transaction. | 
**budget_id** | **int** | The budget ID for this transaction. | [optional] 
**budget_name** | **str** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] 
**category_id** | **int** | Category ID for this transaction. | [optional] 
**category_name** | **str** | Category name for this transaction. | [optional] 
**currency_code** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_decimal_places** | **int** | Number of decimals in the currency | [optional] 
**currency_id** | **int** | Submit either a currency_id or a currency_code. | [optional] 
**currency_symbol** | **str** |  | [optional] 
**description** | **str** |  | 
**destination_iban** | **str** |  | [optional] 
**destination_id** | **int** | ID of the destination account. Submit either this or destination_name. | [optional] 
**destination_name** | **str** | Name of the destination account. Submit either this or destination_id. | [optional] 
**destination_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**foreign_amount** | **float** | Foreign amount of the transaction. | [optional] 
**foreign_currency_code** | **str** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_decimal_places** | **int** | Number of decimals in the currency | [optional] 
**foreign_currency_id** | **int** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_symbol** | **str** |  | [optional] 
**piggy_bank_id** | **int** | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | **str** | Optional. Use either this or the piggy_bank_id | [optional] 
**source_iban** | **str** |  | [optional] 
**source_id** | **int** | ID of the source account. Submit either this or source_name. | [optional] 
**source_name** | **str** | Name of the source account. Submit either this or source_id. | [optional] 
**source_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**tags** | **list[str]** | Array of tags. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


