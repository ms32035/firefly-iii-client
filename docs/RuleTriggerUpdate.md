# RuleTriggerUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the trigger is active. | [optional] 
**order** | **int** | Order of the trigger | [optional] 
**stop_processing** | **bool** | When true, other triggers will not be checked if this trigger was triggered. | [optional] 
**type** | [**RuleTriggerKeyword**](RuleTriggerKeyword.md) |  | [optional] 
**value** | **str** | The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger. If the rule trigger is something like &#39;has any tag&#39;, submit the string &#39;true&#39;. | [optional] 

## Example

```python
from firefly_iii_client.models.rule_trigger_update import RuleTriggerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTriggerUpdate from a JSON string
rule_trigger_update_instance = RuleTriggerUpdate.from_json(json)
# print the JSON string representation of the object
print(RuleTriggerUpdate.to_json())

# convert the object into a dict
rule_trigger_update_dict = rule_trigger_update_instance.to_dict()
# create an instance of RuleTriggerUpdate from a dict
rule_trigger_update_form_dict = rule_trigger_update.from_dict(rule_trigger_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


