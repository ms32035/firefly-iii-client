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

from firefly_iii_client.models.webhook_store import WebhookStore

class TestWebhookStore(unittest.TestCase):
    """WebhookStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookStore:
        """Test WebhookStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookStore`
        """
        model = WebhookStore()
        if include_optional:
            return WebhookStore(
                active = False,
                delivery = 'JSON',
                response = 'RESPONSE_TRANSACTIONS',
                title = 'Update magic mirror on new transaction',
                trigger = 'DESTROY_TRANSACTION',
                url = 'https://example.com'
            )
        else:
            return WebhookStore(
                delivery = 'JSON',
                response = 'RESPONSE_TRANSACTIONS',
                title = 'Update magic mirror on new transaction',
                trigger = 'DESTROY_TRANSACTION',
                url = 'https://example.com',
        )
        """

    def testWebhookStore(self):
        """Test WebhookStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
