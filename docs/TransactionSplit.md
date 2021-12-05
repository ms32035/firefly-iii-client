# TransactionSplit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | 
**date** | **datetime** | Date of the transaction | 
**description** | **str** | Description of the transaction. | 
**destination_id** | **str, none_type** | ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account. | 
**source_id** | **str, none_type** | ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. | 
**type** | **str** | Type of transaction. | 
**bill_id** | **str, none_type** | Optional. Use either this or the bill_name | [optional] 
**bill_name** | **str, none_type** | Optional. Use either this or the bill_id | [optional] 
**book_date** | **datetime, none_type** |  | [optional] 
**budget_id** | **str, none_type** | The budget ID for this transaction. | [optional] 
**budget_name** | **str, none_type** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] [readonly] 
**bunq_payment_id** | **str, none_type** | Internal ID of bunq transaction. DEPRECATED | [optional] 
**category_id** | **str, none_type** | The category ID for this transaction. | [optional] 
**category_name** | **str, none_type** | The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name. | [optional] 
**currency_code** | **str, none_type** | Currency code. Default is the source account&#39;s currency, or the user&#39;s default currency. Can be used instead of currency_id. | [optional] 
**currency_decimal_places** | **int** | Number of decimals used in this currency. | [optional] [readonly] 
**currency_id** | **str, none_type** | Currency ID. Default is the source account&#39;s currency, or the user&#39;s default currency. Can be used instead of currency_code. | [optional] 
**currency_name** | **str** |  | [optional] [readonly] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**destination_iban** | **str, none_type** |  | [optional] [readonly] 
**destination_name** | **str, none_type** | Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough. | [optional] 
**destination_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**due_date** | **datetime, none_type** |  | [optional] 
**external_id** | **str, none_type** | Reference to external ID in other systems. | [optional] 
**foreign_amount** | **str, none_type** | The amount in a foreign currency. | [optional] 
**foreign_currency_code** | **str, none_type** | Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount. | [optional] 
**foreign_currency_decimal_places** | **int, none_type** | Number of decimals in the currency | [optional] [readonly] 
**foreign_currency_id** | **str, none_type** | Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount. | [optional] 
**foreign_currency_symbol** | **str, none_type** |  | [optional] [readonly] 
**import_hash_v2** | **str, none_type** | Hash value of original import transaction (for duplicate detection). | [optional] [readonly] 
**interest_date** | **datetime, none_type** |  | [optional] 
**internal_reference** | **str, none_type** | Reference to internal reference of other systems. | [optional] 
**invoice_date** | **datetime, none_type** |  | [optional] 
**latitude** | **float, none_type** | Latitude of the transaction&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**longitude** | **float, none_type** | Latitude of the transaction&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**order** | **int, none_type** | Order of this entry in the list of transactions. | [optional] 
**original_source** | **str, none_type** | System generated identifier for original creator of transaction. | [optional] [readonly] 
**payment_date** | **datetime, none_type** |  | [optional] 
**process_date** | **datetime, none_type** |  | [optional] 
**reconciled** | **bool** | If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user. | [optional] 
**recurrence_count** | **int, none_type** | The # of the current transaction created under this recurrence. | [optional] [readonly] 
**recurrence_id** | **int, none_type** | Reference to recurrence that made the transaction. | [optional] [readonly] 
**recurrence_total** | **int, none_type** | Total number of transactions expected to be created by this recurrence repetition. Will be 0 if infinite. | [optional] [readonly] 
**sepa_batch_id** | **str, none_type** | SEPA Batch ID | [optional] 
**sepa_cc** | **str, none_type** | SEPA Clearing Code | [optional] 
**sepa_ci** | **str, none_type** | SEPA Creditor Identifier | [optional] 
**sepa_country** | **str, none_type** | SEPA Country | [optional] 
**sepa_ct_id** | **str, none_type** | SEPA end-to-end Identifier | [optional] 
**sepa_ct_op** | **str, none_type** | SEPA Opposing Account Identifier | [optional] 
**sepa_db** | **str, none_type** | SEPA mandate identifier | [optional] 
**sepa_ep** | **str, none_type** | SEPA External Purpose indicator | [optional] 
**source_iban** | **str, none_type** |  | [optional] [readonly] 
**source_name** | **str, none_type** | Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name. | [optional] 
**source_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**tags** | **[str], none_type** | Array of tags. | [optional] 
**transaction_journal_id** | **str** | ID of the underlying transaction journal. Each transaction consists of a transaction group (see the top ID) and one or more journals making up the splits of the transaction.  | [optional] [readonly] 
**user** | **str** | User ID | [optional] [readonly] 
**zoom_level** | **int, none_type** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


