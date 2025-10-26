# RecurrenceProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the recurrence is even active. | [optional] 
**apply_rules** | **bool** | Whether or not to fire the rules after the creation of a transaction. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** | Not to be confused with the description of the actual transaction(s) being created. | [optional] 
**first_date** | **date** | First time the recurring transaction will fire. Must be after today. | [optional] 
**latest_date** | **date** | Last time the recurring transaction has fired. | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**nr_of_repetitions** | **int** | Max number of created transactions. Use either this field or repeat_until. | [optional] 
**repeat_until** | **date** | Date until the recurring transaction can fire. Use either this field or repetitions. | [optional] 
**repetitions** | [**List[RecurrenceRepetition]**](RecurrenceRepetition.md) |  | [optional] 
**title** | **str** |  | [optional] 
**transactions** | [**List[RecurrenceTransaction]**](RecurrenceTransaction.md) |  | [optional] 
**type** | [**RecurrenceTransactionType**](RecurrenceTransactionType.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.recurrence_properties import RecurrenceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceProperties from a JSON string
recurrence_properties_instance = RecurrenceProperties.from_json(json)
# print the JSON string representation of the object
print(RecurrenceProperties.to_json())

# convert the object into a dict
recurrence_properties_dict = recurrence_properties_instance.to_dict()
# create an instance of RecurrenceProperties from a dict
recurrence_properties_from_dict = RecurrenceProperties.from_dict(recurrence_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


