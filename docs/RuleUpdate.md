# RuleUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[RuleActionUpdate]**](RuleActionUpdate.md) |  | [optional] 
**active** | **bool** | Whether or not the rule is even active. Default is true. | [optional]  if omitted the server will use the default value of True
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**rule_group_id** | **str** | ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory. | [optional] 
**stop_processing** | **bool** | If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false. | [optional]  if omitted the server will use the default value of False
**strict** | **bool** | If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true. | [optional] 
**title** | **str** |  | [optional] 
**trigger** | [**RuleTriggerType**](RuleTriggerType.md) |  | [optional] 
**triggers** | [**[RuleTriggerUpdate]**](RuleTriggerUpdate.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


