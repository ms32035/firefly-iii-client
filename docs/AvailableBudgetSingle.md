# AvailableBudgetSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AvailableBudgetRead**](AvailableBudgetRead.md) |  | 

## Example

```python
from firefly_iii_client.models.available_budget_single import AvailableBudgetSingle

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBudgetSingle from a JSON string
available_budget_single_instance = AvailableBudgetSingle.from_json(json)
# print the JSON string representation of the object
print(AvailableBudgetSingle.to_json())

# convert the object into a dict
available_budget_single_dict = available_budget_single_instance.to_dict()
# create an instance of AvailableBudgetSingle from a dict
available_budget_single_from_dict = AvailableBudgetSingle.from_dict(available_budget_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


