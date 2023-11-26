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

class InlineResponse20039(object):
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
        'created_at': 'str',
        'id': 'str',
        'issues_events': 'str',
        'merge_requests_events': 'str',
        'note_events': 'str',
        'password': 'str',
        'project_id': 'str',
        'push_events': 'str',
        'result': 'str',
        'result_code': 'str',
        'tag_push_events': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'issues_events': 'issues_events',
        'merge_requests_events': 'merge_requests_events',
        'note_events': 'note_events',
        'password': 'password',
        'project_id': 'project_id',
        'push_events': 'push_events',
        'result': 'result',
        'result_code': 'result_code',
        'tag_push_events': 'tag_push_events',
        'url': 'url'
    }

    def __init__(self, created_at=None, id=None, issues_events=None, merge_requests_events=None, note_events=None, password=None, project_id=None, push_events=None, result=None, result_code=None, tag_push_events=None, url=None):  # noqa: E501
        """InlineResponse20039 - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._id = None
        self._issues_events = None
        self._merge_requests_events = None
        self._note_events = None
        self._password = None
        self._project_id = None
        self._push_events = None
        self._result = None
        self._result_code = None
        self._tag_push_events = None
        self._url = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if issues_events is not None:
            self.issues_events = issues_events
        if merge_requests_events is not None:
            self.merge_requests_events = merge_requests_events
        if note_events is not None:
            self.note_events = note_events
        if password is not None:
            self.password = password
        if project_id is not None:
            self.project_id = project_id
        if push_events is not None:
            self.push_events = push_events
        if result is not None:
            self.result = result
        if result_code is not None:
            self.result_code = result_code
        if tag_push_events is not None:
            self.tag_push_events = tag_push_events
        if url is not None:
            self.url = url

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20039.  # noqa: E501


        :return: The created_at of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20039.


        :param created_at: The created_at of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this InlineResponse20039.  # noqa: E501


        :return: The id of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20039.


        :param id: The id of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issues_events(self):
        """Gets the issues_events of this InlineResponse20039.  # noqa: E501


        :return: The issues_events of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._issues_events

    @issues_events.setter
    def issues_events(self, issues_events):
        """Sets the issues_events of this InlineResponse20039.


        :param issues_events: The issues_events of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._issues_events = issues_events

    @property
    def merge_requests_events(self):
        """Gets the merge_requests_events of this InlineResponse20039.  # noqa: E501


        :return: The merge_requests_events of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._merge_requests_events

    @merge_requests_events.setter
    def merge_requests_events(self, merge_requests_events):
        """Sets the merge_requests_events of this InlineResponse20039.


        :param merge_requests_events: The merge_requests_events of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._merge_requests_events = merge_requests_events

    @property
    def note_events(self):
        """Gets the note_events of this InlineResponse20039.  # noqa: E501


        :return: The note_events of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._note_events

    @note_events.setter
    def note_events(self, note_events):
        """Sets the note_events of this InlineResponse20039.


        :param note_events: The note_events of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._note_events = note_events

    @property
    def password(self):
        """Gets the password of this InlineResponse20039.  # noqa: E501


        :return: The password of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineResponse20039.


        :param password: The password of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def project_id(self):
        """Gets the project_id of this InlineResponse20039.  # noqa: E501


        :return: The project_id of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this InlineResponse20039.


        :param project_id: The project_id of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def push_events(self):
        """Gets the push_events of this InlineResponse20039.  # noqa: E501


        :return: The push_events of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._push_events

    @push_events.setter
    def push_events(self, push_events):
        """Sets the push_events of this InlineResponse20039.


        :param push_events: The push_events of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._push_events = push_events

    @property
    def result(self):
        """Gets the result of this InlineResponse20039.  # noqa: E501


        :return: The result of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse20039.


        :param result: The result of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def result_code(self):
        """Gets the result_code of this InlineResponse20039.  # noqa: E501


        :return: The result_code of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this InlineResponse20039.


        :param result_code: The result_code of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._result_code = result_code

    @property
    def tag_push_events(self):
        """Gets the tag_push_events of this InlineResponse20039.  # noqa: E501


        :return: The tag_push_events of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._tag_push_events

    @tag_push_events.setter
    def tag_push_events(self, tag_push_events):
        """Sets the tag_push_events of this InlineResponse20039.


        :param tag_push_events: The tag_push_events of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._tag_push_events = tag_push_events

    @property
    def url(self):
        """Gets the url of this InlineResponse20039.  # noqa: E501


        :return: The url of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20039.


        :param url: The url of this InlineResponse20039.  # noqa: E501
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
        if issubclass(InlineResponse20039, dict):
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
        if not isinstance(other, InlineResponse20039):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
