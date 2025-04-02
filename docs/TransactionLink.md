# TransactionLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**inward_id** | **str** | The inward transaction transaction_journal_id for the link. This becomes the &#39;is paid by&#39; transaction of the set. | 
**link_type_id** | **str** | The link type ID to use. You can also use the link_type_name field. | 
**link_type_name** | **str** | The link type name to use. You can also use the link_type_id field. | [optional] 
**notes** | **str** | Optional. Some notes. | [optional] 
**outward_id** | **str** | The outward transaction transaction_journal_id for the link. This becomes the &#39;pays for&#39; transaction of the set. | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.transaction_link import TransactionLink

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionLink from a JSON string
transaction_link_instance = TransactionLink.from_json(json)
# print the JSON string representation of the object
print(TransactionLink.to_json())

# convert the object into a dict
transaction_link_dict = transaction_link_instance.to_dict()
# create an instance of TransactionLink from a dict
transaction_link_from_dict = TransactionLink.from_dict(transaction_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


