# RuleTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of thing this trigger responds to. A limited set is possible | 
**value** | **str** | The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger. | 
**active** | **bool** | If the trigger is active. Defaults to true. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**order** | **int** | Order of the trigger | [optional] [readonly] 
**stop_processing** | **bool** | When true, other triggers will not be checked if this trigger was triggered. Defaults to false. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


