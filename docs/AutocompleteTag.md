# AutocompleteTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Name of the tag found by an auto-complete search. | 
**tag** | **str** | Name of the tag found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_tag import AutocompleteTag

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteTag from a JSON string
autocomplete_tag_instance = AutocompleteTag.from_json(json)
# print the JSON string representation of the object
print(AutocompleteTag.to_json())

# convert the object into a dict
autocomplete_tag_dict = autocomplete_tag_instance.to_dict()
# create an instance of AutocompleteTag from a dict
autocomplete_tag_form_dict = autocomplete_tag.from_dict(autocomplete_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


