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
from typing import Optional, Set
from typing_extensions import Self

class CronResultRow(BaseModel):
    """
    CronResultRow
    """ # noqa: E501
    job_errored: Optional[StrictBool] = Field(default=None, description="If the cron job ran into some kind of an error, this value will be true.")
    job_fired: Optional[StrictBool] = Field(default=None, description="This value tells you if this specific cron job actually fired. It may not fire. Some cron jobs only fire every 24 hours, for example. ")
    job_succeeded: Optional[StrictBool] = Field(default=None, description="This value tells you if this specific cron job actually did something. The job may fire but not change anything. ")
    message: Optional[StrictStr] = Field(default=None, description="If the cron job ran into some kind of an error, this value will be the error message. The success message if the job actually ran OK. ")
    __properties: ClassVar[List[str]] = ["job_errored", "job_fired", "job_succeeded", "message"]

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
        """Create an instance of CronResultRow from a JSON string"""
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
        # set to None if job_errored (nullable) is None
        # and model_fields_set contains the field
        if self.job_errored is None and "job_errored" in self.model_fields_set:
            _dict['job_errored'] = None

        # set to None if job_fired (nullable) is None
        # and model_fields_set contains the field
        if self.job_fired is None and "job_fired" in self.model_fields_set:
            _dict['job_fired'] = None

        # set to None if job_succeeded (nullable) is None
        # and model_fields_set contains the field
        if self.job_succeeded is None and "job_succeeded" in self.model_fields_set:
            _dict['job_succeeded'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CronResultRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job_errored": obj.get("job_errored"),
            "job_fired": obj.get("job_fired"),
            "job_succeeded": obj.get("job_succeeded"),
            "message": obj.get("message")
        })
        return _obj


