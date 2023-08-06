# firefly_iii_client.model.rule.Rule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**trigger** | [**RuleTriggerType**](RuleTriggerType.md) | [**RuleTriggerType**](RuleTriggerType.md) |  | 
**rule_group_id** | str,  | str,  | ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory. | 
**title** | str,  | str,  |  | 
**[triggers](#triggers)** | list, tuple,  | tuple,  |  | 
**[actions](#actions)** | list, tuple,  | tuple,  |  | 
**active** | bool,  | BoolClass,  | Whether or not the rule is even active. Default is true. | [optional] if omitted the server will use the default value of True
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  |  | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**rule_group_title** | str,  | str,  | Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory. | [optional] 
**stop_processing** | bool,  | BoolClass,  | If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false. | [optional] if omitted the server will use the default value of False
**strict** | bool,  | BoolClass,  | If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true. | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RuleAction**](RuleAction.md) | [**RuleAction**](RuleAction.md) | [**RuleAction**](RuleAction.md) |  | 

# triggers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RuleTrigger**](RuleTrigger.md) | [**RuleTrigger**](RuleTrigger.md) | [**RuleTrigger**](RuleTrigger.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

