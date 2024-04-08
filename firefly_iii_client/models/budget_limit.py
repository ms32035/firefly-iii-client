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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BudgetLimit(BaseModel):
    """
    BudgetLimit
    """ # noqa: E501
    amount: StrictStr
    budget_id: StrictStr = Field(description="The budget ID of the associated budget.")
    created_at: Optional[datetime] = None
    currency_code: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    currency_decimal_places: Optional[StrictInt] = None
    currency_id: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    currency_name: Optional[StrictStr] = None
    currency_symbol: Optional[StrictStr] = None
    end: datetime = Field(description="End date of the budget limit.")
    period: Optional[StrictStr] = Field(default=None, description="Period of the budget limit. Only used when auto-generated by auto-budget.")
    spent: Optional[StrictStr] = None
    start: datetime = Field(description="Start date of the budget limit.")
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["amount", "budget_id", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_name", "currency_symbol", "end", "period", "spent", "start", "updated_at"]

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
        """Create an instance of BudgetLimit from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "budget_id",
            "created_at",
            "currency_decimal_places",
            "currency_name",
            "currency_symbol",
            "period",
            "spent",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if period (nullable) is None
        # and model_fields_set contains the field
        if self.period is None and "period" in self.model_fields_set:
            _dict['period'] = None

        # set to None if spent (nullable) is None
        # and model_fields_set contains the field
        if self.spent is None and "spent" in self.model_fields_set:
            _dict['spent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BudgetLimit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "budget_id": obj.get("budget_id"),
            "created_at": obj.get("created_at"),
            "currency_code": obj.get("currency_code"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "currency_id": obj.get("currency_id"),
            "currency_name": obj.get("currency_name"),
            "currency_symbol": obj.get("currency_symbol"),
            "end": obj.get("end"),
            "period": obj.get("period"),
            "spent": obj.get("spent"),
            "start": obj.get("start"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


