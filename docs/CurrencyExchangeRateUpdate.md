# CurrencyExchangeRateUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date to which the exchange rate is applicable. | 
**rate** | **str** | The exchange rate from the base currency to the destination currency. | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_update import CurrencyExchangeRateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateUpdate from a JSON string
currency_exchange_rate_update_instance = CurrencyExchangeRateUpdate.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateUpdate.to_json())

# convert the object into a dict
currency_exchange_rate_update_dict = currency_exchange_rate_update_instance.to_dict()
# create an instance of CurrencyExchangeRateUpdate from a dict
currency_exchange_rate_update_from_dict = CurrencyExchangeRateUpdate.from_dict(currency_exchange_rate_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


