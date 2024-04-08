# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**group_title** | **str** | Title of the transaction if it has been split in more than one piece. Empty otherwise. | [optional] 
**transactions** | [**List[TransactionSplit]**](TransactionSplit.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**user** | **str** | User ID | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


