# ObjectGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**order** | **int** | Order of the object group | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.object_group import ObjectGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectGroup from a JSON string
object_group_instance = ObjectGroup.from_json(json)
# print the JSON string representation of the object
print(ObjectGroup.to_json())

# convert the object into a dict
object_group_dict = object_group_instance.to_dict()
# create an instance of ObjectGroup from a dict
object_group_from_dict = ObjectGroup.from_dict(object_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


