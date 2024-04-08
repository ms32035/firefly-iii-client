# CategoryEarned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**currency_decimal_places** | **int** | Number of decimals supported by the currency | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**sum** | **str** | The amount earned. | [optional] 

## Example

```python
from firefly_iii_client.models.category_earned import CategoryEarned

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryEarned from a JSON string
category_earned_instance = CategoryEarned.from_json(json)
# print the JSON string representation of the object
print(CategoryEarned.to_json())

# convert the object into a dict
category_earned_dict = category_earned_instance.to_dict()
# create an instance of CategoryEarned from a dict
category_earned_form_dict = category_earned.from_dict(category_earned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


