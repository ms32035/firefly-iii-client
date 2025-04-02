# AccountSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccountRead**](AccountRead.md) |  | 

## Example

```python
from firefly_iii_client.models.account_single import AccountSingle

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSingle from a JSON string
account_single_instance = AccountSingle.from_json(json)
# print the JSON string representation of the object
print(AccountSingle.to_json())

# convert the object into a dict
account_single_dict = account_single_instance.to_dict()
# create an instance of AccountSingle from a dict
account_single_from_dict = AccountSingle.from_dict(account_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


