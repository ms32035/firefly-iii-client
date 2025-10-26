# PiggyBankEventProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**object_has_currency_setting** | **bool** | Indicates whether the object has a currency setting. If false, the object uses the administration&#39;s primary currency. | [optional] [readonly] 
**pc_amount** | **str** |  | [optional] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**transaction_group_id** | **str** | The transaction group associated with the event. | [optional] 
**transaction_journal_id** | **str** | The journal associated with the event. | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from firefly_iii_client.models.piggy_bank_event_properties import PiggyBankEventProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankEventProperties from a JSON string
piggy_bank_event_properties_instance = PiggyBankEventProperties.from_json(json)
# print the JSON string representation of the object
print(PiggyBankEventProperties.to_json())

# convert the object into a dict
piggy_bank_event_properties_dict = piggy_bank_event_properties_instance.to_dict()
# create an instance of PiggyBankEventProperties from a dict
piggy_bank_event_properties_from_dict = PiggyBankEventProperties.from_dict(piggy_bank_event_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


