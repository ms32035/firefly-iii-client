# CategoryProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**earned** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Amount(s) earned in the currencies in the database for this category. ONLY present when start and date are set. | [optional] [readonly] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**object_has_currency_setting** | **bool** | This object never has its own currency setting, so this value is always false. | [optional] 
**pc_earned** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Amount(s) earned in the primary currency in the database for this category. ONLY present when start and date are set.  | [optional] [readonly] 
**pc_spent** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Amount(s) spent in the primary currency in the database for this category. ONLY present when start and date are set.  | [optional] [readonly] 
**pc_transferred** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Amount(s) transferred in primary currency in the database for this category. ONLY present when start and date are set.  | [optional] [readonly] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**spent** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Amount(s) spent in the currencies in the database for this category. ONLY present when start and date are set. | [optional] [readonly] 
**transferred** | [**List[ArrayEntryWithCurrencyAndSum]**](ArrayEntryWithCurrencyAndSum.md) | Amount(s) transferred in the currencies in the database for this category. ONLY present when start and date are set.  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.category_properties import CategoryProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryProperties from a JSON string
category_properties_instance = CategoryProperties.from_json(json)
# print the JSON string representation of the object
print(CategoryProperties.to_json())

# convert the object into a dict
category_properties_dict = category_properties_instance.to_dict()
# create an instance of CategoryProperties from a dict
category_properties_from_dict = CategoryProperties.from_dict(category_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


