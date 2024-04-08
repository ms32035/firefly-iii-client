# RecurrenceRepetitionStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moment** | **str** | Information that defined the type of repetition. - For &#39;daily&#39;, this is empty. - For &#39;weekly&#39;, it is day of the week between 1 and 7 (Monday - Sunday). - For &#39;ndom&#39;, it is &#39;1,2&#39; or &#39;4,5&#39; or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). &#39;2,3&#39; means: the 2nd Wednesday of the month - For &#39;monthly&#39; it is the day of the month (1 - 31) - For yearly, it is a full date, ie &#39;2018-09-17&#39;. The year you use does not matter.  | 
**skip** | **int** | How many occurrences to skip. 0 means skip nothing. 1 means every other. | [optional] 
**type** | [**RecurrenceRepetitionType**](RecurrenceRepetitionType.md) |  | 
**weekend** | **int** | How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday.  | [optional] 

## Example

```python
from firefly_iii_client.models.recurrence_repetition_store import RecurrenceRepetitionStore

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceRepetitionStore from a JSON string
recurrence_repetition_store_instance = RecurrenceRepetitionStore.from_json(json)
# print the JSON string representation of the object
print(RecurrenceRepetitionStore.to_json())

# convert the object into a dict
recurrence_repetition_store_dict = recurrence_repetition_store_instance.to_dict()
# create an instance of RecurrenceRepetitionStore from a dict
recurrence_repetition_store_form_dict = recurrence_repetition_store.from_dict(recurrence_repetition_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


