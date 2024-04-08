# InsightGroupEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The currency code of the expenses listed for this account. | [optional] 
**currency_id** | **str** | The currency ID of the expenses listed for this account. | [optional] 
**difference** | **str** | The amount spent or earned between start date and end date, a number defined as a string, for this object and all asset accounts. | [optional] 
**difference_float** | **float** | The amount spent or earned between start date and end date, a number as a float, for this object and all asset accounts. May have rounding errors. | [optional] 
**id** | **str** | This ID is a reference to the original object. | [optional] 
**name** | **str** | This is the name of the object. | [optional] 

## Example

```python
from firefly_iii_client.models.insight_group_entry import InsightGroupEntry

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroupEntry from a JSON string
insight_group_entry_instance = InsightGroupEntry.from_json(json)
# print the JSON string representation of the object
print(InsightGroupEntry.to_json())

# convert the object into a dict
insight_group_entry_dict = insight_group_entry_instance.to_dict()
# create an instance of InsightGroupEntry from a dict
insight_group_entry_form_dict = insight_group_entry.from_dict(insight_group_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


