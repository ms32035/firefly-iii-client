# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 6.1.24
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.api.data_api import DataApi


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_update_transactions(self) -> None:
        """Test case for bulk_update_transactions

        Bulk update transaction properties. For more information, see https://docs.firefly-iii.org/references/firefly-iii/api/specials/
        """
        pass

    def test_destroy_data(self) -> None:
        """Test case for destroy_data

        Endpoint to destroy user data
        """
        pass

    def test_export_accounts(self) -> None:
        """Test case for export_accounts

        Export account data from Firefly III
        """
        pass

    def test_export_bills(self) -> None:
        """Test case for export_bills

        Export bills from Firefly III
        """
        pass

    def test_export_budgets(self) -> None:
        """Test case for export_budgets

        Export budgets and budget amount data from Firefly III
        """
        pass

    def test_export_categories(self) -> None:
        """Test case for export_categories

        Export category data from Firefly III
        """
        pass

    def test_export_piggies(self) -> None:
        """Test case for export_piggies

        Export piggy banks from Firefly III
        """
        pass

    def test_export_recurring(self) -> None:
        """Test case for export_recurring

        Export recurring transaction data from Firefly III
        """
        pass

    def test_export_rules(self) -> None:
        """Test case for export_rules

        Export rule groups and rule data from Firefly III
        """
        pass

    def test_export_tags(self) -> None:
        """Test case for export_tags

        Export tag data from Firefly III
        """
        pass

    def test_export_transactions(self) -> None:
        """Test case for export_transactions

        Export transaction data from Firefly III
        """
        pass

    def test_purge_data(self) -> None:
        """Test case for purge_data

        Endpoint to purge user data
        """
        pass


if __name__ == '__main__':
    unittest.main()