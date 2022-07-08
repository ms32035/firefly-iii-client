# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) |  | 
**account_number** | **str, none_type** |  | [optional] 
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional]  if omitted the server will use the default value of True
**bic** | **str, none_type** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**credit_card_type** | [**CreditCardType**](CreditCardType.md) |  | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**current_balance** | **str** |  | [optional] [readonly] 
**current_balance_date** | **datetime** |  | [optional] [readonly] 
**current_debt** | **str, none_type** | Represents the current debt for liabilities. | [optional] 
**iban** | **str, none_type** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional]  if omitted the server will use the default value of True
**interest** | **str, none_type** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | [**LiabilityDirection**](LiabilityDirection.md) |  | [optional] 
**latitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**liability_direction** | [**LiabilityDirection**](LiabilityDirection.md) |  | [optional] 
**liability_type** | [**LiabilityType**](LiabilityType.md) |  | [optional] 
**longitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**monthly_payment_date** | **datetime, none_type** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**opening_balance** | **str** | Represents the opening balance, the initial amount this account holds. | [optional] 
**opening_balance_date** | **datetime, none_type** | Represents the date of the opening balance. | [optional] 
**order** | **int, none_type** | Order of the account. Is NULL if account is not asset or liability. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**virtual_balance** | **str** |  | [optional] 
**zoom_level** | **int, none_type** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


