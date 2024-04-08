# RuleRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Rule**](Rule.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.rule_read import RuleRead

# TODO update the JSON string below
json = "{}"
# create an instance of RuleRead from a JSON string
rule_read_instance = RuleRead.from_json(json)
# print the JSON string representation of the object
print(RuleRead.to_json())

# convert the object into a dict
rule_read_dict = rule_read_instance.to_dict()
# create an instance of RuleRead from a dict
rule_read_form_dict = rule_read.from_dict(rule_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


