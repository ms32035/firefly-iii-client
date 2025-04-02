# BillPaidDatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date the bill was paid. | [optional] [readonly] 
**transaction_group_id** | **str** | Transaction group ID of the paid bill. | [optional] [readonly] 
**transaction_journal_id** | **str** | Transaction journal ID of the paid bill. | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.bill_paid_dates_inner import BillPaidDatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaidDatesInner from a JSON string
bill_paid_dates_inner_instance = BillPaidDatesInner.from_json(json)
# print the JSON string representation of the object
print(BillPaidDatesInner.to_json())

# convert the object into a dict
bill_paid_dates_inner_dict = bill_paid_dates_inner_instance.to_dict()
# create an instance of BillPaidDatesInner from a dict
bill_paid_dates_inner_from_dict = BillPaidDatesInner.from_dict(bill_paid_dates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


