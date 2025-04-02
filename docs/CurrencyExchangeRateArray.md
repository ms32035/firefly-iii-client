# CurrencyExchangeRateArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CurrencyExchangeRateRead]**](CurrencyExchangeRateRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_array import CurrencyExchangeRateArray

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateArray from a JSON string
currency_exchange_rate_array_instance = CurrencyExchangeRateArray.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateArray.to_json())

# convert the object into a dict
currency_exchange_rate_array_dict = currency_exchange_rate_array_instance.to_dict()
# create an instance of CurrencyExchangeRateArray from a dict
currency_exchange_rate_array_from_dict = CurrencyExchangeRateArray.from_dict(currency_exchange_rate_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


