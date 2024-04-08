# PiggyBankSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PiggyBankRead**](PiggyBankRead.md) |  | 

## Example

```python
from firefly_iii_client.models.piggy_bank_single import PiggyBankSingle

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankSingle from a JSON string
piggy_bank_single_instance = PiggyBankSingle.from_json(json)
# print the JSON string representation of the object
print(PiggyBankSingle.to_json())

# convert the object into a dict
piggy_bank_single_dict = piggy_bank_single_instance.to_dict()
# create an instance of PiggyBankSingle from a dict
piggy_bank_single_form_dict = piggy_bank_single.from_dict(piggy_bank_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


