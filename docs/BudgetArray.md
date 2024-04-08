# BudgetArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BudgetRead]**](BudgetRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.budget_array import BudgetArray

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetArray from a JSON string
budget_array_instance = BudgetArray.from_json(json)
# print the JSON string representation of the object
print(BudgetArray.to_json())

# convert the object into a dict
budget_array_dict = budget_array_instance.to_dict()
# create an instance of BudgetArray from a dict
budget_array_form_dict = budget_array.from_dict(budget_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


