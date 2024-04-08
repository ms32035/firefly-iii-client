# TransactionLinkSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionLinkRead**](TransactionLinkRead.md) |  | 

## Example

```python
from firefly_iii_client.models.transaction_link_single import TransactionLinkSingle

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionLinkSingle from a JSON string
transaction_link_single_instance = TransactionLinkSingle.from_json(json)
# print the JSON string representation of the object
print(TransactionLinkSingle.to_json())

# convert the object into a dict
transaction_link_single_dict = transaction_link_single_instance.to_dict()
# create an instance of TransactionLinkSingle from a dict
transaction_link_single_form_dict = transaction_link_single.from_dict(transaction_link_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


