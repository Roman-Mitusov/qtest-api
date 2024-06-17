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


class IntegrationAutoFillMappingVM(object):
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
        'external_project_id': 'str',
        'external_type_id': 'str',
        'send_attachment_to_jira': 'str',
        'configures': 'list[AutoFillConfigurationVM]'
    }

    attribute_map = {
        'external_project_id': 'externalProjectId',
        'external_type_id': 'externalTypeId',
        'send_attachment_to_jira': 'sendAttachmentToJira',
        'configures': 'configures'
    }

    def __init__(self, external_project_id=None, external_type_id=None, send_attachment_to_jira=None, configures=None, _configuration=None):  # noqa: E501
        """IntegrationAutoFillMappingVM - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_project_id = None
        self._external_type_id = None
        self._send_attachment_to_jira = None
        self._configures = None
        self.discriminator = None

        if external_project_id is not None:
            self.external_project_id = external_project_id
        if external_type_id is not None:
            self.external_type_id = external_type_id
        if send_attachment_to_jira is not None:
            self.send_attachment_to_jira = send_attachment_to_jira
        if configures is not None:
            self.configures = configures

    @property
    def external_project_id(self):
        """Gets the external_project_id of this IntegrationAutoFillMappingVM.  # noqa: E501


        :return: The external_project_id of this IntegrationAutoFillMappingVM.  # noqa: E501
        :rtype: str
        """
        return self._external_project_id

    @external_project_id.setter
    def external_project_id(self, external_project_id):
        """Sets the external_project_id of this IntegrationAutoFillMappingVM.


        :param external_project_id: The external_project_id of this IntegrationAutoFillMappingVM.  # noqa: E501
        :type: str
        """

        self._external_project_id = external_project_id

    @property
    def external_type_id(self):
        """Gets the external_type_id of this IntegrationAutoFillMappingVM.  # noqa: E501


        :return: The external_type_id of this IntegrationAutoFillMappingVM.  # noqa: E501
        :rtype: str
        """
        return self._external_type_id

    @external_type_id.setter
    def external_type_id(self, external_type_id):
        """Sets the external_type_id of this IntegrationAutoFillMappingVM.


        :param external_type_id: The external_type_id of this IntegrationAutoFillMappingVM.  # noqa: E501
        :type: str
        """

        self._external_type_id = external_type_id

    @property
    def send_attachment_to_jira(self):
        """Gets the send_attachment_to_jira of this IntegrationAutoFillMappingVM.  # noqa: E501


        :return: The send_attachment_to_jira of this IntegrationAutoFillMappingVM.  # noqa: E501
        :rtype: str
        """
        return self._send_attachment_to_jira

    @send_attachment_to_jira.setter
    def send_attachment_to_jira(self, send_attachment_to_jira):
        """Sets the send_attachment_to_jira of this IntegrationAutoFillMappingVM.


        :param send_attachment_to_jira: The send_attachment_to_jira of this IntegrationAutoFillMappingVM.  # noqa: E501
        :type: str
        """

        self._send_attachment_to_jira = send_attachment_to_jira

    @property
    def configures(self):
        """Gets the configures of this IntegrationAutoFillMappingVM.  # noqa: E501


        :return: The configures of this IntegrationAutoFillMappingVM.  # noqa: E501
        :rtype: list[AutoFillConfigurationVM]
        """
        return self._configures

    @configures.setter
    def configures(self, configures):
        """Sets the configures of this IntegrationAutoFillMappingVM.


        :param configures: The configures of this IntegrationAutoFillMappingVM.  # noqa: E501
        :type: list[AutoFillConfigurationVM]
        """

        self._configures = configures

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
        if issubclass(IntegrationAutoFillMappingVM, dict):
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
        if not isinstance(other, IntegrationAutoFillMappingVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationAutoFillMappingVM):
            return True

        return self.to_dict() != other.to_dict()
