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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.webhook_delivery import WebhookDelivery
from firefly_iii_client.models.webhook_response import WebhookResponse
from firefly_iii_client.models.webhook_trigger import WebhookTrigger
from typing import Optional, Set
from typing_extensions import Self

class WebhookUpdate(BaseModel):
    """
    WebhookUpdate
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="Boolean to indicate if the webhook is active")
    delivery: Optional[WebhookDelivery] = None
    response: Optional[WebhookResponse] = None
    secret: Optional[StrictStr] = Field(default=None, description="A 24-character secret for the webhook. It's generated by Firefly III when saving a new webhook. If you submit a new secret through the PUT endpoint it will generate a new secret for the selected webhook, a new secret bearing no relation to whatever you just submitted.")
    title: Optional[StrictStr] = Field(default=None, description="A title for the webhook for easy recognition.")
    trigger: Optional[WebhookTrigger] = None
    url: Optional[StrictStr] = Field(default=None, description="The URL of the webhook. Has to start with `https`.")
    __properties: ClassVar[List[str]] = ["active", "delivery", "response", "secret", "title", "trigger", "url"]

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
        """Create an instance of WebhookUpdate from a JSON string"""
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
        """Create an instance of WebhookUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "delivery": obj.get("delivery"),
            "response": obj.get("response"),
            "secret": obj.get("secret"),
            "title": obj.get("title"),
            "trigger": obj.get("trigger"),
            "url": obj.get("url")
        })
        return _obj


