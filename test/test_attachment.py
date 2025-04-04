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

from firefly_iii_client.models.attachment import Attachment

class TestAttachment(unittest.TestCase):
    """Attachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attachment:
        """Test Attachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attachment`
        """
        model = Attachment()
        if include_optional:
            return Attachment(
                attachable_id = '134',
                attachable_type = 'Bill',
                created_at = '2018-09-17T12:46:47+01:00',
                download_url = 'https://demo.firefly-iii.org/api/v1/attachments/191/download',
                filename = 'file.pdf',
                hash = '0c3f95f34370baa88f9fd9a671fea305',
                md5 = '0c3f95f34370baa88f9fd9a671fea305',
                mime = 'application/pdf',
                notes = 'Some notes',
                size = 48211,
                title = 'Some PDF file',
                updated_at = '2018-09-17T12:46:47+01:00',
                upload_url = 'https://demo.firefly-iii.org/api/v1/attachments/191/download'
            )
        else:
            return Attachment(
                attachable_id = '134',
                attachable_type = 'Bill',
                filename = 'file.pdf',
        )
        """

    def testAttachment(self):
        """Test Attachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
