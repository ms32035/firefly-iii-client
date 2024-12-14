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

from firefly_iii_client.models.link_type import LinkType

class TestLinkType(unittest.TestCase):
    """LinkType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkType:
        """Test LinkType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkType`
        """
        model = LinkType()
        if include_optional:
            return LinkType(
                editable = False,
                inward = 'is (partially) paid for by',
                name = 'Paid',
                outward = '(partially) pays for'
            )
        else:
            return LinkType(
                inward = 'is (partially) paid for by',
                name = 'Paid',
                outward = '(partially) pays for',
        )
        """

    def testLinkType(self):
        """Test LinkType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
