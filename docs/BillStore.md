# BillStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_max** | **str** |  | 
**amount_min** | **str** |  | 
**date** | **datetime** |  | 
**name** | **str** |  | 
**repeat_freq** | [**BillRepeatFrequency**](BillRepeatFrequency.md) |  | 
**active** | **bool** | If the bill is active. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code | [optional] 
**currency_id** | **str** | Use either currency_id or currency_code | [optional] 
**end_date** | **datetime** | The date after which this bill is no longer valid or applicable | [optional] 
**extension_date** | **datetime** | The date before which the bill must be renewed (or cancelled) | [optional] 
**notes** | **str, none_type** |  | [optional] 
**object_group_id** | **str, none_type** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str, none_type** | The name of the group. NULL if no group. | [optional] 
**skip** | **int** | How often the bill must be skipped. 1 means a bi-monthly bill. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


