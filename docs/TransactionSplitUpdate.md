# TransactionSplitUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the transaction. | 
**budget_id** | **int** | The budget ID for this transaction. | [optional] 
**budget_name** | **str** | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] 
**category_id** | **int** | The category ID for this transaction. | [optional] 
**category_name** | **str** | The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name. | [optional] 
**currency_code** | **str** | Currency code. Default is the source account&#39;s currency, or the user&#39;s default currency. Can be used instead of currency_id. | [optional] 
**currency_id** | **int** | Currency ID. Default is the source account&#39;s currency, or the user&#39;s default currency. Can be used instead of currency_code. | [optional] 
**description** | **str** | Description of the transaction. Will only be used if more than one split is submitted. | [optional] 
**destination_id** | **int** | ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account. | [optional] 
**destination_name** | **str** | Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough. | [optional] 
**foreign_amount** | **float** | The amount in a foreign currency. | [optional] 
**foreign_currency_code** | **str** | Currency code. Default is NULL. Can be used instead of the foreign_currency_id, but either is required when submitting a foreign amount. | [optional] 
**foreign_currency_id** | **int** | Currency ID. Default is null. Is required when you submit a foreign amount. | [optional] 
**reconciled** | **bool** | If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user. | [optional] 
**source_id** | **int** | ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. | 
**source_name** | **str** | Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


