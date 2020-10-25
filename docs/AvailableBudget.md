# AvailableBudget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** | Use either currency_id or currency_code. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **int** | Use either currency_id or currency_code. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**end** | **date** | End date of the available budget. | 
**spent_in_budgets** | [**list[BudgetSpent]**](BudgetSpent.md) |  | [optional] [readonly] 
**spent_outside_budget** | [**list[BudgetSpent]**](BudgetSpent.md) |  | [optional] [readonly] 
**start** | **date** | Start date of the available budget. | 
**updated_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


