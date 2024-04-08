# RuleGroupStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**title** | **str** |  | 

## Example

```python
from firefly_iii_client.models.rule_group_store import RuleGroupStore

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroupStore from a JSON string
rule_group_store_instance = RuleGroupStore.from_json(json)
# print the JSON string representation of the object
print(RuleGroupStore.to_json())

# convert the object into a dict
rule_group_store_dict = rule_group_store_instance.to_dict()
# create an instance of RuleGroupStore from a dict
rule_group_store_form_dict = rule_group_store.from_dict(rule_group_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


