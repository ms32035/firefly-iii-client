# AttachmentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.attachment_update import AttachmentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentUpdate from a JSON string
attachment_update_instance = AttachmentUpdate.from_json(json)
# print the JSON string representation of the object
print(AttachmentUpdate.to_json())

# convert the object into a dict
attachment_update_dict = attachment_update_instance.to_dict()
# create an instance of AttachmentUpdate from a dict
attachment_update_from_dict = AttachmentUpdate.from_dict(attachment_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


