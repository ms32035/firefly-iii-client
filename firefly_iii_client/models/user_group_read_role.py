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


class UserGroupReadRole(str, Enum):
    """
    The possible roles of the user in this user group are documented here: https://docs.firefly-iii.org/references/firefly-iii/api/ 
    """

    """
    allowed enum values
    """
    OWNER = 'owner'
    RO = 'ro'
    MNG_TRX = 'mng_trx'
    MNG_META = 'mng_meta'
    READ_BUDGETS = 'read_budgets'
    READ_PIGGIES = 'read_piggies'
    READ_SUBSCRIPTIONS = 'read_subscriptions'
    READ_RULES = 'read_rules'
    READ_RECURRING = 'read_recurring'
    READ_WEBHOOKS = 'read_webhooks'
    READ_CURRENCIES = 'read_currencies'
    MNG_BUDGETS = 'mng_budgets'
    MNG_PIGGIES = 'mng_piggies'
    MNG_SUBSCRIPTIONS = 'mng_subscriptions'
    MNG_RULES = 'mng_rules'
    MNG_RECURRING = 'mng_recurring'
    MNG_WEBHOOKS = 'mng_webhooks'
    MNG_CURRENCIES = 'mng_currencies'
    VIEW_REPORTS = 'view_reports'
    VIEW_MEMBERSHIPS = 'view_memberships'
    FULL = 'full'
    OWNER = 'owner'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserGroupReadRole from a JSON string"""
        return cls(json.loads(json_str))


