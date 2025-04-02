# BudgetUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**auto_budget_amount** | **str** |  | [optional] 
**auto_budget_currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_period** | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) |  | [optional] 
**auto_budget_type** | [**AutoBudgetType**](AutoBudgetType.md) |  | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from firefly_iii_client.models.budget_update import BudgetUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUpdate from a JSON string
budget_update_instance = BudgetUpdate.from_json(json)
# print the JSON string representation of the object
print(BudgetUpdate.to_json())

# convert the object into a dict
budget_update_dict = budget_update_instance.to_dict()
# create an instance of BudgetUpdate from a dict
budget_update_from_dict = BudgetUpdate.from_dict(budget_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


