# CurrencyExchangeProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**var_date** | **datetime** | Date and time of the exchange rate. | [optional] [readonly] 
**from_currency_code** | **str** | Base currency code for this exchange rate entry. | [optional] [readonly] 
**from_currency_decimal_places** | **int** | Base currency decimal places for this exchange rate entry. | [optional] [readonly] 
**from_currency_id** | **str** | Base currency ID for this exchange rate entry. | [optional] [readonly] 
**from_currency_name** | **str** | Base currency name for this exchange rate entry. | [optional] [readonly] 
**from_currency_symbol** | **str** | Base currency symbol for this exchange rate entry. | [optional] [readonly] 
**rate** | **str** | The actual exchange rate. How many &#39;to&#39; currency will you get for 1 &#39;from&#39; currency? | [optional] [readonly] 
**to_currency_code** | **str** | Destination currency code for this exchange rate entry. | [optional] [readonly] 
**to_currency_decimal_places** | **int** | Destination currency decimal places for this exchange rate entry. | [optional] [readonly] 
**to_currency_id** | **str** | Destination currency ID for this exchange rate entry. | [optional] [readonly] 
**to_currency_name** | **str** | Destination currency name for this exchange rate entry. | [optional] [readonly] 
**to_currency_symbol** | **str** | Destination currency symbol for this exchange rate entry. | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.currency_exchange_properties import CurrencyExchangeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeProperties from a JSON string
currency_exchange_properties_instance = CurrencyExchangeProperties.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeProperties.to_json())

# convert the object into a dict
currency_exchange_properties_dict = currency_exchange_properties_instance.to_dict()
# create an instance of CurrencyExchangeProperties from a dict
currency_exchange_properties_from_dict = CurrencyExchangeProperties.from_dict(currency_exchange_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


