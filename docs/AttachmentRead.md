# AttachmentRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Attachment**](Attachment.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.attachment_read import AttachmentRead

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRead from a JSON string
attachment_read_instance = AttachmentRead.from_json(json)
# print the JSON string representation of the object
print(AttachmentRead.to_json())

# convert the object into a dict
attachment_read_dict = attachment_read_instance.to_dict()
# create an instance of AttachmentRead from a dict
attachment_read_form_dict = attachment_read.from_dict(attachment_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


