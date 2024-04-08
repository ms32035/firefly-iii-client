# RecurrenceTransactionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | [optional] 
**bill_id** | **str** | Optional. | [optional] 
**budget_id** | **str** | The budget ID for this transaction. | [optional] 
**category_id** | **str** | Category ID for this transaction. | [optional] 
**currency_code** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_id** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**description** | **str** |  | [optional] 
**destination_id** | **str** | ID of the destination account. Submit either this or destination_name. | [optional] 
**foreign_amount** | **str** | Foreign amount of the transaction. | [optional] 
**foreign_currency_id** | **str** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**id** | **str** |  | 
**piggy_bank_id** | **str** |  | [optional] 
**source_id** | **str** | ID of the source account. Submit either this or source_name. | [optional] 
**tags** | **List[str]** | Array of tags. | [optional] 

## Example

```python
from firefly_iii_client.models.recurrence_transaction_update import RecurrenceTransactionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceTransactionUpdate from a JSON string
recurrence_transaction_update_instance = RecurrenceTransactionUpdate.from_json(json)
# print the JSON string representation of the object
print(RecurrenceTransactionUpdate.to_json())

# convert the object into a dict
recurrence_transaction_update_dict = recurrence_transaction_update_instance.to_dict()
# create an instance of RecurrenceTransactionUpdate from a dict
recurrence_transaction_update_form_dict = recurrence_transaction_update.from_dict(recurrence_transaction_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


