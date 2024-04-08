# ObjectGroupArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ObjectGroupRead]**](ObjectGroupRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.object_group_array import ObjectGroupArray

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectGroupArray from a JSON string
object_group_array_instance = ObjectGroupArray.from_json(json)
# print the JSON string representation of the object
print(ObjectGroupArray.to_json())

# convert the object into a dict
object_group_array_dict = object_group_array_instance.to_dict()
# create an instance of ObjectGroupArray from a dict
object_group_array_form_dict = object_group_array.from_dict(object_group_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


