# RuleAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**list[RuleAction]**](RuleAction.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**rule_group_id** | **int** | Reference to the rule group of which this rule is a part. | [optional] 
**stop_processing** | **bool** | If set to true, other rules in this group will not fire if this rule has fired. | [optional] 
**strict** | **bool** | When the rule is strict, ALL triggers must be triggerd for the actions to fire. If not, one is enough. | [optional] 
**title** | **str** |  | [optional] 
**triggers** | [**list[RuleTrigger]**](RuleTrigger.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


