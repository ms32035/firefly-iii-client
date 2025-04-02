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

from firefly_iii_client.models.autocomplete_transaction_type import AutocompleteTransactionType

class TestAutocompleteTransactionType(unittest.TestCase):
    """AutocompleteTransactionType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutocompleteTransactionType:
        """Test AutocompleteTransactionType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutocompleteTransactionType`
        """
        model = AutocompleteTransactionType()
        if include_optional:
            return AutocompleteTransactionType(
                id = '2',
                name = 'Withdrawal',
                type = 'Withdrawal'
            )
        else:
            return AutocompleteTransactionType(
                id = '2',
                name = 'Withdrawal',
                type = 'Withdrawal',
        )
        """

    def testAutocompleteTransactionType(self):
        """Test AutocompleteTransactionType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
