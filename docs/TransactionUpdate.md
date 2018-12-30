# TransactionUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_id** | **int** | Optional. Use either this or the bill_name | [optional] 
**bill_name** | **str** | Optional. Use either this or the bill_id | [optional] 
**book_date** | **date** |  | [optional] 
**bunq_payment_id** | **str** |  | [optional] 
**date** | **date** |  | 
**description** | **str** |  | 
**due_date** | **date** |  | [optional] 
**external_id** | **str** | Reference to external ID in other systems. | [optional] 
**interest_date** | **date** |  | [optional] 
**internal_reference** | **str** | Reference to internal reference of other systems. | [optional] 
**invoice_date** | **date** |  | [optional] 
**notes** | **str** |  | [optional] 
**payment_date** | **date** |  | [optional] 
**piggy_bank_id** | **int** | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | **str** | Optional. Use either this or the piggy_bank_id | [optional] 
**process_date** | **date** |  | [optional] 
**sepa_batch_id** | **str** | SEPA Batch ID | [optional] 
**sepa_cc** | **str** | SEPA Clearing Code | [optional] 
**sepa_ci** | **str** | SEPA Creditor Identifier | [optional] 
**sepa_country** | **str** | SEPA Country | [optional] 
**sepa_ct_id** | **str** | SEPA end-to-end Identifier | [optional] 
**sepa_ct_op** | **str** | SEPA Opposing Account Identifier | [optional] 
**sepa_db** | **str** | SEPA mandate identifier | [optional] 
**sepa_ep** | **str** | SEPA External Purpose indicator | [optional] 
**tags** | **str** | Comma-separated list of tags. | [optional] 
**transactions** | [**list[TransactionSplitUpdate]**](TransactionSplitUpdate.md) |  | 
**type** | **str** | Type of transaction | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


