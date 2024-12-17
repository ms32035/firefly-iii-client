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

from firefly_iii_client.models.unauthenticated_response import UnauthenticatedResponse

class TestUnauthenticatedResponse(unittest.TestCase):
    """UnauthenticatedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnauthenticatedResponse:
        """Test UnauthenticatedResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnauthenticatedResponse`
        """
        model = UnauthenticatedResponse()
        if include_optional:
            return UnauthenticatedResponse(
                exception = 'AuthenticationException',
                message = 'Unauthenticated'
            )
        else:
            return UnauthenticatedResponse(
        )
        """

    def testUnauthenticatedResponse(self):
        """Test UnauthenticatedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()