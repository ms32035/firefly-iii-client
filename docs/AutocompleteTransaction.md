# AutocompleteTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Transaction description | 
**id** | **str** | The ID of a transaction journal (basically a single split). | 
**name** | **str** | Transaction description | 
**transaction_group_id** | **str** | The ID of the underlying transaction group. | [optional] 

## Example

```python
from firefly_iii_client.models.autocomplete_transaction import AutocompleteTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteTransaction from a JSON string
autocomplete_transaction_instance = AutocompleteTransaction.from_json(json)
# print the JSON string representation of the object
print(AutocompleteTransaction.to_json())

# convert the object into a dict
autocomplete_transaction_dict = autocomplete_transaction_instance.to_dict()
# create an instance of AutocompleteTransaction from a dict
autocomplete_transaction_from_dict = AutocompleteTransaction.from_dict(autocomplete_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


