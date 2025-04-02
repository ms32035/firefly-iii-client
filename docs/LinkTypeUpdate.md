# LinkTypeUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inward** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**outward** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.link_type_update import LinkTypeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTypeUpdate from a JSON string
link_type_update_instance = LinkTypeUpdate.from_json(json)
# print the JSON string representation of the object
print(LinkTypeUpdate.to_json())

# convert the object into a dict
link_type_update_dict = link_type_update_instance.to_dict()
# create an instance of LinkTypeUpdate from a dict
link_type_update_from_dict = LinkTypeUpdate.from_dict(link_type_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


