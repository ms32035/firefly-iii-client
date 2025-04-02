# BillSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BillRead**](BillRead.md) |  | 

## Example

```python
from firefly_iii_client.models.bill_single import BillSingle

# TODO update the JSON string below
json = "{}"
# create an instance of BillSingle from a JSON string
bill_single_instance = BillSingle.from_json(json)
# print the JSON string representation of the object
print(BillSingle.to_json())

# convert the object into a dict
bill_single_dict = bill_single_instance.to_dict()
# create an instance of BillSingle from a dict
bill_single_from_dict = BillSingle.from_dict(bill_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


