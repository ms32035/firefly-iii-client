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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.recurrence_repetition_update import RecurrenceRepetitionUpdate
from firefly_iii_client.models.recurrence_transaction_update import RecurrenceTransactionUpdate
from typing import Optional, Set
from typing_extensions import Self

class RecurrenceUpdate(BaseModel):
    """
    RecurrenceUpdate
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="If the recurrence is even active.")
    apply_rules: Optional[StrictBool] = Field(default=None, description="Whether or not to fire the rules after the creation of a transaction.")
    description: Optional[StrictStr] = Field(default=None, description="Not to be confused with the description of the actual transaction(s) being created.")
    first_date: Optional[date] = Field(default=None, description="First time the recurring transaction will fire.")
    notes: Optional[StrictStr] = None
    nr_of_repetitions: Optional[StrictInt] = Field(default=None, description="Max number of created transactions. Use either this field or repeat_until.")
    repeat_until: Optional[date] = Field(default=None, description="Date until the recurring transaction can fire. After that date, it's basically inactive. Use either this field or repetitions.")
    repetitions: Optional[List[RecurrenceRepetitionUpdate]] = None
    title: Optional[StrictStr] = None
    transactions: Optional[List[RecurrenceTransactionUpdate]] = None
    __properties: ClassVar[List[str]] = ["active", "apply_rules", "description", "first_date", "notes", "nr_of_repetitions", "repeat_until", "repetitions", "title", "transactions"]

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
        """Create an instance of RecurrenceUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in repetitions (list)
        _items = []
        if self.repetitions:
            for _item in self.repetitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['repetitions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if nr_of_repetitions (nullable) is None
        # and model_fields_set contains the field
        if self.nr_of_repetitions is None and "nr_of_repetitions" in self.model_fields_set:
            _dict['nr_of_repetitions'] = None

        # set to None if repeat_until (nullable) is None
        # and model_fields_set contains the field
        if self.repeat_until is None and "repeat_until" in self.model_fields_set:
            _dict['repeat_until'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecurrenceUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "apply_rules": obj.get("apply_rules"),
            "description": obj.get("description"),
            "first_date": obj.get("first_date"),
            "notes": obj.get("notes"),
            "nr_of_repetitions": obj.get("nr_of_repetitions"),
            "repeat_until": obj.get("repeat_until"),
            "repetitions": [RecurrenceRepetitionUpdate.from_dict(_item) for _item in obj["repetitions"]] if obj.get("repetitions") is not None else None,
            "title": obj.get("title"),
            "transactions": [RecurrenceTransactionUpdate.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None
        })
        return _obj


