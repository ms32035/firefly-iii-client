# CurrencyRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Currency**](Currency.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.currency_read import CurrencyRead

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyRead from a JSON string
currency_read_instance = CurrencyRead.from_json(json)
# print the JSON string representation of the object
print(CurrencyRead.to_json())

# convert the object into a dict
currency_read_dict = currency_read_instance.to_dict()
# create an instance of CurrencyRead from a dict
currency_read_form_dict = currency_read.from_dict(currency_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


