# firefly_iii_client.model.bill_store.BillStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | str,  | str,  |  | 
**amount_max** | str,  | str,  |  | 
**amount_min** | str,  | str,  |  | 
**repeat_freq** | [**BillRepeatFrequency**](BillRepeatFrequency.md) | [**BillRepeatFrequency**](BillRepeatFrequency.md) |  | 
**active** | bool,  | BoolClass,  | If the bill is active. | [optional] 
**currency_code** | str,  | str,  | Use either currency_id or currency_code | [optional] 
**currency_id** | str,  | str,  | Use either currency_id or currency_code | [optional] 
**end_date** | str, datetime,  | str,  | The date after which this bill is no longer valid or applicable | [optional] value must conform to RFC-3339 date-time
**extension_date** | str, datetime,  | str,  | The date before which the bill must be renewed (or cancelled) | [optional] value must conform to RFC-3339 date-time
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**object_group_id** | None, str,  | NoneClass, str,  | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | None, str,  | NoneClass, str,  | The name of the group. NULL if no group. | [optional] 
**skip** | decimal.Decimal, int,  | decimal.Decimal,  | How often the bill must be skipped. 1 means a bi-monthly bill. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

