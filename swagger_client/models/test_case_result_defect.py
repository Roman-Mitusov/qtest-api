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


class TestCaseResultDefect(object):
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
        'id': 'int',
        'client_id': 'int',
        'project_id': 'int',
        'result_id': 'int',
        'defect_id': 'int',
        'external_issue_id': 'str',
        'external_issue_unique_id': 'str',
        'external_issue_status': 'str',
        'external_issue_resolution': 'str',
        'external_issue_type': 'str',
        'external_issue_summary': 'str',
        'external_issue_url': 'str',
        'integration_connection_id': 'int',
        'external_project_id': 'str',
        'result_type': 'int',
        'defect': 'Defect',
        'test_case_id': 'int',
        'test_case_run_id': 'int',
        'test_case_version_id': 'int',
        'deleted': 'bool',
        'internal_defect': 'bool',
        'long_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'client_id': 'clientId',
        'project_id': 'projectId',
        'result_id': 'resultId',
        'defect_id': 'defectId',
        'external_issue_id': 'externalIssueId',
        'external_issue_unique_id': 'externalIssueUniqueId',
        'external_issue_status': 'externalIssueStatus',
        'external_issue_resolution': 'externalIssueResolution',
        'external_issue_type': 'externalIssueType',
        'external_issue_summary': 'externalIssueSummary',
        'external_issue_url': 'externalIssueUrl',
        'integration_connection_id': 'integrationConnectionId',
        'external_project_id': 'externalProjectId',
        'result_type': 'resultType',
        'defect': 'defect',
        'test_case_id': 'testCaseId',
        'test_case_run_id': 'testCaseRunId',
        'test_case_version_id': 'testCaseVersionId',
        'deleted': 'deleted',
        'internal_defect': 'internalDefect',
        'long_id': 'longId'
    }

    def __init__(self, id=None, client_id=None, project_id=None, result_id=None, defect_id=None, external_issue_id=None, external_issue_unique_id=None, external_issue_status=None, external_issue_resolution=None, external_issue_type=None, external_issue_summary=None, external_issue_url=None, integration_connection_id=None, external_project_id=None, result_type=None, defect=None, test_case_id=None, test_case_run_id=None, test_case_version_id=None, deleted=False, internal_defect=False, long_id=None, _configuration=None):  # noqa: E501
        """TestCaseResultDefect - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._client_id = None
        self._project_id = None
        self._result_id = None
        self._defect_id = None
        self._external_issue_id = None
        self._external_issue_unique_id = None
        self._external_issue_status = None
        self._external_issue_resolution = None
        self._external_issue_type = None
        self._external_issue_summary = None
        self._external_issue_url = None
        self._integration_connection_id = None
        self._external_project_id = None
        self._result_type = None
        self._defect = None
        self._test_case_id = None
        self._test_case_run_id = None
        self._test_case_version_id = None
        self._deleted = None
        self._internal_defect = None
        self._long_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if client_id is not None:
            self.client_id = client_id
        if project_id is not None:
            self.project_id = project_id
        if result_id is not None:
            self.result_id = result_id
        if defect_id is not None:
            self.defect_id = defect_id
        if external_issue_id is not None:
            self.external_issue_id = external_issue_id
        if external_issue_unique_id is not None:
            self.external_issue_unique_id = external_issue_unique_id
        if external_issue_status is not None:
            self.external_issue_status = external_issue_status
        if external_issue_resolution is not None:
            self.external_issue_resolution = external_issue_resolution
        if external_issue_type is not None:
            self.external_issue_type = external_issue_type
        if external_issue_summary is not None:
            self.external_issue_summary = external_issue_summary
        if external_issue_url is not None:
            self.external_issue_url = external_issue_url
        if integration_connection_id is not None:
            self.integration_connection_id = integration_connection_id
        if external_project_id is not None:
            self.external_project_id = external_project_id
        if result_type is not None:
            self.result_type = result_type
        if defect is not None:
            self.defect = defect
        if test_case_id is not None:
            self.test_case_id = test_case_id
        if test_case_run_id is not None:
            self.test_case_run_id = test_case_run_id
        if test_case_version_id is not None:
            self.test_case_version_id = test_case_version_id
        if deleted is not None:
            self.deleted = deleted
        if internal_defect is not None:
            self.internal_defect = internal_defect
        if long_id is not None:
            self.long_id = long_id

    @property
    def id(self):
        """Gets the id of this TestCaseResultDefect.  # noqa: E501


        :return: The id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestCaseResultDefect.


        :param id: The id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def client_id(self):
        """Gets the client_id of this TestCaseResultDefect.  # noqa: E501


        :return: The client_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this TestCaseResultDefect.


        :param client_id: The client_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def project_id(self):
        """Gets the project_id of this TestCaseResultDefect.  # noqa: E501


        :return: The project_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TestCaseResultDefect.


        :param project_id: The project_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def result_id(self):
        """Gets the result_id of this TestCaseResultDefect.  # noqa: E501


        :return: The result_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this TestCaseResultDefect.


        :param result_id: The result_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._result_id = result_id

    @property
    def defect_id(self):
        """Gets the defect_id of this TestCaseResultDefect.  # noqa: E501


        :return: The defect_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._defect_id

    @defect_id.setter
    def defect_id(self, defect_id):
        """Sets the defect_id of this TestCaseResultDefect.


        :param defect_id: The defect_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._defect_id = defect_id

    @property
    def external_issue_id(self):
        """Gets the external_issue_id of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_id

    @external_issue_id.setter
    def external_issue_id(self, external_issue_id):
        """Sets the external_issue_id of this TestCaseResultDefect.


        :param external_issue_id: The external_issue_id of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_id = external_issue_id

    @property
    def external_issue_unique_id(self):
        """Gets the external_issue_unique_id of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_unique_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_unique_id

    @external_issue_unique_id.setter
    def external_issue_unique_id(self, external_issue_unique_id):
        """Sets the external_issue_unique_id of this TestCaseResultDefect.


        :param external_issue_unique_id: The external_issue_unique_id of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_unique_id = external_issue_unique_id

    @property
    def external_issue_status(self):
        """Gets the external_issue_status of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_status of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_status

    @external_issue_status.setter
    def external_issue_status(self, external_issue_status):
        """Sets the external_issue_status of this TestCaseResultDefect.


        :param external_issue_status: The external_issue_status of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_status = external_issue_status

    @property
    def external_issue_resolution(self):
        """Gets the external_issue_resolution of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_resolution of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_resolution

    @external_issue_resolution.setter
    def external_issue_resolution(self, external_issue_resolution):
        """Sets the external_issue_resolution of this TestCaseResultDefect.


        :param external_issue_resolution: The external_issue_resolution of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_resolution = external_issue_resolution

    @property
    def external_issue_type(self):
        """Gets the external_issue_type of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_type of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_type

    @external_issue_type.setter
    def external_issue_type(self, external_issue_type):
        """Sets the external_issue_type of this TestCaseResultDefect.


        :param external_issue_type: The external_issue_type of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_type = external_issue_type

    @property
    def external_issue_summary(self):
        """Gets the external_issue_summary of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_summary of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_summary

    @external_issue_summary.setter
    def external_issue_summary(self, external_issue_summary):
        """Sets the external_issue_summary of this TestCaseResultDefect.


        :param external_issue_summary: The external_issue_summary of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_summary = external_issue_summary

    @property
    def external_issue_url(self):
        """Gets the external_issue_url of this TestCaseResultDefect.  # noqa: E501


        :return: The external_issue_url of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_issue_url

    @external_issue_url.setter
    def external_issue_url(self, external_issue_url):
        """Sets the external_issue_url of this TestCaseResultDefect.


        :param external_issue_url: The external_issue_url of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_issue_url = external_issue_url

    @property
    def integration_connection_id(self):
        """Gets the integration_connection_id of this TestCaseResultDefect.  # noqa: E501


        :return: The integration_connection_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._integration_connection_id

    @integration_connection_id.setter
    def integration_connection_id(self, integration_connection_id):
        """Sets the integration_connection_id of this TestCaseResultDefect.


        :param integration_connection_id: The integration_connection_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._integration_connection_id = integration_connection_id

    @property
    def external_project_id(self):
        """Gets the external_project_id of this TestCaseResultDefect.  # noqa: E501


        :return: The external_project_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: str
        """
        return self._external_project_id

    @external_project_id.setter
    def external_project_id(self, external_project_id):
        """Sets the external_project_id of this TestCaseResultDefect.


        :param external_project_id: The external_project_id of this TestCaseResultDefect.  # noqa: E501
        :type: str
        """

        self._external_project_id = external_project_id

    @property
    def result_type(self):
        """Gets the result_type of this TestCaseResultDefect.  # noqa: E501


        :return: The result_type of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this TestCaseResultDefect.


        :param result_type: The result_type of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._result_type = result_type

    @property
    def defect(self):
        """Gets the defect of this TestCaseResultDefect.  # noqa: E501


        :return: The defect of this TestCaseResultDefect.  # noqa: E501
        :rtype: Defect
        """
        return self._defect

    @defect.setter
    def defect(self, defect):
        """Sets the defect of this TestCaseResultDefect.


        :param defect: The defect of this TestCaseResultDefect.  # noqa: E501
        :type: Defect
        """

        self._defect = defect

    @property
    def test_case_id(self):
        """Gets the test_case_id of this TestCaseResultDefect.  # noqa: E501


        :return: The test_case_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._test_case_id

    @test_case_id.setter
    def test_case_id(self, test_case_id):
        """Sets the test_case_id of this TestCaseResultDefect.


        :param test_case_id: The test_case_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._test_case_id = test_case_id

    @property
    def test_case_run_id(self):
        """Gets the test_case_run_id of this TestCaseResultDefect.  # noqa: E501


        :return: The test_case_run_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._test_case_run_id

    @test_case_run_id.setter
    def test_case_run_id(self, test_case_run_id):
        """Sets the test_case_run_id of this TestCaseResultDefect.


        :param test_case_run_id: The test_case_run_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._test_case_run_id = test_case_run_id

    @property
    def test_case_version_id(self):
        """Gets the test_case_version_id of this TestCaseResultDefect.  # noqa: E501


        :return: The test_case_version_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._test_case_version_id

    @test_case_version_id.setter
    def test_case_version_id(self, test_case_version_id):
        """Sets the test_case_version_id of this TestCaseResultDefect.


        :param test_case_version_id: The test_case_version_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._test_case_version_id = test_case_version_id

    @property
    def deleted(self):
        """Gets the deleted of this TestCaseResultDefect.  # noqa: E501


        :return: The deleted of this TestCaseResultDefect.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TestCaseResultDefect.


        :param deleted: The deleted of this TestCaseResultDefect.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def internal_defect(self):
        """Gets the internal_defect of this TestCaseResultDefect.  # noqa: E501


        :return: The internal_defect of this TestCaseResultDefect.  # noqa: E501
        :rtype: bool
        """
        return self._internal_defect

    @internal_defect.setter
    def internal_defect(self, internal_defect):
        """Sets the internal_defect of this TestCaseResultDefect.


        :param internal_defect: The internal_defect of this TestCaseResultDefect.  # noqa: E501
        :type: bool
        """

        self._internal_defect = internal_defect

    @property
    def long_id(self):
        """Gets the long_id of this TestCaseResultDefect.  # noqa: E501


        :return: The long_id of this TestCaseResultDefect.  # noqa: E501
        :rtype: int
        """
        return self._long_id

    @long_id.setter
    def long_id(self, long_id):
        """Sets the long_id of this TestCaseResultDefect.


        :param long_id: The long_id of this TestCaseResultDefect.  # noqa: E501
        :type: int
        """

        self._long_id = long_id

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
        if issubclass(TestCaseResultDefect, dict):
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
        if not isinstance(other, TestCaseResultDefect):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestCaseResultDefect):
            return True

        return self.to_dict() != other.to_dict()
