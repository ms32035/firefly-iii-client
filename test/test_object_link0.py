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

from firefly_iii_client.models.object_link0 import ObjectLink0

class TestObjectLink0(unittest.TestCase):
    """ObjectLink0 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectLink0:
        """Test ObjectLink0
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectLink0`
        """
        model = ObjectLink0()
        if include_optional:
            return ObjectLink0(
                rel = 'self',
                uri = '/OBJECTS/1'
            )
        else:
            return ObjectLink0(
        )
        """

    def testObjectLink0(self):
        """Test ObjectLink0"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
