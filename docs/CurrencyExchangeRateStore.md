# CurrencyExchangeRateStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date to which the exchange rate is applicable. | 
**var_from** | **str** | The base currency code. | 
**rate** | **str** | The exchange rate from the base currency to the destination currency. | 
**to** | **str** | The destination currency code. | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_store import CurrencyExchangeRateStore

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateStore from a JSON string
currency_exchange_rate_store_instance = CurrencyExchangeRateStore.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateStore.to_json())

# convert the object into a dict
currency_exchange_rate_store_dict = currency_exchange_rate_store_instance.to_dict()
# create an instance of CurrencyExchangeRateStore from a dict
currency_exchange_rate_store_from_dict = CurrencyExchangeRateStore.from_dict(currency_exchange_rate_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


