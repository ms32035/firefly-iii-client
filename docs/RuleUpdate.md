# RuleUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[RuleActionUpdate]**](RuleActionUpdate.md) |  | [optional] 
**active** | **bool** | Whether or not the rule is even active. Default is true. | [optional] [default to True]
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**rule_group_id** | **str** | ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory. | [optional] 
**stop_processing** | **bool** | If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false. | [optional] [default to False]
**strict** | **bool** | If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true. | [optional] 
**title** | **str** |  | [optional] 
**trigger** | [**RuleTriggerType**](RuleTriggerType.md) |  | [optional] 
**triggers** | [**List[RuleTriggerUpdate]**](RuleTriggerUpdate.md) |  | [optional] 

## Example

```python
from firefly_iii_client.models.rule_update import RuleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RuleUpdate from a JSON string
rule_update_instance = RuleUpdate.from_json(json)
# print the JSON string representation of the object
print(RuleUpdate.to_json())

# convert the object into a dict
rule_update_dict = rule_update_instance.to_dict()
# create an instance of RuleUpdate from a dict
rule_update_from_dict = RuleUpdate.from_dict(rule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


