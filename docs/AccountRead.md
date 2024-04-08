# AccountRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Account**](Account.md) |  | 
**id** | **str** |  | 
**type** | **str** | Immutable value | 

## Example

```python
from firefly_iii_client.models.account_read import AccountRead

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRead from a JSON string
account_read_instance = AccountRead.from_json(json)
# print the JSON string representation of the object
print(AccountRead.to_json())

# convert the object into a dict
account_read_dict = account_read_instance.to_dict()
# create an instance of AccountRead from a dict
account_read_form_dict = account_read.from_dict(account_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


