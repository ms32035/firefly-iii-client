# TransactionRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Transaction**](Transaction.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.transaction_read import TransactionRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRead from a JSON string
transaction_read_instance = TransactionRead.from_json(json)
# print the JSON string representation of the object
print(TransactionRead.to_json())

# convert the object into a dict
transaction_read_dict = transaction_read_instance.to_dict()
# create an instance of TransactionRead from a dict
transaction_read_from_dict = TransactionRead.from_dict(transaction_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


