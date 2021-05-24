# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | Can only be one one these account types. import, initial-balance and reconciliation cannot be set manually. | 
**account_number** | **str, none_type** |  | [optional] 
**account_role** | **str, none_type** | Is only mandatory when the type is asset. | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional] 
**bic** | **str, none_type** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**credit_card_type** | **str, none_type** | Mandatory when the account_role is ccAsset. Can only be monthlyFull or null. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**current_balance** | **str** |  | [optional] [readonly] 
**current_balance_date** | **datetime** |  | [optional] [readonly] 
**iban** | **str, none_type** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] 
**interest** | **str, none_type** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | **str, none_type** | Mandatory when type is liability. Period over which the interest is calculated. | [optional] 
**latitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**liability_type** | **str, none_type** | Mandatory when type is liability. Specifies the exact type. | [optional] 
**longitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**monthly_payment_date** | **datetime, none_type** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**opening_balance** | **str** | Represents the opening balance, the initial amount this account holds. | [optional] 
**opening_balance_date** | **datetime, none_type** | Represents the date of the opening balance. | [optional] 
**order** | **int, none_type** | Order of the account. Is NULL if account is not asset or liability. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**virtual_balance** | **str** |  | [optional] 
**zoom_level** | **int, none_type** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


