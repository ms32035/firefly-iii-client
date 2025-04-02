# UserGroupSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserGroupRead**](UserGroupRead.md) |  | 

## Example

```python
from firefly_iii_client.models.user_group_single import UserGroupSingle

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupSingle from a JSON string
user_group_single_instance = UserGroupSingle.from_json(json)
# print the JSON string representation of the object
print(UserGroupSingle.to_json())

# convert the object into a dict
user_group_single_dict = user_group_single_instance.to_dict()
# create an instance of UserGroupSingle from a dict
user_group_single_from_dict = UserGroupSingle.from_dict(user_group_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


