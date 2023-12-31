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

class InlineResponse20014(object):
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
        'message_count': 'int',
        'notification_count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'message_count': 'message_count',
        'notification_count': 'notification_count',
        'total_count': 'total_count'
    }

    def __init__(self, message_count=None, notification_count=None, total_count=None):  # noqa: E501
        """InlineResponse20014 - a model defined in Swagger"""  # noqa: E501
        self._message_count = None
        self._notification_count = None
        self._total_count = None
        self.discriminator = None
        if message_count is not None:
            self.message_count = message_count
        if notification_count is not None:
            self.notification_count = notification_count
        if total_count is not None:
            self.total_count = total_count

    @property
    def message_count(self):
        """Gets the message_count of this InlineResponse20014.  # noqa: E501


        :return: The message_count of this InlineResponse20014.  # noqa: E501
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count):
        """Sets the message_count of this InlineResponse20014.


        :param message_count: The message_count of this InlineResponse20014.  # noqa: E501
        :type: int
        """

        self._message_count = message_count

    @property
    def notification_count(self):
        """Gets the notification_count of this InlineResponse20014.  # noqa: E501


        :return: The notification_count of this InlineResponse20014.  # noqa: E501
        :rtype: int
        """
        return self._notification_count

    @notification_count.setter
    def notification_count(self, notification_count):
        """Sets the notification_count of this InlineResponse20014.


        :param notification_count: The notification_count of this InlineResponse20014.  # noqa: E501
        :type: int
        """

        self._notification_count = notification_count

    @property
    def total_count(self):
        """Gets the total_count of this InlineResponse20014.  # noqa: E501


        :return: The total_count of this InlineResponse20014.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this InlineResponse20014.


        :param total_count: The total_count of this InlineResponse20014.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(InlineResponse20014, dict):
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
        if not isinstance(other, InlineResponse20014):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
