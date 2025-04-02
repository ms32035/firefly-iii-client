# UserGroupReadMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[UserGroupReadRole]**](UserGroupReadRole.md) |  | [optional] 
**user_email** | **str** | The email address of the member | [optional] [readonly] 
**user_id** | **str** | The ID of the member. | [optional] [readonly] 
**you** | **bool** | Is this you? (the current user) | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.user_group_read_members import UserGroupReadMembers

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupReadMembers from a JSON string
user_group_read_members_instance = UserGroupReadMembers.from_json(json)
# print the JSON string representation of the object
print(UserGroupReadMembers.to_json())

# convert the object into a dict
user_group_read_members_dict = user_group_read_members_instance.to_dict()
# create an instance of UserGroupReadMembers from a dict
user_group_read_members_from_dict = UserGroupReadMembers.from_dict(user_group_read_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


