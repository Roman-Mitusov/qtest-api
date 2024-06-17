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


class AllowedValueInputResource(object):
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
        'default': 'bool',
        'value': 'int',
        'label': 'str',
        'order': 'int',
        'is_default': 'bool',
        'is_active': 'bool',
        'color': 'str'
    }

    attribute_map = {
        'default': 'default',
        'value': 'value',
        'label': 'label',
        'order': 'order',
        'is_default': 'is_default',
        'is_active': 'is_active',
        'color': 'color'
    }

    def __init__(self, default=False, value=None, label=None, order=None, is_default=False, is_active=False, color=None, _configuration=None):  # noqa: E501
        """AllowedValueInputResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default = None
        self._value = None
        self._label = None
        self._order = None
        self._is_default = None
        self._is_active = None
        self._color = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if value is not None:
            self.value = value
        if label is not None:
            self.label = label
        if order is not None:
            self.order = order
        if is_default is not None:
            self.is_default = is_default
        if is_active is not None:
            self.is_active = is_active
        if color is not None:
            self.color = color

    @property
    def default(self):
        """Gets the default of this AllowedValueInputResource.  # noqa: E501


        :return: The default of this AllowedValueInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AllowedValueInputResource.


        :param default: The default of this AllowedValueInputResource.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def value(self):
        """Gets the value of this AllowedValueInputResource.  # noqa: E501


        :return: The value of this AllowedValueInputResource.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AllowedValueInputResource.


        :param value: The value of this AllowedValueInputResource.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def label(self):
        """Gets the label of this AllowedValueInputResource.  # noqa: E501


        :return: The label of this AllowedValueInputResource.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AllowedValueInputResource.


        :param label: The label of this AllowedValueInputResource.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def order(self):
        """Gets the order of this AllowedValueInputResource.  # noqa: E501


        :return: The order of this AllowedValueInputResource.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AllowedValueInputResource.


        :param order: The order of this AllowedValueInputResource.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def is_default(self):
        """Gets the is_default of this AllowedValueInputResource.  # noqa: E501


        :return: The is_default of this AllowedValueInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AllowedValueInputResource.


        :param is_default: The is_default of this AllowedValueInputResource.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_active(self):
        """Gets the is_active of this AllowedValueInputResource.  # noqa: E501


        :return: The is_active of this AllowedValueInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AllowedValueInputResource.


        :param is_active: The is_active of this AllowedValueInputResource.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def color(self):
        """Gets the color of this AllowedValueInputResource.  # noqa: E501


        :return: The color of this AllowedValueInputResource.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AllowedValueInputResource.


        :param color: The color of this AllowedValueInputResource.  # noqa: E501
        :type: str
        """

        self._color = color

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
        if issubclass(AllowedValueInputResource, dict):
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
        if not isinstance(other, AllowedValueInputResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllowedValueInputResource):
            return True

        return self.to_dict() != other.to_dict()
