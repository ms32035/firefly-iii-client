# firefly_iii_client.model.configuration.Configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**editable** | bool,  | BoolClass,  | If this config variable can be edited by the user | 
**title** | [**ConfigValueFilter**](ConfigValueFilter.md) | [**ConfigValueFilter**](ConfigValueFilter.md) |  | 
**value** | [**PolymorphicProperty**](PolymorphicProperty.md) | [**PolymorphicProperty**](PolymorphicProperty.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

