# CategoryUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.category_update import CategoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryUpdate from a JSON string
category_update_instance = CategoryUpdate.from_json(json)
# print the JSON string representation of the object
print(CategoryUpdate.to_json())

# convert the object into a dict
category_update_dict = category_update_instance.to_dict()
# create an instance of CategoryUpdate from a dict
category_update_form_dict = category_update.from_dict(category_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


