# CategoryRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Category**](Category.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.category_read import CategoryRead

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryRead from a JSON string
category_read_instance = CategoryRead.from_json(json)
# print the JSON string representation of the object
print(CategoryRead.to_json())

# convert the object into a dict
category_read_dict = category_read_instance.to_dict()
# create an instance of CategoryRead from a dict
category_read_form_dict = category_read.from_dict(category_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


