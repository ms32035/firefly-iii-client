# ArrayEntryWithCurrencyAndSum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**currency_decimal_places** | **int** | Number of decimals supported by the currency | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**sum** | **str** | The amount earned, spent or transferred. | [optional] 

## Example

```python
from firefly_iii_client.models.array_entry_with_currency_and_sum import ArrayEntryWithCurrencyAndSum

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayEntryWithCurrencyAndSum from a JSON string
array_entry_with_currency_and_sum_instance = ArrayEntryWithCurrencyAndSum.from_json(json)
# print the JSON string representation of the object
print(ArrayEntryWithCurrencyAndSum.to_json())

# convert the object into a dict
array_entry_with_currency_and_sum_dict = array_entry_with_currency_and_sum_instance.to_dict()
# create an instance of ArrayEntryWithCurrencyAndSum from a dict
array_entry_with_currency_and_sum_from_dict = ArrayEntryWithCurrencyAndSum.from_dict(array_entry_with_currency_and_sum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


