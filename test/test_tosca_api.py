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
from swagger_client.api.tosca_api import ToscaApi  # noqa: E501
from swagger_client.rest import ApiException


class TestToscaApi(unittest.TestCase):
    """ToscaApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tosca_api.ToscaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notify_test_event_import(self):
        """Test case for notify_test_event_import

        Import Tosca TestEvent objects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
