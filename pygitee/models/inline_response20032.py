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

class InlineResponse20032(object):
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
        'base_commit': 'BaseCommit',
        'commits': 'Commits',
        'files': 'Files',
        'merge_base_commit': 'MergeBaseCommit',
        'truncated': 'bool'
    }

    attribute_map = {
        'base_commit': 'base_commit',
        'commits': 'commits',
        'files': 'files',
        'merge_base_commit': 'merge_base_commit',
        'truncated': 'truncated'
    }

    def __init__(self, base_commit=None, commits=None, files=None, merge_base_commit=None, truncated=None):  # noqa: E501
        """InlineResponse20032 - a model defined in Swagger"""  # noqa: E501
        self._base_commit = None
        self._commits = None
        self._files = None
        self._merge_base_commit = None
        self._truncated = None
        self.discriminator = None
        if base_commit is not None:
            self.base_commit = base_commit
        if commits is not None:
            self.commits = commits
        if files is not None:
            self.files = files
        if merge_base_commit is not None:
            self.merge_base_commit = merge_base_commit
        if truncated is not None:
            self.truncated = truncated

    @property
    def base_commit(self):
        """Gets the base_commit of this InlineResponse20032.  # noqa: E501


        :return: The base_commit of this InlineResponse20032.  # noqa: E501
        :rtype: BaseCommit
        """
        return self._base_commit

    @base_commit.setter
    def base_commit(self, base_commit):
        """Sets the base_commit of this InlineResponse20032.


        :param base_commit: The base_commit of this InlineResponse20032.  # noqa: E501
        :type: BaseCommit
        """

        self._base_commit = base_commit

    @property
    def commits(self):
        """Gets the commits of this InlineResponse20032.  # noqa: E501


        :return: The commits of this InlineResponse20032.  # noqa: E501
        :rtype: Commits
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        """Sets the commits of this InlineResponse20032.


        :param commits: The commits of this InlineResponse20032.  # noqa: E501
        :type: Commits
        """

        self._commits = commits

    @property
    def files(self):
        """Gets the files of this InlineResponse20032.  # noqa: E501


        :return: The files of this InlineResponse20032.  # noqa: E501
        :rtype: Files
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this InlineResponse20032.


        :param files: The files of this InlineResponse20032.  # noqa: E501
        :type: Files
        """

        self._files = files

    @property
    def merge_base_commit(self):
        """Gets the merge_base_commit of this InlineResponse20032.  # noqa: E501


        :return: The merge_base_commit of this InlineResponse20032.  # noqa: E501
        :rtype: MergeBaseCommit
        """
        return self._merge_base_commit

    @merge_base_commit.setter
    def merge_base_commit(self, merge_base_commit):
        """Sets the merge_base_commit of this InlineResponse20032.


        :param merge_base_commit: The merge_base_commit of this InlineResponse20032.  # noqa: E501
        :type: MergeBaseCommit
        """

        self._merge_base_commit = merge_base_commit

    @property
    def truncated(self):
        """Gets the truncated of this InlineResponse20032.  # noqa: E501


        :return: The truncated of this InlineResponse20032.  # noqa: E501
        :rtype: bool
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this InlineResponse20032.


        :param truncated: The truncated of this InlineResponse20032.  # noqa: E501
        :type: bool
        """

        self._truncated = truncated

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
        if issubclass(InlineResponse20032, dict):
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
        if not isinstance(other, InlineResponse20032):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
