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

from firefly_iii_client.models.configuration import Configuration

class TestConfiguration(unittest.TestCase):
    """Configuration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Configuration:
        """Test Configuration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Configuration`
        """
        model = Configuration()
        if include_optional:
            return Configuration(
                editable = True,
                title = 'configuration.is_demo_site',
                value = None
            )
        else:
            return Configuration(
                editable = True,
                title = 'configuration.is_demo_site',
                value = None,
        )
        """

    def testConfiguration(self):
        """Test Configuration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
