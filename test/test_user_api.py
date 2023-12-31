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
from pygitee.api.user_api import UserApi  # noqa: E501
from pygitee.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_followers_get(self):
        """Test case for user_followers_get

        列出授权用户的关注者  # noqa: E501
        """
        pass

    def test_user_following_get(self):
        """Test case for user_following_get

        列出授权用户正关注的用户  # noqa: E501
        """
        pass

    def test_user_following_username_delete(self):
        """Test case for user_following_username_delete

        取消关注一个用户  # noqa: E501
        """
        pass

    def test_user_following_username_get(self):
        """Test case for user_following_username_get

        检查授权用户是否关注了一个用户  # noqa: E501
        """
        pass

    def test_user_following_username_put(self):
        """Test case for user_following_username_put

        关注一个用户  # noqa: E501
        """
        pass

    def test_user_get(self):
        """Test case for user_get

        获取授权用户的资料  # noqa: E501
        """
        pass

    def test_user_keys_get(self):
        """Test case for user_keys_get

        列出授权用户的所有公钥  # noqa: E501
        """
        pass

    def test_user_keys_id_delete(self):
        """Test case for user_keys_id_delete

        删除一个公钥  # noqa: E501
        """
        pass

    def test_user_keys_id_get(self):
        """Test case for user_keys_id_get

        获取一个公钥  # noqa: E501
        """
        pass

    def test_user_keys_post(self):
        """Test case for user_keys_post

        添加一个公钥  # noqa: E501
        """
        pass

    def test_user_namespace_get(self):
        """Test case for user_namespace_get

        获取授权用户的一个 Namespace  # noqa: E501
        """
        pass

    def test_user_namespaces_get(self):
        """Test case for user_namespaces_get

        列出授权用户所有的 Namespace  # noqa: E501
        """
        pass

    def test_user_patch(self):
        """Test case for user_patch

        更新授权用户的资料  # noqa: E501
        """
        pass

    def test_user_starred_get(self):
        """Test case for user_starred_get

        列出授权用户 star 了的仓库  # noqa: E501
        """
        pass

    def test_user_starred_owner_repo_delete(self):
        """Test case for user_starred_owner_repo_delete

        取消 star 一个仓库  # noqa: E501
        """
        pass

    def test_user_starred_owner_repo_get(self):
        """Test case for user_starred_owner_repo_get

        检查授权用户是否 star 了一个仓库  # noqa: E501
        """
        pass

    def test_user_starred_owner_repo_put(self):
        """Test case for user_starred_owner_repo_put

        star 一个仓库  # noqa: E501
        """
        pass

    def test_user_subscriptions_get(self):
        """Test case for user_subscriptions_get

        列出授权用户 watch 了的仓库  # noqa: E501
        """
        pass

    def test_user_subscriptions_owner_repo_delete(self):
        """Test case for user_subscriptions_owner_repo_delete

        取消 watch 一个仓库  # noqa: E501
        """
        pass

    def test_user_subscriptions_owner_repo_get(self):
        """Test case for user_subscriptions_owner_repo_get

        检查授权用户是否 watch 了一个仓库  # noqa: E501
        """
        pass

    def test_user_subscriptions_owner_repo_put(self):
        """Test case for user_subscriptions_owner_repo_put

        watch 一个仓库  # noqa: E501
        """
        pass

    def test_users_organization_post(self):
        """Test case for users_organization_post

        创建组织  # noqa: E501
        """
        pass

    def test_users_username_events_get(self):
        """Test case for users_username_events_get

        列出用户的动态  # noqa: E501
        """
        pass

    def test_users_username_events_public_get(self):
        """Test case for users_username_events_public_get

        列出用户的公开动态  # noqa: E501
        """
        pass

    def test_users_username_followers_get(self):
        """Test case for users_username_followers_get

        列出指定用户的关注者  # noqa: E501
        """
        pass

    def test_users_username_following_get(self):
        """Test case for users_username_following_get

        列出指定用户正在关注的用户  # noqa: E501
        """
        pass

    def test_users_username_following_target_user_get(self):
        """Test case for users_username_following_target_user_get

        检查指定用户是否关注目标用户  # noqa: E501
        """
        pass

    def test_users_username_get(self):
        """Test case for users_username_get

        获取一个用户  # noqa: E501
        """
        pass

    def test_users_username_keys_get(self):
        """Test case for users_username_keys_get

        列出指定用户的所有公钥  # noqa: E501
        """
        pass

    def test_users_username_received_events_get(self):
        """Test case for users_username_received_events_get

        列出一个用户收到的动态  # noqa: E501
        """
        pass

    def test_users_username_received_events_public_get(self):
        """Test case for users_username_received_events_public_get

        列出一个用户收到的公开动态  # noqa: E501
        """
        pass

    def test_users_username_starred_get(self):
        """Test case for users_username_starred_get

        列出用户 star 了的仓库  # noqa: E501
        """
        pass

    def test_users_username_subscriptions_get(self):
        """Test case for users_username_subscriptions_get

        列出用户 watch 了的仓库  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
