# ValidationErrorResponseErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **List[str]** |  | [optional] 
**blocked_code** | **List[str]** |  | [optional] 
**var_date** | **List[str]** |  | [optional] 
**email** | **List[str]** |  | [optional] 
**end** | **List[str]** |  | [optional] 
**iban** | **List[str]** |  | [optional] 
**name** | **List[str]** |  | [optional] 
**role** | **List[str]** |  | [optional] 
**start** | **List[str]** |  | [optional] 
**type** | **List[str]** |  | [optional] 

## Example

```python
from firefly_iii_client.models.validation_error_response_errors import ValidationErrorResponseErrors

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseErrors from a JSON string
validation_error_response_errors_instance = ValidationErrorResponseErrors.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseErrors.to_json())

# convert the object into a dict
validation_error_response_errors_dict = validation_error_response_errors_instance.to_dict()
# create an instance of ValidationErrorResponseErrors from a dict
validation_error_response_errors_form_dict = validation_error_response_errors.from_dict(validation_error_response_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


