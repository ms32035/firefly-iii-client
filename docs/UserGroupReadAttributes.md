# UserGroupReadAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_see_members** | **bool** | Can the current user see the members of this user group? | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**in_use** | **bool** | Is this user group (&#39;financial administration&#39;) currently the active administration? | [optional] [readonly] 
**members** | [**List[UserGroupReadMembers]**](UserGroupReadMembers.md) |  | [optional] 
**native_currency_code** | **str** | Returns the native currency code of the user group. | [optional] 
**native_currency_decimal_places** | **int** | Returns the native currency decimal places of the user group. | [optional] [readonly] 
**native_currency_id** | **str** | Returns the native currency ID of the user group. | [optional] [readonly] 
**native_currency_symbol** | **str** | Returns the native currency symbol of the user group. | [optional] [readonly] 
**title** | **str** | Title of the user group. By default, it is the same as the user&#39;s email address. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.user_group_read_attributes import UserGroupReadAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupReadAttributes from a JSON string
user_group_read_attributes_instance = UserGroupReadAttributes.from_json(json)
# print the JSON string representation of the object
print(UserGroupReadAttributes.to_json())

# convert the object into a dict
user_group_read_attributes_dict = user_group_read_attributes_instance.to_dict()
# create an instance of UserGroupReadAttributes from a dict
user_group_read_attributes_from_dict = UserGroupReadAttributes.from_dict(user_group_read_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


