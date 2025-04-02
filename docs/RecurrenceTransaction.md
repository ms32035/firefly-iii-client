# RecurrenceTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | 
**bill_id** | **str** | Optional. Use either this or the bill_name | [optional] 
**bill_name** | **str** | Optional. Use either this or the bill_id | [optional] 
**budget_id** | **str** | The budget ID for this transaction. | [optional] 
**budget_name** | **str** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] [readonly] 
**category_id** | **str** | Category ID for this transaction. | [optional] 
**category_name** | **str** | Category name for this transaction. | [optional] 
**currency_code** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_decimal_places** | **int** | Number of decimals in the currency | [optional] [readonly] 
**currency_id** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**description** | **str** |  | 
**destination_iban** | **str** |  | [optional] [readonly] 
**destination_id** | **str** | ID of the destination account. Submit either this or destination_name. | [optional] 
**destination_name** | **str** | Name of the destination account. Submit either this or destination_id. | [optional] 
**destination_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**foreign_amount** | **str** | Foreign amount of the transaction. | [optional] 
**foreign_currency_code** | **str** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_decimal_places** | **int** | Number of decimals in the currency | [optional] [readonly] 
**foreign_currency_id** | **str** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_symbol** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] 
**piggy_bank_id** | **str** | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | **str** | Optional. Use either this or the piggy_bank_id | [optional] 
**source_iban** | **str** |  | [optional] [readonly] 
**source_id** | **str** | ID of the source account. Submit either this or source_name. | [optional] 
**source_name** | **str** | Name of the source account. Submit either this or source_id. | [optional] 
**source_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**tags** | **List[str]** | Array of tags. | [optional] 

## Example

```python
from firefly_iii_client.models.recurrence_transaction import RecurrenceTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceTransaction from a JSON string
recurrence_transaction_instance = RecurrenceTransaction.from_json(json)
# print the JSON string representation of the object
print(RecurrenceTransaction.to_json())

# convert the object into a dict
recurrence_transaction_dict = recurrence_transaction_instance.to_dict()
# create an instance of RecurrenceTransaction from a dict
recurrence_transaction_from_dict = RecurrenceTransaction.from_dict(recurrence_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


