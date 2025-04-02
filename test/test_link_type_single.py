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

from firefly_iii_client.models.link_type_single import LinkTypeSingle

class TestLinkTypeSingle(unittest.TestCase):
    """LinkTypeSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkTypeSingle:
        """Test LinkTypeSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkTypeSingle`
        """
        model = LinkTypeSingle()
        if include_optional:
            return LinkTypeSingle(
                data = firefly_iii_client.models.link_type_read.LinkTypeRead(
                    attributes = firefly_iii_client.models.link_type.LinkType(
                        editable = False, 
                        inward = 'is (partially) paid for by', 
                        name = 'Paid', 
                        outward = '(partially) pays for', ), 
                    id = '2', 
                    links = firefly_iii_client.models.object_link.ObjectLink(
                        0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                    type = 'link_types', )
            )
        else:
            return LinkTypeSingle(
                data = firefly_iii_client.models.link_type_read.LinkTypeRead(
                    attributes = firefly_iii_client.models.link_type.LinkType(
                        editable = False, 
                        inward = 'is (partially) paid for by', 
                        name = 'Paid', 
                        outward = '(partially) pays for', ), 
                    id = '2', 
                    links = firefly_iii_client.models.object_link.ObjectLink(
                        0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                            rel = 'self', 
                            uri = '/OBJECTS/1', ), 
                        self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                    type = 'link_types', ),
        )
        """

    def testLinkTypeSingle(self):
        """Test LinkTypeSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
