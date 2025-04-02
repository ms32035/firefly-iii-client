# PiggyBankRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PiggyBank**](PiggyBank.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.piggy_bank_read import PiggyBankRead

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankRead from a JSON string
piggy_bank_read_instance = PiggyBankRead.from_json(json)
# print the JSON string representation of the object
print(PiggyBankRead.to_json())

# convert the object into a dict
piggy_bank_read_dict = piggy_bank_read_instance.to_dict()
# create an instance of PiggyBankRead from a dict
piggy_bank_read_from_dict = PiggyBankRead.from_dict(piggy_bank_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


