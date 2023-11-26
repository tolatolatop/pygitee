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

class Commit(object):
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
        'author': 'str',
        'committer': 'str',
        'message': 'str',
        'parents': 'str',
        'sha': 'str',
        'tree': 'str'
    }

    attribute_map = {
        'author': 'author',
        'committer': 'committer',
        'message': 'message',
        'parents': 'parents',
        'sha': 'sha',
        'tree': 'tree'
    }

    def __init__(self, author=None, committer=None, message=None, parents=None, sha=None, tree=None):  # noqa: E501
        """Commit - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._committer = None
        self._message = None
        self._parents = None
        self._sha = None
        self._tree = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if committer is not None:
            self.committer = committer
        if message is not None:
            self.message = message
        if parents is not None:
            self.parents = parents
        if sha is not None:
            self.sha = sha
        if tree is not None:
            self.tree = tree

    @property
    def author(self):
        """Gets the author of this Commit.  # noqa: E501


        :return: The author of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Commit.


        :param author: The author of this Commit.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def committer(self):
        """Gets the committer of this Commit.  # noqa: E501


        :return: The committer of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this Commit.


        :param committer: The committer of this Commit.  # noqa: E501
        :type: str
        """

        self._committer = committer

    @property
    def message(self):
        """Gets the message of this Commit.  # noqa: E501


        :return: The message of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Commit.


        :param message: The message of this Commit.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def parents(self):
        """Gets the parents of this Commit.  # noqa: E501


        :return: The parents of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this Commit.


        :param parents: The parents of this Commit.  # noqa: E501
        :type: str
        """

        self._parents = parents

    @property
    def sha(self):
        """Gets the sha of this Commit.  # noqa: E501


        :return: The sha of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Commit.


        :param sha: The sha of this Commit.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def tree(self):
        """Gets the tree of this Commit.  # noqa: E501


        :return: The tree of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        """Sets the tree of this Commit.


        :param tree: The tree of this Commit.  # noqa: E501
        :type: str
        """

        self._tree = tree

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
        if issubclass(Commit, dict):
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
        if not isinstance(other, Commit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
