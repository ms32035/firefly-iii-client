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

from firefly_iii_client.models.transaction_link_read import TransactionLinkRead

class TestTransactionLinkRead(unittest.TestCase):
    """TransactionLinkRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionLinkRead:
        """Test TransactionLinkRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionLinkRead`
        """
        model = TransactionLinkRead()
        if include_optional:
            return TransactionLinkRead(
                attributes = firefly_iii_client.models.transaction_link.TransactionLink(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    inward_id = '131', 
                    link_type_id = '5', 
                    link_type_name = 'Is paid by', 
                    notes = 'Some example notes', 
                    outward_id = '131', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'transactionLinks'
            )
        else:
            return TransactionLinkRead(
                attributes = firefly_iii_client.models.transaction_link.TransactionLink(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    inward_id = '131', 
                    link_type_id = '5', 
                    link_type_name = 'Is paid by', 
                    notes = 'Some example notes', 
                    outward_id = '131', 
                    updated_at = '2018-09-17T12:46:47+01:00', ),
                id = '2',
                links = firefly_iii_client.models.object_link.ObjectLink(
                    0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), 
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ),
                type = 'transactionLinks',
        )
        """

    def testTransactionLinkRead(self):
        """Test TransactionLinkRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
