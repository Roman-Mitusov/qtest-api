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


class ProjectUpdateResource(object):
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
        'description': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'admin_ids': 'list[int]',
        'uuid': 'str',
        'template_id': 'int'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'admin_ids': 'admin_ids',
        'uuid': 'uuid',
        'template_id': 'template_id'
    }

    def __init__(self, links=None, id=None, name=None, description=None, start_date=None, end_date=None, admin_ids=None, uuid=None, template_id=None, _configuration=None):  # noqa: E501
        """ProjectUpdateResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._id = None
        self._name = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._admin_ids = None
        self._uuid = None
        self._template_id = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if admin_ids is not None:
            self.admin_ids = admin_ids
        if uuid is not None:
            self.uuid = uuid
        if template_id is not None:
            self.template_id = template_id

    @property
    def links(self):
        """Gets the links of this ProjectUpdateResource.  # noqa: E501


        :return: The links of this ProjectUpdateResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProjectUpdateResource.


        :param links: The links of this ProjectUpdateResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this ProjectUpdateResource.  # noqa: E501


        :return: The id of this ProjectUpdateResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectUpdateResource.


        :param id: The id of this ProjectUpdateResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectUpdateResource.  # noqa: E501

        Name of the Project  # noqa: E501

        :return: The name of this ProjectUpdateResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectUpdateResource.

        Name of the Project  # noqa: E501

        :param name: The name of this ProjectUpdateResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectUpdateResource.  # noqa: E501

        Description of the Project  # noqa: E501

        :return: The description of this ProjectUpdateResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectUpdateResource.

        Description of the Project  # noqa: E501

        :param description: The description of this ProjectUpdateResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def start_date(self):
        """Gets the start_date of this ProjectUpdateResource.  # noqa: E501

        Start date of the Project  # noqa: E501

        :return: The start_date of this ProjectUpdateResource.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ProjectUpdateResource.

        Start date of the Project  # noqa: E501

        :param start_date: The start_date of this ProjectUpdateResource.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ProjectUpdateResource.  # noqa: E501

        End date of the Project  # noqa: E501

        :return: The end_date of this ProjectUpdateResource.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProjectUpdateResource.

        End date of the Project  # noqa: E501

        :param end_date: The end_date of this ProjectUpdateResource.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def admin_ids(self):
        """Gets the admin_ids of this ProjectUpdateResource.  # noqa: E501

        Array of Assigned Admin user id  # noqa: E501

        :return: The admin_ids of this ProjectUpdateResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._admin_ids

    @admin_ids.setter
    def admin_ids(self, admin_ids):
        """Sets the admin_ids of this ProjectUpdateResource.

        Array of Assigned Admin user id  # noqa: E501

        :param admin_ids: The admin_ids of this ProjectUpdateResource.  # noqa: E501
        :type: list[int]
        """

        self._admin_ids = admin_ids

    @property
    def uuid(self):
        """Gets the uuid of this ProjectUpdateResource.  # noqa: E501

        UUID of the Project  # noqa: E501

        :return: The uuid of this ProjectUpdateResource.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ProjectUpdateResource.

        UUID of the Project  # noqa: E501

        :param uuid: The uuid of this ProjectUpdateResource.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def template_id(self):
        """Gets the template_id of this ProjectUpdateResource.  # noqa: E501

        Template id of this project  # noqa: E501

        :return: The template_id of this ProjectUpdateResource.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ProjectUpdateResource.

        Template id of this project  # noqa: E501

        :param template_id: The template_id of this ProjectUpdateResource.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

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
        if issubclass(ProjectUpdateResource, dict):
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
        if not isinstance(other, ProjectUpdateResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUpdateResource):
            return True

        return self.to_dict() != other.to_dict()
