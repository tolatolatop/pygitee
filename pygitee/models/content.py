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

class Content(object):
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
        'links': 'str',
        'download_url': 'str',
        'html_url': 'str',
        'name': 'str',
        'path': 'str',
        'sha': 'str',
        'size': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'links': '_links',
        'download_url': 'download_url',
        'html_url': 'html_url',
        'name': 'name',
        'path': 'path',
        'sha': 'sha',
        'size': 'size',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, links=None, download_url=None, html_url=None, name=None, path=None, sha=None, size=None, type=None, url=None):  # noqa: E501
        """Content - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._download_url = None
        self._html_url = None
        self._name = None
        self._path = None
        self._sha = None
        self._size = None
        self._type = None
        self._url = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if download_url is not None:
            self.download_url = download_url
        if html_url is not None:
            self.html_url = html_url
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if sha is not None:
            self.sha = sha
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def links(self):
        """Gets the links of this Content.  # noqa: E501


        :return: The links of this Content.  # noqa: E501
        :rtype: str
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Content.


        :param links: The links of this Content.  # noqa: E501
        :type: str
        """

        self._links = links

    @property
    def download_url(self):
        """Gets the download_url of this Content.  # noqa: E501


        :return: The download_url of this Content.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this Content.


        :param download_url: The download_url of this Content.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def html_url(self):
        """Gets the html_url of this Content.  # noqa: E501


        :return: The html_url of this Content.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Content.


        :param html_url: The html_url of this Content.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def name(self):
        """Gets the name of this Content.  # noqa: E501


        :return: The name of this Content.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Content.


        :param name: The name of this Content.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this Content.  # noqa: E501


        :return: The path of this Content.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Content.


        :param path: The path of this Content.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def sha(self):
        """Gets the sha of this Content.  # noqa: E501


        :return: The sha of this Content.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Content.


        :param sha: The sha of this Content.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def size(self):
        """Gets the size of this Content.  # noqa: E501


        :return: The size of this Content.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Content.


        :param size: The size of this Content.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this Content.  # noqa: E501


        :return: The type of this Content.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Content.


        :param type: The type of this Content.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this Content.  # noqa: E501


        :return: The url of this Content.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Content.


        :param url: The url of this Content.  # noqa: E501
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
        if issubclass(Content, dict):
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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other