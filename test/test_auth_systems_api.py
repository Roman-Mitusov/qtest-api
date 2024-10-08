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
from swagger_client.api.auth_systems_api import AuthSystemsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthSystemsApi(unittest.TestCase):
    """AuthSystemsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.auth_systems_api.AuthSystemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all(self):
        """Test case for get_all

        Get multiple Authentication Systems  # noqa: E501
        """
        pass

    def test_get_all_ldap_users(self):
        """Test case for get_all_ldap_users

        Get all LDAP users of an authentication LDAP config  # noqa: E501
        """
        pass

    def test_import_l_dap_users(self):
        """Test case for import_l_dap_users

        Associate Manager users with LDAP users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
