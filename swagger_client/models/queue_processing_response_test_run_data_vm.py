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


class QueueProcessingResponseTestRunDataVM(object):
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
        'id': 'int',
        'type': 'str',
        'state': 'str',
        'content_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'state': 'state',
        'content_type': 'contentType',
        'content': 'content'
    }

    def __init__(self, id=None, type=None, state=None, content_type=None, content=None, _configuration=None):  # noqa: E501
        """QueueProcessingResponseTestRunDataVM - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._state = None
        self._content_type = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if content_type is not None:
            self.content_type = content_type
        if content is not None:
            self.content = content

    @property
    def id(self):
        """Gets the id of this QueueProcessingResponseTestRunDataVM.  # noqa: E501


        :return: The id of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueueProcessingResponseTestRunDataVM.


        :param id: The id of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this QueueProcessingResponseTestRunDataVM.  # noqa: E501


        :return: The type of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueueProcessingResponseTestRunDataVM.


        :param type: The type of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def state(self):
        """Gets the state of this QueueProcessingResponseTestRunDataVM.  # noqa: E501


        :return: The state of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this QueueProcessingResponseTestRunDataVM.


        :param state: The state of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def content_type(self):
        """Gets the content_type of this QueueProcessingResponseTestRunDataVM.  # noqa: E501


        :return: The content_type of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this QueueProcessingResponseTestRunDataVM.


        :param content_type: The content_type of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this QueueProcessingResponseTestRunDataVM.  # noqa: E501


        :return: The content of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this QueueProcessingResponseTestRunDataVM.


        :param content: The content of this QueueProcessingResponseTestRunDataVM.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if issubclass(QueueProcessingResponseTestRunDataVM, dict):
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
        if not isinstance(other, QueueProcessingResponseTestRunDataVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueueProcessingResponseTestRunDataVM):
            return True

        return self.to_dict() != other.to_dict()
