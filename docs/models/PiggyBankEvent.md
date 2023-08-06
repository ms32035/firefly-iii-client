# firefly_iii_client.model.piggy_bank_event.PiggyBankEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**currency_code** | str,  | str,  |  | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  |  | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**transaction_group_id** | str,  | str,  | The transaction group associated with the event. | [optional] 
**transaction_journal_id** | str,  | str,  | The journal associated with the event. | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

