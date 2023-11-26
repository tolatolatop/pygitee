# coding: utf-8

"""
    Gitee OpenApi

    All api provided by Gitee  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pygitee
from pygitee.api.releases_api import ReleasesApi  # noqa: E501
from pygitee.rest import ApiException


class TestReleasesApi(unittest.TestCase):
    """ReleasesApi unit test stubs"""

    def setUp(self):
        self.api = ReleasesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_repos_owner_repo_releases_get(self):
        """Test case for repos_owner_repo_releases_get

        获取仓库的所有Releases  # noqa: E501
        """
        pass

    def test_repos_owner_repo_releases_id_get(self):
        """Test case for repos_owner_repo_releases_id_get

        获取仓库的单个Releases  # noqa: E501
        """
        pass

    def test_repos_owner_repo_releases_latest_get(self):
        """Test case for repos_owner_repo_releases_latest_get

        获取仓库的最后更新的Release  # noqa: E501
        """
        pass

    def test_repos_owner_repo_releases_tags_tag_get(self):
        """Test case for repos_owner_repo_releases_tags_tag_get

        根据Tag名称获取仓库的Release  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
