# coding: utf-8

"""
    JumpCloud Directory API

    Allow cusotmers to manage the JumpCloud Directory objects, groupings and mappings.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, valid=None, config=None):
        """
        PolicyTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'valid': 'PolicyTemplateValid',
            'config': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'valid': 'valid',
            'config': 'config'
        }

        self._id = id
        self._name = name
        self._description = description
        self._valid = valid
        self._config = config

    @property
    def id(self):
        """
        Gets the id of this PolicyTemplate.
        ObjectId uniquely indetifying a Policy Template.

        :return: The id of this PolicyTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PolicyTemplate.
        ObjectId uniquely indetifying a Policy Template.

        :param id: The id of this PolicyTemplate.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PolicyTemplate.
        The default display name for the Policy.

        :return: The name of this PolicyTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyTemplate.
        The default display name for the Policy.

        :param name: The name of this PolicyTemplate.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PolicyTemplate.
        The default description for the Policy.

        :return: The description of this PolicyTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PolicyTemplate.
        The default description for the Policy.

        :param description: The description of this PolicyTemplate.
        :type: str
        """

        self._description = description

    @property
    def valid(self):
        """
        Gets the valid of this PolicyTemplate.

        :return: The valid of this PolicyTemplate.
        :rtype: PolicyTemplateValid
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this PolicyTemplate.

        :param valid: The valid of this PolicyTemplate.
        :type: PolicyTemplateValid
        """

        self._valid = valid

    @property
    def config(self):
        """
        Gets the config of this PolicyTemplate.
        The dynamic config options for this particular policy template. Works like the Application Template configuration.

        :return: The config of this PolicyTemplate.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this PolicyTemplate.
        The dynamic config options for this particular policy template. Works like the Application Template configuration.

        :param config: The config of this PolicyTemplate.
        :type: object
        """

        self._config = config

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PolicyTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other