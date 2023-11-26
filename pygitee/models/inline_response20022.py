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

class InlineResponse20022(object):
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
        'active': 'str',
        'organization': 'Organization',
        'organization_url': 'str',
        'remark': 'str',
        'role': 'str',
        'url': 'str',
        'user': 'str'
    }

    attribute_map = {
        'active': 'active',
        'organization': 'organization',
        'organization_url': 'organization_url',
        'remark': 'remark',
        'role': 'role',
        'url': 'url',
        'user': 'user'
    }

    def __init__(self, active=None, organization=None, organization_url=None, remark=None, role=None, url=None, user=None):  # noqa: E501
        """InlineResponse20022 - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._organization = None
        self._organization_url = None
        self._remark = None
        self._role = None
        self._url = None
        self._user = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if organization is not None:
            self.organization = organization
        if organization_url is not None:
            self.organization_url = organization_url
        if remark is not None:
            self.remark = remark
        if role is not None:
            self.role = role
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user

    @property
    def active(self):
        """Gets the active of this InlineResponse20022.  # noqa: E501


        :return: The active of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse20022.


        :param active: The active of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def organization(self):
        """Gets the organization of this InlineResponse20022.  # noqa: E501


        :return: The organization of this InlineResponse20022.  # noqa: E501
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this InlineResponse20022.


        :param organization: The organization of this InlineResponse20022.  # noqa: E501
        :type: Organization
        """

        self._organization = organization

    @property
    def organization_url(self):
        """Gets the organization_url of this InlineResponse20022.  # noqa: E501


        :return: The organization_url of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._organization_url

    @organization_url.setter
    def organization_url(self, organization_url):
        """Sets the organization_url of this InlineResponse20022.


        :param organization_url: The organization_url of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._organization_url = organization_url

    @property
    def remark(self):
        """Gets the remark of this InlineResponse20022.  # noqa: E501


        :return: The remark of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this InlineResponse20022.


        :param remark: The remark of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def role(self):
        """Gets the role of this InlineResponse20022.  # noqa: E501


        :return: The role of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse20022.


        :param role: The role of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def url(self):
        """Gets the url of this InlineResponse20022.  # noqa: E501


        :return: The url of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20022.


        :param url: The url of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this InlineResponse20022.  # noqa: E501


        :return: The user of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineResponse20022.


        :param user: The user of this InlineResponse20022.  # noqa: E501
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
        if issubclass(InlineResponse20022, dict):
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
        if not isinstance(other, InlineResponse20022):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
