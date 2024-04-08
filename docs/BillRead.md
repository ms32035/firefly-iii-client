# BillRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Bill**](Bill.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.bill_read import BillRead

# TODO update the JSON string below
json = "{}"
# create an instance of BillRead from a JSON string
bill_read_instance = BillRead.from_json(json)
# print the JSON string representation of the object
print(BillRead.to_json())

# convert the object into a dict
bill_read_dict = bill_read_instance.to_dict()
# create an instance of BillRead from a dict
bill_read_form_dict = bill_read.from_dict(bill_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


