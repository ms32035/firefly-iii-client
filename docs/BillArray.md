# BillArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillRead]**](BillRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.bill_array import BillArray

# TODO update the JSON string below
json = "{}"
# create an instance of BillArray from a JSON string
bill_array_instance = BillArray.from_json(json)
# print the JSON string representation of the object
print(BillArray.to_json())

# convert the object into a dict
bill_array_dict = bill_array_instance.to_dict()
# create an instance of BillArray from a dict
bill_array_from_dict = BillArray.from_dict(bill_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


