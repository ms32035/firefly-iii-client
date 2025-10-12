# ChartDataSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**entries** | [**List[ChartDataPoint]**](ChartDataPoint.md) | The actual entries for this data set. They &#39;key&#39; value is the label for the data point. The value is the actual (numerical) value. | [optional] 
**label** | **str** | This is the title of the current set. It can refer to an account, a budget or another object (by name). | [optional] 
**pc_entries** | [**List[ChartDataPoint]**](ChartDataPoint.md) | The actual entries for this data set. They &#39;key&#39; value is the label for the data point. The value is the actual (numerical) value. | [optional] 
**period** | [**ChartDatasetPeriodProperty**](ChartDatasetPeriodProperty.md) |  | [optional] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
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
chart_data_set_from_dict = ChartDataSet.from_dict(chart_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


