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
from pygitee.api.default_api import DefaultApi  # noqa: E501
from pygitee.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_emails_get(self):
        """Test case for emails_get

        获取授权用户的全部邮箱  # noqa: E501
        """
        pass

    def test_emojis_get(self):
        """Test case for emojis_get

        列出可使用的 Emoji  # noqa: E501
        """
        pass

    def test_enterprise_enterprise_pull_requests_get(self):
        """Test case for enterprise_enterprise_pull_requests_get

        企业 Pull Request 列表  # noqa: E501
        """
        pass

    def test_gitignore_templates_get(self):
        """Test case for gitignore_templates_get

        列出可使用的 .gitignore 模板  # noqa: E501
        """
        pass

    def test_gitignore_templates_name_get(self):
        """Test case for gitignore_templates_name_get

        获取一个 .gitignore 模板  # noqa: E501
        """
        pass

    def test_gitignore_templates_name_raw_get(self):
        """Test case for gitignore_templates_name_raw_get

        获取一个 .gitignore 模板原始文件  # noqa: E501
        """
        pass

    def test_licenses_get(self):
        """Test case for licenses_get

        列出可使用的开源许可协议  # noqa: E501
        """
        pass

    def test_licenses_license_get(self):
        """Test case for licenses_license_get

        获取一个开源许可协议  # noqa: E501
        """
        pass

    def test_licenses_license_raw_get(self):
        """Test case for licenses_license_raw_get

        获取一个开源许可协议原始文件  # noqa: E501
        """
        pass

    def test_markdown_post(self):
        """Test case for markdown_post

        渲染 Markdown 文本  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
