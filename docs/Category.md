# Category


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**earned** | [**List[CategoryEarned]**](CategoryEarned.md) |  | [optional] [readonly] 
**name** | **str** |  | 
**native_currency_code** | **str** | The administration&#39;s native currency code. | [optional] [readonly] 
**native_currency_decimal_places** | **int** | The administration&#39;s native currency decimal places. | [optional] [readonly] 
**native_currency_id** | **str** | The administration&#39;s native currency ID. | [optional] [readonly] 
**native_currency_symbol** | **str** | The administration&#39;s native currency symbol. | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**spent** | [**List[CategorySpent]**](CategorySpent.md) |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from firefly_iii_client.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_from_dict = Category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


