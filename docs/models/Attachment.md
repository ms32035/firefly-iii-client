# firefly_iii_client.model.attachment.Attachment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**filename** | str,  | str,  |  | 
**attachable_id** | str,  | str,  | ID of the model this attachment is linked to. | 
**attachable_type** | [**AttachableType**](AttachableType.md) | [**AttachableType**](AttachableType.md) |  | 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**download_url** | str,  | str,  |  | [optional] 
**md5** | str,  | str,  | MD5 hash of the file for basic duplicate detection. | [optional] 
**mime** | str,  | str,  |  | [optional] 
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**title** | str,  | str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**upload_url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

