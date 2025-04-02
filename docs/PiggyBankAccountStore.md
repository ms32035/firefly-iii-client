# PiggyBankAccountStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_amount** | **str** | The amount saved currently. | [optional] 
**id** | **str** | The ID of the account. | 
**name** | **str** | The name of the account. | [optional] 

## Example

```python
from firefly_iii_client.models.piggy_bank_account_store import PiggyBankAccountStore

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankAccountStore from a JSON string
piggy_bank_account_store_instance = PiggyBankAccountStore.from_json(json)
# print the JSON string representation of the object
print(PiggyBankAccountStore.to_json())

# convert the object into a dict
piggy_bank_account_store_dict = piggy_bank_account_store_instance.to_dict()
# create an instance of PiggyBankAccountStore from a dict
piggy_bank_account_store_from_dict = PiggyBankAccountStore.from_dict(piggy_bank_account_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


