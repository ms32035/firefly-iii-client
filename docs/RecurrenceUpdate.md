# RecurrenceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the recurrence is even active. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. | [optional] 
**notes** | **str** |  | [optional] 
**nr_of_repetitions** | **int** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**repeat_until** | **date** | Date until the recurring transaction can fire. After that date, it&#39;s basically inactive. Use either this field or repetitions. | [optional] 
**repetitions** | [**List[RecurrenceRepetitionUpdate]**](RecurrenceRepetitionUpdate.md) |  | [optional] 
**title** | **str** |  | [optional] 
**transactions** | [**List[RecurrenceTransactionUpdate]**](RecurrenceTransactionUpdate.md) |  | [optional] 

## Example

```python
from firefly_iii_client.models.recurrence_update import RecurrenceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceUpdate from a JSON string
recurrence_update_instance = RecurrenceUpdate.from_json(json)
# print the JSON string representation of the object
print(RecurrenceUpdate.to_json())

# convert the object into a dict
recurrence_update_dict = recurrence_update_instance.to_dict()
# create an instance of RecurrenceUpdate from a dict
recurrence_update_from_dict = RecurrenceUpdate.from_dict(recurrence_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


