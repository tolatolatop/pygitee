# coding: utf-8

"""
    Gitee OpenApi

    All api provided by Gitee  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pygitee.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def enterprises_enterprise_members_search_get(self, enterprise, query_type, query_value, **kwargs):  # noqa: E501
        """获取企业成员信息(通过用户名/邮箱)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprises_enterprise_members_search_get(enterprise, query_type, query_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise: 企业的路径(path/login) (required)
        :param str query_type: 查询类型：username/email (required)
        :param str query_value: 查询值 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enterprises_enterprise_members_search_get_with_http_info(enterprise, query_type, query_value, **kwargs)  # noqa: E501
        else:
            (data) = self.enterprises_enterprise_members_search_get_with_http_info(enterprise, query_type, query_value, **kwargs)  # noqa: E501
            return data

    def enterprises_enterprise_members_search_get_with_http_info(self, enterprise, query_type, query_value, **kwargs):  # noqa: E501
        """获取企业成员信息(通过用户名/邮箱)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprises_enterprise_members_search_get_with_http_info(enterprise, query_type, query_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise: 企业的路径(path/login) (required)
        :param str query_type: 查询类型：username/email (required)
        :param str query_value: 查询值 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise', 'query_type', 'query_value', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enterprises_enterprise_members_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise' is set
        if ('enterprise' not in params or
                params['enterprise'] is None):
            raise ValueError("Missing the required parameter `enterprise` when calling `enterprises_enterprise_members_search_get`")  # noqa: E501
        # verify the required parameter 'query_type' is set
        if ('query_type' not in params or
                params['query_type'] is None):
            raise ValueError("Missing the required parameter `query_type` when calling `enterprises_enterprise_members_search_get`")  # noqa: E501
        # verify the required parameter 'query_value' is set
        if ('query_value' not in params or
                params['query_value'] is None):
            raise ValueError("Missing the required parameter `query_value` when calling `enterprises_enterprise_members_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'enterprise' in params:
            path_params['enterprise'] = params['enterprise']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'query_type' in params:
            query_params.append(('query_type', params['query_type']))  # noqa: E501
        if 'query_value' in params:
            query_params.append(('query_value', params['query_value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/enterprises/{enterprise}/members/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_issues_get(self, q, **kwargs):  # noqa: E501
        """搜索 Issues  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_issues_get(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str repo: 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues
        :param str language: 筛选指定语言的 issues
        :param str label: 筛选指定标签的 issues
        :param str state: 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝)
        :param str author: 筛选指定创建者 (username/login) 的 issues
        :param str assignee: 筛选指定负责人 (username/login) 的 issues
        :param str sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_issues_get_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.search_issues_get_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def search_issues_get_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索 Issues  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_issues_get_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str repo: 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues
        :param str language: 筛选指定语言的 issues
        :param str label: 筛选指定标签的 issues
        :param str state: 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝)
        :param str author: 筛选指定创建者 (username/login) 的 issues
        :param str assignee: 筛选指定负责人 (username/login) 的 issues
        :param str sort: 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'repo', 'language', 'label', 'state', 'author', 'assignee', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_issues_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search_issues_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'label' in params:
            query_params.append(('label', params['label']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'author' in params:
            query_params.append(('author', params['author']))  # noqa: E501
        if 'assignee' in params:
            query_params.append(('assignee', params['assignee']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/search/issues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_repositories_get(self, q, **kwargs):  # noqa: E501
        """搜索仓库  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_repositories_get(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str owner: 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库
        :param bool fork: 是否搜索含 fork 的仓库，默认：否
        :param str language: 筛选指定语言的仓库
        :param str sort: 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_repositories_get_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.search_repositories_get_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def search_repositories_get_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索仓库  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_repositories_get_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str owner: 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库
        :param bool fork: 是否搜索含 fork 的仓库，默认：否
        :param str language: 筛选指定语言的仓库
        :param str sort: 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'owner', 'fork', 'language', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_repositories_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search_repositories_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
        if 'fork' in params:
            query_params.append(('fork', params['fork']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/search/repositories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_users_get(self, q, **kwargs):  # noqa: E501
        """搜索用户  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_get(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str sort: 排序字段，joined_at(注册时间)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: InlineResponse20053
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_users_get_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.search_users_get_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def search_users_get_with_http_info(self, q, **kwargs):  # noqa: E501
        """搜索用户  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_get_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: 搜索关键字 (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str sort: 排序字段，joined_at(注册时间)，默认为最佳匹配
        :param str order: 排序顺序: desc(default)、asc
        :return: InlineResponse20053
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'access_token', 'page', 'per_page', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search_users_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/search/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20053',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
