# RecurrenceRepetition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moment** | **str** | Information that defined the type of repetition. - For &#39;daily&#39;, this is empty. - For &#39;weekly&#39;, it is day of the week between 1 and 7 (Monday - Sunday). - For &#39;ndom&#39;, it is &#39;1,2&#39; or &#39;4,5&#39; or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). &#39;2,3&#39; means: the 2nd Wednesday of the month - For &#39;monthly&#39; it is the day of the month (1 - 31) - For yearly, it is a full date, ie &#39;2018-09-17&#39;. The year you use does not matter.  | 
**type** | **str** | The type of the repetition. ndom means: the n-th weekday of the month, where you can also specify which day of the week. | 
**created_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** | Auto-generated repetition description. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**occurrences** | **[datetime]** | Array of future dates when the repetition will apply to. Auto generated. | [optional] [readonly] 
**skip** | **int** | How many occurrences to skip. 0 means skip nothing. 1 means every other. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**weekend** | **int** | How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


