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


class LinkedDefectResource(object):
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
        'external_defect_id': 'str',
        'connection_id': 'int',
        'external_project_id': 'str',
        'summary': 'str',
        'status': 'str',
        'pid': 'str',
        'web_url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'external_defect_id': 'external_defect_id',
        'connection_id': 'connection_id',
        'external_project_id': 'external_project_id',
        'summary': 'summary',
        'status': 'status',
        'pid': 'pid',
        'web_url': 'web_url',
        'description': 'description'
    }

    def __init__(self, links=None, id=None, external_defect_id=None, connection_id=None, external_project_id=None, summary=None, status=None, pid=None, web_url=None, description=None, _configuration=None):  # noqa: E501
        """LinkedDefectResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._id = None
        self._external_defect_id = None
        self._connection_id = None
        self._external_project_id = None
        self._summary = None
        self._status = None
        self._pid = None
        self._web_url = None
        self._description = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if external_defect_id is not None:
            self.external_defect_id = external_defect_id
        if connection_id is not None:
            self.connection_id = connection_id
        if external_project_id is not None:
            self.external_project_id = external_project_id
        if summary is not None:
            self.summary = summary
        if status is not None:
            self.status = status
        if pid is not None:
            self.pid = pid
        if web_url is not None:
            self.web_url = web_url
        if description is not None:
            self.description = description

    @property
    def links(self):
        """Gets the links of this LinkedDefectResource.  # noqa: E501


        :return: The links of this LinkedDefectResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LinkedDefectResource.


        :param links: The links of this LinkedDefectResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this LinkedDefectResource.  # noqa: E501

        ID of Defect  # noqa: E501

        :return: The id of this LinkedDefectResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LinkedDefectResource.

        ID of Defect  # noqa: E501

        :param id: The id of this LinkedDefectResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def external_defect_id(self):
        """Gets the external_defect_id of this LinkedDefectResource.  # noqa: E501

        External ID of Defect  # noqa: E501

        :return: The external_defect_id of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._external_defect_id

    @external_defect_id.setter
    def external_defect_id(self, external_defect_id):
        """Sets the external_defect_id of this LinkedDefectResource.

        External ID of Defect  # noqa: E501

        :param external_defect_id: The external_defect_id of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._external_defect_id = external_defect_id

    @property
    def connection_id(self):
        """Gets the connection_id of this LinkedDefectResource.  # noqa: E501

        ID of the external Integration Connection  # noqa: E501

        :return: The connection_id of this LinkedDefectResource.  # noqa: E501
        :rtype: int
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this LinkedDefectResource.

        ID of the external Integration Connection  # noqa: E501

        :param connection_id: The connection_id of this LinkedDefectResource.  # noqa: E501
        :type: int
        """

        self._connection_id = connection_id

    @property
    def external_project_id(self):
        """Gets the external_project_id of this LinkedDefectResource.  # noqa: E501

        ID of external Project  # noqa: E501

        :return: The external_project_id of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._external_project_id

    @external_project_id.setter
    def external_project_id(self, external_project_id):
        """Sets the external_project_id of this LinkedDefectResource.

        ID of external Project  # noqa: E501

        :param external_project_id: The external_project_id of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._external_project_id = external_project_id

    @property
    def summary(self):
        """Gets the summary of this LinkedDefectResource.  # noqa: E501

        Summary of external Defect  # noqa: E501

        :return: The summary of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this LinkedDefectResource.

        Summary of external Defect  # noqa: E501

        :param summary: The summary of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def status(self):
        """Gets the status of this LinkedDefectResource.  # noqa: E501

        Status of external Defect  # noqa: E501

        :return: The status of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LinkedDefectResource.

        Status of external Defect  # noqa: E501

        :param status: The status of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def pid(self):
        """Gets the pid of this LinkedDefectResource.  # noqa: E501

        PID of external Defect  # noqa: E501

        :return: The pid of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this LinkedDefectResource.

        PID of external Defect  # noqa: E501

        :param pid: The pid of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._pid = pid

    @property
    def web_url(self):
        """Gets the web_url of this LinkedDefectResource.  # noqa: E501

        Web url to external Defect  # noqa: E501

        :return: The web_url of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this LinkedDefectResource.

        Web url to external Defect  # noqa: E501

        :param web_url: The web_url of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def description(self):
        """Gets the description of this LinkedDefectResource.  # noqa: E501

        Description of external Defect  # noqa: E501

        :return: The description of this LinkedDefectResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LinkedDefectResource.

        Description of external Defect  # noqa: E501

        :param description: The description of this LinkedDefectResource.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(LinkedDefectResource, dict):
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
        if not isinstance(other, LinkedDefectResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkedDefectResource):
            return True

        return self.to_dict() != other.to_dict()
