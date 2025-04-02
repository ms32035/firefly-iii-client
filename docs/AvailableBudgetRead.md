# AvailableBudgetRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AvailableBudget**](AvailableBudget.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.available_budget_read import AvailableBudgetRead

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBudgetRead from a JSON string
available_budget_read_instance = AvailableBudgetRead.from_json(json)
# print the JSON string representation of the object
print(AvailableBudgetRead.to_json())

# convert the object into a dict
available_budget_read_dict = available_budget_read_instance.to_dict()
# create an instance of AvailableBudgetRead from a dict
available_budget_read_from_dict = AvailableBudgetRead.from_dict(available_budget_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


