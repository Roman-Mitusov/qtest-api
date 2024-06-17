# coding: utf-8

"""
    qTest Manager API Version 11.0.0 - 2023.6

    qTest Manager API Version 11.0.0 - 2023.6  # noqa: E501

    OpenAPI spec version: 11.0.0 - 2023.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.attachment_api import AttachmentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAttachmentApi(unittest.TestCase):
    """AttachmentApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.attachment_api.AttachmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_by_blob_handle_id(self):
        """Test case for delete_by_blob_handle_id

        Deletes an Attachment from an Object  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Gets an Attachment of an Object  # noqa: E501
        """
        pass

    def test_get_attachments_of(self):
        """Test case for get_attachments_of

        Gets all Attachments of an Object  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Searches for Attachments  # noqa: E501
        """
        pass

    def test_upload(self):
        """Test case for upload

        Uploads an Attachment to an Object  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
