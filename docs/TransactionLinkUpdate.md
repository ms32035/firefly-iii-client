# TransactionLinkUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inward_id** | **str** | The inward transaction transaction_journal_id for the link. This becomes the &#39;is paid by&#39; transaction of the set. | [optional] 
**link_type_id** | **str** | The link type ID to use. Use this field OR use the link_type_name field. | [optional] 
**link_type_name** | **str** | The link type name to use. Use this field OR use the link_type_id field. | [optional] 
**notes** | **str, none_type** | Optional. Some notes. If you submit an empty string the current notes will be removed | [optional] 
**outward_id** | **str** | The outward transaction transaction_journal_id for the link. This becomes the &#39;pays for&#39; transaction of the set. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


