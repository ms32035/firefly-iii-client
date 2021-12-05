# AccountStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | Can only be one one these account types. import, initial-balance and reconciliation cannot be set manually. | 
**account_number** | **str, none_type** |  | [optional] 
**account_role** | **str, none_type** | Is only mandatory when the type is asset. | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional] 
**bic** | **str, none_type** |  | [optional] 
**credit_card_type** | **str, none_type** | Mandatory when the account_role is ccAsset. Can only be monthlyFull or null. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**iban** | **str, none_type** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] 
**interest** | **str, none_type** | Mandatory when type is liability. Interest percentage. | [optional]  if omitted the server will use the default value of "0"
**interest_period** | **str, none_type** | Mandatory when type is liability. Period over which the interest is calculated. | [optional]  if omitted the server will use the default value of "monthly"
**latitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**liability_direction** | **str, none_type** | &#39;credit&#39; indicates somebody owes you the liability. &#39;debit&#39; Indicates you owe this debt yourself. Works only for liabiltiies. | [optional]  if omitted the server will use the default value of "debit"
**liability_type** | **str, none_type** | Mandatory when type is liability. Specifies the exact type. | [optional] 
**longitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**monthly_payment_date** | **date, none_type** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**opening_balance** | **str** | Represents the opening balance, the initial amount this account holds. | [optional] 
**opening_balance_date** | **date, none_type** | Represents the date of the opening balance. | [optional] 
**order** | **int** | Order of the account | [optional] 
**virtual_balance** | **str** |  | [optional] 
**zoom_level** | **int, none_type** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


