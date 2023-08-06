# firefly_iii_client.model.currency_update.CurrencyUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The currency code | [optional] 
**decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | How many decimals to use when displaying this currency. Between 0 and 16. | [optional] value must be a 32 bit integer
**default** | bool,  | BoolClass,  | If the currency must be the default for the user. You can only submit TRUE. | [optional] must be one of [True, ] 
**enabled** | bool,  | BoolClass,  | If the currency is enabled | [optional] 
**name** | str,  | str,  | The currency name | [optional] 
**symbol** | str,  | str,  | The currency symbol | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

