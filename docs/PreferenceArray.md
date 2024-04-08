# PreferenceArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PreferenceRead]**](PreferenceRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.preference_array import PreferenceArray

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceArray from a JSON string
preference_array_instance = PreferenceArray.from_json(json)
# print the JSON string representation of the object
print(PreferenceArray.to_json())

# convert the object into a dict
preference_array_dict = preference_array_instance.to_dict()
# create an instance of PreferenceArray from a dict
preference_array_form_dict = preference_array.from_dict(preference_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


