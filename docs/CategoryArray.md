# CategoryArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CategoryRead]**](CategoryRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.category_array import CategoryArray

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryArray from a JSON string
category_array_instance = CategoryArray.from_json(json)
# print the JSON string representation of the object
print(CategoryArray.to_json())

# convert the object into a dict
category_array_dict = category_array_instance.to_dict()
# create an instance of CategoryArray from a dict
category_array_from_dict = CategoryArray.from_dict(category_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


