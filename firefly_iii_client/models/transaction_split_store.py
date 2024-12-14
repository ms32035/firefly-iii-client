# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 6.1.24
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.transaction_type_property import TransactionTypeProperty
from typing import Optional, Set
from typing_extensions import Self

class TransactionSplitStore(BaseModel):
    """
    TransactionSplitStore
    """ # noqa: E501
    amount: StrictStr = Field(description="Amount of the transaction.")
    bill_id: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the bill_name")
    bill_name: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the bill_id")
    book_date: Optional[datetime] = None
    budget_id: Optional[StrictStr] = Field(default=None, description="The budget ID for this transaction.")
    budget_name: Optional[StrictStr] = Field(default=None, description="The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored.")
    bunq_payment_id: Optional[StrictStr] = Field(default=None, description="Internal ID of bunq transaction. Field is no longer used but still works.")
    category_id: Optional[StrictStr] = Field(default=None, description="The category ID for this transaction.")
    category_name: Optional[StrictStr] = Field(default=None, description="The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name.")
    currency_code: Optional[StrictStr] = Field(default=None, description="Currency code. Default is the source account's currency, or the user's default currency. The value you submit may be overruled by the source or destination account.")
    currency_id: Optional[StrictStr] = Field(default=None, description="Currency ID. Default is the source account's currency, or the user's default currency. The value you submit may be overruled by the source or destination account.")
    var_date: datetime = Field(description="Date of the transaction", alias="date")
    description: StrictStr = Field(description="Description of the transaction.")
    destination_id: Optional[StrictStr] = Field(default=None, description="ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account.")
    destination_name: Optional[StrictStr] = Field(default=None, description="Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough.")
    due_date: Optional[datetime] = None
    external_id: Optional[StrictStr] = Field(default=None, description="Reference to external ID in other systems.")
    external_url: Optional[StrictStr] = Field(default=None, description="External, custom URL for this transaction.")
    foreign_amount: Optional[StrictStr] = Field(default=None, description="The amount in a foreign currency.")
    foreign_currency_code: Optional[StrictStr] = Field(default=None, description="Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount.")
    foreign_currency_id: Optional[StrictStr] = Field(default=None, description="Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount.")
    interest_date: Optional[datetime] = None
    internal_reference: Optional[StrictStr] = Field(default=None, description="Reference to internal reference of other systems.")
    invoice_date: Optional[datetime] = None
    notes: Optional[StrictStr] = None
    order: Optional[StrictInt] = Field(default=None, description="Order of this entry in the list of transactions.")
    payment_date: Optional[datetime] = None
    piggy_bank_id: Optional[StrictInt] = Field(default=None, description="Optional. Use either this or the piggy_bank_name")
    piggy_bank_name: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the piggy_bank_id")
    process_date: Optional[datetime] = None
    reconciled: Optional[StrictBool] = Field(default=None, description="If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user.")
    sepa_batch_id: Optional[StrictStr] = Field(default=None, description="SEPA Batch ID")
    sepa_cc: Optional[StrictStr] = Field(default=None, description="SEPA Clearing Code")
    sepa_ci: Optional[StrictStr] = Field(default=None, description="SEPA Creditor Identifier")
    sepa_country: Optional[StrictStr] = Field(default=None, description="SEPA Country")
    sepa_ct_id: Optional[StrictStr] = Field(default=None, description="SEPA end-to-end Identifier")
    sepa_ct_op: Optional[StrictStr] = Field(default=None, description="SEPA Opposing Account Identifier")
    sepa_db: Optional[StrictStr] = Field(default=None, description="SEPA mandate identifier")
    sepa_ep: Optional[StrictStr] = Field(default=None, description="SEPA External Purpose indicator")
    source_id: Optional[StrictStr] = Field(default=None, description="ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account.")
    source_name: Optional[StrictStr] = Field(default=None, description="Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Array of tags.")
    type: TransactionTypeProperty
    __properties: ClassVar[List[str]] = ["amount", "bill_id", "bill_name", "book_date", "budget_id", "budget_name", "bunq_payment_id", "category_id", "category_name", "currency_code", "currency_id", "date", "description", "destination_id", "destination_name", "due_date", "external_id", "external_url", "foreign_amount", "foreign_currency_code", "foreign_currency_id", "interest_date", "internal_reference", "invoice_date", "notes", "order", "payment_date", "piggy_bank_id", "piggy_bank_name", "process_date", "reconciled", "sepa_batch_id", "sepa_cc", "sepa_ci", "sepa_country", "sepa_ct_id", "sepa_ct_op", "sepa_db", "sepa_ep", "source_id", "source_name", "tags", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionSplitStore from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "budget_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if bill_id (nullable) is None
        # and model_fields_set contains the field
        if self.bill_id is None and "bill_id" in self.model_fields_set:
            _dict['bill_id'] = None

        # set to None if bill_name (nullable) is None
        # and model_fields_set contains the field
        if self.bill_name is None and "bill_name" in self.model_fields_set:
            _dict['bill_name'] = None

        # set to None if book_date (nullable) is None
        # and model_fields_set contains the field
        if self.book_date is None and "book_date" in self.model_fields_set:
            _dict['book_date'] = None

        # set to None if budget_id (nullable) is None
        # and model_fields_set contains the field
        if self.budget_id is None and "budget_id" in self.model_fields_set:
            _dict['budget_id'] = None

        # set to None if budget_name (nullable) is None
        # and model_fields_set contains the field
        if self.budget_name is None and "budget_name" in self.model_fields_set:
            _dict['budget_name'] = None

        # set to None if bunq_payment_id (nullable) is None
        # and model_fields_set contains the field
        if self.bunq_payment_id is None and "bunq_payment_id" in self.model_fields_set:
            _dict['bunq_payment_id'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if category_name (nullable) is None
        # and model_fields_set contains the field
        if self.category_name is None and "category_name" in self.model_fields_set:
            _dict['category_name'] = None

        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currency_code'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currency_id'] = None

        # set to None if destination_id (nullable) is None
        # and model_fields_set contains the field
        if self.destination_id is None and "destination_id" in self.model_fields_set:
            _dict['destination_id'] = None

        # set to None if destination_name (nullable) is None
        # and model_fields_set contains the field
        if self.destination_name is None and "destination_name" in self.model_fields_set:
            _dict['destination_name'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['due_date'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if external_url (nullable) is None
        # and model_fields_set contains the field
        if self.external_url is None and "external_url" in self.model_fields_set:
            _dict['external_url'] = None

        # set to None if foreign_amount (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_amount is None and "foreign_amount" in self.model_fields_set:
            _dict['foreign_amount'] = None

        # set to None if foreign_currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_code is None and "foreign_currency_code" in self.model_fields_set:
            _dict['foreign_currency_code'] = None

        # set to None if foreign_currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_id is None and "foreign_currency_id" in self.model_fields_set:
            _dict['foreign_currency_id'] = None

        # set to None if interest_date (nullable) is None
        # and model_fields_set contains the field
        if self.interest_date is None and "interest_date" in self.model_fields_set:
            _dict['interest_date'] = None

        # set to None if internal_reference (nullable) is None
        # and model_fields_set contains the field
        if self.internal_reference is None and "internal_reference" in self.model_fields_set:
            _dict['internal_reference'] = None

        # set to None if invoice_date (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_date is None and "invoice_date" in self.model_fields_set:
            _dict['invoice_date'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if payment_date (nullable) is None
        # and model_fields_set contains the field
        if self.payment_date is None and "payment_date" in self.model_fields_set:
            _dict['payment_date'] = None

        # set to None if piggy_bank_id (nullable) is None
        # and model_fields_set contains the field
        if self.piggy_bank_id is None and "piggy_bank_id" in self.model_fields_set:
            _dict['piggy_bank_id'] = None

        # set to None if piggy_bank_name (nullable) is None
        # and model_fields_set contains the field
        if self.piggy_bank_name is None and "piggy_bank_name" in self.model_fields_set:
            _dict['piggy_bank_name'] = None

        # set to None if process_date (nullable) is None
        # and model_fields_set contains the field
        if self.process_date is None and "process_date" in self.model_fields_set:
            _dict['process_date'] = None

        # set to None if sepa_batch_id (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_batch_id is None and "sepa_batch_id" in self.model_fields_set:
            _dict['sepa_batch_id'] = None

        # set to None if sepa_cc (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_cc is None and "sepa_cc" in self.model_fields_set:
            _dict['sepa_cc'] = None

        # set to None if sepa_ci (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_ci is None and "sepa_ci" in self.model_fields_set:
            _dict['sepa_ci'] = None

        # set to None if sepa_country (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_country is None and "sepa_country" in self.model_fields_set:
            _dict['sepa_country'] = None

        # set to None if sepa_ct_id (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_ct_id is None and "sepa_ct_id" in self.model_fields_set:
            _dict['sepa_ct_id'] = None

        # set to None if sepa_ct_op (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_ct_op is None and "sepa_ct_op" in self.model_fields_set:
            _dict['sepa_ct_op'] = None

        # set to None if sepa_db (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_db is None and "sepa_db" in self.model_fields_set:
            _dict['sepa_db'] = None

        # set to None if sepa_ep (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_ep is None and "sepa_ep" in self.model_fields_set:
            _dict['sepa_ep'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['source_id'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['source_name'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionSplitStore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "bill_id": obj.get("bill_id"),
            "bill_name": obj.get("bill_name"),
            "book_date": obj.get("book_date"),
            "budget_id": obj.get("budget_id"),
            "budget_name": obj.get("budget_name"),
            "bunq_payment_id": obj.get("bunq_payment_id"),
            "category_id": obj.get("category_id"),
            "category_name": obj.get("category_name"),
            "currency_code": obj.get("currency_code"),
            "currency_id": obj.get("currency_id"),
            "date": obj.get("date"),
            "description": obj.get("description"),
            "destination_id": obj.get("destination_id"),
            "destination_name": obj.get("destination_name"),
            "due_date": obj.get("due_date"),
            "external_id": obj.get("external_id"),
            "external_url": obj.get("external_url"),
            "foreign_amount": obj.get("foreign_amount"),
            "foreign_currency_code": obj.get("foreign_currency_code"),
            "foreign_currency_id": obj.get("foreign_currency_id"),
            "interest_date": obj.get("interest_date"),
            "internal_reference": obj.get("internal_reference"),
            "invoice_date": obj.get("invoice_date"),
            "notes": obj.get("notes"),
            "order": obj.get("order"),
            "payment_date": obj.get("payment_date"),
            "piggy_bank_id": obj.get("piggy_bank_id"),
            "piggy_bank_name": obj.get("piggy_bank_name"),
            "process_date": obj.get("process_date"),
            "reconciled": obj.get("reconciled"),
            "sepa_batch_id": obj.get("sepa_batch_id"),
            "sepa_cc": obj.get("sepa_cc"),
            "sepa_ci": obj.get("sepa_ci"),
            "sepa_country": obj.get("sepa_country"),
            "sepa_ct_id": obj.get("sepa_ct_id"),
            "sepa_ct_op": obj.get("sepa_ct_op"),
            "sepa_db": obj.get("sepa_db"),
            "sepa_ep": obj.get("sepa_ep"),
            "source_id": obj.get("source_id"),
            "source_name": obj.get("source_name"),
            "tags": obj.get("tags"),
            "type": obj.get("type")
        })
        return _obj


