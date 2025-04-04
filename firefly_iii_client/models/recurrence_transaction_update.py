# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: v6.2.10
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RecurrenceTransactionUpdate(BaseModel):
    """
    RecurrenceTransactionUpdate
    """ # noqa: E501
    amount: Optional[StrictStr] = Field(default=None, description="Amount of the transaction.")
    bill_id: Optional[StrictStr] = Field(default=None, description="Optional.")
    budget_id: Optional[StrictStr] = Field(default=None, description="The budget ID for this transaction.")
    category_id: Optional[StrictStr] = Field(default=None, description="Category ID for this transaction.")
    currency_code: Optional[StrictStr] = Field(default=None, description="Submit either a currency_id or a currency_code.")
    currency_id: Optional[StrictStr] = Field(default=None, description="Submit either a currency_id or a currency_code.")
    description: Optional[StrictStr] = None
    destination_id: Optional[StrictStr] = Field(default=None, description="ID of the destination account. Submit either this or destination_name.")
    foreign_amount: Optional[StrictStr] = Field(default=None, description="Foreign amount of the transaction.")
    foreign_currency_id: Optional[StrictStr] = Field(default=None, description="Submit either a foreign_currency_id or a foreign_currency_code, or neither.")
    id: StrictStr
    piggy_bank_id: Optional[StrictStr] = None
    source_id: Optional[StrictStr] = Field(default=None, description="ID of the source account. Submit either this or source_name.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Array of tags.")
    __properties: ClassVar[List[str]] = ["amount", "bill_id", "budget_id", "category_id", "currency_code", "currency_id", "description", "destination_id", "foreign_amount", "foreign_currency_id", "id", "piggy_bank_id", "source_id", "tags"]

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
        """Create an instance of RecurrenceTransactionUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
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

        # set to None if foreign_amount (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_amount is None and "foreign_amount" in self.model_fields_set:
            _dict['foreign_amount'] = None

        # set to None if foreign_currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_id is None and "foreign_currency_id" in self.model_fields_set:
            _dict['foreign_currency_id'] = None

        # set to None if piggy_bank_id (nullable) is None
        # and model_fields_set contains the field
        if self.piggy_bank_id is None and "piggy_bank_id" in self.model_fields_set:
            _dict['piggy_bank_id'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecurrenceTransactionUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "bill_id": obj.get("bill_id"),
            "budget_id": obj.get("budget_id"),
            "category_id": obj.get("category_id"),
            "currency_code": obj.get("currency_code"),
            "currency_id": obj.get("currency_id"),
            "description": obj.get("description"),
            "destination_id": obj.get("destination_id"),
            "foreign_amount": obj.get("foreign_amount"),
            "foreign_currency_id": obj.get("foreign_currency_id"),
            "id": obj.get("id"),
            "piggy_bank_id": obj.get("piggy_bank_id"),
            "source_id": obj.get("source_id"),
            "tags": obj.get("tags")
        })
        return _obj


