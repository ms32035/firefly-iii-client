# BudgetLimit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**budget_id** | **int** | The budget ID of the associated budget. | 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **int** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**end** | **date** | End date of the budget limit. | 
**spent** | [**list[BudgetSpent]**](BudgetSpent.md) |  | [optional] [readonly] 
**start** | **date** | Start date of the budget limit. | 
**updated_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


