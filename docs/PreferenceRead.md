# PreferenceRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Preference**](Preference.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.preference_read import PreferenceRead

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceRead from a JSON string
preference_read_instance = PreferenceRead.from_json(json)
# print the JSON string representation of the object
print(PreferenceRead.to_json())

# convert the object into a dict
preference_read_dict = preference_read_instance.to_dict()
# create an instance of PreferenceRead from a dict
preference_read_form_dict = preference_read.from_dict(preference_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


