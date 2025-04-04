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

from firefly_iii_client.models.autocomplete_piggy import AutocompletePiggy

class TestAutocompletePiggy(unittest.TestCase):
    """AutocompletePiggy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutocompletePiggy:
        """Test AutocompletePiggy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutocompletePiggy`
        """
        model = AutocompletePiggy()
        if include_optional:
            return AutocompletePiggy(
                currency_code = 'EUR',
                currency_decimal_places = 2,
                currency_id = '12',
                currency_name = 'Euro',
                currency_symbol = '$',
                id = '2',
                name = 'New couch',
                object_group_id = '5',
                object_group_title = 'Example Group'
            )
        else:
            return AutocompletePiggy(
                id = '2',
                name = 'New couch',
        )
        """

    def testAutocompletePiggy(self):
        """Test AutocompletePiggy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
