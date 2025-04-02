# InsightTransferEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The currency code of the expenses listed for this account. | [optional] 
**currency_id** | **str** | The currency ID of the expenses listed for this account. | [optional] 
**difference** | **str** | The total amount transferred between start date and end date, a number defined as a string, for this asset account. | [optional] 
**difference_float** | **float** | The total amount transferred between start date and end date, a number as a float, for this asset account. May have rounding errors. | [optional] 
**id** | **str** | This ID is a reference to the original object. | [optional] 
**var_in** | **str** | The total amount transferred TO this account between start date and end date, a number defined as a string, for this asset account. | [optional] 
**in_float** | **float** | The total amount transferred FROM this account between start date and end date, a number as a float, for this asset account. May have rounding errors. | [optional] 
**name** | **str** | This is the name of the object. | [optional] 
**out** | **str** | The total amount transferred FROM this account between start date and end date, a number defined as a string, for this asset account. | [optional] 
**out_float** | **float** | The total amount transferred TO this account between start date and end date, a number as a float, for this asset account. May have rounding errors. | [optional] 

## Example

```python
from firefly_iii_client.models.insight_transfer_entry import InsightTransferEntry

# TODO update the JSON string below
json = "{}"
# create an instance of InsightTransferEntry from a JSON string
insight_transfer_entry_instance = InsightTransferEntry.from_json(json)
# print the JSON string representation of the object
print(InsightTransferEntry.to_json())

# convert the object into a dict
insight_transfer_entry_dict = insight_transfer_entry_instance.to_dict()
# create an instance of InsightTransferEntry from a dict
insight_transfer_entry_from_dict = InsightTransferEntry.from_dict(insight_transfer_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


