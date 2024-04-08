# UserArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserRead]**](UserRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.user_array import UserArray

# TODO update the JSON string below
json = "{}"
# create an instance of UserArray from a JSON string
user_array_instance = UserArray.from_json(json)
# print the JSON string representation of the object
print(UserArray.to_json())

# convert the object into a dict
user_array_dict = user_array_instance.to_dict()
# create an instance of UserArray from a dict
user_array_form_dict = user_array.from_dict(user_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


