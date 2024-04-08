# ConfigurationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PolymorphicProperty**](PolymorphicProperty.md) |  | 

## Example

```python
from firefly_iii_client.models.configuration_update import ConfigurationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationUpdate from a JSON string
configuration_update_instance = ConfigurationUpdate.from_json(json)
# print the JSON string representation of the object
print(ConfigurationUpdate.to_json())

# convert the object into a dict
configuration_update_dict = configuration_update_instance.to_dict()
# create an instance of ConfigurationUpdate from a dict
configuration_update_form_dict = configuration_update.from_dict(configuration_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


