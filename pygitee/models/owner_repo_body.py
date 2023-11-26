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

class OwnerRepoBody(object):
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
        'can_comment': 'bool',
        'default_branch': 'str',
        'default_merge_method': 'str',
        'description': 'str',
        'has_issues': 'bool',
        'has_wiki': 'bool',
        'homepage': 'str',
        'issue_comment': 'bool',
        'issue_template_source': 'str',
        'lightweight_pr_enabled': 'bool',
        'merge_enabled': 'bool',
        'name': 'str',
        'online_edit_enabled': 'bool',
        'path': 'str',
        'private': 'bool',
        'pull_requests_enabled': 'bool',
        'rebase_enabled': 'bool',
        'security_hole_enabled': 'bool',
        'squash_enabled': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'can_comment': 'can_comment',
        'default_branch': 'default_branch',
        'default_merge_method': 'default_merge_method',
        'description': 'description',
        'has_issues': 'has_issues',
        'has_wiki': 'has_wiki',
        'homepage': 'homepage',
        'issue_comment': 'issue_comment',
        'issue_template_source': 'issue_template_source',
        'lightweight_pr_enabled': 'lightweight_pr_enabled',
        'merge_enabled': 'merge_enabled',
        'name': 'name',
        'online_edit_enabled': 'online_edit_enabled',
        'path': 'path',
        'private': 'private',
        'pull_requests_enabled': 'pull_requests_enabled',
        'rebase_enabled': 'rebase_enabled',
        'security_hole_enabled': 'security_hole_enabled',
        'squash_enabled': 'squash_enabled'
    }

    def __init__(self, access_token=None, can_comment=None, default_branch=None, default_merge_method=None, description=None, has_issues=None, has_wiki=None, homepage=None, issue_comment=None, issue_template_source=None, lightweight_pr_enabled=None, merge_enabled=None, name=None, online_edit_enabled=None, path=None, private=None, pull_requests_enabled=None, rebase_enabled=None, security_hole_enabled=None, squash_enabled=None):  # noqa: E501
        """OwnerRepoBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._can_comment = None
        self._default_branch = None
        self._default_merge_method = None
        self._description = None
        self._has_issues = None
        self._has_wiki = None
        self._homepage = None
        self._issue_comment = None
        self._issue_template_source = None
        self._lightweight_pr_enabled = None
        self._merge_enabled = None
        self._name = None
        self._online_edit_enabled = None
        self._path = None
        self._private = None
        self._pull_requests_enabled = None
        self._rebase_enabled = None
        self._security_hole_enabled = None
        self._squash_enabled = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if can_comment is not None:
            self.can_comment = can_comment
        if default_branch is not None:
            self.default_branch = default_branch
        if default_merge_method is not None:
            self.default_merge_method = default_merge_method
        if description is not None:
            self.description = description
        if has_issues is not None:
            self.has_issues = has_issues
        if has_wiki is not None:
            self.has_wiki = has_wiki
        if homepage is not None:
            self.homepage = homepage
        if issue_comment is not None:
            self.issue_comment = issue_comment
        if issue_template_source is not None:
            self.issue_template_source = issue_template_source
        if lightweight_pr_enabled is not None:
            self.lightweight_pr_enabled = lightweight_pr_enabled
        if merge_enabled is not None:
            self.merge_enabled = merge_enabled
        self.name = name
        if online_edit_enabled is not None:
            self.online_edit_enabled = online_edit_enabled
        if path is not None:
            self.path = path
        if private is not None:
            self.private = private
        if pull_requests_enabled is not None:
            self.pull_requests_enabled = pull_requests_enabled
        if rebase_enabled is not None:
            self.rebase_enabled = rebase_enabled
        if security_hole_enabled is not None:
            self.security_hole_enabled = security_hole_enabled
        if squash_enabled is not None:
            self.squash_enabled = squash_enabled

    @property
    def access_token(self):
        """Gets the access_token of this OwnerRepoBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OwnerRepoBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def can_comment(self):
        """Gets the can_comment of this OwnerRepoBody.  # noqa: E501

        允许用户对仓库进行评论。默认： 允许(true)  # noqa: E501

        :return: The can_comment of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._can_comment

    @can_comment.setter
    def can_comment(self, can_comment):
        """Sets the can_comment of this OwnerRepoBody.

        允许用户对仓库进行评论。默认： 允许(true)  # noqa: E501

        :param can_comment: The can_comment of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._can_comment = can_comment

    @property
    def default_branch(self):
        """Gets the default_branch of this OwnerRepoBody.  # noqa: E501

        更新默认分支  # noqa: E501

        :return: The default_branch of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this OwnerRepoBody.

        更新默认分支  # noqa: E501

        :param default_branch: The default_branch of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._default_branch = default_branch

    @property
    def default_merge_method(self):
        """Gets the default_merge_method of this OwnerRepoBody.  # noqa: E501

        选择默认合并 Pull Request 的方式,分别为 merge squash rebase  # noqa: E501

        :return: The default_merge_method of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._default_merge_method

    @default_merge_method.setter
    def default_merge_method(self, default_merge_method):
        """Sets the default_merge_method of this OwnerRepoBody.

        选择默认合并 Pull Request 的方式,分别为 merge squash rebase  # noqa: E501

        :param default_merge_method: The default_merge_method of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._default_merge_method = default_merge_method

    @property
    def description(self):
        """Gets the description of this OwnerRepoBody.  # noqa: E501

        仓库描述  # noqa: E501

        :return: The description of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OwnerRepoBody.

        仓库描述  # noqa: E501

        :param description: The description of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def has_issues(self):
        """Gets the has_issues of this OwnerRepoBody.  # noqa: E501

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :return: The has_issues of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._has_issues

    @has_issues.setter
    def has_issues(self, has_issues):
        """Sets the has_issues of this OwnerRepoBody.

        允许提Issue与否。默认: 允许(true)  # noqa: E501

        :param has_issues: The has_issues of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._has_issues = has_issues

    @property
    def has_wiki(self):
        """Gets the has_wiki of this OwnerRepoBody.  # noqa: E501

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :return: The has_wiki of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._has_wiki

    @has_wiki.setter
    def has_wiki(self, has_wiki):
        """Sets the has_wiki of this OwnerRepoBody.

        提供Wiki与否。默认: 提供(true)  # noqa: E501

        :param has_wiki: The has_wiki of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._has_wiki = has_wiki

    @property
    def homepage(self):
        """Gets the homepage of this OwnerRepoBody.  # noqa: E501

        主页(eg: https://gitee.com)  # noqa: E501

        :return: The homepage of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this OwnerRepoBody.

        主页(eg: https://gitee.com)  # noqa: E501

        :param homepage: The homepage of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

    @property
    def issue_comment(self):
        """Gets the issue_comment of this OwnerRepoBody.  # noqa: E501

        允许对“关闭”状态的 Issue 进行评论。默认: 不允许(false)  # noqa: E501

        :return: The issue_comment of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._issue_comment

    @issue_comment.setter
    def issue_comment(self, issue_comment):
        """Sets the issue_comment of this OwnerRepoBody.

        允许对“关闭”状态的 Issue 进行评论。默认: 不允许(false)  # noqa: E501

        :param issue_comment: The issue_comment of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._issue_comment = issue_comment

    @property
    def issue_template_source(self):
        """Gets the issue_template_source of this OwnerRepoBody.  # noqa: E501

        Issue 模版来源 project: 使用仓库 Issue Template 作为模版； enterprise: 使用企业工作项作为模版  # noqa: E501

        :return: The issue_template_source of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._issue_template_source

    @issue_template_source.setter
    def issue_template_source(self, issue_template_source):
        """Sets the issue_template_source of this OwnerRepoBody.

        Issue 模版来源 project: 使用仓库 Issue Template 作为模版； enterprise: 使用企业工作项作为模版  # noqa: E501

        :param issue_template_source: The issue_template_source of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._issue_template_source = issue_template_source

    @property
    def lightweight_pr_enabled(self):
        """Gets the lightweight_pr_enabled of this OwnerRepoBody.  # noqa: E501

        是否接受轻量级 pull request  # noqa: E501

        :return: The lightweight_pr_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._lightweight_pr_enabled

    @lightweight_pr_enabled.setter
    def lightweight_pr_enabled(self, lightweight_pr_enabled):
        """Sets the lightweight_pr_enabled of this OwnerRepoBody.

        是否接受轻量级 pull request  # noqa: E501

        :param lightweight_pr_enabled: The lightweight_pr_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._lightweight_pr_enabled = lightweight_pr_enabled

    @property
    def merge_enabled(self):
        """Gets the merge_enabled of this OwnerRepoBody.  # noqa: E501

        是否开启 merge 合并方式, 默认为开启  # noqa: E501

        :return: The merge_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._merge_enabled

    @merge_enabled.setter
    def merge_enabled(self, merge_enabled):
        """Sets the merge_enabled of this OwnerRepoBody.

        是否开启 merge 合并方式, 默认为开启  # noqa: E501

        :param merge_enabled: The merge_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._merge_enabled = merge_enabled

    @property
    def name(self):
        """Gets the name of this OwnerRepoBody.  # noqa: E501

        仓库名称  # noqa: E501

        :return: The name of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OwnerRepoBody.

        仓库名称  # noqa: E501

        :param name: The name of this OwnerRepoBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def online_edit_enabled(self):
        """Gets the online_edit_enabled of this OwnerRepoBody.  # noqa: E501

        是否允许仓库文件在线编辑  # noqa: E501

        :return: The online_edit_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._online_edit_enabled

    @online_edit_enabled.setter
    def online_edit_enabled(self, online_edit_enabled):
        """Sets the online_edit_enabled of this OwnerRepoBody.

        是否允许仓库文件在线编辑  # noqa: E501

        :param online_edit_enabled: The online_edit_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._online_edit_enabled = online_edit_enabled

    @property
    def path(self):
        """Gets the path of this OwnerRepoBody.  # noqa: E501

        更新仓库路径  # noqa: E501

        :return: The path of this OwnerRepoBody.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this OwnerRepoBody.

        更新仓库路径  # noqa: E501

        :param path: The path of this OwnerRepoBody.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def private(self):
        """Gets the private of this OwnerRepoBody.  # noqa: E501

        仓库公开或私有。  # noqa: E501

        :return: The private of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this OwnerRepoBody.

        仓库公开或私有。  # noqa: E501

        :param private: The private of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def pull_requests_enabled(self):
        """Gets the pull_requests_enabled of this OwnerRepoBody.  # noqa: E501

        接受 pull request，协作开发  # noqa: E501

        :return: The pull_requests_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._pull_requests_enabled

    @pull_requests_enabled.setter
    def pull_requests_enabled(self, pull_requests_enabled):
        """Sets the pull_requests_enabled of this OwnerRepoBody.

        接受 pull request，协作开发  # noqa: E501

        :param pull_requests_enabled: The pull_requests_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._pull_requests_enabled = pull_requests_enabled

    @property
    def rebase_enabled(self):
        """Gets the rebase_enabled of this OwnerRepoBody.  # noqa: E501

        是否开启 rebase 合并方式, 默认为开启  # noqa: E501

        :return: The rebase_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._rebase_enabled

    @rebase_enabled.setter
    def rebase_enabled(self, rebase_enabled):
        """Sets the rebase_enabled of this OwnerRepoBody.

        是否开启 rebase 合并方式, 默认为开启  # noqa: E501

        :param rebase_enabled: The rebase_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._rebase_enabled = rebase_enabled

    @property
    def security_hole_enabled(self):
        """Gets the security_hole_enabled of this OwnerRepoBody.  # noqa: E501

        这个Issue涉及到安全/隐私问题，提交后不公开此Issue（可见范围：仓库成员, 企业成员）  # noqa: E501

        :return: The security_hole_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._security_hole_enabled

    @security_hole_enabled.setter
    def security_hole_enabled(self, security_hole_enabled):
        """Sets the security_hole_enabled of this OwnerRepoBody.

        这个Issue涉及到安全/隐私问题，提交后不公开此Issue（可见范围：仓库成员, 企业成员）  # noqa: E501

        :param security_hole_enabled: The security_hole_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._security_hole_enabled = security_hole_enabled

    @property
    def squash_enabled(self):
        """Gets the squash_enabled of this OwnerRepoBody.  # noqa: E501

        是否开启 squash 合并方式, 默认为开启  # noqa: E501

        :return: The squash_enabled of this OwnerRepoBody.  # noqa: E501
        :rtype: bool
        """
        return self._squash_enabled

    @squash_enabled.setter
    def squash_enabled(self, squash_enabled):
        """Sets the squash_enabled of this OwnerRepoBody.

        是否开启 squash 合并方式, 默认为开启  # noqa: E501

        :param squash_enabled: The squash_enabled of this OwnerRepoBody.  # noqa: E501
        :type: bool
        """

        self._squash_enabled = squash_enabled

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
        if issubclass(OwnerRepoBody, dict):
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
        if not isinstance(other, OwnerRepoBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other