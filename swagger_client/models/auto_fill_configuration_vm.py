# coding: utf-8

"""
    qTest Manager API Version 11.0.0 - 2023.6

    qTest Manager API Version 11.0.0 - 2023.6  # noqa: E501

    OpenAPI spec version: 11.0.0 - 2023.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class AutoFillConfigurationVM(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_field_id': 'str',
        'q_test_field_ids': 'str'
    }

    attribute_map = {
        'external_field_id': 'externalFieldId',
        'q_test_field_ids': 'qTestFieldIds'
    }

    def __init__(self, external_field_id=None, q_test_field_ids=None, _configuration=None):  # noqa: E501
        """AutoFillConfigurationVM - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_field_id = None
        self._q_test_field_ids = None
        self.discriminator = None

        if external_field_id is not None:
            self.external_field_id = external_field_id
        if q_test_field_ids is not None:
            self.q_test_field_ids = q_test_field_ids

    @property
    def external_field_id(self):
        """Gets the external_field_id of this AutoFillConfigurationVM.  # noqa: E501


        :return: The external_field_id of this AutoFillConfigurationVM.  # noqa: E501
        :rtype: str
        """
        return self._external_field_id

    @external_field_id.setter
    def external_field_id(self, external_field_id):
        """Sets the external_field_id of this AutoFillConfigurationVM.


        :param external_field_id: The external_field_id of this AutoFillConfigurationVM.  # noqa: E501
        :type: str
        """

        self._external_field_id = external_field_id

    @property
    def q_test_field_ids(self):
        """Gets the q_test_field_ids of this AutoFillConfigurationVM.  # noqa: E501


        :return: The q_test_field_ids of this AutoFillConfigurationVM.  # noqa: E501
        :rtype: str
        """
        return self._q_test_field_ids

    @q_test_field_ids.setter
    def q_test_field_ids(self, q_test_field_ids):
        """Sets the q_test_field_ids of this AutoFillConfigurationVM.


        :param q_test_field_ids: The q_test_field_ids of this AutoFillConfigurationVM.  # noqa: E501
        :type: str
        """

        self._q_test_field_ids = q_test_field_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AutoFillConfigurationVM, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoFillConfigurationVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoFillConfigurationVM):
            return True

        return self.to_dict() != other.to_dict()
