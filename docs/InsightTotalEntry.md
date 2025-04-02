# InsightTotalEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The currency code of the expenses listed for this expense account. | [optional] 
**currency_id** | **str** | The currency ID of the expenses listed for this expense account. | [optional] 
**difference** | **str** | The amount spent between start date and end date, defined as a string, for this expense account and all asset accounts. | [optional] 
**difference_float** | **float** | The amount spent between start date and end date, defined as a string, for this expense account and all asset accounts. This number is a float (double) and may have rounding errors. | [optional] 

## Example

```python
from firefly_iii_client.models.insight_total_entry import InsightTotalEntry

# TODO update the JSON string below
json = "{}"
# create an instance of InsightTotalEntry from a JSON string
insight_total_entry_instance = InsightTotalEntry.from_json(json)
# print the JSON string representation of the object
print(InsightTotalEntry.to_json())

# convert the object into a dict
insight_total_entry_dict = insight_total_entry_instance.to_dict()
# create an instance of InsightTotalEntry from a dict
insight_total_entry_from_dict = InsightTotalEntry.from_dict(insight_total_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


