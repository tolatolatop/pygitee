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
from pygitee.api.week_report_api import WeekReportApi  # noqa: E501
from pygitee.rest import ApiException


class TestWeekReportApi(unittest.TestCase):
    """WeekReportApi unit test stubs"""

    def setUp(self):
        self.api = WeekReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enterprises_enterprise_users_username_week_reports_get(self):
        """Test case for enterprises_enterprise_users_username_week_reports_get

        个人周报列表  # noqa: E501
        """
        pass

    def test_enterprises_enterprise_week_report_id_patch(self):
        """Test case for enterprises_enterprise_week_report_id_patch

        编辑周报  # noqa: E501
        """
        pass

    def test_enterprises_enterprise_week_report_post(self):
        """Test case for enterprises_enterprise_week_report_post

        新建周报  # noqa: E501
        """
        pass

    def test_enterprises_enterprise_week_reports_get(self):
        """Test case for enterprises_enterprise_week_reports_get

        企业成员周报列表  # noqa: E501
        """
        pass

    def test_enterprises_enterprise_week_reports_id_get(self):
        """Test case for enterprises_enterprise_week_reports_id_get

        周报详情  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
