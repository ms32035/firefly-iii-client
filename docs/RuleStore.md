# RuleStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[RuleActionStore]**](RuleActionStore.md) |  | 
**active** | **bool** | Whether or not the rule is even active. Default is true. | [optional] [default to True]
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**rule_group_id** | **str** | ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory. | 
**rule_group_title** | **str** | Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory. | [optional] 
**stop_processing** | **bool** | If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false. | [optional] 
**strict** | **bool** | If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true. | [optional] [default to True]
**title** | **str** |  | 
**trigger** | [**RuleTriggerType**](RuleTriggerType.md) |  | 
**triggers** | [**List[RuleTriggerStore]**](RuleTriggerStore.md) |  | 

## Example

```python
from firefly_iii_client.models.rule_store import RuleStore

# TODO update the JSON string below
json = "{}"
# create an instance of RuleStore from a JSON string
rule_store_instance = RuleStore.from_json(json)
# print the JSON string representation of the object
print(RuleStore.to_json())

# convert the object into a dict
rule_store_dict = rule_store_instance.to_dict()
# create an instance of RuleStore from a dict
rule_store_from_dict = RuleStore.from_dict(rule_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


