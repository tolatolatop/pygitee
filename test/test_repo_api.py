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
from pygitee.api.repo_api import RepoApi  # noqa: E501
from pygitee.rest import ApiException


class TestRepoApi(unittest.TestCase):
    """RepoApi unit test stubs"""

    def setUp(self):
        self.api = RepoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_networks_owner_repo_events_get(self):
        """Test case for networks_owner_repo_events_get

        列出仓库的所有公开动态  # noqa: E501
        """
        pass

    def test_repos_owner_repo_baidu_statistic_key_get(self):
        """Test case for repos_owner_repo_baidu_statistic_key_get

        获取仓库的百度统计 key  # noqa: E501
        """
        pass

    def test_repos_owner_repo_blame_path_get(self):
        """Test case for repos_owner_repo_blame_path_get

        Blame  # noqa: E501
        """
        pass

    def test_repos_owner_repo_branches_branch_get(self):
        """Test case for repos_owner_repo_branches_branch_get

        获取单个分支  # noqa: E501
        """
        pass

    def test_repos_owner_repo_branches_branch_protection_put(self):
        """Test case for repos_owner_repo_branches_branch_protection_put

        设置分支保护  # noqa: E501
        """
        pass

    def test_repos_owner_repo_branches_get(self):
        """Test case for repos_owner_repo_branches_get

        获取所有分支  # noqa: E501
        """
        pass

    def test_repos_owner_repo_branches_setting_new_put(self):
        """Test case for repos_owner_repo_branches_setting_new_put

        新建保护分支规则  # noqa: E501
        """
        pass

    def test_repos_owner_repo_branches_wildcard_setting_put(self):
        """Test case for repos_owner_repo_branches_wildcard_setting_put

        更新保护分支规则  # noqa: E501
        """
        pass

    def test_repos_owner_repo_clear_put(self):
        """Test case for repos_owner_repo_clear_put

        清空一个仓库  # noqa: E501
        """
        pass

    def test_repos_owner_repo_collaborators_get(self):
        """Test case for repos_owner_repo_collaborators_get

        获取仓库的所有成员  # noqa: E501
        """
        pass

    def test_repos_owner_repo_collaborators_username_get(self):
        """Test case for repos_owner_repo_collaborators_username_get

        判断用户是否为仓库成员  # noqa: E501
        """
        pass

    def test_repos_owner_repo_collaborators_username_permission_get(self):
        """Test case for repos_owner_repo_collaborators_username_permission_get

        查看仓库成员的权限  # noqa: E501
        """
        pass

    def test_repos_owner_repo_commits_get(self):
        """Test case for repos_owner_repo_commits_get

        仓库的所有提交  # noqa: E501
        """
        pass

    def test_repos_owner_repo_commits_sha_get(self):
        """Test case for repos_owner_repo_commits_sha_get

        仓库的某个提交  # noqa: E501
        """
        pass

    def test_repos_owner_repo_compare_base_head_get(self):
        """Test case for repos_owner_repo_compare_base_head_get

        Commits 对比  # noqa: E501
        """
        pass

    def test_repos_owner_repo_contents_path_get(self):
        """Test case for repos_owner_repo_contents_path_get

        获取仓库具体路径下的内容  # noqa: E501
        """
        pass

    def test_repos_owner_repo_contents_path_post(self):
        """Test case for repos_owner_repo_contents_path_post

        新建文件  # noqa: E501
        """
        pass

    def test_repos_owner_repo_contributors_get(self):
        """Test case for repos_owner_repo_contributors_get

        获取仓库贡献者  # noqa: E501
        """
        pass

    def test_repos_owner_repo_events_get(self):
        """Test case for repos_owner_repo_events_get

        列出仓库的所有动态  # noqa: E501
        """
        pass

    def test_repos_owner_repo_forks_get(self):
        """Test case for repos_owner_repo_forks_get

        查看仓库的Forks  # noqa: E501
        """
        pass

    def test_repos_owner_repo_get(self):
        """Test case for repos_owner_repo_get

        获取用户的某个仓库  # noqa: E501
        """
        pass

    def test_repos_owner_repo_git_blobs_sha_get(self):
        """Test case for repos_owner_repo_git_blobs_sha_get

        获取文件Blob  # noqa: E501
        """
        pass

    def test_repos_owner_repo_git_gitee_metrics_get(self):
        """Test case for repos_owner_repo_git_gitee_metrics_get

        获取 Gitee 指数  # noqa: E501
        """
        pass

    def test_repos_owner_repo_git_trees_sha_get(self):
        """Test case for repos_owner_repo_git_trees_sha_get

        获取目录Tree  # noqa: E501
        """
        pass

    def test_repos_owner_repo_keys_available_get(self):
        """Test case for repos_owner_repo_keys_available_get

        获取仓库可部署的公钥  # noqa: E501
        """
        pass

    def test_repos_owner_repo_keys_enable_id_put(self):
        """Test case for repos_owner_repo_keys_enable_id_put

        启用仓库公钥  # noqa: E501
        """
        pass

    def test_repos_owner_repo_keys_get(self):
        """Test case for repos_owner_repo_keys_get

        获取仓库已部署的公钥  # noqa: E501
        """
        pass

    def test_repos_owner_repo_keys_id_get(self):
        """Test case for repos_owner_repo_keys_id_get

        获取仓库的单个公钥  # noqa: E501
        """
        pass

    def test_repos_owner_repo_labels_get(self):
        """Test case for repos_owner_repo_labels_get

        获取仓库所有任务标签  # noqa: E501
        """
        pass

    def test_repos_owner_repo_labels_name_get(self):
        """Test case for repos_owner_repo_labels_name_get

        根据标签名称获取单个标签  # noqa: E501
        """
        pass

    def test_repos_owner_repo_labels_original_name_patch(self):
        """Test case for repos_owner_repo_labels_original_name_patch

        更新一个仓库任务标签  # noqa: E501
        """
        pass

    def test_repos_owner_repo_license_get(self):
        """Test case for repos_owner_repo_license_get

        获取一个仓库使用的开源许可协议  # noqa: E501
        """
        pass

    def test_repos_owner_repo_milestones_get(self):
        """Test case for repos_owner_repo_milestones_get

        获取仓库所有里程碑  # noqa: E501
        """
        pass

    def test_repos_owner_repo_milestones_number_get(self):
        """Test case for repos_owner_repo_milestones_number_get

        获取仓库单个里程碑  # noqa: E501
        """
        pass

    def test_repos_owner_repo_open_post(self):
        """Test case for repos_owner_repo_open_post

        开通Gitee Go  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pages_builds_post(self):
        """Test case for repos_owner_repo_pages_builds_post

        请求建立Pages  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pages_get(self):
        """Test case for repos_owner_repo_pages_get

        获取Pages信息  # noqa: E501
        """
        pass

    def test_repos_owner_repo_project_labels_get(self):
        """Test case for repos_owner_repo_project_labels_get

        获取仓库所有标签  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_get(self):
        """Test case for repos_owner_repo_pulls_get

        获取Pull Request列表  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_assignees_post(self):
        """Test case for repos_owner_repo_pulls_number_assignees_post

        指派用户审查 Pull Request  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_commits_get(self):
        """Test case for repos_owner_repo_pulls_number_commits_get

        获取某Pull Request的所有Commit信息。最多显示250条Commit  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_files_get(self):
        """Test case for repos_owner_repo_pulls_number_files_get

        Pull Request Commit文件列表。最多显示300条diff  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_get(self):
        """Test case for repos_owner_repo_pulls_number_get

        获取单个Pull Request  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_labels_get(self):
        """Test case for repos_owner_repo_pulls_number_labels_get

        获取某个 Pull Request 的所有标签  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_labels_name_delete(self):
        """Test case for repos_owner_repo_pulls_number_labels_name_delete

        删除 Pull Request 标签  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_merge_get(self):
        """Test case for repos_owner_repo_pulls_number_merge_get

        判断Pull Request是否已经合并  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_operate_logs_get(self):
        """Test case for repos_owner_repo_pulls_number_operate_logs_get

        获取某个Pull Request的操作日志  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_review_post(self):
        """Test case for repos_owner_repo_pulls_number_review_post

        处理 Pull Request 审查  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_test_post(self):
        """Test case for repos_owner_repo_pulls_number_test_post

        处理 Pull Request 测试  # noqa: E501
        """
        pass

    def test_repos_owner_repo_pulls_number_testers_post(self):
        """Test case for repos_owner_repo_pulls_number_testers_post

        指派用户测试 Pull Request  # noqa: E501
        """
        pass

    def test_repos_owner_repo_push_config_get(self):
        """Test case for repos_owner_repo_push_config_get

        获取仓库推送规则设置  # noqa: E501
        """
        pass

    def test_repos_owner_repo_raw_path_get(self):
        """Test case for repos_owner_repo_raw_path_get

        获取 raw 文件（100MB 以内）  # noqa: E501
        """
        pass

    def test_repos_owner_repo_readme_get(self):
        """Test case for repos_owner_repo_readme_get

        获取仓库README  # noqa: E501
        """
        pass

    def test_repos_owner_repo_reviewer_put(self):
        """Test case for repos_owner_repo_reviewer_put

        修改代码审查设置  # noqa: E501
        """
        pass

    def test_repos_owner_repo_stargazers_get(self):
        """Test case for repos_owner_repo_stargazers_get

        列出 star 了仓库的用户  # noqa: E501
        """
        pass

    def test_repos_owner_repo_subscribers_get(self):
        """Test case for repos_owner_repo_subscribers_get

        列出 watch 了仓库的用户  # noqa: E501
        """
        pass

    def test_repos_owner_repo_tags_get(self):
        """Test case for repos_owner_repo_tags_get

        列出仓库所有的tags  # noqa: E501
        """
        pass

    def test_repos_owner_repo_tarball_get(self):
        """Test case for repos_owner_repo_tarball_get

        下载仓库 tar.gz  # noqa: E501
        """
        pass

    def test_repos_owner_repo_traffic_data_post(self):
        """Test case for repos_owner_repo_traffic_data_post

        获取最近30天的七日以内访问量  # noqa: E501
        """
        pass

    def test_repos_owner_repo_zipball_get(self):
        """Test case for repos_owner_repo_zipball_get

        下载仓库 zip  # noqa: E501
        """
        pass

    def test_user_repos_get(self):
        """Test case for user_repos_get

        列出授权用户的所有仓库  # noqa: E501
        """
        pass

    def test_users_username_repos_get(self):
        """Test case for users_username_repos_get

        获取某个用户的公开仓库  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()