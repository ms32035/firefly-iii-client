# BudgetLimitSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BudgetLimitRead**](BudgetLimitRead.md) |  | 

## Example

```python
from firefly_iii_client.models.budget_limit_single import BudgetLimitSingle

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLimitSingle from a JSON string
budget_limit_single_instance = BudgetLimitSingle.from_json(json)
# print the JSON string representation of the object
print(BudgetLimitSingle.to_json())

# convert the object into a dict
budget_limit_single_dict = budget_limit_single_instance.to_dict()
# create an instance of BudgetLimitSingle from a dict
budget_limit_single_from_dict = BudgetLimitSingle.from_dict(budget_limit_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


