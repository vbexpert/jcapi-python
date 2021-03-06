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


class SystemInsightsUptime(object):
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
        'collection_time': 'str',
        'days': 'int',
        'hours': 'int',
        'minutes': 'int',
        'seconds': 'int',
        'system_id': 'str',
        'total_seconds': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'days': 'days',
        'hours': 'hours',
        'minutes': 'minutes',
        'seconds': 'seconds',
        'system_id': 'system_id',
        'total_seconds': 'total_seconds'
    }

    def __init__(self, collection_time=None, days=None, hours=None, minutes=None, seconds=None, system_id=None, total_seconds=None):  # noqa: E501
        """SystemInsightsUptime - a model defined in Swagger"""  # noqa: E501

        self._collection_time = None
        self._days = None
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._system_id = None
        self._total_seconds = None
        self.discriminator = None

        if collection_time is not None:
            self.collection_time = collection_time
        if days is not None:
            self.days = days
        if hours is not None:
            self.hours = hours
        if minutes is not None:
            self.minutes = minutes
        if seconds is not None:
            self.seconds = seconds
        if system_id is not None:
            self.system_id = system_id
        if total_seconds is not None:
            self.total_seconds = total_seconds

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsUptime.  # noqa: E501


        :return: The collection_time of this SystemInsightsUptime.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsUptime.


        :param collection_time: The collection_time of this SystemInsightsUptime.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def days(self):
        """Gets the days of this SystemInsightsUptime.  # noqa: E501


        :return: The days of this SystemInsightsUptime.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this SystemInsightsUptime.


        :param days: The days of this SystemInsightsUptime.  # noqa: E501
        :type: int
        """

        self._days = days

    @property
    def hours(self):
        """Gets the hours of this SystemInsightsUptime.  # noqa: E501


        :return: The hours of this SystemInsightsUptime.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this SystemInsightsUptime.


        :param hours: The hours of this SystemInsightsUptime.  # noqa: E501
        :type: int
        """

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this SystemInsightsUptime.  # noqa: E501


        :return: The minutes of this SystemInsightsUptime.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this SystemInsightsUptime.


        :param minutes: The minutes of this SystemInsightsUptime.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def seconds(self):
        """Gets the seconds of this SystemInsightsUptime.  # noqa: E501


        :return: The seconds of this SystemInsightsUptime.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this SystemInsightsUptime.


        :param seconds: The seconds of this SystemInsightsUptime.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsUptime.  # noqa: E501


        :return: The system_id of this SystemInsightsUptime.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsUptime.


        :param system_id: The system_id of this SystemInsightsUptime.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def total_seconds(self):
        """Gets the total_seconds of this SystemInsightsUptime.  # noqa: E501


        :return: The total_seconds of this SystemInsightsUptime.  # noqa: E501
        :rtype: str
        """
        return self._total_seconds

    @total_seconds.setter
    def total_seconds(self, total_seconds):
        """Sets the total_seconds of this SystemInsightsUptime.


        :param total_seconds: The total_seconds of this SystemInsightsUptime.  # noqa: E501
        :type: str
        """

        self._total_seconds = total_seconds

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
        if issubclass(SystemInsightsUptime, dict):
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
        if not isinstance(other, SystemInsightsUptime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
