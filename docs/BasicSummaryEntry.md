# BasicSummaryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**currency_decimal_places** | **int** | Number of decimals for the associated currency. | [optional] 
**currency_id** | **str** | The currency ID of the associated currency. | [optional] 
**currency_symbol** | **str** |  | [optional] 
**key** | **str** | This is a reference to the type of info shared, not influenced by translations or user preferences. The EUR value is a reference to the currency code. Possibilities are: balance-in-ABC, spent-in-ABC, earned-in-ABC, bills-paid-in-ABC, bills-unpaid-in-ABC, left-to-spend-in-ABC and net-worth-in-ABC. | [optional] 
**local_icon** | **str** | Reference to a font-awesome icon without the fa- part. | [optional] 
**monetary_value** | **float** | The amount as a float. | [optional] 
**sub_title** | **str** | A short explanation of the amounts origin. Already formatted according to the locale of the user or translated, if relevant. | [optional] 
**title** | **str** | A translated title for the information shared. | [optional] 
**value_parsed** | **str** | The amount formatted according to the users locale | [optional] 

## Example

```python
from firefly_iii_client.models.basic_summary_entry import BasicSummaryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BasicSummaryEntry from a JSON string
basic_summary_entry_instance = BasicSummaryEntry.from_json(json)
# print the JSON string representation of the object
print(BasicSummaryEntry.to_json())

# convert the object into a dict
basic_summary_entry_dict = basic_summary_entry_instance.to_dict()
# create an instance of BasicSummaryEntry from a dict
basic_summary_entry_form_dict = basic_summary_entry.from_dict(basic_summary_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


