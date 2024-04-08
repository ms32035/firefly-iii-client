# AutocompleteCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Name of the category found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_category import AutocompleteCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteCategory from a JSON string
autocomplete_category_instance = AutocompleteCategory.from_json(json)
# print the JSON string representation of the object
print(AutocompleteCategory.to_json())

# convert the object into a dict
autocomplete_category_dict = autocomplete_category_instance.to_dict()
# create an instance of AutocompleteCategory from a dict
autocomplete_category_form_dict = autocomplete_category.from_dict(autocomplete_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


