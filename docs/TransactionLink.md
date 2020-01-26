# TransactionLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**inward_id** | **int** | The inward transaction transaction_journal_id for the link. This becomes the &#39;is paid by&#39; transaction of the set. | 
**link_type_id** | **int** | The link type ID to use. You can also use the link_type_name field. | 
**link_type_name** | **str** | The link type name to use. You can also use the link_type_id field. | [optional] 
**notes** | **str** | Optional. Some notes. | [optional] 
**outward_id** | **int** | The outward transaction transaction_journal_id for the link. This becomes the &#39;pays for&#39; transaction of the set. | 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


