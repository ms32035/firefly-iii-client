# AutocompleteCurrencyCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Currency code. | 
**decimal_places** | **int** |  | 
**id** | **str** |  | 
**name** | **str** | Currency name with the code between brackets. | 
**symbol** | **str** |  | 

## Example

```python
from firefly_iii_client.models.autocomplete_currency_code import AutocompleteCurrencyCode

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteCurrencyCode from a JSON string
autocomplete_currency_code_instance = AutocompleteCurrencyCode.from_json(json)
# print the JSON string representation of the object
print(AutocompleteCurrencyCode.to_json())

# convert the object into a dict
autocomplete_currency_code_dict = autocomplete_currency_code_instance.to_dict()
# create an instance of AutocompleteCurrencyCode from a dict
autocomplete_currency_code_from_dict = AutocompleteCurrencyCode.from_dict(autocomplete_currency_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


