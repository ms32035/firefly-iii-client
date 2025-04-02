# AutocompleteObjectGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Title of the object group found by an auto-complete search. | 
**title** | **str** | Title of the object group found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_object_group import AutocompleteObjectGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteObjectGroup from a JSON string
autocomplete_object_group_instance = AutocompleteObjectGroup.from_json(json)
# print the JSON string representation of the object
print(AutocompleteObjectGroup.to_json())

# convert the object into a dict
autocomplete_object_group_dict = autocomplete_object_group_instance.to_dict()
# create an instance of AutocompleteObjectGroup from a dict
autocomplete_object_group_from_dict = AutocompleteObjectGroup.from_dict(autocomplete_object_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


