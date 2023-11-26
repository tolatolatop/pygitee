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

class IssueStateDetail(object):
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
        'color': 'str',
        'command': 'str',
        'created_at': 'object',
        'icon': 'str',
        'id': 'int',
        'serial': 'str',
        'title': 'str',
        'updated_at': 'object'
    }

    attribute_map = {
        'color': 'color',
        'command': 'command',
        'created_at': 'created_at',
        'icon': 'icon',
        'id': 'id',
        'serial': 'serial',
        'title': 'title',
        'updated_at': 'updated_at'
    }

    def __init__(self, color=None, command=None, created_at=None, icon=None, id=None, serial=None, title=None, updated_at=None):  # noqa: E501
        """IssueStateDetail - a model defined in Swagger"""  # noqa: E501
        self._color = None
        self._command = None
        self._created_at = None
        self._icon = None
        self._id = None
        self._serial = None
        self._title = None
        self._updated_at = None
        self.discriminator = None
        if color is not None:
            self.color = color
        if command is not None:
            self.command = command
        if created_at is not None:
            self.created_at = created_at
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if serial is not None:
            self.serial = serial
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def color(self):
        """Gets the color of this IssueStateDetail.  # noqa: E501


        :return: The color of this IssueStateDetail.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this IssueStateDetail.


        :param color: The color of this IssueStateDetail.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def command(self):
        """Gets the command of this IssueStateDetail.  # noqa: E501


        :return: The command of this IssueStateDetail.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this IssueStateDetail.


        :param command: The command of this IssueStateDetail.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def created_at(self):
        """Gets the created_at of this IssueStateDetail.  # noqa: E501


        :return: The created_at of this IssueStateDetail.  # noqa: E501
        :rtype: object
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IssueStateDetail.


        :param created_at: The created_at of this IssueStateDetail.  # noqa: E501
        :type: object
        """

        self._created_at = created_at

    @property
    def icon(self):
        """Gets the icon of this IssueStateDetail.  # noqa: E501


        :return: The icon of this IssueStateDetail.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this IssueStateDetail.


        :param icon: The icon of this IssueStateDetail.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this IssueStateDetail.  # noqa: E501


        :return: The id of this IssueStateDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueStateDetail.


        :param id: The id of this IssueStateDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def serial(self):
        """Gets the serial of this IssueStateDetail.  # noqa: E501


        :return: The serial of this IssueStateDetail.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this IssueStateDetail.


        :param serial: The serial of this IssueStateDetail.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def title(self):
        """Gets the title of this IssueStateDetail.  # noqa: E501


        :return: The title of this IssueStateDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IssueStateDetail.


        :param title: The title of this IssueStateDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this IssueStateDetail.  # noqa: E501


        :return: The updated_at of this IssueStateDetail.  # noqa: E501
        :rtype: object
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IssueStateDetail.


        :param updated_at: The updated_at of this IssueStateDetail.  # noqa: E501
        :type: object
        """

        self._updated_at = updated_at

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
        if issubclass(IssueStateDetail, dict):
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
        if not isinstance(other, IssueStateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
