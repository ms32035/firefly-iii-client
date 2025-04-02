# AvailableBudgetArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AvailableBudgetRead]**](AvailableBudgetRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.available_budget_array import AvailableBudgetArray

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBudgetArray from a JSON string
available_budget_array_instance = AvailableBudgetArray.from_json(json)
# print the JSON string representation of the object
print(AvailableBudgetArray.to_json())

# convert the object into a dict
available_budget_array_dict = available_budget_array_instance.to_dict()
# create an instance of AvailableBudgetArray from a dict
available_budget_array_from_dict = AvailableBudgetArray.from_dict(available_budget_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


