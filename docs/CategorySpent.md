# CategorySpent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**currency_decimal_places** | **int** | Number of decimals supported by the currency | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**sum** | **str** | The amount spent. | [optional] 

## Example

```python
from firefly_iii_client.models.category_spent import CategorySpent

# TODO update the JSON string below
json = "{}"
# create an instance of CategorySpent from a JSON string
category_spent_instance = CategorySpent.from_json(json)
# print the JSON string representation of the object
print(CategorySpent.to_json())

# convert the object into a dict
category_spent_dict = category_spent_instance.to_dict()
# create an instance of CategorySpent from a dict
category_spent_from_dict = CategorySpent.from_dict(category_spent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


