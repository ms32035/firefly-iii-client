# AutocompleteBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Name of the budget found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_budget import AutocompleteBudget

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteBudget from a JSON string
autocomplete_budget_instance = AutocompleteBudget.from_json(json)
# print the JSON string representation of the object
print(AutocompleteBudget.to_json())

# convert the object into a dict
autocomplete_budget_dict = autocomplete_budget_instance.to_dict()
# create an instance of AutocompleteBudget from a dict
autocomplete_budget_from_dict = AutocompleteBudget.from_dict(autocomplete_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


