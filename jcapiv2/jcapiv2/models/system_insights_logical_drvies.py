# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SystemInsightsLogicalDrvies(object):
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
        'boot_partition': 'int',
        'collection_time': 'str',
        'device_id': 'str',
        'file_system': 'str',
        'free_space': 'str',
        'size': 'str',
        'system_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'boot_partition': 'boot_partition',
        'collection_time': 'collection_time',
        'device_id': 'device_id',
        'file_system': 'file_system',
        'free_space': 'free_space',
        'size': 'size',
        'system_id': 'system_id',
        'type': 'type'
    }

    def __init__(self, boot_partition=None, collection_time=None, device_id=None, file_system=None, free_space=None, size=None, system_id=None, type=None):  # noqa: E501
        """SystemInsightsLogicalDrvies - a model defined in Swagger"""  # noqa: E501

        self._boot_partition = None
        self._collection_time = None
        self._device_id = None
        self._file_system = None
        self._free_space = None
        self._size = None
        self._system_id = None
        self._type = None
        self.discriminator = None

        if boot_partition is not None:
            self.boot_partition = boot_partition
        if collection_time is not None:
            self.collection_time = collection_time
        if device_id is not None:
            self.device_id = device_id
        if file_system is not None:
            self.file_system = file_system
        if free_space is not None:
            self.free_space = free_space
        if size is not None:
            self.size = size
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type

    @property
    def boot_partition(self):
        """Gets the boot_partition of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The boot_partition of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: int
        """
        return self._boot_partition

    @boot_partition.setter
    def boot_partition(self, boot_partition):
        """Sets the boot_partition of this SystemInsightsLogicalDrvies.


        :param boot_partition: The boot_partition of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: int
        """

        self._boot_partition = boot_partition

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The collection_time of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsLogicalDrvies.


        :param collection_time: The collection_time of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def device_id(self):
        """Gets the device_id of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The device_id of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this SystemInsightsLogicalDrvies.


        :param device_id: The device_id of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def file_system(self):
        """Gets the file_system of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The file_system of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """Sets the file_system of this SystemInsightsLogicalDrvies.


        :param file_system: The file_system of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._file_system = file_system

    @property
    def free_space(self):
        """Gets the free_space of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The free_space of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._free_space

    @free_space.setter
    def free_space(self, free_space):
        """Sets the free_space of this SystemInsightsLogicalDrvies.


        :param free_space: The free_space of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._free_space = free_space

    @property
    def size(self):
        """Gets the size of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The size of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SystemInsightsLogicalDrvies.


        :param size: The size of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The system_id of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsLogicalDrvies.


        :param system_id: The system_id of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this SystemInsightsLogicalDrvies.  # noqa: E501


        :return: The type of this SystemInsightsLogicalDrvies.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsLogicalDrvies.


        :param type: The type of this SystemInsightsLogicalDrvies.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(SystemInsightsLogicalDrvies, dict):
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
        if not isinstance(other, SystemInsightsLogicalDrvies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
