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


class AutomationTestLogResource(object):
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
        'test_case_version_id': 'int',
        'exe_start_date': 'datetime',
        'exe_end_date': 'datetime',
        'note': 'str',
        'attachments': 'list[AttachmentResource]',
        'name': 'str',
        'planned_exe_time': 'int',
        'actual_exe_time': 'int',
        'build_number': 'str',
        'build_url': 'str',
        'properties': 'list[PropertyResource]',
        'automation_content': 'str',
        'system_name': 'str',
        'status': 'str',
        'order': 'int',
        'test_step_logs': 'list[AutomationTestStepLog]',
        'testcase_properties': 'list[PropertyResource]',
        'module_names': 'list[str]',
        'agent_ids': 'list[int]',
        'defect_pids': 'list[str]',
        'tosca_guid': 'str',
        'tosca_node_path': 'str',
        'tosca_state': 'str'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'test_case_version_id': 'test_case_version_id',
        'exe_start_date': 'exe_start_date',
        'exe_end_date': 'exe_end_date',
        'note': 'note',
        'attachments': 'attachments',
        'name': 'name',
        'planned_exe_time': 'planned_exe_time',
        'actual_exe_time': 'actual_exe_time',
        'build_number': 'build_number',
        'build_url': 'build_url',
        'properties': 'properties',
        'automation_content': 'automation_content',
        'system_name': 'system_name',
        'status': 'status',
        'order': 'order',
        'test_step_logs': 'test_step_logs',
        'testcase_properties': 'testcase_properties',
        'module_names': 'module_names',
        'agent_ids': 'agent_ids',
        'defect_pids': 'defect_pids',
        'tosca_guid': 'tosca_guid',
        'tosca_node_path': 'tosca_node_path',
        'tosca_state': 'tosca_state'
    }

    def __init__(self, links=None, id=None, test_case_version_id=None, exe_start_date=None, exe_end_date=None, note=None, attachments=None, name=None, planned_exe_time=None, actual_exe_time=None, build_number=None, build_url=None, properties=None, automation_content=None, system_name=None, status=None, order=None, test_step_logs=None, testcase_properties=None, module_names=None, agent_ids=None, defect_pids=None, tosca_guid=None, tosca_node_path=None, tosca_state=None, _configuration=None):  # noqa: E501
        """AutomationTestLogResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._id = None
        self._test_case_version_id = None
        self._exe_start_date = None
        self._exe_end_date = None
        self._note = None
        self._attachments = None
        self._name = None
        self._planned_exe_time = None
        self._actual_exe_time = None
        self._build_number = None
        self._build_url = None
        self._properties = None
        self._automation_content = None
        self._system_name = None
        self._status = None
        self._order = None
        self._test_step_logs = None
        self._testcase_properties = None
        self._module_names = None
        self._agent_ids = None
        self._defect_pids = None
        self._tosca_guid = None
        self._tosca_node_path = None
        self._tosca_state = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if test_case_version_id is not None:
            self.test_case_version_id = test_case_version_id
        self.exe_start_date = exe_start_date
        self.exe_end_date = exe_end_date
        if note is not None:
            self.note = note
        if attachments is not None:
            self.attachments = attachments
        if name is not None:
            self.name = name
        if planned_exe_time is not None:
            self.planned_exe_time = planned_exe_time
        if actual_exe_time is not None:
            self.actual_exe_time = actual_exe_time
        if build_number is not None:
            self.build_number = build_number
        if build_url is not None:
            self.build_url = build_url
        if properties is not None:
            self.properties = properties
        if automation_content is not None:
            self.automation_content = automation_content
        if system_name is not None:
            self.system_name = system_name
        if status is not None:
            self.status = status
        if order is not None:
            self.order = order
        if test_step_logs is not None:
            self.test_step_logs = test_step_logs
        if testcase_properties is not None:
            self.testcase_properties = testcase_properties
        if module_names is not None:
            self.module_names = module_names
        if agent_ids is not None:
            self.agent_ids = agent_ids
        if defect_pids is not None:
            self.defect_pids = defect_pids
        if tosca_guid is not None:
            self.tosca_guid = tosca_guid
        if tosca_node_path is not None:
            self.tosca_node_path = tosca_node_path
        if tosca_state is not None:
            self.tosca_state = tosca_state

    @property
    def links(self):
        """Gets the links of this AutomationTestLogResource.  # noqa: E501


        :return: The links of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AutomationTestLogResource.


        :param links: The links of this AutomationTestLogResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this AutomationTestLogResource.  # noqa: E501


        :return: The id of this AutomationTestLogResource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AutomationTestLogResource.


        :param id: The id of this AutomationTestLogResource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def test_case_version_id(self):
        """Gets the test_case_version_id of this AutomationTestLogResource.  # noqa: E501

        ID of the Test Case Version  # noqa: E501

        :return: The test_case_version_id of this AutomationTestLogResource.  # noqa: E501
        :rtype: int
        """
        return self._test_case_version_id

    @test_case_version_id.setter
    def test_case_version_id(self, test_case_version_id):
        """Sets the test_case_version_id of this AutomationTestLogResource.

        ID of the Test Case Version  # noqa: E501

        :param test_case_version_id: The test_case_version_id of this AutomationTestLogResource.  # noqa: E501
        :type: int
        """

        self._test_case_version_id = test_case_version_id

    @property
    def exe_start_date(self):
        """Gets the exe_start_date of this AutomationTestLogResource.  # noqa: E501

        Execution start date  # noqa: E501

        :return: The exe_start_date of this AutomationTestLogResource.  # noqa: E501
        :rtype: datetime
        """
        return self._exe_start_date

    @exe_start_date.setter
    def exe_start_date(self, exe_start_date):
        """Sets the exe_start_date of this AutomationTestLogResource.

        Execution start date  # noqa: E501

        :param exe_start_date: The exe_start_date of this AutomationTestLogResource.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and exe_start_date is None:
            raise ValueError("Invalid value for `exe_start_date`, must not be `None`")  # noqa: E501

        self._exe_start_date = exe_start_date

    @property
    def exe_end_date(self):
        """Gets the exe_end_date of this AutomationTestLogResource.  # noqa: E501

        Execution end date  # noqa: E501

        :return: The exe_end_date of this AutomationTestLogResource.  # noqa: E501
        :rtype: datetime
        """
        return self._exe_end_date

    @exe_end_date.setter
    def exe_end_date(self, exe_end_date):
        """Sets the exe_end_date of this AutomationTestLogResource.

        Execution end date  # noqa: E501

        :param exe_end_date: The exe_end_date of this AutomationTestLogResource.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and exe_end_date is None:
            raise ValueError("Invalid value for `exe_end_date`, must not be `None`")  # noqa: E501

        self._exe_end_date = exe_end_date

    @property
    def note(self):
        """Gets the note of this AutomationTestLogResource.  # noqa: E501

        Note  # noqa: E501

        :return: The note of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AutomationTestLogResource.

        Note  # noqa: E501

        :param note: The note of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def attachments(self):
        """Gets the attachments of this AutomationTestLogResource.  # noqa: E501

        Test Log attachments  # noqa: E501

        :return: The attachments of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[AttachmentResource]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this AutomationTestLogResource.

        Test Log attachments  # noqa: E501

        :param attachments: The attachments of this AutomationTestLogResource.  # noqa: E501
        :type: list[AttachmentResource]
        """

        self._attachments = attachments

    @property
    def name(self):
        """Gets the name of this AutomationTestLogResource.  # noqa: E501

        Test Run's name  # noqa: E501

        :return: The name of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutomationTestLogResource.

        Test Run's name  # noqa: E501

        :param name: The name of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def planned_exe_time(self):
        """Gets the planned_exe_time of this AutomationTestLogResource.  # noqa: E501


        :return: The planned_exe_time of this AutomationTestLogResource.  # noqa: E501
        :rtype: int
        """
        return self._planned_exe_time

    @planned_exe_time.setter
    def planned_exe_time(self, planned_exe_time):
        """Sets the planned_exe_time of this AutomationTestLogResource.


        :param planned_exe_time: The planned_exe_time of this AutomationTestLogResource.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                planned_exe_time is not None and planned_exe_time > 9999999):  # noqa: E501
            raise ValueError("Invalid value for `planned_exe_time`, must be a value less than or equal to `9999999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                planned_exe_time is not None and planned_exe_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `planned_exe_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._planned_exe_time = planned_exe_time

    @property
    def actual_exe_time(self):
        """Gets the actual_exe_time of this AutomationTestLogResource.  # noqa: E501


        :return: The actual_exe_time of this AutomationTestLogResource.  # noqa: E501
        :rtype: int
        """
        return self._actual_exe_time

    @actual_exe_time.setter
    def actual_exe_time(self, actual_exe_time):
        """Sets the actual_exe_time of this AutomationTestLogResource.


        :param actual_exe_time: The actual_exe_time of this AutomationTestLogResource.  # noqa: E501
        :type: int
        """

        self._actual_exe_time = actual_exe_time

    @property
    def build_number(self):
        """Gets the build_number of this AutomationTestLogResource.  # noqa: E501

        Jenkins jobs build number  # noqa: E501

        :return: The build_number of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this AutomationTestLogResource.

        Jenkins jobs build number  # noqa: E501

        :param build_number: The build_number of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._build_number = build_number

    @property
    def build_url(self):
        """Gets the build_url of this AutomationTestLogResource.  # noqa: E501

        Jenkins jobs build URL  # noqa: E501

        :return: The build_url of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._build_url

    @build_url.setter
    def build_url(self, build_url):
        """Sets the build_url of this AutomationTestLogResource.

        Jenkins jobs build URL  # noqa: E501

        :param build_url: The build_url of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._build_url = build_url

    @property
    def properties(self):
        """Gets the properties of this AutomationTestLogResource.  # noqa: E501


        :return: The properties of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AutomationTestLogResource.


        :param properties: The properties of this AutomationTestLogResource.  # noqa: E501
        :type: list[PropertyResource]
        """

        self._properties = properties

    @property
    def automation_content(self):
        """Gets the automation_content of this AutomationTestLogResource.  # noqa: E501

        Test Case's automation content  # noqa: E501

        :return: The automation_content of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._automation_content

    @automation_content.setter
    def automation_content(self, automation_content):
        """Sets the automation_content of this AutomationTestLogResource.

        Test Case's automation content  # noqa: E501

        :param automation_content: The automation_content of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._automation_content = automation_content

    @property
    def system_name(self):
        """Gets the system_name of this AutomationTestLogResource.  # noqa: E501


        :return: The system_name of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this AutomationTestLogResource.


        :param system_name: The system_name of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def status(self):
        """Gets the status of this AutomationTestLogResource.  # noqa: E501

        Test Log status  # noqa: E501

        :return: The status of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AutomationTestLogResource.

        Test Log status  # noqa: E501

        :param status: The status of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def order(self):
        """Gets the order of this AutomationTestLogResource.  # noqa: E501


        :return: The order of this AutomationTestLogResource.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AutomationTestLogResource.


        :param order: The order of this AutomationTestLogResource.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def test_step_logs(self):
        """Gets the test_step_logs of this AutomationTestLogResource.  # noqa: E501

        Arrays of Test Step Log  # noqa: E501

        :return: The test_step_logs of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[AutomationTestStepLog]
        """
        return self._test_step_logs

    @test_step_logs.setter
    def test_step_logs(self, test_step_logs):
        """Sets the test_step_logs of this AutomationTestLogResource.

        Arrays of Test Step Log  # noqa: E501

        :param test_step_logs: The test_step_logs of this AutomationTestLogResource.  # noqa: E501
        :type: list[AutomationTestStepLog]
        """

        self._test_step_logs = test_step_logs

    @property
    def testcase_properties(self):
        """Gets the testcase_properties of this AutomationTestLogResource.  # noqa: E501

        Arrays of Test case Properties  # noqa: E501

        :return: The testcase_properties of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[PropertyResource]
        """
        return self._testcase_properties

    @testcase_properties.setter
    def testcase_properties(self, testcase_properties):
        """Sets the testcase_properties of this AutomationTestLogResource.

        Arrays of Test case Properties  # noqa: E501

        :param testcase_properties: The testcase_properties of this AutomationTestLogResource.  # noqa: E501
        :type: list[PropertyResource]
        """

        self._testcase_properties = testcase_properties

    @property
    def module_names(self):
        """Gets the module_names of this AutomationTestLogResource.  # noqa: E501

        Arrays of Modules  # noqa: E501

        :return: The module_names of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._module_names

    @module_names.setter
    def module_names(self, module_names):
        """Sets the module_names of this AutomationTestLogResource.

        Arrays of Modules  # noqa: E501

        :param module_names: The module_names of this AutomationTestLogResource.  # noqa: E501
        :type: list[str]
        """

        self._module_names = module_names

    @property
    def agent_ids(self):
        """Gets the agent_ids of this AutomationTestLogResource.  # noqa: E501


        :return: The agent_ids of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """Sets the agent_ids of this AutomationTestLogResource.


        :param agent_ids: The agent_ids of this AutomationTestLogResource.  # noqa: E501
        :type: list[int]
        """

        self._agent_ids = agent_ids

    @property
    def defect_pids(self):
        """Gets the defect_pids of this AutomationTestLogResource.  # noqa: E501

        Defect pids  # noqa: E501

        :return: The defect_pids of this AutomationTestLogResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._defect_pids

    @defect_pids.setter
    def defect_pids(self, defect_pids):
        """Sets the defect_pids of this AutomationTestLogResource.

        Defect pids  # noqa: E501

        :param defect_pids: The defect_pids of this AutomationTestLogResource.  # noqa: E501
        :type: list[str]
        """

        self._defect_pids = defect_pids

    @property
    def tosca_guid(self):
        """Gets the tosca_guid of this AutomationTestLogResource.  # noqa: E501

        GUID of Tosca test case.  # noqa: E501

        :return: The tosca_guid of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._tosca_guid

    @tosca_guid.setter
    def tosca_guid(self, tosca_guid):
        """Sets the tosca_guid of this AutomationTestLogResource.

        GUID of Tosca test case.  # noqa: E501

        :param tosca_guid: The tosca_guid of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._tosca_guid = tosca_guid

    @property
    def tosca_node_path(self):
        """Gets the tosca_node_path of this AutomationTestLogResource.  # noqa: E501

        Node Path of Tosca test case.  # noqa: E501

        :return: The tosca_node_path of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._tosca_node_path

    @tosca_node_path.setter
    def tosca_node_path(self, tosca_node_path):
        """Sets the tosca_node_path of this AutomationTestLogResource.

        Node Path of Tosca test case.  # noqa: E501

        :param tosca_node_path: The tosca_node_path of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._tosca_node_path = tosca_node_path

    @property
    def tosca_state(self):
        """Gets the tosca_state of this AutomationTestLogResource.  # noqa: E501


        :return: The tosca_state of this AutomationTestLogResource.  # noqa: E501
        :rtype: str
        """
        return self._tosca_state

    @tosca_state.setter
    def tosca_state(self, tosca_state):
        """Sets the tosca_state of this AutomationTestLogResource.


        :param tosca_state: The tosca_state of this AutomationTestLogResource.  # noqa: E501
        :type: str
        """

        self._tosca_state = tosca_state

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
        if issubclass(AutomationTestLogResource, dict):
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
        if not isinstance(other, AutomationTestLogResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutomationTestLogResource):
            return True

        return self.to_dict() != other.to_dict()
