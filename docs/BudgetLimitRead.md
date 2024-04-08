# BudgetLimitRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**BudgetLimit**](BudgetLimit.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.budget_limit_read import BudgetLimitRead

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLimitRead from a JSON string
budget_limit_read_instance = BudgetLimitRead.from_json(json)
# print the JSON string representation of the object
print(BudgetLimitRead.to_json())

# convert the object into a dict
budget_limit_read_dict = budget_limit_read_instance.to_dict()
# create an instance of BudgetLimitRead from a dict
budget_limit_read_form_dict = budget_limit_read.from_dict(budget_limit_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


