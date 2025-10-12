# BillPropertiesPaidDatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount that was paid for this subscription in the subscription&#39;s currency. | [optional] 
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**var_date** | **datetime** | Date the bill was paid. | [optional] [readonly] 
**foreign_amount** | **str** | The foreign amount that was paid for this subscription in the subscription&#39;s currency. | [optional] 
**pc_amount** | **str** | The amount that was paid for this subscription in the administration&#39;s primary currency. | [optional] 
**pc_foreign_amount** | **str** | The foreign amount that was paid for this subscription in the administration&#39;s primary currency. | [optional] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**subscription_id** | **str** | ID of this subscription. | [optional] [readonly] 
**transaction_group_id** | **str** | Transaction group ID of the transaction linked to this subscription. | [optional] [readonly] 
**transaction_journal_id** | **str** | Transaction journal ID of the transaction linked to this subscription. | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.bill_properties_paid_dates_inner import BillPropertiesPaidDatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BillPropertiesPaidDatesInner from a JSON string
bill_properties_paid_dates_inner_instance = BillPropertiesPaidDatesInner.from_json(json)
# print the JSON string representation of the object
print(BillPropertiesPaidDatesInner.to_json())

# convert the object into a dict
bill_properties_paid_dates_inner_dict = bill_properties_paid_dates_inner_instance.to_dict()
# create an instance of BillPropertiesPaidDatesInner from a dict
bill_properties_paid_dates_inner_from_dict = BillPropertiesPaidDatesInner.from_dict(bill_properties_paid_dates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


