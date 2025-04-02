# AutocompleteRuleGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the rule group found by auto-complete. | [optional] 
**id** | **str** |  | 
**name** | **str** | Name of the rule group found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_rule_group import AutocompleteRuleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteRuleGroup from a JSON string
autocomplete_rule_group_instance = AutocompleteRuleGroup.from_json(json)
# print the JSON string representation of the object
print(AutocompleteRuleGroup.to_json())

# convert the object into a dict
autocomplete_rule_group_dict = autocomplete_rule_group_instance.to_dict()
# create an instance of AutocompleteRuleGroup from a dict
autocomplete_rule_group_from_dict = AutocompleteRuleGroup.from_dict(autocomplete_rule_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


