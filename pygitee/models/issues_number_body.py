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

class IssuesNumberBody(object):
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
        'assignee': 'str',
        'body': 'str',
        'collaborators': 'str',
        'labels': 'str',
        'milestone': 'int',
        'program': 'str',
        'repo': 'str',
        'security_hole': 'bool',
        'state': 'str',
        'title': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'assignee': 'assignee',
        'body': 'body',
        'collaborators': 'collaborators',
        'labels': 'labels',
        'milestone': 'milestone',
        'program': 'program',
        'repo': 'repo',
        'security_hole': 'security_hole',
        'state': 'state',
        'title': 'title'
    }

    def __init__(self, access_token=None, assignee=None, body=None, collaborators=None, labels=None, milestone=None, program=None, repo=None, security_hole=None, state=None, title=None):  # noqa: E501
        """IssuesNumberBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._assignee = None
        self._body = None
        self._collaborators = None
        self._labels = None
        self._milestone = None
        self._program = None
        self._repo = None
        self._security_hole = None
        self._state = None
        self._title = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if assignee is not None:
            self.assignee = assignee
        if body is not None:
            self.body = body
        if collaborators is not None:
            self.collaborators = collaborators
        if labels is not None:
            self.labels = labels
        if milestone is not None:
            self.milestone = milestone
        if program is not None:
            self.program = program
        if repo is not None:
            self.repo = repo
        if security_hole is not None:
            self.security_hole = security_hole
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title

    @property
    def access_token(self):
        """Gets the access_token of this IssuesNumberBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this IssuesNumberBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def assignee(self):
        """Gets the assignee of this IssuesNumberBody.  # noqa: E501

        Issue负责人的个人空间地址  # noqa: E501

        :return: The assignee of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this IssuesNumberBody.

        Issue负责人的个人空间地址  # noqa: E501

        :param assignee: The assignee of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._assignee = assignee

    @property
    def body(self):
        """Gets the body of this IssuesNumberBody.  # noqa: E501

        Issue描述  # noqa: E501

        :return: The body of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this IssuesNumberBody.

        Issue描述  # noqa: E501

        :param body: The body of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def collaborators(self):
        """Gets the collaborators of this IssuesNumberBody.  # noqa: E501

        Issue协助者的个人空间地址, 以 , 分隔  # noqa: E501

        :return: The collaborators of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this IssuesNumberBody.

        Issue协助者的个人空间地址, 以 , 分隔  # noqa: E501

        :param collaborators: The collaborators of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._collaborators = collaborators

    @property
    def labels(self):
        """Gets the labels of this IssuesNumberBody.  # noqa: E501

        用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance  # noqa: E501

        :return: The labels of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IssuesNumberBody.

        用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance  # noqa: E501

        :param labels: The labels of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._labels = labels

    @property
    def milestone(self):
        """Gets the milestone of this IssuesNumberBody.  # noqa: E501

        里程碑序号  # noqa: E501

        :return: The milestone of this IssuesNumberBody.  # noqa: E501
        :rtype: int
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this IssuesNumberBody.

        里程碑序号  # noqa: E501

        :param milestone: The milestone of this IssuesNumberBody.  # noqa: E501
        :type: int
        """

        self._milestone = milestone

    @property
    def program(self):
        """Gets the program of this IssuesNumberBody.  # noqa: E501

        项目ID  # noqa: E501

        :return: The program of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this IssuesNumberBody.

        项目ID  # noqa: E501

        :param program: The program of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._program = program

    @property
    def repo(self):
        """Gets the repo of this IssuesNumberBody.  # noqa: E501

        仓库路径(path)  # noqa: E501

        :return: The repo of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this IssuesNumberBody.

        仓库路径(path)  # noqa: E501

        :param repo: The repo of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def security_hole(self):
        """Gets the security_hole of this IssuesNumberBody.  # noqa: E501

        是否是私有issue(默认为false)  # noqa: E501

        :return: The security_hole of this IssuesNumberBody.  # noqa: E501
        :rtype: bool
        """
        return self._security_hole

    @security_hole.setter
    def security_hole(self, security_hole):
        """Sets the security_hole of this IssuesNumberBody.

        是否是私有issue(默认为false)  # noqa: E501

        :param security_hole: The security_hole of this IssuesNumberBody.  # noqa: E501
        :type: bool
        """

        self._security_hole = security_hole

    @property
    def state(self):
        """Gets the state of this IssuesNumberBody.  # noqa: E501

        Issue 状态，open（开启的）、progressing（进行中）、closed（关闭的）  # noqa: E501

        :return: The state of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IssuesNumberBody.

        Issue 状态，open（开启的）、progressing（进行中）、closed（关闭的）  # noqa: E501

        :param state: The state of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this IssuesNumberBody.  # noqa: E501

        Issue标题  # noqa: E501

        :return: The title of this IssuesNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IssuesNumberBody.

        Issue标题  # noqa: E501

        :param title: The title of this IssuesNumberBody.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(IssuesNumberBody, dict):
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
        if not isinstance(other, IssuesNumberBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other