# AccountStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) |  | 
**account_number** | **str, none_type** |  | [optional] 
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional]  if omitted the server will use the default value of True
**bic** | **str, none_type** |  | [optional] 
**credit_card_type** | [**CreditCardType**](CreditCardType.md) |  | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**iban** | **str, none_type** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional]  if omitted the server will use the default value of True
**interest** | **str, none_type** | Mandatory when type is liability. Interest percentage. | [optional]  if omitted the server will use the default value of "0"
**interest_period** | [**InterestPeriod**](InterestPeriod.md) |  | [optional] 
**latitude** | **float, none_type** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**liability_direction** | [**LiabilityDirection**](LiabilityDirection.md) |  | [optional] 
**liability_type** | [**LiabilityType**](LiabilityType.md) |  | [optional] 
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


