# PiggyBankStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[PiggyBankAccountStore]**](PiggyBankAccountStore.md) |  | [optional] 
**active** | **bool** |  | [optional] [readonly] 
**current_amount** | **str** |  | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 
**order** | **int** |  | [optional] 
**start_date** | **date** | The date you started with this piggy bank. | [optional] 
**target_amount** | **str** |  | 
**target_date** | **date** | The date you intend to finish saving money. | [optional] 

## Example

```python
from firefly_iii_client.models.piggy_bank_store import PiggyBankStore

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankStore from a JSON string
piggy_bank_store_instance = PiggyBankStore.from_json(json)
# print the JSON string representation of the object
print(PiggyBankStore.to_json())

# convert the object into a dict
piggy_bank_store_dict = piggy_bank_store_instance.to_dict()
# create an instance of PiggyBankStore from a dict
piggy_bank_store_from_dict = PiggyBankStore.from_dict(piggy_bank_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


