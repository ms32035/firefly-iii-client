# RuleTriggerStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the trigger is active. Defaults to true. | [optional] [default to True]
**order** | **int** | Order of the trigger | [optional] 
**stop_processing** | **bool** | When true, other triggers will not be checked if this trigger was triggered. Defaults to false. | [optional] [default to False]
**type** | [**RuleTriggerKeyword**](RuleTriggerKeyword.md) |  | 
**value** | **str** | The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger. | 

## Example

```python
from firefly_iii_client.models.rule_trigger_store import RuleTriggerStore

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTriggerStore from a JSON string
rule_trigger_store_instance = RuleTriggerStore.from_json(json)
# print the JSON string representation of the object
print(RuleTriggerStore.to_json())

# convert the object into a dict
rule_trigger_store_dict = rule_trigger_store_instance.to_dict()
# create an instance of RuleTriggerStore from a dict
rule_trigger_store_form_dict = rule_trigger_store.from_dict(rule_trigger_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


