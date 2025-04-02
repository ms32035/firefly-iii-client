# RecurrenceArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RecurrenceRead]**](RecurrenceRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.recurrence_array import RecurrenceArray

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceArray from a JSON string
recurrence_array_instance = RecurrenceArray.from_json(json)
# print the JSON string representation of the object
print(RecurrenceArray.to_json())

# convert the object into a dict
recurrence_array_dict = recurrence_array_instance.to_dict()
# create an instance of RecurrenceArray from a dict
recurrence_array_from_dict = RecurrenceArray.from_dict(recurrence_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


