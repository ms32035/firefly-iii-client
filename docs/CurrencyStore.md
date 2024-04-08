# CurrencyStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**decimal_places** | **int** | Supports 0-16 decimals. | [optional] 
**default** | **bool** | Make this currency the default currency. You can set this value to FALSE, in which case nothing will change to the default currency. If you set it to TRUE, the current default currency will no longer be the default currency. | [optional] 
**enabled** | **bool** | Defaults to true | [optional] [default to True]
**name** | **str** |  | 
**symbol** | **str** |  | 

## Example

```python
from firefly_iii_client.models.currency_store import CurrencyStore

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyStore from a JSON string
currency_store_instance = CurrencyStore.from_json(json)
# print the JSON string representation of the object
print(CurrencyStore.to_json())

# convert the object into a dict
currency_store_dict = currency_store_instance.to_dict()
# create an instance of CurrencyStore from a dict
currency_store_form_dict = currency_store.from_dict(currency_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


