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

class Programs(object):
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
        'assignee': 'Assignee',
        'author': 'Author',
        'description': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'assignee': 'assignee',
        'author': 'author',
        'description': 'description',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, assignee=None, author=None, description=None, id=None, name=None):  # noqa: E501
        """Programs - a model defined in Swagger"""  # noqa: E501
        self._assignee = None
        self._author = None
        self._description = None
        self._id = None
        self._name = None
        self.discriminator = None
        if assignee is not None:
            self.assignee = assignee
        if author is not None:
            self.author = author
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def assignee(self):
        """Gets the assignee of this Programs.  # noqa: E501


        :return: The assignee of this Programs.  # noqa: E501
        :rtype: Assignee
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this Programs.


        :param assignee: The assignee of this Programs.  # noqa: E501
        :type: Assignee
        """

        self._assignee = assignee

    @property
    def author(self):
        """Gets the author of this Programs.  # noqa: E501


        :return: The author of this Programs.  # noqa: E501
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Programs.


        :param author: The author of this Programs.  # noqa: E501
        :type: Author
        """

        self._author = author

    @property
    def description(self):
        """Gets the description of this Programs.  # noqa: E501


        :return: The description of this Programs.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Programs.


        :param description: The description of this Programs.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Programs.  # noqa: E501


        :return: The id of this Programs.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Programs.


        :param id: The id of this Programs.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Programs.  # noqa: E501


        :return: The name of this Programs.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Programs.


        :param name: The name of this Programs.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(Programs, dict):
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
        if not isinstance(other, Programs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
