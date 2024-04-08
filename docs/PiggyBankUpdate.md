# PiggyBankUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the asset account this piggy bank is connected to. | [optional] 
**active** | **bool** |  | [optional] [readonly] 
**currency_code** | **str** |  | [optional] [readonly] 
**currency_id** | **str** |  | [optional] [readonly] 
**current_amount** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 
**order** | **int** |  | [optional] 
**start_date** | **date** | The date you started with this piggy bank. | [optional] 
**target_amount** | **str** |  | [optional] 
**target_date** | **date** | The date you intend to finish saving money. | [optional] 

## Example

```python
from firefly_iii_client.models.piggy_bank_update import PiggyBankUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankUpdate from a JSON string
piggy_bank_update_instance = PiggyBankUpdate.from_json(json)
# print the JSON string representation of the object
print(PiggyBankUpdate.to_json())

# convert the object into a dict
piggy_bank_update_dict = piggy_bank_update_instance.to_dict()
# create an instance of PiggyBankUpdate from a dict
piggy_bank_update_form_dict = piggy_bank_update.from_dict(piggy_bank_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


