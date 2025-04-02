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

from firefly_iii_client.api.accounts_api import AccountsApi


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_account(self) -> None:
        """Test case for delete_account

        Permanently delete account.
        """
        pass

    def test_get_account(self) -> None:
        """Test case for get_account

        Get single account.
        """
        pass

    def test_list_account(self) -> None:
        """Test case for list_account

        List all accounts.
        """
        pass

    def test_list_attachment_by_account(self) -> None:
        """Test case for list_attachment_by_account

        Lists all attachments.
        """
        pass

    def test_list_piggy_bank_by_account(self) -> None:
        """Test case for list_piggy_bank_by_account

        List all piggy banks related to the account.
        """
        pass

    def test_list_transaction_by_account(self) -> None:
        """Test case for list_transaction_by_account

        List all transactions related to the account.
        """
        pass

    def test_store_account(self) -> None:
        """Test case for store_account

        Create new account.
        """
        pass

    def test_update_account(self) -> None:
        """Test case for update_account

        Update existing account.
        """
        pass


if __name__ == '__main__':
    unittest.main()
