# RuleActionUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the action is active. | [optional] 
**order** | **int** | Order of the action | [optional] 
**stop_processing** | **bool** | When true, other actions will not be fired after this action has fired. | [optional] 
**type** | **str** | The type of thing this action will do. A limited set is possible. | [optional] 
**value** | **str, none_type** | The accompanying value the action will set, change or update. Can be empty, but for some types this value is mandatory. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


