# pygitee.SearchApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprises_enterprise_members_search_get**](SearchApi.md#enterprises_enterprise_members_search_get) | **GET** /enterprises/{enterprise}/members/search | 获取企业成员信息(通过用户名/邮箱)
[**search_issues_get**](SearchApi.md#search_issues_get) | **GET** /search/issues | 搜索 Issues
[**search_repositories_get**](SearchApi.md#search_repositories_get) | **GET** /search/repositories | 搜索仓库
[**search_users_get**](SearchApi.md#search_users_get) | **GET** /search/users | 搜索用户

# **enterprises_enterprise_members_search_get**
> enterprises_enterprise_members_search_get(enterprise, query_type, query_value, access_token=access_token)

获取企业成员信息(通过用户名/邮箱)

### Example
```python
from __future__ import print_function
import time
import pygitee
from pygitee.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = pygitee.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = pygitee.SearchApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
query_type = 'query_type_example' # str | 查询类型：username/email
query_value = 'query_value_example' # str | 查询值
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业成员信息(通过用户名/邮箱)
    api_instance.enterprises_enterprise_members_search_get(enterprise, query_type, query_value, access_token=access_token)
except ApiException as e:
    print("Exception when calling SearchApi->enterprises_enterprise_members_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **query_type** | **str**| 查询类型：username/email | 
 **query_value** | **str**| 查询值 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_issues_get**
> InlineResponse2003 search_issues_get(q, access_token=access_token, page=page, per_page=per_page, repo=repo, language=language, label=label, state=state, author=author, assignee=assignee, sort=sort, order=order)

搜索 Issues

### Example
```python
from __future__ import print_function
import time
import pygitee
from pygitee.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = pygitee.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = pygitee.SearchApi(pygitee.ApiClient(configuration))
q = 'q_example' # str | 搜索关键字
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
repo = 'repo_example' # str | 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues (optional)
language = 'language_example' # str | 筛选指定语言的 issues (optional)
label = 'label_example' # str | 筛选指定标签的 issues (optional)
state = 'state_example' # str | 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝) (optional)
author = 'author_example' # str | 筛选指定创建者 (username/login) 的 issues (optional)
assignee = 'assignee_example' # str | 筛选指定负责人 (username/login) 的 issues (optional)
sort = 'sort_example' # str | 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配 (optional)
order = 'order_example' # str | 排序顺序: desc(default)、asc (optional)

try:
    # 搜索 Issues
    api_response = api_instance.search_issues_get(q, access_token=access_token, page=page, per_page=per_page, repo=repo, language=language, label=label, state=state, author=author, assignee=assignee, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键字 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **repo** | **str**| 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues | [optional] 
 **language** | **str**| 筛选指定语言的 issues | [optional] 
 **label** | **str**| 筛选指定标签的 issues | [optional] 
 **state** | **str**| 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝) | [optional] 
 **author** | **str**| 筛选指定创建者 (username/login) 的 issues | [optional] 
 **assignee** | **str**| 筛选指定负责人 (username/login) 的 issues | [optional] 
 **sort** | **str**| 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配 | [optional] 
 **order** | **str**| 排序顺序: desc(default)、asc | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_repositories_get**
> InlineResponse2007 search_repositories_get(q, access_token=access_token, page=page, per_page=per_page, owner=owner, fork=fork, language=language, sort=sort, order=order)

搜索仓库

### Example
```python
from __future__ import print_function
import time
import pygitee
from pygitee.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = pygitee.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = pygitee.SearchApi(pygitee.ApiClient(configuration))
q = 'q_example' # str | 搜索关键字
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
owner = 'owner_example' # str | 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库 (optional)
fork = true # bool | 是否搜索含 fork 的仓库，默认：否 (optional)
language = 'language_example' # str | 筛选指定语言的仓库 (optional)
sort = 'sort_example' # str | 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配 (optional)
order = 'order_example' # str | 排序顺序: desc(default)、asc (optional)

try:
    # 搜索仓库
    api_response = api_instance.search_repositories_get(q, access_token=access_token, page=page, per_page=per_page, owner=owner, fork=fork, language=language, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_repositories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键字 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **owner** | **str**| 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库 | [optional] 
 **fork** | **bool**| 是否搜索含 fork 的仓库，默认：否 | [optional] 
 **language** | **str**| 筛选指定语言的仓库 | [optional] 
 **sort** | **str**| 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配 | [optional] 
 **order** | **str**| 排序顺序: desc(default)、asc | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_get**
> InlineResponse20050 search_users_get(q, access_token=access_token, page=page, per_page=per_page, sort=sort, order=order)

搜索用户

### Example
```python
from __future__ import print_function
import time
import pygitee
from pygitee.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = pygitee.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = pygitee.SearchApi(pygitee.ApiClient(configuration))
q = 'q_example' # str | 搜索关键字
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
sort = 'sort_example' # str | 排序字段，joined_at(注册时间)，默认为最佳匹配 (optional)
order = 'order_example' # str | 排序顺序: desc(default)、asc (optional)

try:
    # 搜索用户
    api_response = api_instance.search_users_get(q, access_token=access_token, page=page, per_page=per_page, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键字 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **sort** | **str**| 排序字段，joined_at(注册时间)，默认为最佳匹配 | [optional] 
 **order** | **str**| 排序顺序: desc(default)、asc | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

