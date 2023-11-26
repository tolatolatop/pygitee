# coding: utf-8

"""
    Gitee OpenApi

    All api provided by Gitee  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20034(object):
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
        'commit': 'Commit',
        'content': 'Content'
    }

    attribute_map = {
        'commit': 'commit',
        'content': 'content'
    }

    def __init__(self, commit=None, content=None):  # noqa: E501
        """InlineResponse20034 - a model defined in Swagger"""  # noqa: E501
        self._commit = None
        self._content = None
        self.discriminator = None
        if commit is not None:
            self.commit = commit
        if content is not None:
            self.content = content

    @property
    def commit(self):
        """Gets the commit of this InlineResponse20034.  # noqa: E501


        :return: The commit of this InlineResponse20034.  # noqa: E501
        :rtype: Commit
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this InlineResponse20034.


        :param commit: The commit of this InlineResponse20034.  # noqa: E501
        :type: Commit
        """

        self._commit = commit

    @property
    def content(self):
        """Gets the content of this InlineResponse20034.  # noqa: E501


        :return: The content of this InlineResponse20034.  # noqa: E501
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse20034.


        :param content: The content of this InlineResponse20034.  # noqa: E501
        :type: Content
        """

        self._content = content

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
        if issubclass(InlineResponse20034, dict):
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
        if not isinstance(other, InlineResponse20034):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
