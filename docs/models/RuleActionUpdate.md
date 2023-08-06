# firefly_iii_client.model.rule_action_update.RuleActionUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**active** | bool,  | BoolClass,  | If the action is active. | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the action | [optional] value must be a 32 bit integer
**stop_processing** | bool,  | BoolClass,  | When true, other actions will not be fired after this action has fired. | [optional] 
**type** | [**RuleActionKeyword**](RuleActionKeyword.md) | [**RuleActionKeyword**](RuleActionKeyword.md) |  | [optional] 
**value** | None, str,  | NoneClass, str,  | The accompanying value the action will set, change or update. Can be empty, but for some types this value is mandatory. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

