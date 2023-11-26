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

class RepoPushConfigBody(object):
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
        'author_email_suffix': 'str',
        'commit_message_regex': 'str',
        'except_manager': 'bool',
        'max_file_size': 'int',
        'restrict_author_email_suffix': 'bool',
        'restrict_commit_message': 'bool',
        'restrict_file_size': 'bool',
        'restrict_push_own_commit': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'author_email_suffix': 'author_email_suffix',
        'commit_message_regex': 'commit_message_regex',
        'except_manager': 'except_manager',
        'max_file_size': 'max_file_size',
        'restrict_author_email_suffix': 'restrict_author_email_suffix',
        'restrict_commit_message': 'restrict_commit_message',
        'restrict_file_size': 'restrict_file_size',
        'restrict_push_own_commit': 'restrict_push_own_commit'
    }

    def __init__(self, access_token=None, author_email_suffix=None, commit_message_regex=None, except_manager=None, max_file_size=None, restrict_author_email_suffix=None, restrict_commit_message=None, restrict_file_size=None, restrict_push_own_commit=None):  # noqa: E501
        """RepoPushConfigBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._author_email_suffix = None
        self._commit_message_regex = None
        self._except_manager = None
        self._max_file_size = None
        self._restrict_author_email_suffix = None
        self._restrict_commit_message = None
        self._restrict_file_size = None
        self._restrict_push_own_commit = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if author_email_suffix is not None:
            self.author_email_suffix = author_email_suffix
        if commit_message_regex is not None:
            self.commit_message_regex = commit_message_regex
        if except_manager is not None:
            self.except_manager = except_manager
        if max_file_size is not None:
            self.max_file_size = max_file_size
        if restrict_author_email_suffix is not None:
            self.restrict_author_email_suffix = restrict_author_email_suffix
        if restrict_commit_message is not None:
            self.restrict_commit_message = restrict_commit_message
        if restrict_file_size is not None:
            self.restrict_file_size = restrict_file_size
        if restrict_push_own_commit is not None:
            self.restrict_push_own_commit = restrict_push_own_commit

    @property
    def access_token(self):
        """Gets the access_token of this RepoPushConfigBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this RepoPushConfigBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this RepoPushConfigBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this RepoPushConfigBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def author_email_suffix(self):
        """Gets the author_email_suffix of this RepoPushConfigBody.  # noqa: E501

        指定邮箱域名的后缀  # noqa: E501

        :return: The author_email_suffix of this RepoPushConfigBody.  # noqa: E501
        :rtype: str
        """
        return self._author_email_suffix

    @author_email_suffix.setter
    def author_email_suffix(self, author_email_suffix):
        """Sets the author_email_suffix of this RepoPushConfigBody.

        指定邮箱域名的后缀  # noqa: E501

        :param author_email_suffix: The author_email_suffix of this RepoPushConfigBody.  # noqa: E501
        :type: str
        """

        self._author_email_suffix = author_email_suffix

    @property
    def commit_message_regex(self):
        """Gets the commit_message_regex of this RepoPushConfigBody.  # noqa: E501

        用于验证提交信息的正则表达式  # noqa: E501

        :return: The commit_message_regex of this RepoPushConfigBody.  # noqa: E501
        :rtype: str
        """
        return self._commit_message_regex

    @commit_message_regex.setter
    def commit_message_regex(self, commit_message_regex):
        """Sets the commit_message_regex of this RepoPushConfigBody.

        用于验证提交信息的正则表达式  # noqa: E501

        :param commit_message_regex: The commit_message_regex of this RepoPushConfigBody.  # noqa: E501
        :type: str
        """

        self._commit_message_regex = commit_message_regex

    @property
    def except_manager(self):
        """Gets the except_manager of this RepoPushConfigBody.  # noqa: E501

        仓库管理员不受上述规则限制  # noqa: E501

        :return: The except_manager of this RepoPushConfigBody.  # noqa: E501
        :rtype: bool
        """
        return self._except_manager

    @except_manager.setter
    def except_manager(self, except_manager):
        """Sets the except_manager of this RepoPushConfigBody.

        仓库管理员不受上述规则限制  # noqa: E501

        :param except_manager: The except_manager of this RepoPushConfigBody.  # noqa: E501
        :type: bool
        """

        self._except_manager = except_manager

    @property
    def max_file_size(self):
        """Gets the max_file_size of this RepoPushConfigBody.  # noqa: E501

        限制单文件大小（MB）  # noqa: E501

        :return: The max_file_size of this RepoPushConfigBody.  # noqa: E501
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        """Sets the max_file_size of this RepoPushConfigBody.

        限制单文件大小（MB）  # noqa: E501

        :param max_file_size: The max_file_size of this RepoPushConfigBody.  # noqa: E501
        :type: int
        """

        self._max_file_size = max_file_size

    @property
    def restrict_author_email_suffix(self):
        """Gets the restrict_author_email_suffix of this RepoPushConfigBody.  # noqa: E501

        启用只允许指定邮箱域名后缀的提交  # noqa: E501

        :return: The restrict_author_email_suffix of this RepoPushConfigBody.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_author_email_suffix

    @restrict_author_email_suffix.setter
    def restrict_author_email_suffix(self, restrict_author_email_suffix):
        """Sets the restrict_author_email_suffix of this RepoPushConfigBody.

        启用只允许指定邮箱域名后缀的提交  # noqa: E501

        :param restrict_author_email_suffix: The restrict_author_email_suffix of this RepoPushConfigBody.  # noqa: E501
        :type: bool
        """

        self._restrict_author_email_suffix = restrict_author_email_suffix

    @property
    def restrict_commit_message(self):
        """Gets the restrict_commit_message of this RepoPushConfigBody.  # noqa: E501

        启用提交信息正则表达式校验  # noqa: E501

        :return: The restrict_commit_message of this RepoPushConfigBody.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_commit_message

    @restrict_commit_message.setter
    def restrict_commit_message(self, restrict_commit_message):
        """Sets the restrict_commit_message of this RepoPushConfigBody.

        启用提交信息正则表达式校验  # noqa: E501

        :param restrict_commit_message: The restrict_commit_message of this RepoPushConfigBody.  # noqa: E501
        :type: bool
        """

        self._restrict_commit_message = restrict_commit_message

    @property
    def restrict_file_size(self):
        """Gets the restrict_file_size of this RepoPushConfigBody.  # noqa: E501

        启用限制单文件大小  # noqa: E501

        :return: The restrict_file_size of this RepoPushConfigBody.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_file_size

    @restrict_file_size.setter
    def restrict_file_size(self, restrict_file_size):
        """Sets the restrict_file_size of this RepoPushConfigBody.

        启用限制单文件大小  # noqa: E501

        :param restrict_file_size: The restrict_file_size of this RepoPushConfigBody.  # noqa: E501
        :type: bool
        """

        self._restrict_file_size = restrict_file_size

    @property
    def restrict_push_own_commit(self):
        """Gets the restrict_push_own_commit of this RepoPushConfigBody.  # noqa: E501

        启用只能推送自己的提交（所推送提交中的邮箱必须与推送者所设置的提交邮箱一致）  # noqa: E501

        :return: The restrict_push_own_commit of this RepoPushConfigBody.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_push_own_commit

    @restrict_push_own_commit.setter
    def restrict_push_own_commit(self, restrict_push_own_commit):
        """Sets the restrict_push_own_commit of this RepoPushConfigBody.

        启用只能推送自己的提交（所推送提交中的邮箱必须与推送者所设置的提交邮箱一致）  # noqa: E501

        :param restrict_push_own_commit: The restrict_push_own_commit of this RepoPushConfigBody.  # noqa: E501
        :type: bool
        """

        self._restrict_push_own_commit = restrict_push_own_commit

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
        if issubclass(RepoPushConfigBody, dict):
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
        if not isinstance(other, RepoPushConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
