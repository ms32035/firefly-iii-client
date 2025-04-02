# AutocompleteAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_currency_code** | **str** | Code for the currency used by this account. Even if \&quot;convertToNative\&quot; is on, the account currency code is displayed here. | [optional] 
**account_currency_decimal_places** | **int** | Number of decimal places for the currency used by this account. Even if \&quot;convertToNative\&quot; is on, the account currency code is displayed here. | [optional] 
**account_currency_id** | **str** | ID for the currency used by this account. Even if \&quot;convertToNative\&quot; is on, the account currency ID is displayed here. | [optional] 
**account_currency_name** | **str** | Name for the currency used by this account. Even if \&quot;convertToNative\&quot; is on, the account currency name is displayed here. | [optional] 
**account_currency_symbol** | **str** | Code for the currency used by this account. Even if \&quot;convertToNative\&quot; is on, the account currency code is displayed here. | [optional] 
**currency_code** | **str** | Currency code for the currency used by this account. If the user prefers amounts converted to their native currency, this native currency is used instead. | 
**currency_decimal_places** | **int** | Number of decimal places for the currency used by this account. If the user prefers amounts converted to their native currency, this native currency is used instead. | 
**currency_id** | **str** | ID for the currency used by this account. If the user prefers amounts converted to their native currency, this native currency is used instead. | 
**currency_name** | **str** | Currency name for the currency used by this account. If the user prefers amounts converted to their native currency, this native currency is used instead. | 
**currency_symbol** | **str** | Currency symbol for the currency used by this account. If the user prefers amounts converted to their native currency, this native currency is used instead. | 
**id** | **str** |  | 
**name** | **str** | Name of the account found by an auto-complete search. | 
**name_with_balance** | **str** | Asset accounts and liabilities have a second field with the given date&#39;s account balance in the account currency or native currency. | 
**type** | **str** | Account type of the account found by the auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_account import AutocompleteAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteAccount from a JSON string
autocomplete_account_instance = AutocompleteAccount.from_json(json)
# print the JSON string representation of the object
print(AutocompleteAccount.to_json())

# convert the object into a dict
autocomplete_account_dict = autocomplete_account_instance.to_dict()
# create an instance of AutocompleteAccount from a dict
autocomplete_account_from_dict = AutocompleteAccount.from_dict(autocomplete_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


