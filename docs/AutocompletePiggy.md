# AutocompletePiggy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Currency code for this piggy bank. This will always be the currency of the piggy bank, never the user&#39;s native currency. | [optional] 
**currency_decimal_places** | **int** | Number of decimal places for the currency used by this piggy bank. This will always be the currency of the piggy bank, never the user&#39;s native currency. | [optional] 
**currency_id** | **str** | Currency ID for this piggy bank. This will always be the currency of the piggy bank, never the user&#39;s native currency. | [optional] 
**currency_name** | **str** | Currency name for the currency used by this piggy bank. This will always be the currency of the piggy bank, never the user&#39;s native currency. | [optional] 
**currency_symbol** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** | Name of the piggy bank found by an auto-complete search. | 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 

## Example

```python
from firefly_iii_client.models.autocomplete_piggy import AutocompletePiggy

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompletePiggy from a JSON string
autocomplete_piggy_instance = AutocompletePiggy.from_json(json)
# print the JSON string representation of the object
print(AutocompletePiggy.to_json())

# convert the object into a dict
autocomplete_piggy_dict = autocomplete_piggy_instance.to_dict()
# create an instance of AutocompletePiggy from a dict
autocomplete_piggy_from_dict = AutocompletePiggy.from_dict(autocomplete_piggy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


