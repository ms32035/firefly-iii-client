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

from firefly_iii_client.models.attachment_array import AttachmentArray

class TestAttachmentArray(unittest.TestCase):
    """AttachmentArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachmentArray:
        """Test AttachmentArray
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachmentArray`
        """
        model = AttachmentArray()
        if include_optional:
            return AttachmentArray(
                data = [
                    firefly_iii_client.models.attachment_read.AttachmentRead(
                        attributes = firefly_iii_client.models.attachment.Attachment(
                            attachable_id = '134', 
                            attachable_type = 'Bill', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            download_url = 'https://demo.firefly-iii.org/api/v1/attachments/191/download', 
                            filename = 'file.pdf', 
                            md5 = '0c3f95f34370baa88f9fd9a671fea305', 
                            mime = 'application/pdf', 
                            notes = 'Some notes', 
                            size = 48211, 
                            title = 'Some PDF file', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            upload_url = 'https://demo.firefly-iii.org/api/v1/attachments/191/download', ), 
                        id = '2', 
                        links = firefly_iii_client.models.object_link.ObjectLink(
                            0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), 
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                        type = 'attachments', )
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
            return AttachmentArray(
                data = [
                    firefly_iii_client.models.attachment_read.AttachmentRead(
                        attributes = firefly_iii_client.models.attachment.Attachment(
                            attachable_id = '134', 
                            attachable_type = 'Bill', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            download_url = 'https://demo.firefly-iii.org/api/v1/attachments/191/download', 
                            filename = 'file.pdf', 
                            md5 = '0c3f95f34370baa88f9fd9a671fea305', 
                            mime = 'application/pdf', 
                            notes = 'Some notes', 
                            size = 48211, 
                            title = 'Some PDF file', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            upload_url = 'https://demo.firefly-iii.org/api/v1/attachments/191/download', ), 
                        id = '2', 
                        links = firefly_iii_client.models.object_link.ObjectLink(
                            0 = firefly_iii_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), 
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', ), 
                        type = 'attachments', )
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

    def testAttachmentArray(self):
        """Test AttachmentArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
