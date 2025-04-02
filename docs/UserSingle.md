# UserSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserRead**](UserRead.md) |  | 

## Example

```python
from firefly_iii_client.models.user_single import UserSingle

# TODO update the JSON string below
json = "{}"
# create an instance of UserSingle from a JSON string
user_single_instance = UserSingle.from_json(json)
# print the JSON string representation of the object
print(UserSingle.to_json())

# convert the object into a dict
user_single_dict = user_single_instance.to_dict()
# create an instance of UserSingle from a dict
user_single_from_dict = UserSingle.from_dict(user_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


