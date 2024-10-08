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
from swagger_client.api.defect_api import DefectApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefectApi(unittest.TestCase):
    """DefectApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.defect_api.DefectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_comment(self):
        """Test case for add_comment

        Adds a Comment to a Defect  # noqa: E501
        """
        pass

    def test_delete_comment(self):
        """Test case for delete_comment

        Deletes a Comment of a Defect  # noqa: E501
        """
        pass

    def test_get_comments(self):
        """Test case for get_comments

        Gets all Comments of a Defect  # noqa: E501
        """
        pass

    def test_get_defect(self):
        """Test case for get_defect

        Gets a Defect  # noqa: E501
        """
        pass

    def test_get_defect_comment_by_id(self):
        """Test case for get_defect_comment_by_id

        Gets a Comment of a Defect  # noqa: E501
        """
        pass

    def test_get_last_changed(self):
        """Test case for get_last_changed

        Gets recently updated Defects  # noqa: E501
        """
        pass

    def test_submit_defect(self):
        """Test case for submit_defect

        Submit a Defect  # noqa: E501
        """
        pass

    def test_update_comment(self):
        """Test case for update_comment

        Updates a Comment of a Defect  # noqa: E501
        """
        pass

    def test_update_defect(self):
        """Test case for update_defect

        Updates a Defect  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
