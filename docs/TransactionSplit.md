# TransactionSplit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | 
**bill_id** | **str** | Optional. Use either this or the bill_name | [optional] 
**bill_name** | **str** | Optional. Use either this or the bill_id | [optional] 
**book_date** | **datetime** |  | [optional] 
**budget_id** | **str** | The budget ID for this transaction. | [optional] 
**budget_name** | **str** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] [readonly] 
**bunq_payment_id** | **str** | Internal ID of bunq transaction. DEPRECATED | [optional] 
**category_id** | **str** | The category ID for this transaction. | [optional] 
**category_name** | **str** | The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name. | [optional] 
**currency_code** | **str** | Currency code. Default is the source account&#39;s currency, or the user&#39;s default currency. Can be used instead of currency_id. | [optional] 
**currency_decimal_places** | **int** | Number of decimals used in this currency. | [optional] [readonly] 
**currency_id** | **str** | Currency ID. Default is the source account&#39;s currency, or the user&#39;s default currency. Can be used instead of currency_code. | [optional] 
**currency_name** | **str** |  | [optional] [readonly] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**var_date** | **datetime** | Date of the transaction | 
**description** | **str** | Description of the transaction. | 
**destination_iban** | **str** |  | [optional] [readonly] 
**destination_id** | **str** | ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account. | 
**destination_name** | **str** | Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough. | [optional] 
**destination_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**external_id** | **str** | Reference to external ID in other systems. | [optional] 
**external_url** | **str** | External, custom URL for this transaction. | [optional] 
**foreign_amount** | **str** | The amount in a foreign currency. | [optional] 
**foreign_currency_code** | **str** | Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount. | [optional] 
**foreign_currency_decimal_places** | **int** | Number of decimals in the currency | [optional] [readonly] 
**foreign_currency_id** | **str** | Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount. | [optional] 
**foreign_currency_symbol** | **str** |  | [optional] [readonly] 
**has_attachments** | **bool** | If the transaction has attachments. | [optional] 
**import_hash_v2** | **str** | Hash value of original import transaction (for duplicate detection). | [optional] [readonly] 
**interest_date** | **datetime** |  | [optional] 
**internal_reference** | **str** | Reference to internal reference of other systems. | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**latitude** | **float** | Latitude of the transaction&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**longitude** | **float** | Latitude of the transaction&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**notes** | **str** |  | [optional] 
**order** | **int** | Order of this entry in the list of transactions. | [optional] 
**original_source** | **str** | System generated identifier for original creator of transaction. | [optional] [readonly] 
**payment_date** | **datetime** |  | [optional] 
**process_date** | **datetime** |  | [optional] 
**reconciled** | **bool** | If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user. | [optional] 
**recurrence_count** | **int** | The # of the current transaction created under this recurrence. | [optional] [readonly] 
**recurrence_id** | **str** | Reference to recurrence that made the transaction. | [optional] [readonly] 
**recurrence_total** | **int** | Total number of transactions expected to be created by this recurrence repetition. Will be 0 if infinite. | [optional] [readonly] 
**sepa_batch_id** | **str** | SEPA Batch ID | [optional] 
**sepa_cc** | **str** | SEPA Clearing Code | [optional] 
**sepa_ci** | **str** | SEPA Creditor Identifier | [optional] 
**sepa_country** | **str** | SEPA Country | [optional] 
**sepa_ct_id** | **str** | SEPA end-to-end Identifier | [optional] 
**sepa_ct_op** | **str** | SEPA Opposing Account Identifier | [optional] 
**sepa_db** | **str** | SEPA mandate identifier | [optional] 
**sepa_ep** | **str** | SEPA External Purpose indicator | [optional] 
**source_iban** | **str** |  | [optional] [readonly] 
**source_id** | **str** | ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. | 
**source_name** | **str** | Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name. | [optional] 
**source_type** | [**AccountTypeProperty**](AccountTypeProperty.md) |  | [optional] 
**tags** | **List[str]** | Array of tags. | [optional] 
**transaction_journal_id** | **str** | ID of the underlying transaction journal. Each transaction consists of a transaction group (see the top ID) and one or more journals making up the splits of the transaction.  | [optional] [readonly] 
**type** | [**TransactionTypeProperty**](TransactionTypeProperty.md) |  | 
**user** | **str** | User ID | [optional] [readonly] 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

## Example

```python
from firefly_iii_client.models.transaction_split import TransactionSplit

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSplit from a JSON string
transaction_split_instance = TransactionSplit.from_json(json)
# print the JSON string representation of the object
print(TransactionSplit.to_json())

# convert the object into a dict
transaction_split_dict = transaction_split_instance.to_dict()
# create an instance of TransactionSplit from a dict
transaction_split_from_dict = TransactionSplit.from_dict(transaction_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


