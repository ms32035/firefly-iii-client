# firefly_iii_client.model.available_budget.AvailableBudget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  |  | 
**start** | str, datetime,  | str,  | Start date of the available budget. | value must conform to RFC-3339 date-time
**end** | str, datetime,  | str,  | End date of the available budget. | value must conform to RFC-3339 date-time
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**currency_code** | str,  | str,  | Use either currency_id or currency_code. | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  | Use either currency_id or currency_code. | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**[spent_in_budgets](#spent_in_budgets)** | list, tuple,  | tuple,  |  | [optional] 
**[spent_outside_budget](#spent_outside_budget)** | list, tuple,  | tuple,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# spent_in_budgets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BudgetSpent**](BudgetSpent.md) | [**BudgetSpent**](BudgetSpent.md) | [**BudgetSpent**](BudgetSpent.md) |  | 

# spent_outside_budget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BudgetSpent**](BudgetSpent.md) | [**BudgetSpent**](BudgetSpent.md) | [**BudgetSpent**](BudgetSpent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

