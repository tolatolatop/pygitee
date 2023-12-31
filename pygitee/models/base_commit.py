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

class BaseCommit(object):
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
        'comments_url': 'str',
        'commit': 'str',
        'committer': 'str',
        'html_url': 'str',
        'parents': 'str',
        'sha': 'str',
        'url': 'str'
    }

    attribute_map = {
        'author': 'author',
        'comments_url': 'comments_url',
        'commit': 'commit',
        'committer': 'committer',
        'html_url': 'html_url',
        'parents': 'parents',
        'sha': 'sha',
        'url': 'url'
    }

    def __init__(self, author=None, comments_url=None, commit=None, committer=None, html_url=None, parents=None, sha=None, url=None):  # noqa: E501
        """BaseCommit - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._comments_url = None
        self._commit = None
        self._committer = None
        self._html_url = None
        self._parents = None
        self._sha = None
        self._url = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if comments_url is not None:
            self.comments_url = comments_url
        if commit is not None:
            self.commit = commit
        if committer is not None:
            self.committer = committer
        if html_url is not None:
            self.html_url = html_url
        if parents is not None:
            self.parents = parents
        if sha is not None:
            self.sha = sha
        if url is not None:
            self.url = url

    @property
    def author(self):
        """Gets the author of this BaseCommit.  # noqa: E501


        :return: The author of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this BaseCommit.


        :param author: The author of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def comments_url(self):
        """Gets the comments_url of this BaseCommit.  # noqa: E501


        :return: The comments_url of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._comments_url

    @comments_url.setter
    def comments_url(self, comments_url):
        """Sets the comments_url of this BaseCommit.


        :param comments_url: The comments_url of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._comments_url = comments_url

    @property
    def commit(self):
        """Gets the commit of this BaseCommit.  # noqa: E501


        :return: The commit of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this BaseCommit.


        :param commit: The commit of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._commit = commit

    @property
    def committer(self):
        """Gets the committer of this BaseCommit.  # noqa: E501


        :return: The committer of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this BaseCommit.


        :param committer: The committer of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._committer = committer

    @property
    def html_url(self):
        """Gets the html_url of this BaseCommit.  # noqa: E501


        :return: The html_url of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this BaseCommit.


        :param html_url: The html_url of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def parents(self):
        """Gets the parents of this BaseCommit.  # noqa: E501


        :return: The parents of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this BaseCommit.


        :param parents: The parents of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._parents = parents

    @property
    def sha(self):
        """Gets the sha of this BaseCommit.  # noqa: E501


        :return: The sha of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this BaseCommit.


        :param sha: The sha of this BaseCommit.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def url(self):
        """Gets the url of this BaseCommit.  # noqa: E501


        :return: The url of this BaseCommit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BaseCommit.


        :param url: The url of this BaseCommit.  # noqa: E501
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
        if issubclass(BaseCommit, dict):
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
        if not isinstance(other, BaseCommit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
