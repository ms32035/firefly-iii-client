# PiggyBankEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**currency_decimal_places** | **int** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**transaction_group_id** | **str** | The transaction group associated with the event. | [optional] 
**transaction_journal_id** | **str** | The journal associated with the event. | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from firefly_iii_client.models.piggy_bank_event import PiggyBankEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankEvent from a JSON string
piggy_bank_event_instance = PiggyBankEvent.from_json(json)
# print the JSON string representation of the object
print(PiggyBankEvent.to_json())

# convert the object into a dict
piggy_bank_event_dict = piggy_bank_event_instance.to_dict()
# create an instance of PiggyBankEvent from a dict
piggy_bank_event_from_dict = PiggyBankEvent.from_dict(piggy_bank_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


