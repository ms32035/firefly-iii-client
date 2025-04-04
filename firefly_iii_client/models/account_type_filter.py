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


class AccountTypeFilter(str, Enum):
    """
    AccountTypeFilter
    """

    """
    allowed enum values
    """
    ALL = 'all'
    ASSET = 'asset'
    CASH = 'cash'
    EXPENSE = 'expense'
    REVENUE = 'revenue'
    SPECIAL = 'special'
    HIDDEN = 'hidden'
    LIABILITY = 'liability'
    LIABILITIES = 'liabilities'
    DEFAULT_ACCOUNT = 'Default account'
    CASH_ACCOUNT = 'Cash account'
    ASSET_ACCOUNT = 'Asset account'
    EXPENSE_ACCOUNT = 'Expense account'
    REVENUE_ACCOUNT = 'Revenue account'
    INITIAL_BALANCE_ACCOUNT = 'Initial balance account'
    BENEFICIARY_ACCOUNT = 'Beneficiary account'
    IMPORT_ACCOUNT = 'Import account'
    RECONCILIATION_ACCOUNT = 'Reconciliation account'
    LOAN = 'Loan'
    DEBT = 'Debt'
    MORTGAGE = 'Mortgage'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccountTypeFilter from a JSON string"""
        return cls(json.loads(json_str))


