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

class ContentsPathBody1(object):
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
        'author_email': 'str',
        'author_name': 'str',
        'branch': 'str',
        'committer_email': 'str',
        'committer_name': 'str',
        'content': 'str',
        'message': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'author_email': 'author[email]',
        'author_name': 'author[name]',
        'branch': 'branch',
        'committer_email': 'committer[email]',
        'committer_name': 'committer[name]',
        'content': 'content',
        'message': 'message'
    }

    def __init__(self, access_token=None, author_email=None, author_name=None, branch=None, committer_email=None, committer_name=None, content=None, message=None):  # noqa: E501
        """ContentsPathBody1 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._author_email = None
        self._author_name = None
        self._branch = None
        self._committer_email = None
        self._committer_name = None
        self._content = None
        self._message = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if author_email is not None:
            self.author_email = author_email
        if author_name is not None:
            self.author_name = author_name
        if branch is not None:
            self.branch = branch
        if committer_email is not None:
            self.committer_email = committer_email
        if committer_name is not None:
            self.committer_name = committer_name
        self.content = content
        self.message = message

    @property
    def access_token(self):
        """Gets the access_token of this ContentsPathBody1.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ContentsPathBody1.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this ContentsPathBody1.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def author_email(self):
        """Gets the author_email of this ContentsPathBody1.  # noqa: E501

        Author的邮箱，默认为当前用户的邮箱  # noqa: E501

        :return: The author_email of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """Sets the author_email of this ContentsPathBody1.

        Author的邮箱，默认为当前用户的邮箱  # noqa: E501

        :param author_email: The author_email of this ContentsPathBody1.  # noqa: E501
        :type: str
        """

        self._author_email = author_email

    @property
    def author_name(self):
        """Gets the author_name of this ContentsPathBody1.  # noqa: E501

        Author的名字，默认为当前用户的名字  # noqa: E501

        :return: The author_name of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this ContentsPathBody1.

        Author的名字，默认为当前用户的名字  # noqa: E501

        :param author_name: The author_name of this ContentsPathBody1.  # noqa: E501
        :type: str
        """

        self._author_name = author_name

    @property
    def branch(self):
        """Gets the branch of this ContentsPathBody1.  # noqa: E501

        分支名称。默认为仓库对默认分支  # noqa: E501

        :return: The branch of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this ContentsPathBody1.

        分支名称。默认为仓库对默认分支  # noqa: E501

        :param branch: The branch of this ContentsPathBody1.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def committer_email(self):
        """Gets the committer_email of this ContentsPathBody1.  # noqa: E501

        Committer的邮箱，默认为当前用户的邮箱  # noqa: E501

        :return: The committer_email of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        """Sets the committer_email of this ContentsPathBody1.

        Committer的邮箱，默认为当前用户的邮箱  # noqa: E501

        :param committer_email: The committer_email of this ContentsPathBody1.  # noqa: E501
        :type: str
        """

        self._committer_email = committer_email

    @property
    def committer_name(self):
        """Gets the committer_name of this ContentsPathBody1.  # noqa: E501

        Committer的名字，默认为当前用户的名字  # noqa: E501

        :return: The committer_name of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """Sets the committer_name of this ContentsPathBody1.

        Committer的名字，默认为当前用户的名字  # noqa: E501

        :param committer_name: The committer_name of this ContentsPathBody1.  # noqa: E501
        :type: str
        """

        self._committer_name = committer_name

    @property
    def content(self):
        """Gets the content of this ContentsPathBody1.  # noqa: E501

        文件内容, 要用 base64 编码  # noqa: E501

        :return: The content of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ContentsPathBody1.

        文件内容, 要用 base64 编码  # noqa: E501

        :param content: The content of this ContentsPathBody1.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def message(self):
        """Gets the message of this ContentsPathBody1.  # noqa: E501

        提交信息  # noqa: E501

        :return: The message of this ContentsPathBody1.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ContentsPathBody1.

        提交信息  # noqa: E501

        :param message: The message of this ContentsPathBody1.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if issubclass(ContentsPathBody1, dict):
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
        if not isinstance(other, ContentsPathBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
