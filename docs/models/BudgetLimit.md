# firefly_iii_client.model.budget_limit.BudgetLimit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  |  | 
**budget_id** | str,  | str,  | The budget ID of the associated budget. | 
**start** | str, datetime,  | str,  | Start date of the budget limit. | value must conform to RFC-3339 date-time
**end** | str, datetime,  | str,  | End date of the budget limit. | value must conform to RFC-3339 date-time
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**currency_code** | str,  | str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**currency_name** | str,  | str,  |  | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**period** | None, str,  | NoneClass, str,  | Period of the budget limit. Only used when auto-generated by auto-budget. | [optional] 
**spent** | None, str,  | NoneClass, str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

