# TagArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TagRead]**](TagRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.tag_array import TagArray

# TODO update the JSON string below
json = "{}"
# create an instance of TagArray from a JSON string
tag_array_instance = TagArray.from_json(json)
# print the JSON string representation of the object
print(TagArray.to_json())

# convert the object into a dict
tag_array_dict = tag_array_instance.to_dict()
# create an instance of TagArray from a dict
tag_array_form_dict = tag_array.from_dict(tag_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


