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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.piggy_bank_account_update import PiggyBankAccountUpdate
from typing import Optional, Set
from typing_extensions import Self

class PiggyBankUpdate(BaseModel):
    """
    PiggyBankUpdate
    """ # noqa: E501
    accounts: Optional[List[PiggyBankAccountUpdate]] = None
    active: Optional[StrictBool] = None
    currency_code: Optional[StrictStr] = None
    currency_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    object_group_id: Optional[StrictStr] = Field(default=None, description="The group ID of the group this object is part of. NULL if no group.")
    object_group_title: Optional[StrictStr] = Field(default=None, description="The name of the group. NULL if no group.")
    order: Optional[StrictInt] = None
    start_date: Optional[date] = Field(default=None, description="The date you started with this piggy bank.")
    target_amount: Optional[StrictStr] = None
    target_date: Optional[date] = Field(default=None, description="The date you intend to finish saving money.")
    __properties: ClassVar[List[str]] = ["accounts", "active", "currency_code", "currency_id", "name", "notes", "object_group_id", "object_group_title", "order", "start_date", "target_amount", "target_date"]

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
        """Create an instance of PiggyBankUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "active",
            "currency_code",
            "currency_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item_accounts in self.accounts:
                if _item_accounts:
                    _items.append(_item_accounts.to_dict())
            _dict['accounts'] = _items
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if object_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_id is None and "object_group_id" in self.model_fields_set:
            _dict['object_group_id'] = None

        # set to None if object_group_title (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_title is None and "object_group_title" in self.model_fields_set:
            _dict['object_group_title'] = None

        # set to None if target_amount (nullable) is None
        # and model_fields_set contains the field
        if self.target_amount is None and "target_amount" in self.model_fields_set:
            _dict['target_amount'] = None

        # set to None if target_date (nullable) is None
        # and model_fields_set contains the field
        if self.target_date is None and "target_date" in self.model_fields_set:
            _dict['target_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PiggyBankUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accounts": [PiggyBankAccountUpdate.from_dict(_item) for _item in obj["accounts"]] if obj.get("accounts") is not None else None,
            "active": obj.get("active"),
            "currency_code": obj.get("currency_code"),
            "currency_id": obj.get("currency_id"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "object_group_id": obj.get("object_group_id"),
            "object_group_title": obj.get("object_group_title"),
            "order": obj.get("order"),
            "start_date": obj.get("start_date"),
            "target_amount": obj.get("target_amount"),
            "target_date": obj.get("target_date")
        })
        return _obj


