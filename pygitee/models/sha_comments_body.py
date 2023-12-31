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

class ShaCommentsBody(object):
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
        'body': 'str',
        'path': 'str',
        'position': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'body': 'body',
        'path': 'path',
        'position': 'position'
    }

    def __init__(self, access_token=None, body=None, path=None, position=None):  # noqa: E501
        """ShaCommentsBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._body = None
        self._path = None
        self._position = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.body = body
        if path is not None:
            self.path = path
        if position is not None:
            self.position = position

    @property
    def access_token(self):
        """Gets the access_token of this ShaCommentsBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this ShaCommentsBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ShaCommentsBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this ShaCommentsBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def body(self):
        """Gets the body of this ShaCommentsBody.  # noqa: E501

        评论的内容  # noqa: E501

        :return: The body of this ShaCommentsBody.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ShaCommentsBody.

        评论的内容  # noqa: E501

        :param body: The body of this ShaCommentsBody.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def path(self):
        """Gets the path of this ShaCommentsBody.  # noqa: E501

        文件的相对路径  # noqa: E501

        :return: The path of this ShaCommentsBody.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShaCommentsBody.

        文件的相对路径  # noqa: E501

        :param path: The path of this ShaCommentsBody.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def position(self):
        """Gets the position of this ShaCommentsBody.  # noqa: E501

        Diff的相对行数  # noqa: E501

        :return: The position of this ShaCommentsBody.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ShaCommentsBody.

        Diff的相对行数  # noqa: E501

        :param position: The position of this ShaCommentsBody.  # noqa: E501
        :type: int
        """

        self._position = position

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
        if issubclass(ShaCommentsBody, dict):
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
        if not isinstance(other, ShaCommentsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
