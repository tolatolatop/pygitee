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

class Parents(object):
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
        'sha': 'str',
        'shas': 'object',
        'url': 'str'
    }

    attribute_map = {
        'sha': 'sha',
        'shas': 'shas',
        'url': 'url'
    }

    def __init__(self, sha=None, shas=None, url=None):  # noqa: E501
        """Parents - a model defined in Swagger"""  # noqa: E501
        self._sha = None
        self._shas = None
        self._url = None
        self.discriminator = None
        if sha is not None:
            self.sha = sha
        if shas is not None:
            self.shas = shas
        if url is not None:
            self.url = url

    @property
    def sha(self):
        """Gets the sha of this Parents.  # noqa: E501


        :return: The sha of this Parents.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Parents.


        :param sha: The sha of this Parents.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def shas(self):
        """Gets the shas of this Parents.  # noqa: E501


        :return: The shas of this Parents.  # noqa: E501
        :rtype: object
        """
        return self._shas

    @shas.setter
    def shas(self, shas):
        """Sets the shas of this Parents.


        :param shas: The shas of this Parents.  # noqa: E501
        :type: object
        """

        self._shas = shas

    @property
    def url(self):
        """Gets the url of this Parents.  # noqa: E501


        :return: The url of this Parents.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Parents.


        :param url: The url of this Parents.  # noqa: E501
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
        if issubclass(Parents, dict):
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
        if not isinstance(other, Parents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
