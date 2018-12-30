# AccountUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_role** | **str** | Is only mandatory when the type is asset. | 
**active** | **bool** | If omitted, defaults to true. | [optional] 
**bic** | **str** |  | [optional] 
**credit_card_type** | **str** | Mandatory when the account_role is ccAsset. Can only be monthlyFull. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_id** | **int** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**iban** | **str** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] 
**interest** | **float** | Mandatory when type is liability. Interest percentage. | 
**interest_period** | **str** | Mandatory when type is liability. Period over which the interest is calculated. | 
**liability_amount** | **float** | Mandatory when type is liability. Amount of money in the liability. Must be positive. | 
**liability_start_date** | **date** | Mandatory when type is liability. Start date for the liability. | 
**liability_type** | **str** | Mandatory when type is liability. Specifies the exact type. | 
**monthly_payment_date** | **date** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**opening_balance** | **float** |  | [optional] 
**opening_balance_date** | **date** |  | [optional] 
**type** | **str** | Can only be one one these four account types. | 
**virtual_balance** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


