# firefly_iii_client.model.available_budget_store.AvailableBudgetStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  |  | 
**start** | str, date,  | str,  | Start date of the available budget. | value must conform to RFC-3339 full-date YYYY-MM-DD
**end** | str, date,  | str,  | End date of the available budget. | value must conform to RFC-3339 full-date YYYY-MM-DD
**currency_code** | str,  | str,  | Use either currency_id or currency_code. | [optional] 
**currency_id** | str,  | str,  | Use either currency_id or currency_code. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

