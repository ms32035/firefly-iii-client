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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.rule_action import RuleAction
from firefly_iii_client.models.rule_trigger import RuleTrigger
from firefly_iii_client.models.rule_trigger_type import RuleTriggerType
from typing import Optional, Set
from typing_extensions import Self

class Rule(BaseModel):
    """
    Rule
    """ # noqa: E501
    actions: List[RuleAction]
    active: Optional[StrictBool] = Field(default=True, description="Whether or not the rule is even active. Default is true.")
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    order: Optional[StrictInt] = None
    rule_group_id: StrictStr = Field(description="ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory.")
    rule_group_title: Optional[StrictStr] = Field(default=None, description="Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory.")
    stop_processing: Optional[StrictBool] = Field(default=False, description="If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false.")
    strict: Optional[StrictBool] = Field(default=None, description="If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true.")
    title: StrictStr
    trigger: RuleTriggerType
    triggers: List[RuleTrigger]
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["actions", "active", "created_at", "description", "order", "rule_group_id", "rule_group_title", "stop_processing", "strict", "title", "trigger", "triggers", "updated_at"]

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
        """Create an instance of Rule from a JSON string"""
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
            "created_at",
            "order",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item_triggers in self.triggers:
                if _item_triggers:
                    _items.append(_item_triggers.to_dict())
            _dict['triggers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [RuleAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "active": obj.get("active") if obj.get("active") is not None else True,
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "order": obj.get("order"),
            "rule_group_id": obj.get("rule_group_id"),
            "rule_group_title": obj.get("rule_group_title"),
            "stop_processing": obj.get("stop_processing") if obj.get("stop_processing") is not None else False,
            "strict": obj.get("strict"),
            "title": obj.get("title"),
            "trigger": obj.get("trigger"),
            "triggers": [RuleTrigger.from_dict(_item) for _item in obj["triggers"]] if obj.get("triggers") is not None else None,
            "updated_at": obj.get("updated_at")
        })
        return _obj


