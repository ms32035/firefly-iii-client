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
from firefly_iii_client.models.recurrence_repetition_type import RecurrenceRepetitionType
from typing import Optional, Set
from typing_extensions import Self

class RecurrenceRepetition(BaseModel):
    """
    RecurrenceRepetition
    """ # noqa: E501
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = Field(default=None, description="Auto-generated repetition description.")
    id: Optional[StrictStr] = None
    moment: StrictStr = Field(description="Information that defined the type of repetition. - For 'daily', this is empty. - For 'weekly', it is day of the week between 1 and 7 (Monday - Sunday). - For 'ndom', it is '1,2' or '4,5' or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). '2,3' means: the 2nd Wednesday of the month - For 'monthly' it is the day of the month (1 - 31) - For yearly, it is a full date, ie '2018-09-17'. The year you use does not matter. ")
    occurrences: Optional[List[datetime]] = Field(default=None, description="Array of future dates when the repetition will apply to. Auto generated.")
    skip: Optional[StrictInt] = Field(default=None, description="How many occurrences to skip. 0 means skip nothing. 1 means every other.")
    type: RecurrenceRepetitionType
    updated_at: Optional[datetime] = None
    weekend: Optional[StrictInt] = Field(default=None, description="How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday. ")
    __properties: ClassVar[List[str]] = ["created_at", "description", "id", "moment", "occurrences", "skip", "type", "updated_at", "weekend"]

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
        """Create an instance of RecurrenceRepetition from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "description",
            "id",
            "occurrences",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecurrenceRepetition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "moment": obj.get("moment"),
            "occurrences": obj.get("occurrences"),
            "skip": obj.get("skip"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "weekend": obj.get("weekend")
        })
        return _obj


