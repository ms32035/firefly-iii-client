# PreferenceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PolymorphicProperty**](PolymorphicProperty.md) |  | 

## Example

```python
from firefly_iii_client.models.preference_update import PreferenceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceUpdate from a JSON string
preference_update_instance = PreferenceUpdate.from_json(json)
# print the JSON string representation of the object
print(PreferenceUpdate.to_json())

# convert the object into a dict
preference_update_dict = preference_update_instance.to_dict()
# create an instance of PreferenceUpdate from a dict
preference_update_from_dict = PreferenceUpdate.from_dict(preference_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


