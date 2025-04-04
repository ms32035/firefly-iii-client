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

from firefly_iii_client.api.about_api import AboutApi


class TestAboutApi(unittest.TestCase):
    """AboutApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AboutApi()

    def tearDown(self) -> None:
        pass

    def test_get_about(self) -> None:
        """Test case for get_about

        System information end point.
        """
        pass

    def test_get_cron(self) -> None:
        """Test case for get_cron

        Cron job endpoint
        """
        pass

    def test_get_current_user(self) -> None:
        """Test case for get_current_user

        Currently authenticated user endpoint.
        """
        pass


if __name__ == '__main__':
    unittest.main()
