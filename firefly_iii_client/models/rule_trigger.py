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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.rule_trigger_keyword import RuleTriggerKeyword
from typing import Optional, Set
from typing_extensions import Self

class RuleTrigger(BaseModel):
    """
    RuleTrigger
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=True, description="If the trigger is active. Defaults to true.")
    created_at: Optional[datetime] = None
    id: Optional[StrictStr] = None
    order: Optional[StrictInt] = Field(default=None, description="Order of the trigger")
    stop_processing: Optional[StrictBool] = Field(default=False, description="When true, other triggers will not be checked if this trigger was triggered. Defaults to false.")
    type: RuleTriggerKeyword
    updated_at: Optional[datetime] = None
    value: StrictStr = Field(description="The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger.")
    __properties: ClassVar[List[str]] = ["active", "created_at", "id", "order", "stop_processing", "type", "updated_at", "value"]

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
        """Create an instance of RuleTrigger from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "id",
            "order",
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
        """Create an instance of RuleTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active") if obj.get("active") is not None else True,
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "order": obj.get("order"),
            "stop_processing": obj.get("stop_processing") if obj.get("stop_processing") is not None else False,
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "value": obj.get("value")
        })
        return _obj


