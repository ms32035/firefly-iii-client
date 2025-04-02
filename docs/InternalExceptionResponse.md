# InternalExceptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.internal_exception_response import InternalExceptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalExceptionResponse from a JSON string
internal_exception_response_instance = InternalExceptionResponse.from_json(json)
# print the JSON string representation of the object
print(InternalExceptionResponse.to_json())

# convert the object into a dict
internal_exception_response_dict = internal_exception_response_instance.to_dict()
# create an instance of InternalExceptionResponse from a dict
internal_exception_response_from_dict = InternalExceptionResponse.from_dict(internal_exception_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


