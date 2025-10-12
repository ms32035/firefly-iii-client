# CurrencyExchangeRateStoreByDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The &#39;from&#39;-currency | 
**rates** | **Dict[str, str]** | The actual entries for this data set. They &#39;key&#39; value is &#39;to&#39; currency. The value is the exchange rate. | 

## Example

```python
from firefly_iii_client.models.currency_exchange_rate_store_by_date import CurrencyExchangeRateStoreByDate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRateStoreByDate from a JSON string
currency_exchange_rate_store_by_date_instance = CurrencyExchangeRateStoreByDate.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRateStoreByDate.to_json())

# convert the object into a dict
currency_exchange_rate_store_by_date_dict = currency_exchange_rate_store_by_date_instance.to_dict()
# create an instance of CurrencyExchangeRateStoreByDate from a dict
currency_exchange_rate_store_by_date_from_dict = CurrencyExchangeRateStoreByDate.from_dict(currency_exchange_rate_store_by_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


