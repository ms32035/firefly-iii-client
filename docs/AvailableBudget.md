# AvailableBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** | Use either currency_id or currency_code. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | Use either currency_id or currency_code. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**end** | **datetime** | End date of the available budget. | 
**native_amount** | **str** | The amount of this available budget in the native currency of this administration. | [optional] 
**native_currency_code** | **str** | The currency code of the administration&#39;s native currency. | [optional] [readonly] 
**native_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s native currency. | [optional] [readonly] 
**native_currency_id** | **str** | The currency ID of the administration&#39;s native currency. | [optional] [readonly] 
**native_currency_symbol** | **str** | The currency symbol of the administration&#39;s native currency. | [optional] [readonly] 
**spent_in_budgets** | [**List[BudgetSpent]**](BudgetSpent.md) |  | [optional] [readonly] 
**spent_outside_budget** | [**List[BudgetSpent]**](BudgetSpent.md) |  | [optional] [readonly] 
**start** | **datetime** | Start date of the available budget. | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.available_budget import AvailableBudget

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBudget from a JSON string
available_budget_instance = AvailableBudget.from_json(json)
# print the JSON string representation of the object
print(AvailableBudget.to_json())

# convert the object into a dict
available_budget_dict = available_budget_instance.to_dict()
# create an instance of AvailableBudget from a dict
available_budget_from_dict = AvailableBudget.from_dict(available_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


