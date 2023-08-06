# firefly_iii_client.model.basic_summary_entry.BasicSummaryEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currency_code** | str,  | str,  |  | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | Number of decimals for the associated currency. | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  | The currency ID of the associated currency. | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**key** | str,  | str,  | This is a reference to the type of info shared, not influenced by translations or user preferences. The EUR value is a reference to the currency code. Possibilities are: balance-in-ABC, spent-in-ABC, earned-in-ABC, bills-paid-in-ABC, bills-unpaid-in-ABC, left-to-spend-in-ABC and net-worth-in-ABC. | [optional] 
**local_icon** | str,  | str,  | Reference to a font-awesome icon without the fa- part. | [optional] 
**monetary_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount as a float. | [optional] value must be a 64 bit float
**sub_title** | str,  | str,  | A short explanation of the amounts origin. Already formatted according to the locale of the user or translated, if relevant. | [optional] 
**title** | str,  | str,  | A translated title for the information shared. | [optional] 
**value_parsed** | str,  | str,  | The amount formatted according to the users locale | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

