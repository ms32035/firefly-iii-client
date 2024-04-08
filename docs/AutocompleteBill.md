# AutocompleteBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is the bill active or not? | [optional] 
**id** | **str** |  | 
**name** | **str** | Name of the bill found by an auto-complete search. | 

## Example

```python
from firefly_iii_client.models.autocomplete_bill import AutocompleteBill

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteBill from a JSON string
autocomplete_bill_instance = AutocompleteBill.from_json(json)
# print the JSON string representation of the object
print(AutocompleteBill.to_json())

# convert the object into a dict
autocomplete_bill_dict = autocomplete_bill_instance.to_dict()
# create an instance of AutocompleteBill from a dict
autocomplete_bill_form_dict = autocomplete_bill.from_dict(autocomplete_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


