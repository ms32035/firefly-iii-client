# RuleGroupArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RuleGroupRead]**](RuleGroupRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.rule_group_array import RuleGroupArray

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroupArray from a JSON string
rule_group_array_instance = RuleGroupArray.from_json(json)
# print the JSON string representation of the object
print(RuleGroupArray.to_json())

# convert the object into a dict
rule_group_array_dict = rule_group_array_instance.to_dict()
# create an instance of RuleGroupArray from a dict
rule_group_array_from_dict = RuleGroupArray.from_dict(rule_group_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


