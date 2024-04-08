# ConfigurationSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Configuration**](Configuration.md) |  | 

## Example

```python
from firefly_iii_client.models.configuration_single import ConfigurationSingle

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationSingle from a JSON string
configuration_single_instance = ConfigurationSingle.from_json(json)
# print the JSON string representation of the object
print(ConfigurationSingle.to_json())

# convert the object into a dict
configuration_single_dict = configuration_single_instance.to_dict()
# create an instance of ConfigurationSingle from a dict
configuration_single_form_dict = configuration_single.from_dict(configuration_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


