# RuleArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RuleRead]**](RuleRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.rule_array import RuleArray

# TODO update the JSON string below
json = "{}"
# create an instance of RuleArray from a JSON string
rule_array_instance = RuleArray.from_json(json)
# print the JSON string representation of the object
print(RuleArray.to_json())

# convert the object into a dict
rule_array_dict = rule_array_instance.to_dict()
# create an instance of RuleArray from a dict
rule_array_form_dict = rule_array.from_dict(rule_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


