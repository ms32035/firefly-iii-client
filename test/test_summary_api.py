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

from firefly_iii_client.api.summary_api import SummaryApi


class TestSummaryApi(unittest.TestCase):
    """SummaryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SummaryApi()

    def tearDown(self) -> None:
        pass

    def test_get_basic_summary(self) -> None:
        """Test case for get_basic_summary

        Returns basic sums of the users data.
        """
        pass


if __name__ == '__main__':
    unittest.main()
