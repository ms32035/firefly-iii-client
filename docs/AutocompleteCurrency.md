# AutocompleteCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Currency code. | 
**decimal_places** | **int** |  | 
**id** | **str** |  | 
**name** | **str** | Currency name. | 
**symbol** | **str** |  | 

## Example

```python
from firefly_iii_client.models.autocomplete_currency import AutocompleteCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteCurrency from a JSON string
autocomplete_currency_instance = AutocompleteCurrency.from_json(json)
# print the JSON string representation of the object
print(AutocompleteCurrency.to_json())

# convert the object into a dict
autocomplete_currency_dict = autocomplete_currency_instance.to_dict()
# create an instance of AutocompleteCurrency from a dict
autocomplete_currency_form_dict = autocomplete_currency.from_dict(autocomplete_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


