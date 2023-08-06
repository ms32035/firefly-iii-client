# firefly_iii_client.model.budget_store.BudgetStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**active** | bool,  | BoolClass,  |  | [optional] 
**auto_budget_amount** | None, str,  | NoneClass, str,  |  | [optional] 
**auto_budget_currency_code** | None, str,  | NoneClass, str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**auto_budget_currency_id** | None, str,  | NoneClass, str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**auto_budget_period** | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) |  | [optional] 
**auto_budget_type** | [**AutoBudgetType**](AutoBudgetType.md) | [**AutoBudgetType**](AutoBudgetType.md) |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

