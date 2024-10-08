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


class StatusResource(object):
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
        'links': 'list[Link]',
        'id': 'int',
        'name': 'str',
        'is_default': 'bool',
        'color': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'name': 'name',
        'is_default': 'is_default',
        'color': 'color',
        'active': 'active'
    }

    def __init__(self, links=None, id=None, name=None, is_default=False, color=None, active=False, _configuration=None):  # noqa: E501
        """StatusResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._id = None
        self._name = None
        self._is_default = None
        self._color = None
        self._active = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if color is not None:
            self.color = color
        if active is not None:
            self.active = active

    @property
    def links(self):
        """Gets the links of this StatusResource.  # noqa: E501

        Link to resource  # noqa: E501

        :return: The links of this StatusResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StatusResource.

        Link to resource  # noqa: E501

        :param links: The links of this StatusResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this StatusResource.  # noqa: E501

        ID of Test Run's status  # noqa: E501

        :return: The id of this StatusResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatusResource.

        ID of Test Run's status  # noqa: E501

        :param id: The id of this StatusResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StatusResource.  # noqa: E501

        Name of Test Run's status  # noqa: E501

        :return: The name of this StatusResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatusResource.

        Name of Test Run's status  # noqa: E501

        :param name: The name of this StatusResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this StatusResource.  # noqa: E501

        Is default or not  # noqa: E501

        :return: The is_default of this StatusResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this StatusResource.

        Is default or not  # noqa: E501

        :param is_default: The is_default of this StatusResource.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def color(self):
        """Gets the color of this StatusResource.  # noqa: E501

        Color of Test Run's status  # noqa: E501

        :return: The color of this StatusResource.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this StatusResource.

        Color of Test Run's status  # noqa: E501

        :param color: The color of this StatusResource.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def active(self):
        """Gets the active of this StatusResource.  # noqa: E501

        Active or not  # noqa: E501

        :return: The active of this StatusResource.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this StatusResource.

        Active or not  # noqa: E501

        :param active: The active of this StatusResource.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(StatusResource, dict):
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
        if not isinstance(other, StatusResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusResource):
            return True

        return self.to_dict() != other.to_dict()
