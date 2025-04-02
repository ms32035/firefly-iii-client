# ObjectGroupSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ObjectGroupRead**](ObjectGroupRead.md) |  | 

## Example

```python
from firefly_iii_client.models.object_group_single import ObjectGroupSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectGroupSingle from a JSON string
object_group_single_instance = ObjectGroupSingle.from_json(json)
# print the JSON string representation of the object
print(ObjectGroupSingle.to_json())

# convert the object into a dict
object_group_single_dict = object_group_single_instance.to_dict()
# create an instance of ObjectGroupSingle from a dict
object_group_single_from_dict = ObjectGroupSingle.from_dict(object_group_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


