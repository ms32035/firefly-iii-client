# LinkTypeRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LinkType**](LinkType.md) |  | 
**id** | **str** |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.link_type_read import LinkTypeRead

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTypeRead from a JSON string
link_type_read_instance = LinkTypeRead.from_json(json)
# print the JSON string representation of the object
print(LinkTypeRead.to_json())

# convert the object into a dict
link_type_read_dict = link_type_read_instance.to_dict()
# create an instance of LinkTypeRead from a dict
link_type_read_from_dict = LinkTypeRead.from_dict(link_type_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


