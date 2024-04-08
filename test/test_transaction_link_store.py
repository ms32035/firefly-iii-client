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

from firefly_iii_client.models.transaction_link_store import TransactionLinkStore

class TestTransactionLinkStore(unittest.TestCase):
    """TransactionLinkStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionLinkStore:
        """Test TransactionLinkStore
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionLinkStore`
        """
        model = TransactionLinkStore()
        if include_optional:
            return TransactionLinkStore(
                inward_id = '131',
                link_type_id = '5',
                link_type_name = 'Is paid by',
                notes = 'Some example notes',
                outward_id = '131'
            )
        else:
            return TransactionLinkStore(
                inward_id = '131',
                link_type_id = '5',
                outward_id = '131',
        )
        """

    def testTransactionLinkStore(self):
        """Test TransactionLinkStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
