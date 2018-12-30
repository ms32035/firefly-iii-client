# RecurrenceMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This field contains the meta-information for the transaction that must be stored. | [optional] 
**piggy_bank_id** | **int** | Piggy bank ID. Will only be set when the name is &#39;piggy_bank_id&#39;. This value will then be equal to &#39;value&#39;. | [optional] 
**piggy_bank_name** | **str** | Piggy bank name. Will only be set when the name is &#39;piggy_bank_id&#39;. | [optional] 
**tags** | **list[str]** | An array of tags (so the exploded version of the name-field). Will only be set when the name is &#39;tags&#39;. | [optional] 
**value** | **str** | Either the (valid) ID of a piggy bank or a comma separated list of tags. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


