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

from firefly_iii_client.models.webhook_message_single import WebhookMessageSingle

class TestWebhookMessageSingle(unittest.TestCase):
    """WebhookMessageSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookMessageSingle:
        """Test WebhookMessageSingle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookMessageSingle`
        """
        model = WebhookMessageSingle()
        if include_optional:
            return WebhookMessageSingle(
                data = firefly_iii_client.models.webhook_message_read.WebhookMessageRead(
                    attributes = firefly_iii_client.models.webhook_message.WebhookMessage(
                        created_at = '2018-09-17T12:46:47+01:00', 
                        errored = False, 
                        message = '{some:message}', 
                        sent = False, 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        uuid = '7a344c02-5b52-46b1-90e6-a437431dcf07', 
                        webhook_id = '5', ), 
                    id = '2', 
                    type = 'webhook_messages', )
            )
        else:
            return WebhookMessageSingle(
                data = firefly_iii_client.models.webhook_message_read.WebhookMessageRead(
                    attributes = firefly_iii_client.models.webhook_message.WebhookMessage(
                        created_at = '2018-09-17T12:46:47+01:00', 
                        errored = False, 
                        message = '{some:message}', 
                        sent = False, 
                        updated_at = '2018-09-17T12:46:47+01:00', 
                        uuid = '7a344c02-5b52-46b1-90e6-a437431dcf07', 
                        webhook_id = '5', ), 
                    id = '2', 
                    type = 'webhook_messages', ),
        )
        """

    def testWebhookMessageSingle(self):
        """Test WebhookMessageSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
