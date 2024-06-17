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


class ArtifactHistoryResource(object):
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
        'page': 'int',
        'page_size': 'int',
        'total': 'int',
        'items': 'list[HistoryResource]'
    }

    attribute_map = {
        'links': 'links',
        'page': 'page',
        'page_size': 'page_size',
        'total': 'total',
        'items': 'items'
    }

    def __init__(self, links=None, page=None, page_size=None, total=None, items=None, _configuration=None):  # noqa: E501
        """ArtifactHistoryResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._page = None
        self._page_size = None
        self._total = None
        self._items = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total
        if items is not None:
            self.items = items

    @property
    def links(self):
        """Gets the links of this ArtifactHistoryResource.  # noqa: E501


        :return: The links of this ArtifactHistoryResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ArtifactHistoryResource.


        :param links: The links of this ArtifactHistoryResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def page(self):
        """Gets the page of this ArtifactHistoryResource.  # noqa: E501

        Current page  # noqa: E501

        :return: The page of this ArtifactHistoryResource.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ArtifactHistoryResource.

        Current page  # noqa: E501

        :param page: The page of this ArtifactHistoryResource.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ArtifactHistoryResource.  # noqa: E501

        Current page size  # noqa: E501

        :return: The page_size of this ArtifactHistoryResource.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ArtifactHistoryResource.

        Current page size  # noqa: E501

        :param page_size: The page_size of this ArtifactHistoryResource.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this ArtifactHistoryResource.  # noqa: E501

        Total record found  # noqa: E501

        :return: The total of this ArtifactHistoryResource.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ArtifactHistoryResource.

        Total record found  # noqa: E501

        :param total: The total of this ArtifactHistoryResource.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def items(self):
        """Gets the items of this ArtifactHistoryResource.  # noqa: E501

        Data of records  # noqa: E501

        :return: The items of this ArtifactHistoryResource.  # noqa: E501
        :rtype: list[HistoryResource]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ArtifactHistoryResource.

        Data of records  # noqa: E501

        :param items: The items of this ArtifactHistoryResource.  # noqa: E501
        :type: list[HistoryResource]
        """

        self._items = items

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
        if issubclass(ArtifactHistoryResource, dict):
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
        if not isinstance(other, ArtifactHistoryResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArtifactHistoryResource):
            return True

        return self.to_dict() != other.to_dict()
