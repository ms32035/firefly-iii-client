# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 6.1.24
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CreditCardTypeProperty(str, Enum):
    """
    Mandatory when the account_role is ccAsset. Can only be monthlyFull or null.
    """

    """
    allowed enum values
    """
    MONTHLYFULL = 'monthlyFull'
    NULL = 'null'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CreditCardTypeProperty from a JSON string"""
        return cls(json.loads(json_str))

