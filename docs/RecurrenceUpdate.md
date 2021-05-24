# RecurrenceUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the recurrence is even active. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**nr_of_repetitions** | **int, none_type** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**repeat_until** | **date, none_type** | Date until the recurring transaction can fire. After that date, it&#39;s basically inactive. Use either this field or repetitions. | [optional] 
**repetitions** | [**[RecurrenceRepetitionUpdate]**](RecurrenceRepetitionUpdate.md) |  | [optional] 
**title** | **str** |  | [optional] 
**transactions** | [**[RecurrenceTransactionUpdate]**](RecurrenceTransactionUpdate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


