# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.models.autocomplete_transaction_id import AutocompleteTransactionID

class TestAutocompleteTransactionID(unittest.TestCase):
    """AutocompleteTransactionID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutocompleteTransactionID:
        """Test AutocompleteTransactionID
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutocompleteTransactionID`
        """
        model = AutocompleteTransactionID()
        if include_optional:
            return AutocompleteTransactionID(
                description = '#12: Transaction',
                id = '2',
                name = '#12: Transaction',
                transaction_group_id = '2'
            )
        else:
            return AutocompleteTransactionID(
                description = '#12: Transaction',
                id = '2',
                name = '#12: Transaction',
        )
        """

    def testAutocompleteTransactionID(self):
        """Test AutocompleteTransactionID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
