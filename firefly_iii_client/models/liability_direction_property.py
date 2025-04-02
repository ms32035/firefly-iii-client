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
import json
from enum import Enum
from typing_extensions import Self


class LiabilityDirectionProperty(str, Enum):
    """
    'credit' indicates somebody owes you the liability. 'debit' Indicates you owe this debt yourself. Works only for liabiltiies.
    """

    """
    allowed enum values
    """
    CREDIT = 'credit'
    DEBIT = 'debit'
    NULL = 'null'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LiabilityDirectionProperty from a JSON string"""
        return cls(json.loads(json_str))


