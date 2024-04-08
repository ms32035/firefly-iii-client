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
import json
from enum import Enum
from typing_extensions import Self


class TransactionTypeFilter(str, Enum):
    """
    TransactionTypeFilter
    """

    """
    allowed enum values
    """
    ALL = 'all'
    WITHDRAWAL = 'withdrawal'
    WITHDRAWALS = 'withdrawals'
    EXPENSE = 'expense'
    DEPOSIT = 'deposit'
    DEPOSITS = 'deposits'
    INCOME = 'income'
    TRANSFER = 'transfer'
    TRANSFERS = 'transfers'
    OPENING_BALANCE = 'opening_balance'
    RECONCILIATION = 'reconciliation'
    SPECIAL = 'special'
    SPECIALS = 'specials'
    DEFAULT = 'default'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionTypeFilter from a JSON string"""
        return cls(json.loads(json_str))


