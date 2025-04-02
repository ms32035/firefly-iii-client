# PiggyBankAccountRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_amount** | **str** |  | 
**id** | **str** | The ID of the account. | [readonly] 
**name** | **str** |  | [readonly] 
**native_current_amount** | **str** | If convertToNative is on, this will show the amount in the native currency. | 

## Example

```python
from firefly_iii_client.models.piggy_bank_account_read import PiggyBankAccountRead

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankAccountRead from a JSON string
piggy_bank_account_read_instance = PiggyBankAccountRead.from_json(json)
# print the JSON string representation of the object
print(PiggyBankAccountRead.to_json())

# convert the object into a dict
piggy_bank_account_read_dict = piggy_bank_account_read_instance.to_dict()
# create an instance of PiggyBankAccountRead from a dict
piggy_bank_account_read_from_dict = PiggyBankAccountRead.from_dict(piggy_bank_account_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


