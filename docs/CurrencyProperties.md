# CurrencyProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**decimal_places** | **int** | Supports 0-16 decimals. | [optional] 
**enabled** | **bool** | Defaults to true | [optional] [default to True]
**name** | **str** |  | 
**primary** | **bool** | Is the primary currency? | [optional] 
**symbol** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.currency_properties import CurrencyProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyProperties from a JSON string
currency_properties_instance = CurrencyProperties.from_json(json)
# print the JSON string representation of the object
print(CurrencyProperties.to_json())

# convert the object into a dict
currency_properties_dict = currency_properties_instance.to_dict()
# create an instance of CurrencyProperties from a dict
currency_properties_from_dict = CurrencyProperties.from_dict(currency_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


