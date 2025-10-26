# PiggyBankProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[PiggyBankAccountRead]**](PiggyBankAccountRead.md) |  | [optional] 
**active** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**current_amount** | **str** |  | [optional] 
**left_to_save** | **str** |  | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_order** | **int** | The order of the group. At least 1, for the highest sorting. | [optional] [readonly] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 
**object_has_currency_setting** | **bool** | Indicates whether the object has a currency setting. If false, the object uses the administration&#39;s primary currency. | [optional] [readonly] 
**order** | **int** |  | [optional] 
**pc_current_amount** | **str** | The current amount in the primary currency of the administration. | [optional] 
**pc_left_to_save** | **str** |  | [optional] 
**pc_save_per_month** | **str** |  | [optional] [readonly] 
**pc_target_amount** | **str** | The target amount in the primary currency of the administration. | [optional] 
**percentage** | **float** | The percentage of the target amount that has been saved, if a target amount is set. | [optional] [readonly] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**save_per_month** | **str** |  | [optional] [readonly] 
**start_date** | **datetime** | The date you started with this piggy bank. | [optional] 
**target_amount** | **str** |  | 
**target_date** | **datetime** | The date you intend to finish saving money. | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.piggy_bank_properties import PiggyBankProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PiggyBankProperties from a JSON string
piggy_bank_properties_instance = PiggyBankProperties.from_json(json)
# print the JSON string representation of the object
print(PiggyBankProperties.to_json())

# convert the object into a dict
piggy_bank_properties_dict = piggy_bank_properties_instance.to_dict()
# create an instance of PiggyBankProperties from a dict
piggy_bank_properties_from_dict = PiggyBankProperties.from_dict(piggy_bank_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


