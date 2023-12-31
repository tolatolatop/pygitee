# coding: utf-8

"""
    Gitee OpenApi

    All api provided by Gitee  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20026(object):
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
        'links': 'str',
        'commit': 'str',
        'name': 'str',
        'protected': 'str',
        'protection_url': 'str'
    }

    attribute_map = {
        'links': '_links',
        'commit': 'commit',
        'name': 'name',
        'protected': 'protected',
        'protection_url': 'protection_url'
    }

    def __init__(self, links=None, commit=None, name=None, protected=None, protection_url=None):  # noqa: E501
        """InlineResponse20026 - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._commit = None
        self._name = None
        self._protected = None
        self._protection_url = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if commit is not None:
            self.commit = commit
        if name is not None:
            self.name = name
        if protected is not None:
            self.protected = protected
        if protection_url is not None:
            self.protection_url = protection_url

    @property
    def links(self):
        """Gets the links of this InlineResponse20026.  # noqa: E501


        :return: The links of this InlineResponse20026.  # noqa: E501
        :rtype: str
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InlineResponse20026.


        :param links: The links of this InlineResponse20026.  # noqa: E501
        :type: str
        """

        self._links = links

    @property
    def commit(self):
        """Gets the commit of this InlineResponse20026.  # noqa: E501


        :return: The commit of this InlineResponse20026.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this InlineResponse20026.


        :param commit: The commit of this InlineResponse20026.  # noqa: E501
        :type: str
        """

        self._commit = commit

    @property
    def name(self):
        """Gets the name of this InlineResponse20026.  # noqa: E501


        :return: The name of this InlineResponse20026.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20026.


        :param name: The name of this InlineResponse20026.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protected(self):
        """Gets the protected of this InlineResponse20026.  # noqa: E501


        :return: The protected of this InlineResponse20026.  # noqa: E501
        :rtype: str
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this InlineResponse20026.


        :param protected: The protected of this InlineResponse20026.  # noqa: E501
        :type: str
        """

        self._protected = protected

    @property
    def protection_url(self):
        """Gets the protection_url of this InlineResponse20026.  # noqa: E501


        :return: The protection_url of this InlineResponse20026.  # noqa: E501
        :rtype: str
        """
        return self._protection_url

    @protection_url.setter
    def protection_url(self, protection_url):
        """Sets the protection_url of this InlineResponse20026.


        :param protection_url: The protection_url of this InlineResponse20026.  # noqa: E501
        :type: str
        """

        self._protection_url = protection_url

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
        if issubclass(InlineResponse20026, dict):
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
        if not isinstance(other, InlineResponse20026):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
