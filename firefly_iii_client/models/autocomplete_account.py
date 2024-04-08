# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class AutocompleteAccount(BaseModel):
    """
    AutocompleteAccount
    """ # noqa: E501
    currency_code: StrictStr = Field(description="Currency code for the currency used by this account.")
    currency_decimal_places: StrictInt = Field(description="Number of decimal places for the currency used by this account.")
    currency_id: StrictStr = Field(description="ID for the currency used by this account.")
    currency_name: StrictStr = Field(description="Currency name for the currency used by this account.")
    currency_symbol: StrictStr = Field(description="Currency symbol for the currency used by this account.")
    id: StrictStr
    name: StrictStr = Field(description="Name of the account found by an auto-complete search.")
    name_with_balance: StrictStr = Field(description="Asset accounts and liabilities have a second field with the given date's account balance.")
    type: StrictStr = Field(description="Account type of the account found by the auto-complete search.")
    __properties: ClassVar[List[str]] = ["currency_code", "currency_decimal_places", "currency_id", "currency_name", "currency_symbol", "id", "name", "name_with_balance", "type"]

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
        """Create an instance of AutocompleteAccount from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutocompleteAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency_code": obj.get("currency_code"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "currency_id": obj.get("currency_id"),
            "currency_name": obj.get("currency_name"),
            "currency_symbol": obj.get("currency_symbol"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "name_with_balance": obj.get("name_with_balance"),
            "type": obj.get("type")
        })
        return _obj


