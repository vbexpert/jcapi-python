# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SystemNetworkInterfaces(object):
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
        'address': 'str',
        'family': 'str',
        'internal': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'address': 'address',
        'family': 'family',
        'internal': 'internal',
        'name': 'name'
    }

    def __init__(self, address=None, family=None, internal=None, name=None):  # noqa: E501
        """SystemNetworkInterfaces - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._family = None
        self._internal = None
        self._name = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if family is not None:
            self.family = family
        if internal is not None:
            self.internal = internal
        if name is not None:
            self.name = name

    @property
    def address(self):
        """Gets the address of this SystemNetworkInterfaces.  # noqa: E501


        :return: The address of this SystemNetworkInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SystemNetworkInterfaces.


        :param address: The address of this SystemNetworkInterfaces.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def family(self):
        """Gets the family of this SystemNetworkInterfaces.  # noqa: E501


        :return: The family of this SystemNetworkInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this SystemNetworkInterfaces.


        :param family: The family of this SystemNetworkInterfaces.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def internal(self):
        """Gets the internal of this SystemNetworkInterfaces.  # noqa: E501


        :return: The internal of this SystemNetworkInterfaces.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this SystemNetworkInterfaces.


        :param internal: The internal of this SystemNetworkInterfaces.  # noqa: E501
        :type: bool
        """

        self._internal = internal

    @property
    def name(self):
        """Gets the name of this SystemNetworkInterfaces.  # noqa: E501


        :return: The name of this SystemNetworkInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemNetworkInterfaces.


        :param name: The name of this SystemNetworkInterfaces.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SystemNetworkInterfaces, dict):
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
        if not isinstance(other, SystemNetworkInterfaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
