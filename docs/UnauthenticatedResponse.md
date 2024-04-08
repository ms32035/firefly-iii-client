# UnauthenticatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.unauthenticated_response import UnauthenticatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthenticatedResponse from a JSON string
unauthenticated_response_instance = UnauthenticatedResponse.from_json(json)
# print the JSON string representation of the object
print(UnauthenticatedResponse.to_json())

# convert the object into a dict
unauthenticated_response_dict = unauthenticated_response_instance.to_dict()
# create an instance of UnauthenticatedResponse from a dict
unauthenticated_response_form_dict = unauthenticated_response.from_dict(unauthenticated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


