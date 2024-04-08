# Currency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**decimal_places** | **int** | Supports 0-16 decimals. | [optional] 
**default** | **bool** | Make this currency the default currency. | [optional] 
**enabled** | **bool** | Defaults to true | [optional] [default to True]
**name** | **str** |  | 
**symbol** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_form_dict = currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


