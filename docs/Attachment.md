# Attachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachable_id** | **str** | ID of the model this attachment is linked to. | 
**attachable_type** | [**AttachableType**](AttachableType.md) |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**download_url** | **str** |  | [optional] 
**filename** | **str** |  | 
**md5** | **str** | MD5 hash of the file for basic duplicate detection. | [optional] 
**mime** | **str** |  | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**size** | **int** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_form_dict = attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


