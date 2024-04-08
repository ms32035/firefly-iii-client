# TagModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**var_date** | **date** | The date to which the tag is applicable. | [optional] 
**description** | **str** |  | [optional] 
**latitude** | **float** | Latitude of the tag&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**longitude** | **float** | Latitude of the tag&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**tag** | **str** | The tag | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

## Example

```python
from firefly_iii_client.models.tag_model import TagModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagModel from a JSON string
tag_model_instance = TagModel.from_json(json)
# print the JSON string representation of the object
print(TagModel.to_json())

# convert the object into a dict
tag_model_dict = tag_model_instance.to_dict()
# create an instance of TagModel from a dict
tag_model_form_dict = tag_model.from_dict(tag_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


