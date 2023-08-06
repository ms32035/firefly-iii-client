# firefly_iii_client.model.tag_model.TagModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tag** | str,  | str,  | The tag | 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**date** | None, str, date,  | NoneClass, str,  | The date to which the tag is applicable. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**latitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude of the tag&#x27;s location, if applicable. Can be used to draw a map. | [optional] value must be a 64 bit float
**longitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude of the tag&#x27;s location, if applicable. Can be used to draw a map. | [optional] value must be a 64 bit float
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**zoom_level** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

