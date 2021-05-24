# Recurrence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the recurrence is even active. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **datetime** | First time the recurring transaction will fire. Must be after today. | [optional] 
**latest_date** | **datetime, none_type** | Last time the recurring transaction has fired. | [optional] [readonly] 
**notes** | **str, none_type** |  | [optional] 
**nr_of_repetitions** | **int, none_type** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**repeat_until** | **datetime, none_type** | Date until the recurring transaction can fire. Use either this field or repetitions. | [optional] 
**repetitions** | [**[RecurrenceRepetition]**](RecurrenceRepetition.md) |  | [optional] 
**title** | **str** |  | [optional] 
**transactions** | [**[RecurrenceTransaction]**](RecurrenceTransaction.md) |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


