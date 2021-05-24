# RecurrenceStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_date** | **date** | First time the recurring transaction will fire. Must be after today. | 
**repeat_until** | **date, none_type** | Date until the recurring transaction can fire. Use either this field or repetitions. | 
**repetitions** | [**[RecurrenceRepetitionStore]**](RecurrenceRepetitionStore.md) |  | 
**title** | **str** |  | 
**transactions** | [**[RecurrenceTransactionStore]**](RecurrenceTransactionStore.md) |  | 
**type** | **str** |  | 
**active** | **bool** | If the recurrence is even active. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**notes** | **str, none_type** |  | [optional] 
**nr_of_repetitions** | **int, none_type** | Max number of created transactions. Use either this field or repeat_until. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


