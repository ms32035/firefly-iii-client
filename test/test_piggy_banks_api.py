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

from firefly_iii_client.api.piggy_banks_api import PiggyBanksApi


class TestPiggyBanksApi(unittest.TestCase):
    """PiggyBanksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PiggyBanksApi()

    def tearDown(self) -> None:
        pass

    def test_delete_piggy_bank(self) -> None:
        """Test case for delete_piggy_bank

        Delete a piggy bank.
        """
        pass

    def test_get_piggy_bank(self) -> None:
        """Test case for get_piggy_bank

        Get a single piggy bank.
        """
        pass

    def test_list_attachment_by_piggy_bank(self) -> None:
        """Test case for list_attachment_by_piggy_bank

        Lists all attachments.
        """
        pass

    def test_list_event_by_piggy_bank(self) -> None:
        """Test case for list_event_by_piggy_bank

        List all events linked to a piggy bank.
        """
        pass

    def test_list_piggy_bank(self) -> None:
        """Test case for list_piggy_bank

        List all piggy banks.
        """
        pass

    def test_store_piggy_bank(self) -> None:
        """Test case for store_piggy_bank

        Store a new piggy bank
        """
        pass

    def test_update_piggy_bank(self) -> None:
        """Test case for update_piggy_bank

        Update existing piggy bank.
        """
        pass


if __name__ == '__main__':
    unittest.main()
