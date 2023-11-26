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


class ReleasesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def repos_owner_repo_releases_get(self, owner, repo, **kwargs):  # noqa: E501
        """获取仓库的所有Releases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_get(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str direction: 可选。升序/降序。不填为升序
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_get_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_get_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_get_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """获取仓库的所有Releases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_get_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :param int page: 当前的页码
        :param int per_page: 每页的数量，最大为 100
        :param str direction: 可选。升序/降序。不填为升序
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'access_token', 'page', 'per_page', 'direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_get`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501

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
            '/repos/{owner}/{repo}/releases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repos_owner_repo_releases_id_delete(self, owner, repo, **kwargs):  # noqa: E501
        """删除仓库Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_id_delete(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_id_delete_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_id_delete_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_id_delete_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """删除仓库Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_id_delete_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_id_delete`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

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
            '/repos/{owner}/{repo}/releases/{id}', 'DELETE',
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

    def repos_owner_repo_releases_id_get(self, owner, repo, id, **kwargs):  # noqa: E501
        """获取仓库的单个Releases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_id_get(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: 发行版本的ID (required)
        :param str access_token: 用户授权码
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_id_get_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_id_get_with_http_info(owner, repo, id, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_id_get_with_http_info(self, owner, repo, id, **kwargs):  # noqa: E501
        """获取仓库的单个Releases  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_id_get_with_http_info(owner, repo, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param int id: 发行版本的ID (required)
        :param str access_token: 用户授权码
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_id_get`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_id_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `repos_owner_repo_releases_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/repos/{owner}/{repo}/releases/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repos_owner_repo_releases_id_patch(self, owner, repo, **kwargs):  # noqa: E501
        """更新仓库Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_id_patch(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param ReleasesIdBody body:
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_id_patch_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_id_patch_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_id_patch_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """更新仓库Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_id_patch_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param ReleasesIdBody body:
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_id_patch`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repo}/releases/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repos_owner_repo_releases_latest_get(self, owner, repo, **kwargs):  # noqa: E501
        """获取仓库的最后更新的Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_latest_get(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_latest_get_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_latest_get_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_latest_get_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """获取仓库的最后更新的Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_latest_get_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str access_token: 用户授权码
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_latest_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_latest_get`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_latest_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

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
            '/repos/{owner}/{repo}/releases/latest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repos_owner_repo_releases_post(self, owner, repo, **kwargs):  # noqa: E501
        """创建仓库Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_post(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param RepoReleasesBody body:
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_post_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_post_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_post_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """创建仓库Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_post_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param RepoReleasesBody body:
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_post`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['access_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repo}/releases', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repos_owner_repo_releases_tags_tag_get(self, owner, repo, tag, **kwargs):  # noqa: E501
        """根据Tag名称获取仓库的Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_tags_tag_get(owner, repo, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str tag: Tag 名称 (required)
        :param str access_token: 用户授权码
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repos_owner_repo_releases_tags_tag_get_with_http_info(owner, repo, tag, **kwargs)  # noqa: E501
        else:
            (data) = self.repos_owner_repo_releases_tags_tag_get_with_http_info(owner, repo, tag, **kwargs)  # noqa: E501
            return data

    def repos_owner_repo_releases_tags_tag_get_with_http_info(self, owner, repo, tag, **kwargs):  # noqa: E501
        """根据Tag名称获取仓库的Release  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repos_owner_repo_releases_tags_tag_get_with_http_info(owner, repo, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: 仓库所属空间地址(企业、组织或个人的地址path) (required)
        :param str repo: 仓库路径(path) (required)
        :param str tag: Tag 名称 (required)
        :param str access_token: 用户授权码
        :return: InlineResponse20048
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'tag', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repos_owner_repo_releases_tags_tag_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `repos_owner_repo_releases_tags_tag_get`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repos_owner_repo_releases_tags_tag_get`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `repos_owner_repo_releases_tags_tag_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'tag' in params:
            path_params['tag'] = params['tag']  # noqa: E501

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
            '/repos/{owner}/{repo}/releases/tags/{tag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20048',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
