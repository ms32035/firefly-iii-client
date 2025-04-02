# AutocompleteRecurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the recurrence found by auto-complete. | [optional] 
**id** | **str** |  | 
**name** | **str** | Name of the recurrence found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_recurrence import AutocompleteRecurrence

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteRecurrence from a JSON string
autocomplete_recurrence_instance = AutocompleteRecurrence.from_json(json)
# print the JSON string representation of the object
print(AutocompleteRecurrence.to_json())

# convert the object into a dict
autocomplete_recurrence_dict = autocomplete_recurrence_instance.to_dict()
# create an instance of AutocompleteRecurrence from a dict
autocomplete_recurrence_from_dict = AutocompleteRecurrence.from_dict(autocomplete_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


