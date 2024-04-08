# PreferenceSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PreferenceRead**](PreferenceRead.md) |  | 

## Example

```python
from firefly_iii_client.models.preference_single import PreferenceSingle

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceSingle from a JSON string
preference_single_instance = PreferenceSingle.from_json(json)
# print the JSON string representation of the object
print(PreferenceSingle.to_json())

# convert the object into a dict
preference_single_dict = preference_single_instance.to_dict()
# create an instance of PreferenceSingle from a dict
preference_single_form_dict = preference_single.from_dict(preference_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


