# firefly_iii_client.model.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  | The new users email address. | 
**blocked** | bool,  | BoolClass,  | Boolean to indicate if the user is blocked. | [optional] 
**blocked_code** | [**UserBlockedCodeProperty**](UserBlockedCodeProperty.md) | [**UserBlockedCodeProperty**](UserBlockedCodeProperty.md) |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**role** | [**UserRoleProperty**](UserRoleProperty.md) | [**UserRoleProperty**](UserRoleProperty.md) |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

