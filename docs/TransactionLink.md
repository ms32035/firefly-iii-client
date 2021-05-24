# TransactionLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inward_id** | **str** | The inward transaction transaction_journal_id for the link. This becomes the &#39;is paid by&#39; transaction of the set. | 
**link_type_id** | **str** | The link type ID to use. You can also use the link_type_name field. | 
**outward_id** | **str** | The outward transaction transaction_journal_id for the link. This becomes the &#39;pays for&#39; transaction of the set. | 
**created_at** | **datetime** |  | [optional] [readonly] 
**link_type_name** | **str** | The link type name to use. You can also use the link_type_id field. | [optional] 
**notes** | **str, none_type** | Optional. Some notes. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


