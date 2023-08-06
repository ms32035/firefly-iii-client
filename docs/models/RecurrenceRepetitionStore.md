# firefly_iii_client.model.recurrence_repetition_store.RecurrenceRepetitionStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | [**RecurrenceRepetitionType**](RecurrenceRepetitionType.md) | [**RecurrenceRepetitionType**](RecurrenceRepetitionType.md) |  | 
**moment** | str,  | str,  | Information that defined the type of repetition. - For &#x27;daily&#x27;, this is empty. - For &#x27;weekly&#x27;, it is day of the week between 1 and 7 (Monday - Sunday). - For &#x27;ndom&#x27;, it is &#x27;1,2&#x27; or &#x27;4,5&#x27; or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). &#x27;2,3&#x27; means: the 2nd Wednesday of the month - For &#x27;monthly&#x27; it is the day of the month (1 - 31) - For yearly, it is a full date, ie &#x27;2018-09-17&#x27;. The year you use does not matter.  | 
**skip** | decimal.Decimal, int,  | decimal.Decimal,  | How many occurrences to skip. 0 means skip nothing. 1 means every other. | [optional] value must be a 32 bit integer
**weekend** | decimal.Decimal, int,  | decimal.Decimal,  | How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday.  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

