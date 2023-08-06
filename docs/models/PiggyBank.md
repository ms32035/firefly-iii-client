# firefly_iii_client.model.piggy_bank.PiggyBank

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | str,  | str,  | The ID of the asset account this piggy bank is connected to. | 
**target_amount** | None, str,  | NoneClass, str,  |  | 
**name** | str,  | str,  |  | 
**account_name** | str,  | str,  | The name of the asset account this piggy bank is connected to. | [optional] 
**active** | bool,  | BoolClass,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**currency_code** | str,  | str,  |  | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | Number of decimals supported by the currency | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  |  | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**current_amount** | str,  | str,  |  | [optional] 
**left_to_save** | None, str,  | NoneClass, str,  |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**object_group_id** | None, str,  | NoneClass, str,  | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_order** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The order of the group. At least 1, for the highest sorting. | [optional] value must be a 32 bit integer
**object_group_title** | None, str,  | NoneClass, str,  | The name of the group. NULL if no group. | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**percentage** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 32 bit float
**save_per_month** | None, str,  | NoneClass, str,  |  | [optional] 
**start_date** | str, date,  | str,  | The date you started with this piggy bank. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**target_date** | None, str, date,  | NoneClass, str,  | The date you intend to finish saving money. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

