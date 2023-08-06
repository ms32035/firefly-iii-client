# firefly_iii_client.model.account_update.AccountUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**type** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**account_number** | None, str,  | NoneClass, str,  |  | [optional] 
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**active** | bool,  | BoolClass,  | If omitted, defaults to true. | [optional] if omitted the server will use the default value of True
**bic** | None, str,  | NoneClass, str,  |  | [optional] 
**credit_card_type** | [**CreditCardType**](CreditCardType.md) | [**CreditCardType**](CreditCardType.md) |  | [optional] 
**currency_code** | str,  | str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**currency_id** | str,  | str,  | Use either currency_id or currency_code. Defaults to the user&#x27;s default currency. | [optional] 
**iban** | None, str,  | NoneClass, str,  |  | [optional] 
**include_net_worth** | bool,  | BoolClass,  | If omitted, defaults to true. | [optional] if omitted the server will use the default value of True
**interest** | None, str,  | NoneClass, str,  | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | [**InterestPeriod**](InterestPeriod.md) | [**InterestPeriod**](InterestPeriod.md) |  | [optional] 
**latitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude of the account&#x27;s location, if applicable. Can be used to draw a map. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] value must be a 64 bit float
**liability_type** | [**LiabilityType**](LiabilityType.md) | [**LiabilityType**](LiabilityType.md) |  | [optional] 
**longitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude of the account&#x27;s location, if applicable. Can be used to draw a map. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] value must be a 64 bit float
**monthly_payment_date** | None, str, datetime,  | NoneClass, str,  | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] value must conform to RFC-3339 date-time
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**opening_balance** | str,  | str,  |  | [optional] 
**opening_balance_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**order** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the account | [optional] value must be a 32 bit integer
**virtual_balance** | str,  | str,  |  | [optional] 
**zoom_level** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

