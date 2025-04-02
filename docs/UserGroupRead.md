# UserGroupRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserGroupReadAttributes**](UserGroupReadAttributes.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.user_group_read import UserGroupRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupRead from a JSON string
user_group_read_instance = UserGroupRead.from_json(json)
# print the JSON string representation of the object
print(UserGroupRead.to_json())

# convert the object into a dict
user_group_read_dict = user_group_read_instance.to_dict()
# create an instance of UserGroupRead from a dict
user_group_read_from_dict = UserGroupRead.from_dict(user_group_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


