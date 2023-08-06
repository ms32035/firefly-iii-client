# firefly_iii_client.model.insight_total_entry.InsightTotalEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currency_code** | str,  | str,  | The currency code of the expenses listed for this expense account. | [optional] 
**currency_id** | str,  | str,  | The currency ID of the expenses listed for this expense account. | [optional] 
**difference** | str,  | str,  | The amount spent between start date and end date, defined as a string, for this expense account and all asset accounts. | [optional] 
**difference_float** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount spent between start date and end date, defined as a string, for this expense account and all asset accounts. This number is a float (double) and may have rounding errors. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

