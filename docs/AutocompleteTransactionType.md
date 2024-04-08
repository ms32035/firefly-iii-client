# AutocompleteTransactionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | Type of the object found by an auto-complete search. | 
**type** | **str** | Name of the object found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_transaction_type import AutocompleteTransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteTransactionType from a JSON string
autocomplete_transaction_type_instance = AutocompleteTransactionType.from_json(json)
# print the JSON string representation of the object
print(AutocompleteTransactionType.to_json())

# convert the object into a dict
autocomplete_transaction_type_dict = autocomplete_transaction_type_instance.to_dict()
# create an instance of AutocompleteTransactionType from a dict
autocomplete_transaction_type_form_dict = autocomplete_transaction_type.from_dict(autocomplete_transaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


