# TransactionSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionRead**](TransactionRead.md) |  | 

## Example

```python
from firefly_iii_client.models.transaction_single import TransactionSingle

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSingle from a JSON string
transaction_single_instance = TransactionSingle.from_json(json)
# print the JSON string representation of the object
print(TransactionSingle.to_json())

# convert the object into a dict
transaction_single_dict = transaction_single_instance.to_dict()
# create an instance of TransactionSingle from a dict
transaction_single_form_dict = transaction_single.from_dict(transaction_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


