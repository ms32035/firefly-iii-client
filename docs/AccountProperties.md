# AccountProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**active** | **bool** |  | [optional] [default to True]
**balance_difference** | **str** | If you submit a start AND end date, this will be the difference between those two moments. | [optional] [readonly] 
**bic** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**credit_card_type** | [**CreditCardTypeProperty**](CreditCardTypeProperty.md) |  | [optional] 
**currency_code** | **str** | The currency code of the currency associated with this object. | [optional] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**currency_id** | **str** | The currency ID of the currency associated with this object. | [optional] 
**currency_name** | **str** | The currency name of the currency associated with this object. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**current_balance** | **str** | The current balance of the account in the account&#39;s currency. If the account has no currency, this is the balance in the administration&#39;s primary currency. Either way, the &#x60;currency_*&#x60; fields reflect the currency used. | [optional] [readonly] 
**current_balance_date** | **datetime** | The timestamp for this date is always 23:59:59, to indicate it&#39;s the balance at the very END of that particular day. | [optional] [readonly] 
**debt_amount** | **str** | In liability accounts (loans, debts and mortgages), this is the amount of debt in the account&#39;s currency (see the &#x60;currency_*&#x60; fields). In asset accounts, this is NULL. | [optional] 
**iban** | **str** |  | [optional] 
**include_net_worth** | **bool** |  | [optional] [default to True]
**interest** | **str** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | [**InterestPeriodProperty**](InterestPeriodProperty.md) |  | [optional] 
**last_activity** | **datetime** | Last activity of the account. | [optional] 
**latitude** | **float** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**liability_direction** | [**LiabilityDirectionProperty**](LiabilityDirectionProperty.md) |  | [optional] 
**liability_type** | [**LiabilityTypeProperty**](LiabilityTypeProperty.md) |  | [optional] 
**longitude** | **float** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**monthly_payment_date** | **datetime** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**object_group_id** | **str** | The group ID of the group this object is part of. NULL if no group. | [optional] 
**object_group_order** | **int** | The order of the group. At least 1, for the highest sorting. | [optional] [readonly] 
**object_group_title** | **str** | The name of the group. NULL if no group. | [optional] 
**object_has_currency_setting** | **bool** | Indicates whether the account has a currency setting. If false, the account uses the administration&#39;s primary currency. Asset accounts and liability accounts always have a currency setting, while expense and revenue accounts do not. | [optional] [readonly] 
**opening_balance** | **str** | Represents the opening balance, the initial amount this account holds in the currency of the account or the administration&#39;s primary currency if the account has no currency. Either way, the &#x60;currency_*&#x60; fields reflect the currency used. | [optional] 
**opening_balance_date** | **datetime** | Represents the date of the opening balance. | [optional] 
**order** | **int** | Order of the account. Is NULL if account is not asset or liability. | [optional] 
**pc_balance_difference** | **str** | If you submit a start AND end date, this will be the difference in the currency of the account or the administration&#39;s primary currency between those two moments. | [optional] [readonly] 
**pc_current_balance** | **str** | The current balance of the account in the administration&#39;s primary currency. The &#x60;primary_currency_*&#x60; fields reflect the currency used. This field is NULL if the user does have &#39;convert to primary&#39; set to true in their settings. | [optional] [readonly] 
**pc_debt_amount** | **str** | In liability accounts (loans, debts and mortgages), this is the amount of debt in the administration&#39;s primary currency (see the &#x60;currency_*&#x60; fields. In asset accounts, this is NULL. | [optional] 
**pc_opening_balance** | **str** | The opening balance of the account in the administration&#39;s primary currency (pc). The &#x60;primary_currency_*&#x60; fields reflect the currency used. This field is NULL if the user does have &#39;convert to primary&#39; set to true in their settings. | [optional] 
**pc_virtual_balance** | **str** | The virtual balance of the account in the administration&#39;s primary currency (pc). The &#x60;primary_currency_*&#x60; fields reflect the currency used. This field is NULL if the user does have &#39;convert to primary&#39; set to true in their settings. | [optional] 
**primary_currency_code** | **str** | The currency code of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_decimal_places** | **int** | The currency decimal places of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_id** | **str** | The currency ID of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_name** | **str** | The currency name of the administration&#39;s primary currency. | [optional] [readonly] 
**primary_currency_symbol** | **str** | The currency symbol of the administration&#39;s primary currency. | [optional] [readonly] 
**type** | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**virtual_balance** | **str** | The virtual balance of the account in the account&#39;s currency or the administration&#39;s primary currency if the account has no currency. | [optional] 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

## Example

```python
from firefly_iii_client.models.account_properties import AccountProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AccountProperties from a JSON string
account_properties_instance = AccountProperties.from_json(json)
# print the JSON string representation of the object
print(AccountProperties.to_json())

# convert the object into a dict
account_properties_dict = account_properties_instance.to_dict()
# create an instance of AccountProperties from a dict
account_properties_from_dict = AccountProperties.from_dict(account_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


