# firefly_iii_client.model.chart_data_set.ChartDataSet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**currency_code** | str,  | str,  |  | [optional] 
**currency_decimal_places** | decimal.Decimal, int,  | decimal.Decimal,  | Number of decimals for the currency associated to the data in the entries. | [optional] value must be a 32 bit integer
**currency_id** | str,  | str,  | The currency ID of the currency associated to the data in the entries. | [optional] 
**currency_symbol** | str,  | str,  |  | [optional] 
**end_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[entries](#entries)** | list, tuple,  | tuple,  | The actual entries for this data set. They &#x27;key&#x27; value is the label for the data point. The value is the actual (numerical) value. | [optional] 
**label** | str,  | str,  | This is the title of the current set. It can refer to an account, a budget or another object (by name). | [optional] 
**start_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**type** | str,  | str,  | Indicated the type of chart that is expected to be rendered. You can safely ignore this if you want. | [optional] 
**yAxisID** | decimal.Decimal, int,  | decimal.Decimal,  | Used to indicate the Y axis for this data set. Is usually between 0 and 1 (left and right side of the chart). | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# entries

The actual entries for this data set. They 'key' value is the label for the data point. The value is the actual (numerical) value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The actual entries for this data set. They &#x27;key&#x27; value is the label for the data point. The value is the actual (numerical) value. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ChartDataPoint**](ChartDataPoint.md) | [**ChartDataPoint**](ChartDataPoint.md) | [**ChartDataPoint**](ChartDataPoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

