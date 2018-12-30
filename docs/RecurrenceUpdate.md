# RecurrenceUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. Must be after today. | 
**nr_of_repetitions** | **int** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**piggy_bank_id** | **int** | Piggy bank to relate the newly created transaction to. Will only work for transfers. | [optional] 
**repeat_until** | **date** | Date until the recurring transaction can fire. Use either this field or repetitions. | 
**repetitions** | [**list[RecurrenceRepetitionUpdate]**](RecurrenceRepetitionUpdate.md) |  | 
**tags** | **str** | Tags to be used for each created transaction, comma separated. | [optional] 
**title** | **str** |  | 
**transactions** | [**list[RecurrenceTransactionUpdate]**](RecurrenceTransactionUpdate.md) |  | 
**type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


