# CurrencyExchangeRateSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrencyExchangeRateRead**](CurrencyExchangeRateRead.md) |  | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_single import CurrencyExchangeRateSingle

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateSingle from a JSON string
currency_exchange_rate_single_instance = CurrencyExchangeRateSingle.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateSingle.to_json())

# convert the object into a dict
currency_exchange_rate_single_dict = currency_exchange_rate_single_instance.to_dict()
# create an instance of CurrencyExchangeRateSingle from a dict
currency_exchange_rate_single_from_dict = CurrencyExchangeRateSingle.from_dict(currency_exchange_rate_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


