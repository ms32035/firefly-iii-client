# RecurrenceRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Recurrence**](Recurrence.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.recurrence_read import RecurrenceRead

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceRead from a JSON string
recurrence_read_instance = RecurrenceRead.from_json(json)
# print the JSON string representation of the object
print(RecurrenceRead.to_json())

# convert the object into a dict
recurrence_read_dict = recurrence_read_instance.to_dict()
# create an instance of RecurrenceRead from a dict
recurrence_read_form_dict = recurrence_read.from_dict(recurrence_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


