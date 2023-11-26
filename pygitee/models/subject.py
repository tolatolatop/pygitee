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

class Subject(object):
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
        'latest_comment_url': 'str',
        'title': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'latest_comment_url': 'latest_comment_url',
        'title': 'title',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, latest_comment_url=None, title=None, type=None, url=None):  # noqa: E501
        """Subject - a model defined in Swagger"""  # noqa: E501
        self._latest_comment_url = None
        self._title = None
        self._type = None
        self._url = None
        self.discriminator = None
        if latest_comment_url is not None:
            self.latest_comment_url = latest_comment_url
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def latest_comment_url(self):
        """Gets the latest_comment_url of this Subject.  # noqa: E501


        :return: The latest_comment_url of this Subject.  # noqa: E501
        :rtype: str
        """
        return self._latest_comment_url

    @latest_comment_url.setter
    def latest_comment_url(self, latest_comment_url):
        """Sets the latest_comment_url of this Subject.


        :param latest_comment_url: The latest_comment_url of this Subject.  # noqa: E501
        :type: str
        """

        self._latest_comment_url = latest_comment_url

    @property
    def title(self):
        """Gets the title of this Subject.  # noqa: E501


        :return: The title of this Subject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Subject.


        :param title: The title of this Subject.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this Subject.  # noqa: E501


        :return: The type of this Subject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subject.


        :param type: The type of this Subject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this Subject.  # noqa: E501


        :return: The url of this Subject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Subject.


        :param url: The url of this Subject.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Subject, dict):
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
        if not isinstance(other, Subject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
