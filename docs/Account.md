# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_role** | **str** | Is only mandatory when the type is asset. | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional] 
**bic** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**credit_card_type** | **str** | Mandatory when the account_role is ccAsset. Can only be monthlyFull. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **int** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**current_balance** | **str** |  | [optional] [readonly] 
**current_balance_date** | **date** |  | [optional] [readonly] 
**iban** | **str** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] 
**interest** | **str** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | **str** | Mandatory when type is liability. Period over which the interest is calculated. | [optional] 
**liability_amount** | **str** | Mandatory when type is liability. Amount of money in the liability. Must be positive. | [optional] 
**liability_start_date** | **date** | Mandatory when type is liability. Start date for the liability. | [optional] 
**liability_type** | **str** | Mandatory when type is liability. Specifies the exact type. | [optional] 
**monthly_payment_date** | **date** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**opening_balance** | **str** |  | [optional] 
**opening_balance_date** | **date** |  | [optional] 
**order** | **int** | Order of the account | [optional] 
**type** | **str** | Can only be one one these account types. import, initial-balance and reconciliation cannot be set manually. | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**virtual_balance** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


