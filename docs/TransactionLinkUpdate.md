# TransactionLinkUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inward_id** | **str** | The inward transaction transaction_journal_id for the link. This becomes the &#39;is paid by&#39; transaction of the set. | [optional] 
**link_type_id** | **str** | The link type ID to use. Use this field OR use the link_type_name field. | [optional] 
**link_type_name** | **str** | The link type name to use. Use this field OR use the link_type_id field. | [optional] 
**notes** | **str** | Optional. Some notes. If you submit an empty string the current notes will be removed | [optional] 
**outward_id** | **str** | The outward transaction transaction_journal_id for the link. This becomes the &#39;pays for&#39; transaction of the set. | [optional] 

## Example

```python
from firefly_iii_client.models.transaction_link_update import TransactionLinkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionLinkUpdate from a JSON string
transaction_link_update_instance = TransactionLinkUpdate.from_json(json)
# print the JSON string representation of the object
print(TransactionLinkUpdate.to_json())

# convert the object into a dict
transaction_link_update_dict = transaction_link_update_instance.to_dict()
# create an instance of TransactionLinkUpdate from a dict
transaction_link_update_form_dict = transaction_link_update.from_dict(transaction_link_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


