# Recurrence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the recurrence is even active. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. Must be after today. | 
**latest_date** | **date** | First time the recurring transaction will fire. Must be after today. | [optional] 
**notes** | **str** |  | [optional] 
**nr_of_repetitions** | **int** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**repeat_until** | **date** | Date until the recurring transaction can fire. Use either this field or repetitions. | [optional] 
**repetitions** | [**list[RecurrenceRepetition]**](RecurrenceRepetition.md) |  | [optional] 
**title** | **str** |  | 
**transactions** | [**list[RecurrenceTransaction]**](RecurrenceTransaction.md) |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


