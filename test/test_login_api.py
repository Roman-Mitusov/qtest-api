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
from swagger_client.api.login_api import LoginApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_access_token(self):
        """Test case for post_access_token

        Log in  # noqa: E501
        """
        pass

    def test_token_status(self):
        """Test case for token_status

        Gets status of access token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
