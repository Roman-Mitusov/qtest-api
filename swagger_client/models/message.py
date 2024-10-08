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


class Message(object):
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
        'no_logging': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'no_logging': 'noLogging',
        'message': 'message'
    }

    def __init__(self, no_logging=False, message=None, _configuration=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._no_logging = None
        self._message = None
        self.discriminator = None

        if no_logging is not None:
            self.no_logging = no_logging
        if message is not None:
            self.message = message

    @property
    def no_logging(self):
        """Gets the no_logging of this Message.  # noqa: E501


        :return: The no_logging of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._no_logging

    @no_logging.setter
    def no_logging(self, no_logging):
        """Sets the no_logging of this Message.


        :param no_logging: The no_logging of this Message.  # noqa: E501
        :type: bool
        """

        self._no_logging = no_logging

    @property
    def message(self):
        """Gets the message of this Message.  # noqa: E501

        Error message text  # noqa: E501

        :return: The message of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Message.

        Error message text  # noqa: E501

        :param message: The message of this Message.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Message):
            return True

        return self.to_dict() != other.to_dict()
