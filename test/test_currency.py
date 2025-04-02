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

from firefly_iii_client.models.currency import Currency

class TestCurrency(unittest.TestCase):
    """Currency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Currency:
        """Test Currency
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Currency`
        """
        model = Currency()
        if include_optional:
            return Currency(
                code = 'AMS',
                created_at = '2018-09-17T12:46:47+01:00',
                decimal_places = 2,
                default = False,
                enabled = True,
                name = 'Ankh-Morpork dollar',
                native = False,
                symbol = 'AM$',
                updated_at = '2018-09-17T12:46:47+01:00'
            )
        else:
            return Currency(
                code = 'AMS',
                name = 'Ankh-Morpork dollar',
                symbol = 'AM$',
        )
        """

    def testCurrency(self):
        """Test Currency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
