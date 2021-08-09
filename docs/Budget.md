# Budget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**active** | **bool** |  | [optional] 
**auto_budget_amount** | **str, none_type** |  | [optional] 
**auto_budget_currency_code** | **str, none_type** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_currency_id** | **str, none_type** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_period** | **str, none_type** | Period for the auto budget | [optional] 
**auto_budget_type** | **str, none_type** | The type of auto-budget that Firefly III must create. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**order** | **int** |  | [optional] [readonly] 
**spent** | [**[BudgetSpent]**](BudgetSpent.md) | Information on how much was spent in this budget. Is only filled in when the start and end date are submitted. | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


