# PiggyBankArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PiggyBankRead]**](PiggyBankRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.piggy_bank_array import PiggyBankArray

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankArray from a JSON string
piggy_bank_array_instance = PiggyBankArray.from_json(json)
# print the JSON string representation of the object
print(PiggyBankArray.to_json())

# convert the object into a dict
piggy_bank_array_dict = piggy_bank_array_instance.to_dict()
# create an instance of PiggyBankArray from a dict
piggy_bank_array_form_dict = piggy_bank_array.from_dict(piggy_bank_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


