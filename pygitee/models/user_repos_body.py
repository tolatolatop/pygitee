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

class UserReposBody(object):
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
        'auto_init': 'bool',
        'can_comment': 'bool',
        'description': 'str',
        'gitignore_template': 'str',
        'has_issues': 'bool',
        'has_wiki': 'bool',
        'homepage': 'str',
        'license_template': 'str',
        'name': 'str',
        'path': 'str',
        'private': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'auto_init': 'auto_init',
        'can_comment': 'can_comment',
        'description': 'description',
        'gitignore_template': 'gitignore_template',
        'has_issues': 'has_issues',
        'has_wiki': 'has_wiki',
        'homepage': 'homepage',
        'license_template': 'license_template',
        'name': 'name',
        'path': 'path',
        'private': 'private'
    }

    def __init__(self, access_token=None, auto_init=None, can_comment=None, description=None, gitignore_template=None, has_issues=None, has_wiki=None, homepage=None, license_template=None, name=None, path=None, private=None):  # noqa: E501
        """UserReposBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._auto_init = None
        self._can_comment = None
        self._description = None
        self._gitignore_template = None
        self._has_issues = None
        self._has_wiki = None
        self._homepage = None
        self._license_template = None
        self._name = None
        self._path = None
        self._private = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if auto_init is not None:
            self.auto_init = auto_init
        if can_comment is not None:
            self.can_comment = can_comment
        if description is not None:
            self.description = description
        if gitignore_template is not None:
            self.gitignore_template = gitignore_template
        if has_issues is not None:
            self.has_issues = has_issues
        if has_wiki is not None:
            self.has_wiki = has_wiki
        if homepage is not None:
            self.homepage = homepage
        if license_template is not None:
            self.license_template = license_template
        self.name = name
        if path is not None:
            self.path = path
        if private is not None:
            self.private = private

    @property
    def access_token(self):
        """Gets the access_token of this UserReposBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this UserReposBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this UserReposBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def auto_init(self):
        """Gets the auto_init of this UserReposBody.  # noqa: E501

        值为true时则会用README初始化仓库。默认: 不初始化(false)  # noqa: E501

        :return: The auto_init of this UserReposBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_init

    @auto_init.setter
    def auto_init(self, auto_init):
        """Sets the auto_init of this UserReposBody.

        值为true时则会用README初始化仓库。默认: 不初始化(false)  # noqa: E501

        :param auto_init: The auto_init of this UserReposBody.  # noqa: E501
        :type: bool
        """

        self._auto_init = auto_init

    @property
    def can_comment(self):
        """Gets the can_comment of this UserReposBody.  # noqa: E501

        允许用户对仓库进行评论。默认： 允许(true)  # noqa: E501

        :return: The can_comment of this UserReposBody.  # noqa: E501
        :rtype: bool
        """
        return self._can_comment

    @can_comment.setter
    def can_comment(self, can_comment):
        """Sets the can_comment of this UserReposBody.

        允许用户对仓库进行评论。默认： 允许(true)  # noqa: E501

        :param can_comment: The can_comment of this UserReposBody.  # noqa: E501
        :type: bool
        """

        self._can_comment = can_comment

    @property
    def description(self):
        """Gets the description of this UserReposBody.  # noqa: E501

        仓库描述  # noqa: E501

        :return: The description of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserReposBody.

        仓库描述  # noqa: E501

        :param description: The description of this UserReposBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gitignore_template(self):
        """Gets the gitignore_template of this UserReposBody.  # noqa: E501

        Git Ignore模版  # noqa: E501

        :return: The gitignore_template of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._gitignore_template

    @gitignore_template.setter
    def gitignore_template(self, gitignore_template):
        """Sets the gitignore_template of this UserReposBody.

        Git Ignore模版  # noqa: E501

        :param gitignore_template: The gitignore_template of this UserReposBody.  # noqa: E501
        :type: str
        """

        self._gitignore_template = gitignore_template

    @property
    def has_issues(self):
        """Gets the has_issues of this UserReposBody.  # noqa: E501

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :return: The has_issues of this UserReposBody.  # noqa: E501
        :rtype: bool
        """
        return self._has_issues

    @has_issues.setter
    def has_issues(self, has_issues):
        """Sets the has_issues of this UserReposBody.

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :param has_issues: The has_issues of this UserReposBody.  # noqa: E501
        :type: bool
        """

        self._has_issues = has_issues

    @property
    def has_wiki(self):
        """Gets the has_wiki of this UserReposBody.  # noqa: E501

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :return: The has_wiki of this UserReposBody.  # noqa: E501
        :rtype: bool
        """
        return self._has_wiki

    @has_wiki.setter
    def has_wiki(self, has_wiki):
        """Sets the has_wiki of this UserReposBody.

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :param has_wiki: The has_wiki of this UserReposBody.  # noqa: E501
        :type: bool
        """

        self._has_wiki = has_wiki

    @property
    def homepage(self):
        """Gets the homepage of this UserReposBody.  # noqa: E501

        主页(eg: https://gitee.com)  # noqa: E501

        :return: The homepage of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this UserReposBody.

        主页(eg: https://gitee.com)  # noqa: E501

        :param homepage: The homepage of this UserReposBody.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

    @property
    def license_template(self):
        """Gets the license_template of this UserReposBody.  # noqa: E501

        License模版  # noqa: E501

        :return: The license_template of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._license_template

    @license_template.setter
    def license_template(self, license_template):
        """Sets the license_template of this UserReposBody.

        License模版  # noqa: E501

        :param license_template: The license_template of this UserReposBody.  # noqa: E501
        :type: str
        """

        self._license_template = license_template

    @property
    def name(self):
        """Gets the name of this UserReposBody.  # noqa: E501

        仓库名称  # noqa: E501

        :return: The name of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserReposBody.

        仓库名称  # noqa: E501

        :param name: The name of this UserReposBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this UserReposBody.  # noqa: E501

        仓库路径  # noqa: E501

        :return: The path of this UserReposBody.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this UserReposBody.

        仓库路径  # noqa: E501

        :param path: The path of this UserReposBody.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def private(self):
        """Gets the private of this UserReposBody.  # noqa: E501

        目前仅支持私有  # noqa: E501

        :return: The private of this UserReposBody.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this UserReposBody.

        目前仅支持私有  # noqa: E501

        :param private: The private of this UserReposBody.  # noqa: E501
        :type: bool
        """

        self._private = private

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
        if issubclass(UserReposBody, dict):
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
        if not isinstance(other, UserReposBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
