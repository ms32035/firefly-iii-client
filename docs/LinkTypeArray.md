# LinkTypeArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LinkTypeRead]**](LinkTypeRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.link_type_array import LinkTypeArray

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTypeArray from a JSON string
link_type_array_instance = LinkTypeArray.from_json(json)
# print the JSON string representation of the object
print(LinkTypeArray.to_json())

# convert the object into a dict
link_type_array_dict = link_type_array_instance.to_dict()
# create an instance of LinkTypeArray from a dict
link_type_array_form_dict = link_type_array.from_dict(link_type_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


