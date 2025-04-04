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

from firefly_iii_client.models.configuration_single import ConfigurationSingle

class TestConfigurationSingle(unittest.TestCase):
    """ConfigurationSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationSingle:
        """Test ConfigurationSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationSingle`
        """
        model = ConfigurationSingle()
        if include_optional:
            return ConfigurationSingle(
                data = firefly_iii_client.models.configuration.Configuration(
                    editable = True, 
                    title = 'configuration.is_demo_site', 
                    value = null, )
            )
        else:
            return ConfigurationSingle(
                data = firefly_iii_client.models.configuration.Configuration(
                    editable = True, 
                    title = 'configuration.is_demo_site', 
                    value = null, ),
        )
        """

    def testConfigurationSingle(self):
        """Test ConfigurationSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
