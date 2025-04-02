# BudgetLimitArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BudgetLimitRead]**](BudgetLimitRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.budget_limit_array import BudgetLimitArray

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLimitArray from a JSON string
budget_limit_array_instance = BudgetLimitArray.from_json(json)
# print the JSON string representation of the object
print(BudgetLimitArray.to_json())

# convert the object into a dict
budget_limit_array_dict = budget_limit_array_instance.to_dict()
# create an instance of BudgetLimitArray from a dict
budget_limit_array_from_dict = BudgetLimitArray.from_dict(budget_limit_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


