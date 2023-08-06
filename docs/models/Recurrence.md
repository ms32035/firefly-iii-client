# firefly_iii_client.model.recurrence.Recurrence

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**active** | bool,  | BoolClass,  | If the recurrence is even active. | [optional] 
**apply_rules** | bool,  | BoolClass,  | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | str, date,  | str,  | First time the recurring transaction will fire. Must be after today. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**latest_date** | None, str, date,  | NoneClass, str,  | Last time the recurring transaction has fired. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**nr_of_repetitions** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Max number of created transactions. Use either this field or repeat_until. | [optional] value must be a 32 bit integer
**repeat_until** | None, str, date,  | NoneClass, str,  | Date until the recurring transaction can fire. Use either this field or repetitions. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[repetitions](#repetitions)** | list, tuple,  | tuple,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**[transactions](#transactions)** | list, tuple,  | tuple,  |  | [optional] 
**type** | [**RecurrenceTransactionType**](RecurrenceTransactionType.md) | [**RecurrenceTransactionType**](RecurrenceTransactionType.md) |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# repetitions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RecurrenceRepetition**](RecurrenceRepetition.md) | [**RecurrenceRepetition**](RecurrenceRepetition.md) | [**RecurrenceRepetition**](RecurrenceRepetition.md) |  | 

# transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RecurrenceTransaction**](RecurrenceTransaction.md) | [**RecurrenceTransaction**](RecurrenceTransaction.md) | [**RecurrenceTransaction**](RecurrenceTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

