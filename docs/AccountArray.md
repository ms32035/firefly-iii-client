# AccountArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountRead]**](AccountRead.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from firefly_iii_client.models.account_array import AccountArray

# TODO update the JSON string below
json = "{}"
# create an instance of AccountArray from a JSON string
account_array_instance = AccountArray.from_json(json)
# print the JSON string representation of the object
print(AccountArray.to_json())

# convert the object into a dict
account_array_dict = account_array_instance.to_dict()
# create an instance of AccountArray from a dict
account_array_from_dict = AccountArray.from_dict(account_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


