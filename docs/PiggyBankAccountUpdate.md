# PiggyBankAccountUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_amount** | **str** | The amount saved currently. | [optional] 
**id** | **str** | The ID of the account. | 
**name** | **str** | The name of the account. | [optional] 

## Example

```python
from firefly_iii_client.models.piggy_bank_account_update import PiggyBankAccountUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankAccountUpdate from a JSON string
piggy_bank_account_update_instance = PiggyBankAccountUpdate.from_json(json)
# print the JSON string representation of the object
print(PiggyBankAccountUpdate.to_json())

# convert the object into a dict
piggy_bank_account_update_dict = piggy_bank_account_update_instance.to_dict()
# create an instance of PiggyBankAccountUpdate from a dict
piggy_bank_account_update_from_dict = PiggyBankAccountUpdate.from_dict(piggy_bank_account_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


