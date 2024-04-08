# AttachmentArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AttachmentRead]**](AttachmentRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.attachment_array import AttachmentArray

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentArray from a JSON string
attachment_array_instance = AttachmentArray.from_json(json)
# print the JSON string representation of the object
print(AttachmentArray.to_json())

# convert the object into a dict
attachment_array_dict = attachment_array_instance.to_dict()
# create an instance of AttachmentArray from a dict
attachment_array_form_dict = attachment_array.from_dict(attachment_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


