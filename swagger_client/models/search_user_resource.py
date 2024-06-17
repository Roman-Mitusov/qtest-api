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


class SearchUserResource(object):
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
        'username': 'str',
        'email': 'str',
        'password': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'status': 'int',
        'avatar': 'str',
        'ldap_username': 'str',
        'user_group_ids': 'list[int]',
        'send_activation_email': 'bool',
        'external_auth_config_id': 'int',
        'external_user_name': 'str',
        'include_default_groups': 'bool',
        'assigned_projects': 'list[int]'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'username': 'username',
        'email': 'email',
        'password': 'password',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'status': 'status',
        'avatar': 'avatar',
        'ldap_username': 'ldap_username',
        'user_group_ids': 'user_group_ids',
        'send_activation_email': 'send_activation_email',
        'external_auth_config_id': 'external_auth_config_id',
        'external_user_name': 'external_user_name',
        'include_default_groups': 'include_default_groups',
        'assigned_projects': 'assigned_projects'
    }

    def __init__(self, links=None, id=None, username=None, email=None, password=None, first_name=None, last_name=None, status=None, avatar=None, ldap_username=None, user_group_ids=None, send_activation_email=False, external_auth_config_id=None, external_user_name=None, include_default_groups=False, assigned_projects=None, _configuration=None):  # noqa: E501
        """SearchUserResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._id = None
        self._username = None
        self._email = None
        self._password = None
        self._first_name = None
        self._last_name = None
        self._status = None
        self._avatar = None
        self._ldap_username = None
        self._user_group_ids = None
        self._send_activation_email = None
        self._external_auth_config_id = None
        self._external_user_name = None
        self._include_default_groups = None
        self._assigned_projects = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if status is not None:
            self.status = status
        if avatar is not None:
            self.avatar = avatar
        if ldap_username is not None:
            self.ldap_username = ldap_username
        if user_group_ids is not None:
            self.user_group_ids = user_group_ids
        if send_activation_email is not None:
            self.send_activation_email = send_activation_email
        if external_auth_config_id is not None:
            self.external_auth_config_id = external_auth_config_id
        if external_user_name is not None:
            self.external_user_name = external_user_name
        if include_default_groups is not None:
            self.include_default_groups = include_default_groups
        if assigned_projects is not None:
            self.assigned_projects = assigned_projects

    @property
    def links(self):
        """Gets the links of this SearchUserResource.  # noqa: E501

        Link to resource  # noqa: E501

        :return: The links of this SearchUserResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SearchUserResource.

        Link to resource  # noqa: E501

        :param links: The links of this SearchUserResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this SearchUserResource.  # noqa: E501

        ID of the User  # noqa: E501

        :return: The id of this SearchUserResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchUserResource.

        ID of the User  # noqa: E501

        :param id: The id of this SearchUserResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this SearchUserResource.  # noqa: E501

        Login username of the User  # noqa: E501

        :return: The username of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SearchUserResource.

        Login username of the User  # noqa: E501

        :param username: The username of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this SearchUserResource.  # noqa: E501

        Contact email of the User  # noqa: E501

        :return: The email of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SearchUserResource.

        Contact email of the User  # noqa: E501

        :param email: The email of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this SearchUserResource.  # noqa: E501


        :return: The password of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SearchUserResource.


        :param password: The password of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def first_name(self):
        """Gets the first_name of this SearchUserResource.  # noqa: E501

        First name of the User  # noqa: E501

        :return: The first_name of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SearchUserResource.

        First name of the User  # noqa: E501

        :param first_name: The first_name of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SearchUserResource.  # noqa: E501

        Last name of the User  # noqa: E501

        :return: The last_name of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SearchUserResource.

        Last name of the User  # noqa: E501

        :param last_name: The last_name of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def status(self):
        """Gets the status of this SearchUserResource.  # noqa: E501

        Status of the User  # noqa: E501

        :return: The status of this SearchUserResource.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchUserResource.

        Status of the User  # noqa: E501

        :param status: The status of this SearchUserResource.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def avatar(self):
        """Gets the avatar of this SearchUserResource.  # noqa: E501

        Avatar URL of the User  # noqa: E501

        :return: The avatar of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this SearchUserResource.

        Avatar URL of the User  # noqa: E501

        :param avatar: The avatar of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def ldap_username(self):
        """Gets the ldap_username of this SearchUserResource.  # noqa: E501

        LDAP username  # noqa: E501

        :return: The ldap_username of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._ldap_username

    @ldap_username.setter
    def ldap_username(self, ldap_username):
        """Sets the ldap_username of this SearchUserResource.

        LDAP username  # noqa: E501

        :param ldap_username: The ldap_username of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._ldap_username = ldap_username

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this SearchUserResource.  # noqa: E501


        :return: The user_group_ids of this SearchUserResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this SearchUserResource.


        :param user_group_ids: The user_group_ids of this SearchUserResource.  # noqa: E501
        :type: list[int]
        """

        self._user_group_ids = user_group_ids

    @property
    def send_activation_email(self):
        """Gets the send_activation_email of this SearchUserResource.  # noqa: E501


        :return: The send_activation_email of this SearchUserResource.  # noqa: E501
        :rtype: bool
        """
        return self._send_activation_email

    @send_activation_email.setter
    def send_activation_email(self, send_activation_email):
        """Sets the send_activation_email of this SearchUserResource.


        :param send_activation_email: The send_activation_email of this SearchUserResource.  # noqa: E501
        :type: bool
        """

        self._send_activation_email = send_activation_email

    @property
    def external_auth_config_id(self):
        """Gets the external_auth_config_id of this SearchUserResource.  # noqa: E501


        :return: The external_auth_config_id of this SearchUserResource.  # noqa: E501
        :rtype: int
        """
        return self._external_auth_config_id

    @external_auth_config_id.setter
    def external_auth_config_id(self, external_auth_config_id):
        """Sets the external_auth_config_id of this SearchUserResource.


        :param external_auth_config_id: The external_auth_config_id of this SearchUserResource.  # noqa: E501
        :type: int
        """

        self._external_auth_config_id = external_auth_config_id

    @property
    def external_user_name(self):
        """Gets the external_user_name of this SearchUserResource.  # noqa: E501


        :return: The external_user_name of this SearchUserResource.  # noqa: E501
        :rtype: str
        """
        return self._external_user_name

    @external_user_name.setter
    def external_user_name(self, external_user_name):
        """Sets the external_user_name of this SearchUserResource.


        :param external_user_name: The external_user_name of this SearchUserResource.  # noqa: E501
        :type: str
        """

        self._external_user_name = external_user_name

    @property
    def include_default_groups(self):
        """Gets the include_default_groups of this SearchUserResource.  # noqa: E501


        :return: The include_default_groups of this SearchUserResource.  # noqa: E501
        :rtype: bool
        """
        return self._include_default_groups

    @include_default_groups.setter
    def include_default_groups(self, include_default_groups):
        """Sets the include_default_groups of this SearchUserResource.


        :param include_default_groups: The include_default_groups of this SearchUserResource.  # noqa: E501
        :type: bool
        """

        self._include_default_groups = include_default_groups

    @property
    def assigned_projects(self):
        """Gets the assigned_projects of this SearchUserResource.  # noqa: E501

        Arrays of Project that user assigned to  # noqa: E501

        :return: The assigned_projects of this SearchUserResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._assigned_projects

    @assigned_projects.setter
    def assigned_projects(self, assigned_projects):
        """Sets the assigned_projects of this SearchUserResource.

        Arrays of Project that user assigned to  # noqa: E501

        :param assigned_projects: The assigned_projects of this SearchUserResource.  # noqa: E501
        :type: list[int]
        """

        self._assigned_projects = assigned_projects

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
        if issubclass(SearchUserResource, dict):
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
        if not isinstance(other, SearchUserResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchUserResource):
            return True

        return self.to_dict() != other.to_dict()
