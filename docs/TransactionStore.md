# TransactionStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_rules** | **bool** | Whether or not to apply rules when submitting transaction. | [optional] 
**error_if_duplicate_hash** | **bool** | Break if the submitted transaction exists already. | [optional] 
**fire_webhooks** | **bool** | Whether or not to fire the webhooks that are related to this event. | [optional] [default to True]
**group_title** | **str** | Title of the transaction if it has been split in more than one piece. Empty otherwise. | [optional] 
**transactions** | [**List[TransactionSplitStore]**](TransactionSplitStore.md) |  | 

## Example

```python
from firefly_iii_client.models.transaction_store import TransactionStore

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStore from a JSON string
transaction_store_instance = TransactionStore.from_json(json)
# print the JSON string representation of the object
print(TransactionStore.to_json())

# convert the object into a dict
transaction_store_dict = transaction_store_instance.to_dict()
# create an instance of TransactionStore from a dict
transaction_store_form_dict = transaction_store.from_dict(transaction_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


