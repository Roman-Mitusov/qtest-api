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


class ProjectUsersProfile(object):
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
        'user_profile_id': 'int',
        'user_ids': 'list[int]'
    }

    attribute_map = {
        'user_profile_id': 'userProfileId',
        'user_ids': 'userIds'
    }

    def __init__(self, user_profile_id=None, user_ids=None, _configuration=None):  # noqa: E501
        """ProjectUsersProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_profile_id = None
        self._user_ids = None
        self.discriminator = None

        if user_profile_id is not None:
            self.user_profile_id = user_profile_id
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def user_profile_id(self):
        """Gets the user_profile_id of this ProjectUsersProfile.  # noqa: E501

        ID of user profile  # noqa: E501

        :return: The user_profile_id of this ProjectUsersProfile.  # noqa: E501
        :rtype: int
        """
        return self._user_profile_id

    @user_profile_id.setter
    def user_profile_id(self, user_profile_id):
        """Sets the user_profile_id of this ProjectUsersProfile.

        ID of user profile  # noqa: E501

        :param user_profile_id: The user_profile_id of this ProjectUsersProfile.  # noqa: E501
        :type: int
        """

        self._user_profile_id = user_profile_id

    @property
    def user_ids(self):
        """Gets the user_ids of this ProjectUsersProfile.  # noqa: E501

        Array User ID  # noqa: E501

        :return: The user_ids of this ProjectUsersProfile.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ProjectUsersProfile.

        Array User ID  # noqa: E501

        :param user_ids: The user_ids of this ProjectUsersProfile.  # noqa: E501
        :type: list[int]
        """

        self._user_ids = user_ids

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
        if issubclass(ProjectUsersProfile, dict):
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
        if not isinstance(other, ProjectUsersProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUsersProfile):
            return True

        return self.to_dict() != other.to_dict()
