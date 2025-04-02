# Preference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**data** | [**PolymorphicProperty**](PolymorphicProperty.md) |  | 
**name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.preference import Preference

# TODO update the JSON string below
json = "{}"
# create an instance of Preference from a JSON string
preference_instance = Preference.from_json(json)
# print the JSON string representation of the object
print(Preference.to_json())

# convert the object into a dict
preference_dict = preference_instance.to_dict()
# create an instance of Preference from a dict
preference_from_dict = Preference.from_dict(preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


