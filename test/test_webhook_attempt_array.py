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

from firefly_iii_client.models.webhook_attempt_array import WebhookAttemptArray

class TestWebhookAttemptArray(unittest.TestCase):
    """WebhookAttemptArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookAttemptArray:
        """Test WebhookAttemptArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookAttemptArray`
        """
        model = WebhookAttemptArray()
        if include_optional:
            return WebhookAttemptArray(
                data = [
                    firefly_iii_client.models.webhook_attempt_read.WebhookAttemptRead(
                        attributes = firefly_iii_client.models.webhook_attempt.WebhookAttempt(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            logs = 'Page not found', 
                            response = 'Page not found', 
                            status_code = 404, 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            webhook_message_id = '5', ), 
                        id = '2', 
                        type = 'webhook_attempts', )
                    ],
                meta = firefly_iii_client.models.meta.Meta(
                    pagination = firefly_iii_client.models.meta_pagination.Meta_pagination(
                        count = 20, 
                        current_page = 1, 
                        per_page = 100, 
                        total = 3, 
                        total_pages = 1, ), )
            )
        else:
            return WebhookAttemptArray(
                data = [
                    firefly_iii_client.models.webhook_attempt_read.WebhookAttemptRead(
                        attributes = firefly_iii_client.models.webhook_attempt.WebhookAttempt(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            logs = 'Page not found', 
                            response = 'Page not found', 
                            status_code = 404, 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            webhook_message_id = '5', ), 
                        id = '2', 
                        type = 'webhook_attempts', )
                    ],
                meta = firefly_iii_client.models.meta.Meta(
                    pagination = firefly_iii_client.models.meta_pagination.Meta_pagination(
                        count = 20, 
                        current_page = 1, 
                        per_page = 100, 
                        total = 3, 
                        total_pages = 1, ), ),
        )
        """

    def testWebhookAttemptArray(self):
        """Test WebhookAttemptArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
