# RuleActionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the action is active. | [optional] 
**order** | **int** | Order of the action | [optional] 
**stop_processing** | **bool** | When true, other actions will not be fired after this action has fired. | [optional] 
**type** | [**RuleActionKeyword**](RuleActionKeyword.md) |  | [optional] 
**value** | **str** | The accompanying value the action will set, change or update. Can be empty, but for some types this value is mandatory. | [optional] 

## Example

```python
from firefly_iii_client.models.rule_action_update import RuleActionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RuleActionUpdate from a JSON string
rule_action_update_instance = RuleActionUpdate.from_json(json)
# print the JSON string representation of the object
print(RuleActionUpdate.to_json())

# convert the object into a dict
rule_action_update_dict = rule_action_update_instance.to_dict()
# create an instance of RuleActionUpdate from a dict
rule_action_update_form_dict = rule_action_update.from_dict(rule_action_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


