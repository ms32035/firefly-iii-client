# RuleGroupSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RuleGroupRead**](RuleGroupRead.md) |  | 

## Example

```python
from firefly_iii_client.models.rule_group_single import RuleGroupSingle

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroupSingle from a JSON string
rule_group_single_instance = RuleGroupSingle.from_json(json)
# print the JSON string representation of the object
print(RuleGroupSingle.to_json())

# convert the object into a dict
rule_group_single_dict = rule_group_single_instance.to_dict()
# create an instance of RuleGroupSingle from a dict
rule_group_single_form_dict = rule_group_single.from_dict(rule_group_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


