# CurrencySingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrencyRead**](CurrencyRead.md) |  | 

## Example

```python
from firefly_iii_client.models.currency_single import CurrencySingle

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencySingle from a JSON string
currency_single_instance = CurrencySingle.from_json(json)
# print the JSON string representation of the object
print(CurrencySingle.to_json())

# convert the object into a dict
currency_single_dict = currency_single_instance.to_dict()
# create an instance of CurrencySingle from a dict
currency_single_form_dict = currency_single.from_dict(currency_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


