# CurrencyExchangeRateRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CurrencyExchangeRateReadAttributes**](CurrencyExchangeRateReadAttributes.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_read import CurrencyExchangeRateRead

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateRead from a JSON string
currency_exchange_rate_read_instance = CurrencyExchangeRateRead.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateRead.to_json())

# convert the object into a dict
currency_exchange_rate_read_dict = currency_exchange_rate_read_instance.to_dict()
# create an instance of CurrencyExchangeRateRead from a dict
currency_exchange_rate_read_from_dict = CurrencyExchangeRateRead.from_dict(currency_exchange_rate_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


