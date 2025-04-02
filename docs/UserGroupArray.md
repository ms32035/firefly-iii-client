# UserGroupArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserGroupRead]**](UserGroupRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.user_group_array import UserGroupArray

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupArray from a JSON string
user_group_array_instance = UserGroupArray.from_json(json)
# print the JSON string representation of the object
print(UserGroupArray.to_json())

# convert the object into a dict
user_group_array_dict = user_group_array_instance.to_dict()
# create an instance of UserGroupArray from a dict
user_group_array_from_dict = UserGroupArray.from_dict(user_group_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


