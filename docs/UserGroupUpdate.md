# UserGroupUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_currency_code** | **str** | Use either native_currency_id or native_currency_code. This will set the native currency for the user group (&#39;financial administration&#39;). | [optional] 
**native_currency_id** | **str** | Use either native_currency_id or native_currency_code. This will set the native currency for the user group (&#39;financial administration&#39;). | [optional] 
**title** | **str** | A descriptive title for the user group. | 

## Example

```python
from firefly_iii_client.models.user_group_update import UserGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupUpdate from a JSON string
user_group_update_instance = UserGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(UserGroupUpdate.to_json())

# convert the object into a dict
user_group_update_dict = user_group_update_instance.to_dict()
# create an instance of UserGroupUpdate from a dict
user_group_update_from_dict = UserGroupUpdate.from_dict(user_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


