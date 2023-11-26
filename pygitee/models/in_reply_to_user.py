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

class InReplyToUser(object):
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
        'avatar_url': 'str',
        'events_url': 'str',
        'followers_url': 'str',
        'following_url': 'str',
        'gists_url': 'str',
        'html_url': 'str',
        'id': 'int',
        'login': 'str',
        'member_role': 'str',
        'name': 'str',
        'organizations_url': 'str',
        'received_events_url': 'str',
        'remark': 'str',
        'repos_url': 'str',
        'starred_url': 'str',
        'subscriptions_url': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'events_url': 'events_url',
        'followers_url': 'followers_url',
        'following_url': 'following_url',
        'gists_url': 'gists_url',
        'html_url': 'html_url',
        'id': 'id',
        'login': 'login',
        'member_role': 'member_role',
        'name': 'name',
        'organizations_url': 'organizations_url',
        'received_events_url': 'received_events_url',
        'remark': 'remark',
        'repos_url': 'repos_url',
        'starred_url': 'starred_url',
        'subscriptions_url': 'subscriptions_url',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, avatar_url=None, events_url=None, followers_url=None, following_url=None, gists_url=None, html_url=None, id=None, login=None, member_role=None, name=None, organizations_url=None, received_events_url=None, remark=None, repos_url=None, starred_url=None, subscriptions_url=None, type=None, url=None):  # noqa: E501
        """InReplyToUser - a model defined in Swagger"""  # noqa: E501
        self._avatar_url = None
        self._events_url = None
        self._followers_url = None
        self._following_url = None
        self._gists_url = None
        self._html_url = None
        self._id = None
        self._login = None
        self._member_role = None
        self._name = None
        self._organizations_url = None
        self._received_events_url = None
        self._remark = None
        self._repos_url = None
        self._starred_url = None
        self._subscriptions_url = None
        self._type = None
        self._url = None
        self.discriminator = None
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if events_url is not None:
            self.events_url = events_url
        if followers_url is not None:
            self.followers_url = followers_url
        if following_url is not None:
            self.following_url = following_url
        if gists_url is not None:
            self.gists_url = gists_url
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if member_role is not None:
            self.member_role = member_role
        if name is not None:
            self.name = name
        if organizations_url is not None:
            self.organizations_url = organizations_url
        if received_events_url is not None:
            self.received_events_url = received_events_url
        if remark is not None:
            self.remark = remark
        if repos_url is not None:
            self.repos_url = repos_url
        if starred_url is not None:
            self.starred_url = starred_url
        if subscriptions_url is not None:
            self.subscriptions_url = subscriptions_url
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def avatar_url(self):
        """Gets the avatar_url of this InReplyToUser.  # noqa: E501


        :return: The avatar_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this InReplyToUser.


        :param avatar_url: The avatar_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def events_url(self):
        """Gets the events_url of this InReplyToUser.  # noqa: E501


        :return: The events_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._events_url

    @events_url.setter
    def events_url(self, events_url):
        """Sets the events_url of this InReplyToUser.


        :param events_url: The events_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._events_url = events_url

    @property
    def followers_url(self):
        """Gets the followers_url of this InReplyToUser.  # noqa: E501


        :return: The followers_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._followers_url

    @followers_url.setter
    def followers_url(self, followers_url):
        """Sets the followers_url of this InReplyToUser.


        :param followers_url: The followers_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._followers_url = followers_url

    @property
    def following_url(self):
        """Gets the following_url of this InReplyToUser.  # noqa: E501


        :return: The following_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._following_url

    @following_url.setter
    def following_url(self, following_url):
        """Sets the following_url of this InReplyToUser.


        :param following_url: The following_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._following_url = following_url

    @property
    def gists_url(self):
        """Gets the gists_url of this InReplyToUser.  # noqa: E501


        :return: The gists_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._gists_url

    @gists_url.setter
    def gists_url(self, gists_url):
        """Sets the gists_url of this InReplyToUser.


        :param gists_url: The gists_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._gists_url = gists_url

    @property
    def html_url(self):
        """Gets the html_url of this InReplyToUser.  # noqa: E501


        :return: The html_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this InReplyToUser.


        :param html_url: The html_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this InReplyToUser.  # noqa: E501


        :return: The id of this InReplyToUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InReplyToUser.


        :param id: The id of this InReplyToUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this InReplyToUser.  # noqa: E501


        :return: The login of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this InReplyToUser.


        :param login: The login of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def member_role(self):
        """Gets the member_role of this InReplyToUser.  # noqa: E501


        :return: The member_role of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._member_role

    @member_role.setter
    def member_role(self, member_role):
        """Sets the member_role of this InReplyToUser.


        :param member_role: The member_role of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._member_role = member_role

    @property
    def name(self):
        """Gets the name of this InReplyToUser.  # noqa: E501


        :return: The name of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InReplyToUser.


        :param name: The name of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organizations_url(self):
        """Gets the organizations_url of this InReplyToUser.  # noqa: E501


        :return: The organizations_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._organizations_url

    @organizations_url.setter
    def organizations_url(self, organizations_url):
        """Sets the organizations_url of this InReplyToUser.


        :param organizations_url: The organizations_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._organizations_url = organizations_url

    @property
    def received_events_url(self):
        """Gets the received_events_url of this InReplyToUser.  # noqa: E501


        :return: The received_events_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._received_events_url

    @received_events_url.setter
    def received_events_url(self, received_events_url):
        """Sets the received_events_url of this InReplyToUser.


        :param received_events_url: The received_events_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._received_events_url = received_events_url

    @property
    def remark(self):
        """Gets the remark of this InReplyToUser.  # noqa: E501


        :return: The remark of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this InReplyToUser.


        :param remark: The remark of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def repos_url(self):
        """Gets the repos_url of this InReplyToUser.  # noqa: E501


        :return: The repos_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._repos_url

    @repos_url.setter
    def repos_url(self, repos_url):
        """Sets the repos_url of this InReplyToUser.


        :param repos_url: The repos_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._repos_url = repos_url

    @property
    def starred_url(self):
        """Gets the starred_url of this InReplyToUser.  # noqa: E501


        :return: The starred_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._starred_url

    @starred_url.setter
    def starred_url(self, starred_url):
        """Sets the starred_url of this InReplyToUser.


        :param starred_url: The starred_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._starred_url = starred_url

    @property
    def subscriptions_url(self):
        """Gets the subscriptions_url of this InReplyToUser.  # noqa: E501


        :return: The subscriptions_url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._subscriptions_url

    @subscriptions_url.setter
    def subscriptions_url(self, subscriptions_url):
        """Sets the subscriptions_url of this InReplyToUser.


        :param subscriptions_url: The subscriptions_url of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._subscriptions_url = subscriptions_url

    @property
    def type(self):
        """Gets the type of this InReplyToUser.  # noqa: E501


        :return: The type of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InReplyToUser.


        :param type: The type of this InReplyToUser.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this InReplyToUser.  # noqa: E501


        :return: The url of this InReplyToUser.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InReplyToUser.


        :param url: The url of this InReplyToUser.  # noqa: E501
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
        if issubclass(InReplyToUser, dict):
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
        if not isinstance(other, InReplyToUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other