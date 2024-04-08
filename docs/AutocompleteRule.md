# AutocompleteRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the rule found by auto-complete. | [optional] 
**id** | **str** |  | 
**name** | **str** | Name of the rule found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_rule import AutocompleteRule

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteRule from a JSON string
autocomplete_rule_instance = AutocompleteRule.from_json(json)
# print the JSON string representation of the object
print(AutocompleteRule.to_json())

# convert the object into a dict
autocomplete_rule_dict = autocomplete_rule_instance.to_dict()
# create an instance of AutocompleteRule from a dict
autocomplete_rule_form_dict = autocomplete_rule.from_dict(autocomplete_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


