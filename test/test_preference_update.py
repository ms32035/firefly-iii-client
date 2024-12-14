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

from firefly_iii_client.models.preference_update import PreferenceUpdate

class TestPreferenceUpdate(unittest.TestCase):
    """PreferenceUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PreferenceUpdate:
        """Test PreferenceUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PreferenceUpdate`
        """
        model = PreferenceUpdate()
        if include_optional:
            return PreferenceUpdate(
                data = None
            )
        else:
            return PreferenceUpdate(
                data = None,
        )
        """

    def testPreferenceUpdate(self):
        """Test PreferenceUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
