# AutocompletePiggyBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Currency code for this piggy bank. | [optional] 
**currency_decimal_places** | **int** |  | [optional] 
**currency_id** | **str** | Currency ID for this piggy bank. | [optional] 
**currency_symbol** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** | Name of the piggy bank found by an auto-complete search. | 
**name_with_balance** | **str** | Name of the piggy bank found by an auto-complete search with the current balance formatted nicely. | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 

## Example

```python
from firefly_iii_client.models.autocomplete_piggy_balance import AutocompletePiggyBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompletePiggyBalance from a JSON string
autocomplete_piggy_balance_instance = AutocompletePiggyBalance.from_json(json)
# print the JSON string representation of the object
print(AutocompletePiggyBalance.to_json())

# convert the object into a dict
autocomplete_piggy_balance_dict = autocomplete_piggy_balance_instance.to_dict()
# create an instance of AutocompletePiggyBalance from a dict
autocomplete_piggy_balance_form_dict = autocomplete_piggy_balance.from_dict(autocomplete_piggy_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


