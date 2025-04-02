# PiggyBankEventArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PiggyBankEventRead]**](PiggyBankEventRead.md) |  | 
**links** | [**PageLink**](PageLink.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.piggy_bank_event_array import PiggyBankEventArray

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankEventArray from a JSON string
piggy_bank_event_array_instance = PiggyBankEventArray.from_json(json)
# print the JSON string representation of the object
print(PiggyBankEventArray.to_json())

# convert the object into a dict
piggy_bank_event_array_dict = piggy_bank_event_array_instance.to_dict()
# create an instance of PiggyBankEventArray from a dict
piggy_bank_event_array_from_dict = PiggyBankEventArray.from_dict(piggy_bank_event_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


