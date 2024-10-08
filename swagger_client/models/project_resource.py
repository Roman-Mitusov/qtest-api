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


class ProjectResource(object):
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
        'status_id': 'int',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'admins': 'list[str]',
        'admin_ids': 'list[int]',
        'sample': 'bool',
        'user_profile': 'UserProfile',
        'defect_tracking_systems': 'list[DefectTrackingSystem]',
        'x_explorer_access_level': 'int',
        'date_format': 'str',
        'automation': 'bool',
        'template_id': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status_id': 'status_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'admins': 'admins',
        'admin_ids': 'admin_ids',
        'sample': 'sample',
        'user_profile': 'user_profile',
        'defect_tracking_systems': 'defect_tracking_systems',
        'x_explorer_access_level': 'x_explorer_access_level',
        'date_format': 'date_format',
        'automation': 'automation',
        'template_id': 'template_id',
        'uuid': 'uuid'
    }

    def __init__(self, links=None, id=None, name=None, description=None, status_id=None, start_date=None, end_date=None, admins=None, admin_ids=None, sample=False, user_profile=None, defect_tracking_systems=None, x_explorer_access_level=None, date_format=None, automation=False, template_id=None, uuid=None, _configuration=None):  # noqa: E501
        """ProjectResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._id = None
        self._name = None
        self._description = None
        self._status_id = None
        self._start_date = None
        self._end_date = None
        self._admins = None
        self._admin_ids = None
        self._sample = None
        self._user_profile = None
        self._defect_tracking_systems = None
        self._x_explorer_access_level = None
        self._date_format = None
        self._automation = None
        self._template_id = None
        self._uuid = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status_id is not None:
            self.status_id = status_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if admins is not None:
            self.admins = admins
        if admin_ids is not None:
            self.admin_ids = admin_ids
        if sample is not None:
            self.sample = sample
        if user_profile is not None:
            self.user_profile = user_profile
        if defect_tracking_systems is not None:
            self.defect_tracking_systems = defect_tracking_systems
        if x_explorer_access_level is not None:
            self.x_explorer_access_level = x_explorer_access_level
        if date_format is not None:
            self.date_format = date_format
        if automation is not None:
            self.automation = automation
        if template_id is not None:
            self.template_id = template_id
        if uuid is not None:
            self.uuid = uuid

    @property
    def links(self):
        """Gets the links of this ProjectResource.  # noqa: E501


        :return: The links of this ProjectResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProjectResource.


        :param links: The links of this ProjectResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this ProjectResource.  # noqa: E501

        ID of the Project  # noqa: E501

        :return: The id of this ProjectResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectResource.

        ID of the Project  # noqa: E501

        :param id: The id of this ProjectResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectResource.  # noqa: E501

        Name of the Project  # noqa: E501

        :return: The name of this ProjectResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectResource.

        Name of the Project  # noqa: E501

        :param name: The name of this ProjectResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectResource.  # noqa: E501

        Description of the Project  # noqa: E501

        :return: The description of this ProjectResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectResource.

        Description of the Project  # noqa: E501

        :param description: The description of this ProjectResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status_id(self):
        """Gets the status_id of this ProjectResource.  # noqa: E501

        Status of the Project  # noqa: E501

        :return: The status_id of this ProjectResource.  # noqa: E501
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this ProjectResource.

        Status of the Project  # noqa: E501

        :param status_id: The status_id of this ProjectResource.  # noqa: E501
        :type: int
        """

        self._status_id = status_id

    @property
    def start_date(self):
        """Gets the start_date of this ProjectResource.  # noqa: E501

        Start date of the Project  # noqa: E501

        :return: The start_date of this ProjectResource.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ProjectResource.

        Start date of the Project  # noqa: E501

        :param start_date: The start_date of this ProjectResource.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ProjectResource.  # noqa: E501

        End date of the Project  # noqa: E501

        :return: The end_date of this ProjectResource.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProjectResource.

        End date of the Project  # noqa: E501

        :param end_date: The end_date of this ProjectResource.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def admins(self):
        """Gets the admins of this ProjectResource.  # noqa: E501

        Arrays of admin user  # noqa: E501

        :return: The admins of this ProjectResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this ProjectResource.

        Arrays of admin user  # noqa: E501

        :param admins: The admins of this ProjectResource.  # noqa: E501
        :type: list[str]
        """

        self._admins = admins

    @property
    def admin_ids(self):
        """Gets the admin_ids of this ProjectResource.  # noqa: E501


        :return: The admin_ids of this ProjectResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._admin_ids

    @admin_ids.setter
    def admin_ids(self, admin_ids):
        """Sets the admin_ids of this ProjectResource.


        :param admin_ids: The admin_ids of this ProjectResource.  # noqa: E501
        :type: list[int]
        """

        self._admin_ids = admin_ids

    @property
    def sample(self):
        """Gets the sample of this ProjectResource.  # noqa: E501

        Is sample or not  # noqa: E501

        :return: The sample of this ProjectResource.  # noqa: E501
        :rtype: bool
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this ProjectResource.

        Is sample or not  # noqa: E501

        :param sample: The sample of this ProjectResource.  # noqa: E501
        :type: bool
        """

        self._sample = sample

    @property
    def user_profile(self):
        """Gets the user_profile of this ProjectResource.  # noqa: E501


        :return: The user_profile of this ProjectResource.  # noqa: E501
        :rtype: UserProfile
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        """Sets the user_profile of this ProjectResource.


        :param user_profile: The user_profile of this ProjectResource.  # noqa: E501
        :type: UserProfile
        """

        self._user_profile = user_profile

    @property
    def defect_tracking_systems(self):
        """Gets the defect_tracking_systems of this ProjectResource.  # noqa: E501

        Arrays of External Defect Tracking Connection  # noqa: E501

        :return: The defect_tracking_systems of this ProjectResource.  # noqa: E501
        :rtype: list[DefectTrackingSystem]
        """
        return self._defect_tracking_systems

    @defect_tracking_systems.setter
    def defect_tracking_systems(self, defect_tracking_systems):
        """Sets the defect_tracking_systems of this ProjectResource.

        Arrays of External Defect Tracking Connection  # noqa: E501

        :param defect_tracking_systems: The defect_tracking_systems of this ProjectResource.  # noqa: E501
        :type: list[DefectTrackingSystem]
        """

        self._defect_tracking_systems = defect_tracking_systems

    @property
    def x_explorer_access_level(self):
        """Gets the x_explorer_access_level of this ProjectResource.  # noqa: E501

        Can access Explorer  # noqa: E501

        :return: The x_explorer_access_level of this ProjectResource.  # noqa: E501
        :rtype: int
        """
        return self._x_explorer_access_level

    @x_explorer_access_level.setter
    def x_explorer_access_level(self, x_explorer_access_level):
        """Sets the x_explorer_access_level of this ProjectResource.

        Can access Explorer  # noqa: E501

        :param x_explorer_access_level: The x_explorer_access_level of this ProjectResource.  # noqa: E501
        :type: int
        """

        self._x_explorer_access_level = x_explorer_access_level

    @property
    def date_format(self):
        """Gets the date_format of this ProjectResource.  # noqa: E501

        Client date time format  # noqa: E501

        :return: The date_format of this ProjectResource.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this ProjectResource.

        Client date time format  # noqa: E501

        :param date_format: The date_format of this ProjectResource.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def automation(self):
        """Gets the automation of this ProjectResource.  # noqa: E501

        Automation enabled or not  # noqa: E501

        :return: The automation of this ProjectResource.  # noqa: E501
        :rtype: bool
        """
        return self._automation

    @automation.setter
    def automation(self, automation):
        """Sets the automation of this ProjectResource.

        Automation enabled or not  # noqa: E501

        :param automation: The automation of this ProjectResource.  # noqa: E501
        :type: bool
        """

        self._automation = automation

    @property
    def template_id(self):
        """Gets the template_id of this ProjectResource.  # noqa: E501

        Template id of this project  # noqa: E501

        :return: The template_id of this ProjectResource.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ProjectResource.

        Template id of this project  # noqa: E501

        :param template_id: The template_id of this ProjectResource.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def uuid(self):
        """Gets the uuid of this ProjectResource.  # noqa: E501

        UUID of the Project  # noqa: E501

        :return: The uuid of this ProjectResource.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ProjectResource.

        UUID of the Project  # noqa: E501

        :param uuid: The uuid of this ProjectResource.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(ProjectResource, dict):
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
        if not isinstance(other, ProjectResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectResource):
            return True

        return self.to_dict() != other.to_dict()
