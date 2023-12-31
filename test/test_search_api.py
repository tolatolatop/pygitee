# coding: utf-8

"""
    getV5ReposOwnerRepoSubscribers

    列出 watch 了仓库的用户  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pygitee
from pygitee.api.search_api import SearchApi  # noqa: E501
from pygitee.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enterprises_enterprise_members_search_get(self):
        """Test case for enterprises_enterprise_members_search_get

        获取企业成员信息(通过用户名/邮箱)  # noqa: E501
        """
        pass

    def test_search_issues_get(self):
        """Test case for search_issues_get

        搜索 Issues  # noqa: E501
        """
        pass

    def test_search_repositories_get(self):
        """Test case for search_repositories_get

        搜索仓库  # noqa: E501
        """
        pass

    def test_search_users_get(self):
        """Test case for search_users_get

        搜索用户  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
