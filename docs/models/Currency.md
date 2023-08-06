# firefly_iii_client.model.currency.Currency

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | 
**code** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | Supports 0-16 decimals. | [optional] value must be a 32 bit integer
**default** | bool,  | BoolClass,  | Make this currency the default currency. | [optional] 
**enabled** | bool,  | BoolClass,  | Defaults to true | [optional] if omitted the server will use the default value of True
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

