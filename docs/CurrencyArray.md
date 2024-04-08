# CurrencyArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CurrencyRead]**](CurrencyRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.currency_array import CurrencyArray

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyArray from a JSON string
currency_array_instance = CurrencyArray.from_json(json)
# print the JSON string representation of the object
print(CurrencyArray.to_json())

# convert the object into a dict
currency_array_dict = currency_array_instance.to_dict()
# create an instance of CurrencyArray from a dict
currency_array_form_dict = currency_array.from_dict(currency_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


