# TransactionLinkArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionLinkRead]**](TransactionLinkRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.transaction_link_array import TransactionLinkArray

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionLinkArray from a JSON string
transaction_link_array_instance = TransactionLinkArray.from_json(json)
# print the JSON string representation of the object
print(TransactionLinkArray.to_json())

# convert the object into a dict
transaction_link_array_dict = transaction_link_array_instance.to_dict()
# create an instance of TransactionLinkArray from a dict
transaction_link_array_form_dict = transaction_link_array.from_dict(transaction_link_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


