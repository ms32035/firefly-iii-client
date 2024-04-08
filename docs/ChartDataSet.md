# ChartDataSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**currency_decimal_places** | **int** | Number of decimals for the currency associated to the data in the entries. | [optional] 
**currency_id** | **str** | The currency ID of the currency associated to the data in the entries. | [optional] 
**currency_symbol** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**entries** | [**List[ChartDataPoint]**](ChartDataPoint.md) | The actual entries for this data set. They &#39;key&#39; value is the label for the data point. The value is the actual (numerical) value. | [optional] 
**label** | **str** | This is the title of the current set. It can refer to an account, a budget or another object (by name). | [optional] 
**start_date** | **datetime** |  | [optional] 
**type** | **str** | Indicated the type of chart that is expected to be rendered. You can safely ignore this if you want. | [optional] 
**y_axis_id** | **int** | Used to indicate the Y axis for this data set. Is usually between 0 and 1 (left and right side of the chart). | [optional] 

## Example

```python
from firefly_iii_client.models.chart_data_set import ChartDataSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChartDataSet from a JSON string
chart_data_set_instance = ChartDataSet.from_json(json)
# print the JSON string representation of the object
print(ChartDataSet.to_json())

# convert the object into a dict
chart_data_set_dict = chart_data_set_instance.to_dict()
# create an instance of ChartDataSet from a dict
chart_data_set_form_dict = chart_data_set.from_dict(chart_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


