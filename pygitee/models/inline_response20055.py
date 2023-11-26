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

class InlineResponse20055(object):
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
        'html_url': 'str',
        'id': 'int',
        'name': 'str',
        'parent': 'Parent',
        'path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'html_url': 'html_url',
        'id': 'id',
        'name': 'name',
        'parent': 'parent',
        'path': 'path',
        'type': 'type'
    }

    def __init__(self, html_url=None, id=None, name=None, parent=None, path=None, type=None):  # noqa: E501
        """InlineResponse20055 - a model defined in Swagger"""  # noqa: E501
        self._html_url = None
        self._id = None
        self._name = None
        self._parent = None
        self._path = None
        self._type = None
        self.discriminator = None
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type

    @property
    def html_url(self):
        """Gets the html_url of this InlineResponse20055.  # noqa: E501


        :return: The html_url of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this InlineResponse20055.


        :param html_url: The html_url of this InlineResponse20055.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this InlineResponse20055.  # noqa: E501


        :return: The id of this InlineResponse20055.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20055.


        :param id: The id of this InlineResponse20055.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20055.  # noqa: E501


        :return: The name of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20055.


        :param name: The name of this InlineResponse20055.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this InlineResponse20055.  # noqa: E501


        :return: The parent of this InlineResponse20055.  # noqa: E501
        :rtype: Parent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this InlineResponse20055.


        :param parent: The parent of this InlineResponse20055.  # noqa: E501
        :type: Parent
        """

        self._parent = parent

    @property
    def path(self):
        """Gets the path of this InlineResponse20055.  # noqa: E501


        :return: The path of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this InlineResponse20055.


        :param path: The path of this InlineResponse20055.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this InlineResponse20055.  # noqa: E501


        :return: The type of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20055.


        :param type: The type of this InlineResponse20055.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(InlineResponse20055, dict):
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
        if not isinstance(other, InlineResponse20055):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
