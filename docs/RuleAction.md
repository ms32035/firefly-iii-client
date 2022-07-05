# RuleAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RuleActionKeyword**](RuleActionKeyword.md) |  | 
**value** | **str, none_type** | The accompanying value the action will set, change or update. Can be empty, but for some types this value is mandatory. | 
**active** | **bool** | If the action is active. Defaults to true. | [optional]  if omitted the server will use the default value of True
**created_at** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**order** | **int** | Order of the action | [optional] 
**stop_processing** | **bool** | When true, other actions will not be fired after this action has fired. Defaults to false. | [optional]  if omitted the server will use the default value of False
**updated_at** | **datetime** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


