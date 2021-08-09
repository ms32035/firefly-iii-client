# AccountUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**account_number** | **str, none_type** |  | [optional] 
**account_role** | **str, none_type** | Is only mandatory when the type is asset. | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional] 
**bic** | **str, none_type** |  | [optional] 
**credit_card_type** | **str, none_type** | Mandatory when the account_role is ccAsset. Can only be monthlyFull or null. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**iban** | **str, none_type** |  | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] 
**interest** | **str, none_type** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | **str, none_type** | Mandatory when type is liability. Period over which the interest is calculated. | [optional] 
**latitude** | **float, none_type** | Latitude of the account&#39;s location, if applicable. Can be used to draw a map. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] 
**liability_type** | **str, none_type** | Mandatory when type is liability. Specifies the exact type. | [optional] 
**longitude** | **float, none_type** | Latitude of the account&#39;s location, if applicable. Can be used to draw a map. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] 
**monthly_payment_date** | **date, none_type** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**opening_balance** | **str** |  | [optional] 
**opening_balance_date** | **date, none_type** |  | [optional] 
**order** | **int** | Order of the account | [optional] 
**virtual_balance** | **str** |  | [optional] 
**zoom_level** | **int, none_type** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


