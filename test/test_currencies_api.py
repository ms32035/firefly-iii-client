# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: v6.2.10
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.api.currencies_api import CurrenciesApi


class TestCurrenciesApi(unittest.TestCase):
    """CurrenciesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CurrenciesApi()

    def tearDown(self) -> None:
        pass

    def test_default_currency(self) -> None:
        """Test case for default_currency

        Make currency default currency.
        """
        pass

    def test_delete_currency(self) -> None:
        """Test case for delete_currency

        Delete a currency.
        """
        pass

    def test_disable_currency(self) -> None:
        """Test case for disable_currency

        Disable a currency.
        """
        pass

    def test_enable_currency(self) -> None:
        """Test case for enable_currency

        Enable a single currency.
        """
        pass

    def test_get_currency(self) -> None:
        """Test case for get_currency

        Get a single currency.
        """
        pass

    def test_get_native_currency(self) -> None:
        """Test case for get_native_currency

        Get the native currency of the current administration.
        """
        pass

    def test_list_account_by_currency(self) -> None:
        """Test case for list_account_by_currency

        List all accounts with this currency.
        """
        pass

    def test_list_available_budget_by_currency(self) -> None:
        """Test case for list_available_budget_by_currency

        List all available budgets with this currency.
        """
        pass

    def test_list_bill_by_currency(self) -> None:
        """Test case for list_bill_by_currency

        List all bills with this currency.
        """
        pass

    def test_list_budget_limit_by_currency(self) -> None:
        """Test case for list_budget_limit_by_currency

        List all budget limits with this currency
        """
        pass

    def test_list_currency(self) -> None:
        """Test case for list_currency

        List all currencies.
        """
        pass

    def test_list_recurrence_by_currency(self) -> None:
        """Test case for list_recurrence_by_currency

        List all recurring transactions with this currency.
        """
        pass

    def test_list_rule_by_currency(self) -> None:
        """Test case for list_rule_by_currency

        List all rules with this currency.
        """
        pass

    def test_list_transaction_by_currency(self) -> None:
        """Test case for list_transaction_by_currency

        List all transactions with this currency.
        """
        pass

    def test_store_currency(self) -> None:
        """Test case for store_currency

        Store a new currency
        """
        pass

    def test_update_currency(self) -> None:
        """Test case for update_currency

        Update existing currency.
        """
        pass


if __name__ == '__main__':
    unittest.main()
