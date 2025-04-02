# ObjectGroupRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ObjectGroup**](ObjectGroup.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.object_group_read import ObjectGroupRead

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectGroupRead from a JSON string
object_group_read_instance = ObjectGroupRead.from_json(json)
# print the JSON string representation of the object
print(ObjectGroupRead.to_json())

# convert the object into a dict
object_group_read_dict = object_group_read_instance.to_dict()
# create an instance of ObjectGroupRead from a dict
object_group_read_from_dict = ObjectGroupRead.from_dict(object_group_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


