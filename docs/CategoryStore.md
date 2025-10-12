# CategoryStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from firefly_iii_client.models.category_store import CategoryStore

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryStore from a JSON string
category_store_instance = CategoryStore.from_json(json)
# print the JSON string representation of the object
print(CategoryStore.to_json())

# convert the object into a dict
category_store_dict = category_store_instance.to_dict()
# create an instance of CategoryStore from a dict
category_store_from_dict = CategoryStore.from_dict(category_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


