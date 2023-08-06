# firefly_iii_client.model.piggy_bank_store.PiggyBankStore

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
**active** | bool,  | BoolClass,  |  | [optional] 
**current_amount** | str,  | str,  |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**object_group_id** | None, str,  | NoneClass, str,  | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | None, str,  | NoneClass, str,  | The name of the group. NULL if no group. | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**start_date** | str, date,  | str,  | The date you started with this piggy bank. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**target_date** | None, str, date,  | NoneClass, str,  | The date you intend to finish saving money. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

