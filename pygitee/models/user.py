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

class User(object):
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
        'avatar_url': 'str',
        'html_url': 'str',
        'id': 'int',
        'login': 'str',
        'name': 'str',
        'remark': 'str',
        'url': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'html_url': 'html_url',
        'id': 'id',
        'login': 'login',
        'name': 'name',
        'remark': 'remark',
        'url': 'url'
    }

    def __init__(self, avatar_url=None, html_url=None, id=None, login=None, name=None, remark=None, url=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._avatar_url = None
        self._html_url = None
        self._id = None
        self._login = None
        self._name = None
        self._remark = None
        self._url = None
        self.discriminator = None
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if url is not None:
            self.url = url

    @property
    def avatar_url(self):
        """Gets the avatar_url of this User.  # noqa: E501


        :return: The avatar_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this User.


        :param avatar_url: The avatar_url of this User.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def html_url(self):
        """Gets the html_url of this User.  # noqa: E501


        :return: The html_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this User.


        :param html_url: The html_url of this User.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this User.  # noqa: E501


        :return: The login of this User.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this User.


        :param login: The login of this User.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def remark(self):
        """Gets the remark of this User.  # noqa: E501


        :return: The remark of this User.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this User.


        :param remark: The remark of this User.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def url(self):
        """Gets the url of this User.  # noqa: E501


        :return: The url of this User.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this User.


        :param url: The url of this User.  # noqa: E501
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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
