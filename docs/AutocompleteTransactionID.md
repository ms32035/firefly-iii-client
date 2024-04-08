# AutocompleteTransactionID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Transaction description with ID in the name. | 
**id** | **str** | The ID of a transaction journal (basically a single split). | 
**name** | **str** | Transaction description with ID in the name. | 
**transaction_group_id** | **str** | The ID of the underlying transaction group. | [optional] 

## Example

```python
from firefly_iii_client.models.autocomplete_transaction_id import AutocompleteTransactionID

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteTransactionID from a JSON string
autocomplete_transaction_id_instance = AutocompleteTransactionID.from_json(json)
# print the JSON string representation of the object
print(AutocompleteTransactionID.to_json())

# convert the object into a dict
autocomplete_transaction_id_dict = autocomplete_transaction_id_instance.to_dict()
# create an instance of AutocompleteTransactionID from a dict
autocomplete_transaction_id_form_dict = autocomplete_transaction_id.from_dict(autocomplete_transaction_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


