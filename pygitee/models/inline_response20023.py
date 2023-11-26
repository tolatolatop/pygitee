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

class InlineResponse20023(object):
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
        'action_type': 'str',
        'content': 'str',
        'created_at': 'str',
        'icon': 'str',
        'id': 'str',
        'link_target': 'str',
        'user': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'content': 'content',
        'created_at': 'created_at',
        'icon': 'icon',
        'id': 'id',
        'link_target': 'link_target',
        'user': 'user'
    }

    def __init__(self, action_type=None, content=None, created_at=None, icon=None, id=None, link_target=None, user=None):  # noqa: E501
        """InlineResponse20023 - a model defined in Swagger"""  # noqa: E501
        self._action_type = None
        self._content = None
        self._created_at = None
        self._icon = None
        self._id = None
        self._link_target = None
        self._user = None
        self.discriminator = None
        if action_type is not None:
            self.action_type = action_type
        if content is not None:
            self.content = content
        if created_at is not None:
            self.created_at = created_at
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if link_target is not None:
            self.link_target = link_target
        if user is not None:
            self.user = user

    @property
    def action_type(self):
        """Gets the action_type of this InlineResponse20023.  # noqa: E501


        :return: The action_type of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this InlineResponse20023.


        :param action_type: The action_type of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def content(self):
        """Gets the content of this InlineResponse20023.  # noqa: E501


        :return: The content of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse20023.


        :param content: The content of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20023.  # noqa: E501


        :return: The created_at of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20023.


        :param created_at: The created_at of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def icon(self):
        """Gets the icon of this InlineResponse20023.  # noqa: E501


        :return: The icon of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this InlineResponse20023.


        :param icon: The icon of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this InlineResponse20023.  # noqa: E501


        :return: The id of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20023.


        :param id: The id of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def link_target(self):
        """Gets the link_target of this InlineResponse20023.  # noqa: E501


        :return: The link_target of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._link_target

    @link_target.setter
    def link_target(self, link_target):
        """Sets the link_target of this InlineResponse20023.


        :param link_target: The link_target of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._link_target = link_target

    @property
    def user(self):
        """Gets the user of this InlineResponse20023.  # noqa: E501


        :return: The user of this InlineResponse20023.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineResponse20023.


        :param user: The user of this InlineResponse20023.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(InlineResponse20023, dict):
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
        if not isinstance(other, InlineResponse20023):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
