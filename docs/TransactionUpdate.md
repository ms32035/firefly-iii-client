# TransactionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_rules** | **bool** | Whether or not to apply rules when submitting transaction. | [optional] 
**fire_webhooks** | **bool** | Whether or not to fire the webhooks that are related to this event. | [optional] [default to True]
**group_title** | **str** | Title of the transaction if it has been split in more than one piece. Empty otherwise. | [optional] 
**transactions** | [**List[TransactionSplitUpdate]**](TransactionSplitUpdate.md) |  | [optional] 

## Example

```python
from firefly_iii_client.models.transaction_update import TransactionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUpdate from a JSON string
transaction_update_instance = TransactionUpdate.from_json(json)
# print the JSON string representation of the object
print(TransactionUpdate.to_json())

# convert the object into a dict
transaction_update_dict = transaction_update_instance.to_dict()
# create an instance of TransactionUpdate from a dict
transaction_update_form_dict = transaction_update.from_dict(transaction_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


