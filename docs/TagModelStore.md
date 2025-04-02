# TagModelStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date to which the tag is applicable. | [optional] 
**description** | **str** |  | [optional] 
**latitude** | **float** | Latitude of the tag&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**longitude** | **float** | Latitude of the tag&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**tag** | **str** | The tag | 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

## Example

```python
from firefly_iii_client.models.tag_model_store import TagModelStore

# TODO update the JSON string below
json = "{}"
# create an instance of TagModelStore from a JSON string
tag_model_store_instance = TagModelStore.from_json(json)
# print the JSON string representation of the object
print(TagModelStore.to_json())

# convert the object into a dict
tag_model_store_dict = tag_model_store_instance.to_dict()
# create an instance of TagModelStore from a dict
tag_model_store_from_dict = TagModelStore.from_dict(tag_model_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


