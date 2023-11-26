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

class NotificationsMessagesBody(object):
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
        'access_token': 'str',
        'ids': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'ids': 'ids'
    }

    def __init__(self, access_token=None, ids=None):  # noqa: E501
        """NotificationsMessagesBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._ids = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if ids is not None:
            self.ids = ids

    @property
    def access_token(self):
        """Gets the access_token of this NotificationsMessagesBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this NotificationsMessagesBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this NotificationsMessagesBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this NotificationsMessagesBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def ids(self):
        """Gets the ids of this NotificationsMessagesBody.  # noqa: E501

        指定一组私信 ID，以 , 分隔  # noqa: E501

        :return: The ids of this NotificationsMessagesBody.  # noqa: E501
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this NotificationsMessagesBody.

        指定一组私信 ID，以 , 分隔  # noqa: E501

        :param ids: The ids of this NotificationsMessagesBody.  # noqa: E501
        :type: str
        """

        self._ids = ids

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
        if issubclass(NotificationsMessagesBody, dict):
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
        if not isinstance(other, NotificationsMessagesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
