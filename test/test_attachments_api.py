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

from firefly_iii_client.api.attachments_api import AttachmentsApi


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AttachmentsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_attachment(self) -> None:
        """Test case for delete_attachment

        Delete an attachment.
        """
        pass

    def test_download_attachment(self) -> None:
        """Test case for download_attachment

        Download a single attachment.
        """
        pass

    def test_get_attachment(self) -> None:
        """Test case for get_attachment

        Get a single attachment.
        """
        pass

    def test_list_attachment(self) -> None:
        """Test case for list_attachment

        List all attachments.
        """
        pass

    def test_store_attachment(self) -> None:
        """Test case for store_attachment

        Store a new attachment.
        """
        pass

    def test_update_attachment(self) -> None:
        """Test case for update_attachment

        Update existing attachment.
        """
        pass

    def test_upload_attachment(self) -> None:
        """Test case for upload_attachment

        Upload an attachment.
        """
        pass


if __name__ == '__main__':
    unittest.main()
