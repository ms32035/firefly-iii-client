# CurrencyExchangeRateUpdateNoDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **str** | The exchange rate from the base currency to the destination currency. | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_update_no_date import CurrencyExchangeRateUpdateNoDate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateUpdateNoDate from a JSON string
currency_exchange_rate_update_no_date_instance = CurrencyExchangeRateUpdateNoDate.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateUpdateNoDate.to_json())

# convert the object into a dict
currency_exchange_rate_update_no_date_dict = currency_exchange_rate_update_no_date_instance.to_dict()
# create an instance of CurrencyExchangeRateUpdateNoDate from a dict
currency_exchange_rate_update_no_date_from_dict = CurrencyExchangeRateUpdateNoDate.from_dict(currency_exchange_rate_update_no_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


