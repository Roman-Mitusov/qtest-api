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


class DefectResource(object):
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
        'properties': 'list[PropertyResource]',
        'attachments': 'list[AttachmentResource]',
        'id': 'int',
        'pid': 'str',
        'submitted_date': 'datetime',
        'last_modified_date': 'datetime',
        'submitter_id': 'int',
        'last_modified_user_id': 'int',
        'web_url': 'str'
    }

    attribute_map = {
        'links': 'links',
        'properties': 'properties',
        'attachments': 'attachments',
        'id': 'id',
        'pid': 'pid',
        'submitted_date': 'submitted_date',
        'last_modified_date': 'last_modified_date',
        'submitter_id': 'submitter_id',
        'last_modified_user_id': 'last_modified_user_id',
        'web_url': 'web_url'
    }

    def __init__(self, links=None, properties=None, attachments=None, id=None, pid=None, submitted_date=None, last_modified_date=None, submitter_id=None, last_modified_user_id=None, web_url=None, _configuration=None):  # noqa: E501
        """DefectResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._properties = None
        self._attachments = None
        self._id = None
        self._pid = None
        self._submitted_date = None
        self._last_modified_date = None
        self._submitter_id = None
        self._last_modified_user_id = None
        self._web_url = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if properties is not None:
            self.properties = properties
        if attachments is not None:
            self.attachments = attachments
        if id is not None:
            self.id = id
        if pid is not None:
            self.pid = pid
        if submitted_date is not None:
            self.submitted_date = submitted_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if submitter_id is not None:
            self.submitter_id = submitter_id
        if last_modified_user_id is not None:
            self.last_modified_user_id = last_modified_user_id
        if web_url is not None:
            self.web_url = web_url

    @property
    def links(self):
        """Gets the links of this DefectResource.  # noqa: E501


        :return: The links of this DefectResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DefectResource.


        :param links: The links of this DefectResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def properties(self):
        """Gets the properties of this DefectResource.  # noqa: E501

        Properties of the Defect  # noqa: E501

        :return: The properties of this DefectResource.  # noqa: E501
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DefectResource.

        Properties of the Defect  # noqa: E501

        :param properties: The properties of this DefectResource.  # noqa: E501
        :type: list[PropertyResource]
        """

        self._properties = properties

    @property
    def attachments(self):
        """Gets the attachments of this DefectResource.  # noqa: E501

        Attachments of the Defect  # noqa: E501

        :return: The attachments of this DefectResource.  # noqa: E501
        :rtype: list[AttachmentResource]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this DefectResource.

        Attachments of the Defect  # noqa: E501

        :param attachments: The attachments of this DefectResource.  # noqa: E501
        :type: list[AttachmentResource]
        """

        self._attachments = attachments

    @property
    def id(self):
        """Gets the id of this DefectResource.  # noqa: E501

        ID of the Defect  # noqa: E501

        :return: The id of this DefectResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DefectResource.

        ID of the Defect  # noqa: E501

        :param id: The id of this DefectResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pid(self):
        """Gets the pid of this DefectResource.  # noqa: E501

        PID of the Defect  # noqa: E501

        :return: The pid of this DefectResource.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this DefectResource.

        PID of the Defect  # noqa: E501

        :param pid: The pid of this DefectResource.  # noqa: E501
        :type: str
        """

        self._pid = pid

    @property
    def submitted_date(self):
        """Gets the submitted_date of this DefectResource.  # noqa: E501

        The date Defect was created  # noqa: E501

        :return: The submitted_date of this DefectResource.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """Sets the submitted_date of this DefectResource.

        The date Defect was created  # noqa: E501

        :param submitted_date: The submitted_date of this DefectResource.  # noqa: E501
        :type: datetime
        """

        self._submitted_date = submitted_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this DefectResource.  # noqa: E501

        Last modified date  # noqa: E501

        :return: The last_modified_date of this DefectResource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this DefectResource.

        Last modified date  # noqa: E501

        :param last_modified_date: The last_modified_date of this DefectResource.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def submitter_id(self):
        """Gets the submitter_id of this DefectResource.  # noqa: E501

        ID of the User who create the Defect  # noqa: E501

        :return: The submitter_id of this DefectResource.  # noqa: E501
        :rtype: int
        """
        return self._submitter_id

    @submitter_id.setter
    def submitter_id(self, submitter_id):
        """Sets the submitter_id of this DefectResource.

        ID of the User who create the Defect  # noqa: E501

        :param submitter_id: The submitter_id of this DefectResource.  # noqa: E501
        :type: int
        """

        self._submitter_id = submitter_id

    @property
    def last_modified_user_id(self):
        """Gets the last_modified_user_id of this DefectResource.  # noqa: E501

        Last ID of the User who updated the Defect  # noqa: E501

        :return: The last_modified_user_id of this DefectResource.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_user_id

    @last_modified_user_id.setter
    def last_modified_user_id(self, last_modified_user_id):
        """Sets the last_modified_user_id of this DefectResource.

        Last ID of the User who updated the Defect  # noqa: E501

        :param last_modified_user_id: The last_modified_user_id of this DefectResource.  # noqa: E501
        :type: int
        """

        self._last_modified_user_id = last_modified_user_id

    @property
    def web_url(self):
        """Gets the web_url of this DefectResource.  # noqa: E501

        Web url to the Defect  # noqa: E501

        :return: The web_url of this DefectResource.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this DefectResource.

        Web url to the Defect  # noqa: E501

        :param web_url: The web_url of this DefectResource.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

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
        if issubclass(DefectResource, dict):
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
        if not isinstance(other, DefectResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefectResource):
            return True

        return self.to_dict() != other.to_dict()
