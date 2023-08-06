# firefly_iii_client.model.cron_result_row.CronResultRow

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_errored** | None, bool,  | NoneClass, BoolClass,  | If the cron job ran into some kind of an error, this value will be true. | [optional] 
**job_fired** | None, bool,  | NoneClass, BoolClass,  | This value tells you if this specific cron job actually fired. It may not fire. Some cron jobs only fire every 24 hours, for example.  | [optional] 
**job_succeeded** | None, bool,  | NoneClass, BoolClass,  | This value tells you if this specific cron job actually did something. The job may fire but not change anything.  | [optional] 
**message** | None, str,  | NoneClass, str,  | If the cron job ran into some kind of an error, this value will be the error message. The success message if the job actually ran OK.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

