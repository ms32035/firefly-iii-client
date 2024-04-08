# RuleGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] [readonly] 
**title** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.rule_group import RuleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroup from a JSON string
rule_group_instance = RuleGroup.from_json(json)
# print the JSON string representation of the object
print(RuleGroup.to_json())

# convert the object into a dict
rule_group_dict = rule_group_instance.to_dict()
# create an instance of RuleGroup from a dict
rule_group_form_dict = rule_group.from_dict(rule_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


