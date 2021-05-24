# RuleActionStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of thing this action will do. A limited set is possible. | 
**value** | **str, none_type** | The accompanying value the action will set, change or update. Can be empty, but for some types this value is mandatory. | 
**active** | **bool** | If the action is active. Defaults to true. | [optional] 
**order** | **int** | Order of the action | [optional] 
**stop_processing** | **bool** | When true, other actions will not be fired after this action has fired. Defaults to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


