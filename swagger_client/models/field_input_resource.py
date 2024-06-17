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


class FieldInputResource(object):
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
        'label': 'str',
        'required': 'bool',
        'order': 'int',
        'allowed_values': 'list[AllowedValueResource]',
        'multiple': 'bool',
        'data_type': 'int',
        'searchable': 'bool',
        'default_value': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'label': 'label',
        'required': 'required',
        'order': 'order',
        'allowed_values': 'allowed_values',
        'multiple': 'multiple',
        'data_type': 'data_type',
        'searchable': 'searchable',
        'default_value': 'default_value',
        'is_active': 'is_active'
    }

    def __init__(self, label=None, required=False, order=None, allowed_values=None, multiple=False, data_type=None, searchable=False, default_value=None, is_active=False, _configuration=None):  # noqa: E501
        """FieldInputResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._label = None
        self._required = None
        self._order = None
        self._allowed_values = None
        self._multiple = None
        self._data_type = None
        self._searchable = None
        self._default_value = None
        self._is_active = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if required is not None:
            self.required = required
        if order is not None:
            self.order = order
        if allowed_values is not None:
            self.allowed_values = allowed_values
        if multiple is not None:
            self.multiple = multiple
        if data_type is not None:
            self.data_type = data_type
        if searchable is not None:
            self.searchable = searchable
        if default_value is not None:
            self.default_value = default_value
        if is_active is not None:
            self.is_active = is_active

    @property
    def label(self):
        """Gets the label of this FieldInputResource.  # noqa: E501

        Label of the Field Setting  # noqa: E501

        :return: The label of this FieldInputResource.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FieldInputResource.

        Label of the Field Setting  # noqa: E501

        :param label: The label of this FieldInputResource.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def required(self):
        """Gets the required of this FieldInputResource.  # noqa: E501

        Is required or not  # noqa: E501

        :return: The required of this FieldInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this FieldInputResource.

        Is required or not  # noqa: E501

        :param required: The required of this FieldInputResource.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def order(self):
        """Gets the order of this FieldInputResource.  # noqa: E501

        Display order  # noqa: E501

        :return: The order of this FieldInputResource.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this FieldInputResource.

        Display order  # noqa: E501

        :param order: The order of this FieldInputResource.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def allowed_values(self):
        """Gets the allowed_values of this FieldInputResource.  # noqa: E501

        Allowed values  # noqa: E501

        :return: The allowed_values of this FieldInputResource.  # noqa: E501
        :rtype: list[AllowedValueResource]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this FieldInputResource.

        Allowed values  # noqa: E501

        :param allowed_values: The allowed_values of this FieldInputResource.  # noqa: E501
        :type: list[AllowedValueResource]
        """

        self._allowed_values = allowed_values

    @property
    def multiple(self):
        """Gets the multiple of this FieldInputResource.  # noqa: E501

        Is allowed multiple values  # noqa: E501

        :return: The multiple of this FieldInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this FieldInputResource.

        Is allowed multiple values  # noqa: E501

        :param multiple: The multiple of this FieldInputResource.  # noqa: E501
        :type: bool
        """

        self._multiple = multiple

    @property
    def data_type(self):
        """Gets the data_type of this FieldInputResource.  # noqa: E501

        Data type of the Field  # noqa: E501

        :return: The data_type of this FieldInputResource.  # noqa: E501
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FieldInputResource.

        Data type of the Field  # noqa: E501

        :param data_type: The data_type of this FieldInputResource.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                data_type is not None and data_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._data_type = data_type

    @property
    def searchable(self):
        """Gets the searchable of this FieldInputResource.  # noqa: E501

        Allowed full text search or not  # noqa: E501

        :return: The searchable of this FieldInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this FieldInputResource.

        Allowed full text search or not  # noqa: E501

        :param searchable: The searchable of this FieldInputResource.  # noqa: E501
        :type: bool
        """

        self._searchable = searchable

    @property
    def default_value(self):
        """Gets the default_value of this FieldInputResource.  # noqa: E501

        Default value of the Field  # noqa: E501

        :return: The default_value of this FieldInputResource.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldInputResource.

        Default value of the Field  # noqa: E501

        :param default_value: The default_value of this FieldInputResource.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def is_active(self):
        """Gets the is_active of this FieldInputResource.  # noqa: E501

        Is active or disabled  # noqa: E501

        :return: The is_active of this FieldInputResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this FieldInputResource.

        Is active or disabled  # noqa: E501

        :param is_active: The is_active of this FieldInputResource.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(FieldInputResource, dict):
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
        if not isinstance(other, FieldInputResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldInputResource):
            return True

        return self.to_dict() != other.to_dict()
