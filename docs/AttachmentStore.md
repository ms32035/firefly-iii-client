# AttachmentStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachable_id** | **str** | ID of the model this attachment is linked to. | 
**attachable_type** | [**AttachableType**](AttachableType.md) |  | 
**filename** | **str** |  | 
**notes** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.attachment_store import AttachmentStore

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentStore from a JSON string
attachment_store_instance = AttachmentStore.from_json(json)
# print the JSON string representation of the object
print(AttachmentStore.to_json())

# convert the object into a dict
attachment_store_dict = attachment_store_instance.to_dict()
# create an instance of AttachmentStore from a dict
attachment_store_from_dict = AttachmentStore.from_dict(attachment_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


