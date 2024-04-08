# TransactionSplitStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount of the transaction. | 
**bill_id** | **str** | Optional. Use either this or the bill_name | [optional] 
**bill_name** | **str** | Optional. Use either this or the bill_id | [optional] 
**book_date** | **datetime** |  | [optional] 
**budget_id** | **str** | The budget ID for this transaction. | [optional] 
**budget_name** | **str** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] [readonly] 
**bunq_payment_id** | **str** | Internal ID of bunq transaction. Field is no longer used but still works. | [optional] 
**category_id** | **str** | The category ID for this transaction. | [optional] 
**category_name** | **str** | The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name. | [optional] 
**currency_code** | **str** | Currency code. Default is the source account&#39;s currency, or the user&#39;s default currency. The value you submit may be overruled by the source or destination account. | [optional] 
**currency_id** | **str** | Currency ID. Default is the source account&#39;s currency, or the user&#39;s default currency. The value you submit may be overruled by the source or destination account. | [optional] 
**var_date** | **datetime** | Date of the transaction | 
**description** | **str** | Description of the transaction. | 
**destination_id** | **str** | ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account. | [optional] 
**destination_name** | **str** | Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough. | [optional] 
**due_date** | **datetime** |  | [optional] 
**external_id** | **str** | Reference to external ID in other systems. | [optional] 
**external_url** | **str** | External, custom URL for this transaction. | [optional] 
**foreign_amount** | **str** | The amount in a foreign currency. | [optional] 
**foreign_currency_code** | **str** | Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount. | [optional] 
**foreign_currency_id** | **str** | Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount. | [optional] 
**interest_date** | **datetime** |  | [optional] 
**internal_reference** | **str** | Reference to internal reference of other systems. | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**order** | **int** | Order of this entry in the list of transactions. | [optional] 
**payment_date** | **datetime** |  | [optional] 
**piggy_bank_id** | **int** | Optional. Use either this or the piggy_bank_name | [optional] 
**piggy_bank_name** | **str** | Optional. Use either this or the piggy_bank_id | [optional] 
**process_date** | **datetime** |  | [optional] 
**reconciled** | **bool** | If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user. | [optional] 
**sepa_batch_id** | **str** | SEPA Batch ID | [optional] 
**sepa_cc** | **str** | SEPA Clearing Code | [optional] 
**sepa_ci** | **str** | SEPA Creditor Identifier | [optional] 
**sepa_country** | **str** | SEPA Country | [optional] 
**sepa_ct_id** | **str** | SEPA end-to-end Identifier | [optional] 
**sepa_ct_op** | **str** | SEPA Opposing Account Identifier | [optional] 
**sepa_db** | **str** | SEPA mandate identifier | [optional] 
**sepa_ep** | **str** | SEPA External Purpose indicator | [optional] 
**source_id** | **str** | ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. | [optional] 
**source_name** | **str** | Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name. | [optional] 
**tags** | **List[str]** | Array of tags. | [optional] 
**type** | [**TransactionTypeProperty**](TransactionTypeProperty.md) |  | 

## Example

```python
from firefly_iii_client.models.transaction_split_store import TransactionSplitStore

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSplitStore from a JSON string
transaction_split_store_instance = TransactionSplitStore.from_json(json)
# print the JSON string representation of the object
print(TransactionSplitStore.to_json())

# convert the object into a dict
transaction_split_store_dict = transaction_split_store_instance.to_dict()
# create an instance of TransactionSplitStore from a dict
transaction_split_store_form_dict = transaction_split_store.from_dict(transaction_split_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


