# firefly_iii_client.model.autocomplete_account.AutocompleteAccount

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currency_name** | str,  | str,  | Currency name for the currency used by this account. | 
**currency_symbol** | str,  | str,  | Currency symbol for the currency used by this account. | 
**name** | str,  | str,  | Name of the account found by an auto-complete search. | 
**id** | str,  | str,  |  | 
**name_with_balance** | str,  | str,  | Asset accounts and liabilities have a second field with the given date&#x27;s account balance. | 
**type** | str,  | str,  | Account type of the account found by the auto-complete search. | 
**currency_code** | str,  | str,  | Currency code for the currency used by this account. | 
**currency_id** | str,  | str,  | ID for the currency used by this account. | 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | Number of decimal places for the currency used by this account. | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

