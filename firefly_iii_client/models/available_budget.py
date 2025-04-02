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
from firefly_iii_client.models.budget_spent import BudgetSpent
from typing import Optional, Set
from typing_extensions import Self

class AvailableBudget(BaseModel):
    """
    AvailableBudget
    """ # noqa: E501
    amount: StrictStr
    created_at: Optional[datetime] = None
    currency_code: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code.")
    currency_decimal_places: Optional[StrictInt] = None
    currency_id: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code.")
    currency_symbol: Optional[StrictStr] = None
    end: datetime = Field(description="End date of the available budget.")
    native_amount: Optional[StrictStr] = Field(default=None, description="The amount of this available budget in the native currency of this administration.")
    native_currency_code: Optional[StrictStr] = Field(default=None, description="The currency code of the administration's native currency.")
    native_currency_decimal_places: Optional[StrictInt] = Field(default=None, description="The currency decimal places of the administration's native currency.")
    native_currency_id: Optional[StrictStr] = Field(default=None, description="The currency ID of the administration's native currency.")
    native_currency_symbol: Optional[StrictStr] = Field(default=None, description="The currency symbol of the administration's native currency.")
    spent_in_budgets: Optional[List[BudgetSpent]] = None
    spent_outside_budget: Optional[List[BudgetSpent]] = None
    start: datetime = Field(description="Start date of the available budget.")
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["amount", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "end", "native_amount", "native_currency_code", "native_currency_decimal_places", "native_currency_id", "native_currency_symbol", "spent_in_budgets", "spent_outside_budget", "start", "updated_at"]

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
        """Create an instance of AvailableBudget from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "currency_decimal_places",
            "currency_symbol",
            "native_currency_code",
            "native_currency_decimal_places",
            "native_currency_id",
            "native_currency_symbol",
            "spent_in_budgets",
            "spent_outside_budget",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in spent_in_budgets (list)
        _items = []
        if self.spent_in_budgets:
            for _item_spent_in_budgets in self.spent_in_budgets:
                if _item_spent_in_budgets:
                    _items.append(_item_spent_in_budgets.to_dict())
            _dict['spent_in_budgets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in spent_outside_budget (list)
        _items = []
        if self.spent_outside_budget:
            for _item_spent_outside_budget in self.spent_outside_budget:
                if _item_spent_outside_budget:
                    _items.append(_item_spent_outside_budget.to_dict())
            _dict['spent_outside_budget'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AvailableBudget from a dict"""
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
            "end": obj.get("end"),
            "native_amount": obj.get("native_amount"),
            "native_currency_code": obj.get("native_currency_code"),
            "native_currency_decimal_places": obj.get("native_currency_decimal_places"),
            "native_currency_id": obj.get("native_currency_id"),
            "native_currency_symbol": obj.get("native_currency_symbol"),
            "spent_in_budgets": [BudgetSpent.from_dict(_item) for _item in obj["spent_in_budgets"]] if obj.get("spent_in_budgets") is not None else None,
            "spent_outside_budget": [BudgetSpent.from_dict(_item) for _item in obj["spent_outside_budget"]] if obj.get("spent_outside_budget") is not None else None,
            "start": obj.get("start"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


