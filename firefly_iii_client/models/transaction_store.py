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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.transaction_split_store import TransactionSplitStore
from typing import Optional, Set
from typing_extensions import Self

class TransactionStore(BaseModel):
    """
    TransactionStore
    """ # noqa: E501
    apply_rules: Optional[StrictBool] = Field(default=None, description="Whether or not to apply rules when submitting transaction.")
    error_if_duplicate_hash: Optional[StrictBool] = Field(default=None, description="Break if the submitted transaction exists already.")
    fire_webhooks: Optional[StrictBool] = Field(default=True, description="Whether or not to fire the webhooks that are related to this event.")
    group_title: Optional[StrictStr] = Field(default=None, description="Title of the transaction if it has been split in more than one piece. Empty otherwise.")
    transactions: List[TransactionSplitStore]
    __properties: ClassVar[List[str]] = ["apply_rules", "error_if_duplicate_hash", "fire_webhooks", "group_title", "transactions"]

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
        """Create an instance of TransactionStore from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        # set to None if group_title (nullable) is None
        # and model_fields_set contains the field
        if self.group_title is None and "group_title" in self.model_fields_set:
            _dict['group_title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionStore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apply_rules": obj.get("apply_rules"),
            "error_if_duplicate_hash": obj.get("error_if_duplicate_hash"),
            "fire_webhooks": obj.get("fire_webhooks") if obj.get("fire_webhooks") is not None else True,
            "group_title": obj.get("group_title"),
            "transactions": [TransactionSplitStore.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None
        })
        return _obj


