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

class RepoReviewerBody(object):
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
        'assignees': 'str',
        'assignees_number': 'int',
        'testers': 'str',
        'testers_number': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'assignees': 'assignees',
        'assignees_number': 'assignees_number',
        'testers': 'testers',
        'testers_number': 'testers_number'
    }

    def __init__(self, access_token=None, assignees=None, assignees_number=None, testers=None, testers_number=None):  # noqa: E501
        """RepoReviewerBody - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._assignees = None
        self._assignees_number = None
        self._testers = None
        self._testers_number = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.assignees = assignees
        self.assignees_number = assignees_number
        self.testers = testers
        self.testers_number = testers_number

    @property
    def access_token(self):
        """Gets the access_token of this RepoReviewerBody.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this RepoReviewerBody.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this RepoReviewerBody.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this RepoReviewerBody.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def assignees(self):
        """Gets the assignees of this RepoReviewerBody.  # noqa: E501

        审查人员username，可多个，半角逗号分隔，如：(username1,username2)  # noqa: E501

        :return: The assignees of this RepoReviewerBody.  # noqa: E501
        :rtype: str
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this RepoReviewerBody.

        审查人员username，可多个，半角逗号分隔，如：(username1,username2)  # noqa: E501

        :param assignees: The assignees of this RepoReviewerBody.  # noqa: E501
        :type: str
        """
        if assignees is None:
            raise ValueError("Invalid value for `assignees`, must not be `None`")  # noqa: E501

        self._assignees = assignees

    @property
    def assignees_number(self):
        """Gets the assignees_number of this RepoReviewerBody.  # noqa: E501

        最少审查人数  # noqa: E501

        :return: The assignees_number of this RepoReviewerBody.  # noqa: E501
        :rtype: int
        """
        return self._assignees_number

    @assignees_number.setter
    def assignees_number(self, assignees_number):
        """Sets the assignees_number of this RepoReviewerBody.

        最少审查人数  # noqa: E501

        :param assignees_number: The assignees_number of this RepoReviewerBody.  # noqa: E501
        :type: int
        """
        if assignees_number is None:
            raise ValueError("Invalid value for `assignees_number`, must not be `None`")  # noqa: E501

        self._assignees_number = assignees_number

    @property
    def testers(self):
        """Gets the testers of this RepoReviewerBody.  # noqa: E501

        测试人员username，可多个，半角逗号分隔，如：(username1,username2)  # noqa: E501

        :return: The testers of this RepoReviewerBody.  # noqa: E501
        :rtype: str
        """
        return self._testers

    @testers.setter
    def testers(self, testers):
        """Sets the testers of this RepoReviewerBody.

        测试人员username，可多个，半角逗号分隔，如：(username1,username2)  # noqa: E501

        :param testers: The testers of this RepoReviewerBody.  # noqa: E501
        :type: str
        """
        if testers is None:
            raise ValueError("Invalid value for `testers`, must not be `None`")  # noqa: E501

        self._testers = testers

    @property
    def testers_number(self):
        """Gets the testers_number of this RepoReviewerBody.  # noqa: E501

        最少测试人数  # noqa: E501

        :return: The testers_number of this RepoReviewerBody.  # noqa: E501
        :rtype: int
        """
        return self._testers_number

    @testers_number.setter
    def testers_number(self, testers_number):
        """Sets the testers_number of this RepoReviewerBody.

        最少测试人数  # noqa: E501

        :param testers_number: The testers_number of this RepoReviewerBody.  # noqa: E501
        :type: int
        """
        if testers_number is None:
            raise ValueError("Invalid value for `testers_number`, must not be `None`")  # noqa: E501

        self._testers_number = testers_number

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
        if issubclass(RepoReviewerBody, dict):
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
        if not isinstance(other, RepoReviewerBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other