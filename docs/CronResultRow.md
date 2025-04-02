# CronResultRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_errored** | **bool** | If the cron job ran into some kind of an error, this value will be true. | [optional] 
**job_fired** | **bool** | This value tells you if this specific cron job actually fired. It may not fire. Some cron jobs only fire every 24 hours, for example.  | [optional] 
**job_succeeded** | **bool** | This value tells you if this specific cron job actually did something. The job may fire but not change anything.  | [optional] 
**message** | **str** | If the cron job ran into some kind of an error, this value will be the error message. The success message if the job actually ran OK.  | [optional] 

## Example

```python
from firefly_iii_client.models.cron_result_row import CronResultRow

# TODO update the JSON string below
json = "{}"
# create an instance of CronResultRow from a JSON string
cron_result_row_instance = CronResultRow.from_json(json)
# print the JSON string representation of the object
print(CronResultRow.to_json())

# convert the object into a dict
cron_result_row_dict = cron_result_row_instance.to_dict()
# create an instance of CronResultRow from a dict
cron_result_row_from_dict = CronResultRow.from_dict(cron_result_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


