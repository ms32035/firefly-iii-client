# AvailableBudgetProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount of this available budget in the currency of this available budget. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**end** | **datetime** | End date of the available budget. | [optional] 
**object_has_currency_setting** | **bool** | Indicates whether the object has a currency setting. If false, the object uses the administration&#39;s primary currency. | [optional] [readonly] 
**pc_amount** | **str** | The amount of this available budget in the primary currency (pc) of this administration. | [optional] 
**pc_spent_in_budgets** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | The amount spent in budgets in the primary currency (pc) of this administration.  | [optional] [readonly] 
**pc_spent_outside_budgets** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | The amount spent outside of budgets in the primary currency (pc) of this administration.  | [optional] [readonly] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**spent_in_budgets** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) |  | [optional] [readonly] 
**spent_outside_budgets** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) |  | [optional] [readonly] 
**start** | **datetime** | Start date of the available budget. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.available_budget_properties import AvailableBudgetProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBudgetProperties from a JSON string
available_budget_properties_instance = AvailableBudgetProperties.from_json(json)
# print the JSON string representation of the object
print(AvailableBudgetProperties.to_json())

# convert the object into a dict
available_budget_properties_dict = available_budget_properties_instance.to_dict()
# create an instance of AvailableBudgetProperties from a dict
available_budget_properties_from_dict = AvailableBudgetProperties.from_dict(available_budget_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


