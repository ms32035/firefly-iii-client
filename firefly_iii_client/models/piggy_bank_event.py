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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PiggyBankEvent(BaseModel):
    """
    PiggyBankEvent
    """ # noqa: E501
    amount: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    currency_code: Optional[StrictStr] = None
    currency_decimal_places: Optional[StrictInt] = None
    currency_id: Optional[StrictStr] = None
    currency_symbol: Optional[StrictStr] = None
    transaction_group_id: Optional[StrictStr] = Field(default=None, description="The transaction group associated with the event.")
    transaction_journal_id: Optional[StrictStr] = Field(default=None, description="The journal associated with the event.")
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["amount", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "transaction_group_id", "transaction_journal_id", "updated_at"]

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
        """Create an instance of PiggyBankEvent from a JSON string"""
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
        # set to None if transaction_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_group_id is None and "transaction_group_id" in self.model_fields_set:
            _dict['transaction_group_id'] = None

        # set to None if transaction_journal_id (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_journal_id is None and "transaction_journal_id" in self.model_fields_set:
            _dict['transaction_journal_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PiggyBankEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "currency_code": obj.get("currency_code"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "currency_id": obj.get("currency_id"),
            "currency_symbol": obj.get("currency_symbol"),
            "transaction_group_id": obj.get("transaction_group_id"),
            "transaction_journal_id": obj.get("transaction_journal_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


