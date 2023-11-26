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

class SettingNewBody(object):
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
        'merger': 'str',
        'mode': 'str',
        'pusher': 'str',
        'wildcard': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'merger': 'merger',
        'mode': 'mode',
        'pusher': 'pusher',
        'wildcard': 'wildcard'
    }

    def __init__(self, access_token=None, merger=None, mode=None, pusher=None, wildcard=None):  # noqa: E501
        """SettingNewBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._merger = None
        self._mode = None
        self._pusher = None
        self._wildcard = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.merger = merger
        self.mode = mode
        self.pusher = pusher
        self.wildcard = wildcard

    @property
    def access_token(self):
        """Gets the access_token of this SettingNewBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this SettingNewBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SettingNewBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this SettingNewBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def merger(self):
        """Gets the merger of this SettingNewBody.  # noqa: E501

        可合并 Pull Request 成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开）  # noqa: E501

        :return: The merger of this SettingNewBody.  # noqa: E501
        :rtype: str
        """
        return self._merger

    @merger.setter
    def merger(self, merger):
        """Sets the merger of this SettingNewBody.

        可合并 Pull Request 成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开）  # noqa: E501

        :param merger: The merger of this SettingNewBody.  # noqa: E501
        :type: str
        """
        if merger is None:
            raise ValueError("Invalid value for `merger`, must not be `None`")  # noqa: E501

        self._merger = merger

    @property
    def mode(self):
        """Gets the mode of this SettingNewBody.  # noqa: E501

        模式。standard: 标准模式, review: 评审模式  # noqa: E501

        :return: The mode of this SettingNewBody.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this SettingNewBody.

        模式。standard: 标准模式, review: 评审模式  # noqa: E501

        :param mode: The mode of this SettingNewBody.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def pusher(self):
        """Gets the pusher of this SettingNewBody.  # noqa: E501

        可推送代码成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开）  # noqa: E501

        :return: The pusher of this SettingNewBody.  # noqa: E501
        :rtype: str
        """
        return self._pusher

    @pusher.setter
    def pusher(self, pusher):
        """Sets the pusher of this SettingNewBody.

        可推送代码成员。developer：仓库管理员和开发者；admin：仓库管理员；none：禁止任何人合并; 用户：个人的地址 path（多个用户用 ';' 隔开）  # noqa: E501

        :param pusher: The pusher of this SettingNewBody.  # noqa: E501
        :type: str
        """
        if pusher is None:
            raise ValueError("Invalid value for `pusher`, must not be `None`")  # noqa: E501

        self._pusher = pusher

    @property
    def wildcard(self):
        """Gets the wildcard of this SettingNewBody.  # noqa: E501

        分支/通配符  # noqa: E501

        :return: The wildcard of this SettingNewBody.  # noqa: E501
        :rtype: str
        """
        return self._wildcard

    @wildcard.setter
    def wildcard(self, wildcard):
        """Sets the wildcard of this SettingNewBody.

        分支/通配符  # noqa: E501

        :param wildcard: The wildcard of this SettingNewBody.  # noqa: E501
        :type: str
        """
        if wildcard is None:
            raise ValueError("Invalid value for `wildcard`, must not be `None`")  # noqa: E501

        self._wildcard = wildcard

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
        if issubclass(SettingNewBody, dict):
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
        if not isinstance(other, SettingNewBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
