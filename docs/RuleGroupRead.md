# RuleGroupRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**RuleGroup**](RuleGroup.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.rule_group_read import RuleGroupRead

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroupRead from a JSON string
rule_group_read_instance = RuleGroupRead.from_json(json)
# print the JSON string representation of the object
print(RuleGroupRead.to_json())

# convert the object into a dict
rule_group_read_dict = rule_group_read_instance.to_dict()
# create an instance of RuleGroupRead from a dict
rule_group_read_from_dict = RuleGroupRead.from_dict(rule_group_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


