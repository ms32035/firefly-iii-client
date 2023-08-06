# firefly_iii_client.model.recurrence_repetition.RecurrenceRepetition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | [**RecurrenceRepetitionType**](RecurrenceRepetitionType.md) | [**RecurrenceRepetitionType**](RecurrenceRepetitionType.md) |  | 
**moment** | str,  | str,  | Information that defined the type of repetition. - For &#x27;daily&#x27;, this is empty. - For &#x27;weekly&#x27;, it is day of the week between 1 and 7 (Monday - Sunday). - For &#x27;ndom&#x27;, it is &#x27;1,2&#x27; or &#x27;4,5&#x27; or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). &#x27;2,3&#x27; means: the 2nd Wednesday of the month - For &#x27;monthly&#x27; it is the day of the month (1 - 31) - For yearly, it is a full date, ie &#x27;2018-09-17&#x27;. The year you use does not matter.  | 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | Auto-generated repetition description. | [optional] 
**id** | str,  | str,  |  | [optional] 
**[occurrences](#occurrences)** | list, tuple,  | tuple,  | Array of future dates when the repetition will apply to. Auto generated. | [optional] 
**skip** | decimal.Decimal, int,  | decimal.Decimal,  | How many occurrences to skip. 0 means skip nothing. 1 means every other. | [optional] value must be a 32 bit integer
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**weekend** | decimal.Decimal, int,  | decimal.Decimal,  | How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday.  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# occurrences

Array of future dates when the repetition will apply to. Auto generated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of future dates when the repetition will apply to. Auto generated. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

