# CronResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_budgets** | [**CronResultRow**](CronResultRow.md) |  | [optional] 
**recurring_transactions** | [**CronResultRow**](CronResultRow.md) |  | [optional] 
**telemetry** | [**CronResultRow**](CronResultRow.md) |  | [optional] 

## Example

```python
from firefly_iii_client.models.cron_result import CronResult

# TODO update the JSON string below
json = "{}"
# create an instance of CronResult from a JSON string
cron_result_instance = CronResult.from_json(json)
# print the JSON string representation of the object
print(CronResult.to_json())

# convert the object into a dict
cron_result_dict = cron_result_instance.to_dict()
# create an instance of CronResult from a dict
cron_result_form_dict = cron_result.from_dict(cron_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


