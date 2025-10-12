# AttachmentProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachable_id** | **str** | ID of the model this attachment is linked to. | [optional] 
**attachable_type** | [**AttachableType**](AttachableType.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**download_url** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**hash** | **str** | Hash of the file for basic duplicate detection. | [optional] 
**mime** | **str** |  | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**size** | **int** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.attachment_properties import AttachmentProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentProperties from a JSON string
attachment_properties_instance = AttachmentProperties.from_json(json)
# print the JSON string representation of the object
print(AttachmentProperties.to_json())

# convert the object into a dict
attachment_properties_dict = attachment_properties_instance.to_dict()
# create an instance of AttachmentProperties from a dict
attachment_properties_from_dict = AttachmentProperties.from_dict(attachment_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


