# SystemInfoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**driver** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**php_version** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.system_info_data import SystemInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfoData from a JSON string
system_info_data_instance = SystemInfoData.from_json(json)
# print the JSON string representation of the object
print(SystemInfoData.to_json())

# convert the object into a dict
system_info_data_dict = system_info_data_instance.to_dict()
# create an instance of SystemInfoData from a dict
system_info_data_form_dict = system_info_data.from_dict(system_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


