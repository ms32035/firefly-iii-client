# BudgetSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BudgetRead**](BudgetRead.md) |  | 

## Example

```python
from firefly_iii_client.models.budget_single import BudgetSingle

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSingle from a JSON string
budget_single_instance = BudgetSingle.from_json(json)
# print the JSON string representation of the object
print(BudgetSingle.to_json())

# convert the object into a dict
budget_single_dict = budget_single_instance.to_dict()
# create an instance of BudgetSingle from a dict
budget_single_form_dict = budget_single.from_dict(budget_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


