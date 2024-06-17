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


class AppDetail(object):
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
        'name': 'str',
        'logo_url': 'str',
        'display_order': 'int',
        'url': 'str',
        'redirect_url': 'str',
        'app_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'logo_url': 'logo_url',
        'display_order': 'display_order',
        'url': 'url',
        'redirect_url': 'redirect_url',
        'app_type': 'app_type'
    }

    def __init__(self, name=None, logo_url=None, display_order=None, url=None, redirect_url=None, app_type=None, _configuration=None):  # noqa: E501
        """AppDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._logo_url = None
        self._display_order = None
        self._url = None
        self._redirect_url = None
        self._app_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if logo_url is not None:
            self.logo_url = logo_url
        if display_order is not None:
            self.display_order = display_order
        if url is not None:
            self.url = url
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if app_type is not None:
            self.app_type = app_type

    @property
    def name(self):
        """Gets the name of this AppDetail.  # noqa: E501

        Manager  # noqa: E501

        :return: The name of this AppDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppDetail.

        Manager  # noqa: E501

        :param name: The name of this AppDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo_url(self):
        """Gets the logo_url of this AppDetail.  # noqa: E501

        <link to qTest application logo>  # noqa: E501

        :return: The logo_url of this AppDetail.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this AppDetail.

        <link to qTest application logo>  # noqa: E501

        :param logo_url: The logo_url of this AppDetail.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def display_order(self):
        """Gets the display_order of this AppDetail.  # noqa: E501

        Display order of qTest application  # noqa: E501

        :return: The display_order of this AppDetail.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this AppDetail.

        Display order of qTest application  # noqa: E501

        :param display_order: The display_order of this AppDetail.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def url(self):
        """Gets the url of this AppDetail.  # noqa: E501

        URL to qTest application  # noqa: E501

        :return: The url of this AppDetail.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AppDetail.

        URL to qTest application  # noqa: E501

        :param url: The url of this AppDetail.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def redirect_url(self):
        """Gets the redirect_url of this AppDetail.  # noqa: E501


        :return: The redirect_url of this AppDetail.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this AppDetail.


        :param redirect_url: The redirect_url of this AppDetail.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def app_type(self):
        """Gets the app_type of this AppDetail.  # noqa: E501


        :return: The app_type of this AppDetail.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AppDetail.


        :param app_type: The app_type of this AppDetail.  # noqa: E501
        :type: str
        """

        self._app_type = app_type

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
        if issubclass(AppDetail, dict):
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
        if not isinstance(other, AppDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppDetail):
            return True

        return self.to_dict() != other.to_dict()
