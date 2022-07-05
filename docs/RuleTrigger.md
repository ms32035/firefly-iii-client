# RuleTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RuleTriggerKeyword**](RuleTriggerKeyword.md) |  | 
**value** | **str** | The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger. | 
**active** | **bool** | If the trigger is active. Defaults to true. | [optional]  if omitted the server will use the default value of True
**created_at** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**order** | **int** | Order of the trigger | [optional] [readonly] 
**stop_processing** | **bool** | When true, other triggers will not be checked if this trigger was triggered. Defaults to false. | [optional]  if omitted the server will use the default value of False
**updated_at** | **datetime** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


