# TransactionLinkRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TransactionLink**](TransactionLink.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.transaction_link_read import TransactionLinkRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionLinkRead from a JSON string
transaction_link_read_instance = TransactionLinkRead.from_json(json)
# print the JSON string representation of the object
print(TransactionLinkRead.to_json())

# convert the object into a dict
transaction_link_read_dict = transaction_link_read_instance.to_dict()
# create an instance of TransactionLinkRead from a dict
transaction_link_read_from_dict = TransactionLinkRead.from_dict(transaction_link_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


