# BudgetProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**auto_budget_amount** | **str** | The amount for the auto-budget, if set. | [optional] 
**auto_budget_period** | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) |  | [optional] 
**auto_budget_type** | [**AutoBudgetType**](AutoBudgetType.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_order** | **int** | The order of the group. At least 1, for the highest sorting. | [optional] [readonly] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 
**object_has_currency_setting** | **bool** | Indicates whether the object has a currency setting. If false, the object uses the administration&#39;s primary currency. | [optional] [readonly] 
**order** | **int** |  | [optional] [readonly] 
**pc_auto_budget_amount** | **str** | The amount for the auto-budget, if set in the primary currency of the administration. | [optional] 
**pc_spent** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Information on how much was spent in this budget. Is only filled in when the start and end date are submitted. It is converted to the primary currency of the administration. | [optional] [readonly] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**spent** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Information on how much was spent in this budget. Is only filled in when the start and end date are submitted. | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.budget_properties import BudgetProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetProperties from a JSON string
budget_properties_instance = BudgetProperties.from_json(json)
# print the JSON string representation of the object
print(BudgetProperties.to_json())

# convert the object into a dict
budget_properties_dict = budget_properties_instance.to_dict()
# create an instance of BudgetProperties from a dict
budget_properties_from_dict = BudgetProperties.from_dict(budget_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


