# coding: utf-8

"""
    Gitee OpenApi

    All api provided by Gitee  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pygitee.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def emails_get(self, **kwargs):  # noqa: E501
        """获取授权用户的全部邮箱  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emails_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.emails_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.emails_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def emails_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取授权用户的全部邮箱  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emails_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emails_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

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
            '/emails', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def emojis_get(self, **kwargs):  # noqa: E501
        """列出可使用的 Emoji  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emojis_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.emojis_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.emojis_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def emojis_get_with_http_info(self, **kwargs):  # noqa: E501
        """列出可使用的 Emoji  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emojis_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emojis_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/emojis', 'GET',
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

    def enterprise_enterprise_pull_requests_get(self, enterprise, **kwargs):  # noqa: E501
        """企业 Pull Request 列表  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprise_enterprise_pull_requests_get(enterprise, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise: 企业的路径(path/login) (required)
        :param str access_token: 用户授权码
        :param str issue_number: 可选。Issue 编号(区分大小写，无需添加 # 号)
        :param str repo: 可选。仓库路径(path)
        :param int program_id: 可选。项目ID
        :param str state: 可选。Pull Request 状态
        :param str head: 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch
        :param str base: 可选。Pull Request 提交目标分支的名称。
        :param str sort: 可选。排序字段，默认按创建时间
        :param str since: 可选。起始的更新时间，要求时间格式为 ISO 8601
        :param str direction: 可选。升序/降序
        :param int milestone_number: 可选。里程碑序号(id)
        :param str labels: 用逗号分开的标签。如: bug,performance
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enterprise_enterprise_pull_requests_get_with_http_info(enterprise, **kwargs)  # noqa: E501
        else:
            (data) = self.enterprise_enterprise_pull_requests_get_with_http_info(enterprise, **kwargs)  # noqa: E501
            return data

    def enterprise_enterprise_pull_requests_get_with_http_info(self, enterprise, **kwargs):  # noqa: E501
        """企业 Pull Request 列表  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enterprise_enterprise_pull_requests_get_with_http_info(enterprise, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise: 企业的路径(path/login) (required)
        :param str access_token: 用户授权码
        :param str issue_number: 可选。Issue 编号(区分大小写，无需添加 # 号)
        :param str repo: 可选。仓库路径(path)
        :param int program_id: 可选。项目ID
        :param str state: 可选。Pull Request 状态
        :param str head: 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch
        :param str base: 可选。Pull Request 提交目标分支的名称。
        :param str sort: 可选。排序字段，默认按创建时间
        :param str since: 可选。起始的更新时间，要求时间格式为 ISO 8601
        :param str direction: 可选。升序/降序
        :param int milestone_number: 可选。里程碑序号(id)
        :param str labels: 用逗号分开的标签。如: bug,performance
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise', 'access_token', 'issue_number', 'repo', 'program_id', 'state', 'head', 'base', 'sort', 'since', 'direction', 'milestone_number', 'labels', 'page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enterprise_enterprise_pull_requests_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise' is set
        if ('enterprise' not in params or
                params['enterprise'] is None):
            raise ValueError("Missing the required parameter `enterprise` when calling `enterprise_enterprise_pull_requests_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'enterprise' in params:
            path_params['enterprise'] = params['enterprise']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'issue_number' in params:
            query_params.append(('issue_number', params['issue_number']))  # noqa: E501
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501
        if 'program_id' in params:
            query_params.append(('program_id', params['program_id']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'head' in params:
            query_params.append(('head', params['head']))  # noqa: E501
        if 'base' in params:
            query_params.append(('base', params['base']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'since' in params:
            query_params.append(('since', params['since']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501
        if 'milestone_number' in params:
            query_params.append(('milestone_number', params['milestone_number']))  # noqa: E501
        if 'labels' in params:
            query_params.append(('labels', params['labels']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

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
            '/enterprise/{enterprise}/pull_requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gitignore_templates_get(self, **kwargs):  # noqa: E501
        """列出可使用的 .gitignore 模板  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gitignore_templates_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gitignore_templates_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.gitignore_templates_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def gitignore_templates_get_with_http_info(self, **kwargs):  # noqa: E501
        """列出可使用的 .gitignore 模板  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gitignore_templates_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gitignore_templates_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/gitignore/templates', 'GET',
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

    def gitignore_templates_name_get(self, name, **kwargs):  # noqa: E501
        """获取一个 .gitignore 模板  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gitignore_templates_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: .gitignore 模板名 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gitignore_templates_name_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.gitignore_templates_name_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def gitignore_templates_name_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """获取一个 .gitignore 模板  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gitignore_templates_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: .gitignore 模板名 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gitignore_templates_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `gitignore_templates_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/gitignore/templates/{name}', 'GET',
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

    def gitignore_templates_name_raw_get(self, name, **kwargs):  # noqa: E501
        """获取一个 .gitignore 模板原始文件  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gitignore_templates_name_raw_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: .gitignore 模板名 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gitignore_templates_name_raw_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.gitignore_templates_name_raw_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def gitignore_templates_name_raw_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """获取一个 .gitignore 模板原始文件  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gitignore_templates_name_raw_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: .gitignore 模板名 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gitignore_templates_name_raw_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `gitignore_templates_name_raw_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/gitignore/templates/{name}/raw', 'GET',
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

    def licenses_get(self, **kwargs):  # noqa: E501
        """列出可使用的开源许可协议  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.licenses_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.licenses_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def licenses_get_with_http_info(self, **kwargs):  # noqa: E501
        """列出可使用的开源许可协议  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method licenses_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/licenses', 'GET',
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

    def licenses_license_get(self, license, **kwargs):  # noqa: E501
        """获取一个开源许可协议  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_license_get(license, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license: 协议名称 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.licenses_license_get_with_http_info(license, **kwargs)  # noqa: E501
        else:
            (data) = self.licenses_license_get_with_http_info(license, **kwargs)  # noqa: E501
            return data

    def licenses_license_get_with_http_info(self, license, **kwargs):  # noqa: E501
        """获取一个开源许可协议  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_license_get_with_http_info(license, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license: 协议名称 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method licenses_license_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license' is set
        if ('license' not in params or
                params['license'] is None):
            raise ValueError("Missing the required parameter `license` when calling `licenses_license_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'license' in params:
            path_params['license'] = params['license']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/licenses/{license}', 'GET',
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

    def licenses_license_raw_get(self, license, **kwargs):  # noqa: E501
        """获取一个开源许可协议原始文件  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_license_raw_get(license, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license: 协议名称 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.licenses_license_raw_get_with_http_info(license, **kwargs)  # noqa: E501
        else:
            (data) = self.licenses_license_raw_get_with_http_info(license, **kwargs)  # noqa: E501
            return data

    def licenses_license_raw_get_with_http_info(self, license, **kwargs):  # noqa: E501
        """获取一个开源许可协议原始文件  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_license_raw_get_with_http_info(license, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license: 协议名称 (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method licenses_license_raw_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license' is set
        if ('license' not in params or
                params['license'] is None):
            raise ValueError("Missing the required parameter `license` when calling `licenses_license_raw_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'license' in params:
            path_params['license'] = params['license']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/licenses/{license}/raw', 'GET',
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

    def markdown_post(self, **kwargs):  # noqa: E501
        """渲染 Markdown 文本  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.markdown_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MarkdownBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.markdown_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.markdown_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def markdown_post_with_http_info(self, **kwargs):  # noqa: E501
        """渲染 Markdown 文本  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.markdown_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MarkdownBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method markdown_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/markdown', 'POST',
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
