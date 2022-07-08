# TransactionSplitStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | 
**date** | **datetime** | Date of the transaction | 
**description** | **str** | Description of the transaction. | 
**type** | [**TransactionTypeProperty**](TransactionTypeProperty.md) |  | 
**bill_id** | **str, none_type** | Optional. Use either this or the bill_name | [optional] 
**bill_name** | **str, none_type** | Optional. Use either this or the bill_id | [optional] 
**book_date** | **datetime, none_type** |  | [optional] 
**budget_id** | **str, none_type** | The budget ID for this transaction. | [optional] 
**budget_name** | **str, none_type** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] [readonly] 
**bunq_payment_id** | **str, none_type** | Internal ID of bunq transaction. Field is no longer used but still works. | [optional] 
**category_id** | **str, none_type** | The category ID for this transaction. | [optional] 
**category_name** | **str, none_type** | The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name. | [optional] 
**currency_code** | **str, none_type** | Currency code. Default is the source account&#39;s currency, or the user&#39;s default currency. The value you submit may be overruled by the source or destination account. | [optional] 
**currency_id** | **str, none_type** | Currency ID. Default is the source account&#39;s currency, or the user&#39;s default currency. The value you submit may be overruled by the source or destination account. | [optional] 
**destination_id** | **str, none_type** | ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account. | [optional] 
**destination_name** | **str, none_type** | Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough. | [optional] 
**due_date** | **datetime, none_type** |  | [optional] 
**external_id** | **str, none_type** | Reference to external ID in other systems. | [optional] 
**external_url** | **str, none_type** | External, custom URL for this transaction. | [optional] 
**foreign_amount** | **str, none_type** | The amount in a foreign currency. | [optional] 
**foreign_currency_code** | **str, none_type** | Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount. | [optional] 
**foreign_currency_id** | **str, none_type** | Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount. | [optional] 
**interest_date** | **datetime, none_type** |  | [optional] 
**internal_reference** | **str, none_type** | Reference to internal reference of other systems. | [optional] 
**invoice_date** | **datetime, none_type** |  | [optional] 
**notes** | **str, none_type** |  | [optional] 
**order** | **int, none_type** | Order of this entry in the list of transactions. | [optional] 
**payment_date** | **datetime, none_type** |  | [optional] 
**piggy_bank_id** | **int** | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | **str** | Optional. Use either this or the piggy_bank_id | [optional] 
**process_date** | **datetime, none_type** |  | [optional] 
**reconciled** | **bool** | If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user. | [optional] 
**sepa_batch_id** | **str, none_type** | SEPA Batch ID | [optional] 
**sepa_cc** | **str, none_type** | SEPA Clearing Code | [optional] 
**sepa_ci** | **str, none_type** | SEPA Creditor Identifier | [optional] 
**sepa_country** | **str, none_type** | SEPA Country | [optional] 
**sepa_ct_id** | **str, none_type** | SEPA end-to-end Identifier | [optional] 
**sepa_ct_op** | **str, none_type** | SEPA Opposing Account Identifier | [optional] 
**sepa_db** | **str, none_type** | SEPA mandate identifier | [optional] 
**sepa_ep** | **str, none_type** | SEPA External Purpose indicator | [optional] 
**source_id** | **str, none_type** | ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. | [optional] 
**source_name** | **str, none_type** | Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name. | [optional] 
**tags** | **[str], none_type** | Array of tags. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


