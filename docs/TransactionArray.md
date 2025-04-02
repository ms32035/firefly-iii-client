# TransactionArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionRead]**](TransactionRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.transaction_array import TransactionArray

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionArray from a JSON string
transaction_array_instance = TransactionArray.from_json(json)
# print the JSON string representation of the object
print(TransactionArray.to_json())

# convert the object into a dict
transaction_array_dict = transaction_array_instance.to_dict()
# create an instance of TransactionArray from a dict
transaction_array_from_dict = TransactionArray.from_dict(transaction_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


