# PiggyBank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[PiggyBankAccountRead]**](PiggyBankAccountRead.md) |  | [optional] 
**active** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** |  | [optional] [readonly] 
**currency_decimal_places** | **int** | Number of decimals supported by the currency | [optional] [readonly] 
**currency_id** | **str** |  | [optional] [readonly] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**current_amount** | **str** |  | [optional] 
**left_to_save** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_order** | **int** | The order of the group. At least 1, for the highest sorting. | [optional] [readonly] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 
**order** | **int** |  | [optional] 
**percentage** | **float** |  | [optional] [readonly] 
**save_per_month** | **str** |  | [optional] [readonly] 
**start_date** | **date** | The date you started with this piggy bank. | [optional] 
**target_amount** | **str** |  | 
**target_date** | **date** | The date you intend to finish saving money. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.piggy_bank import PiggyBank

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBank from a JSON string
piggy_bank_instance = PiggyBank.from_json(json)
# print the JSON string representation of the object
print(PiggyBank.to_json())

# convert the object into a dict
piggy_bank_dict = piggy_bank_instance.to_dict()
# create an instance of PiggyBank from a dict
piggy_bank_from_dict = PiggyBank.from_dict(piggy_bank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


