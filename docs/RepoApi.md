# pygitee.RepoApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networks_owner_repo_events_get**](RepoApi.md#networks_owner_repo_events_get) | **GET** /networks/{owner}/{repo}/events | 列出仓库的所有公开动态
[**repos_owner_repo_baidu_statistic_key_get**](RepoApi.md#repos_owner_repo_baidu_statistic_key_get) | **GET** /repos/{owner}/{repo}/baidu_statistic_key | 获取仓库的百度统计 key
[**repos_owner_repo_blame_path_get**](RepoApi.md#repos_owner_repo_blame_path_get) | **GET** /repos/{owner}/{repo}/blame/{path} | Blame
[**repos_owner_repo_branches_branch_get**](RepoApi.md#repos_owner_repo_branches_branch_get) | **GET** /repos/{owner}/{repo}/branches/{branch} | 获取单个分支
[**repos_owner_repo_branches_branch_protection_put**](RepoApi.md#repos_owner_repo_branches_branch_protection_put) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection | 设置分支保护
[**repos_owner_repo_branches_get**](RepoApi.md#repos_owner_repo_branches_get) | **GET** /repos/{owner}/{repo}/branches | 获取所有分支
[**repos_owner_repo_branches_setting_new_put**](RepoApi.md#repos_owner_repo_branches_setting_new_put) | **PUT** /repos/{owner}/{repo}/branches/setting/new | 新建保护分支规则
[**repos_owner_repo_branches_wildcard_setting_put**](RepoApi.md#repos_owner_repo_branches_wildcard_setting_put) | **PUT** /repos/{owner}/{repo}/branches/{wildcard}/setting | 更新保护分支规则
[**repos_owner_repo_clear_put**](RepoApi.md#repos_owner_repo_clear_put) | **PUT** /repos/{owner}/{repo}/clear | 清空一个仓库
[**repos_owner_repo_collaborators_get**](RepoApi.md#repos_owner_repo_collaborators_get) | **GET** /repos/{owner}/{repo}/collaborators | 获取仓库的所有成员
[**repos_owner_repo_collaborators_username_get**](RepoApi.md#repos_owner_repo_collaborators_username_get) | **GET** /repos/{owner}/{repo}/collaborators/{username} | 判断用户是否为仓库成员
[**repos_owner_repo_collaborators_username_permission_get**](RepoApi.md#repos_owner_repo_collaborators_username_permission_get) | **GET** /repos/{owner}/{repo}/collaborators/{username}/permission | 查看仓库成员的权限
[**repos_owner_repo_commits_get**](RepoApi.md#repos_owner_repo_commits_get) | **GET** /repos/{owner}/{repo}/commits | 仓库的所有提交
[**repos_owner_repo_commits_sha_get**](RepoApi.md#repos_owner_repo_commits_sha_get) | **GET** /repos/{owner}/{repo}/commits/{sha} | 仓库的某个提交
[**repos_owner_repo_compare_base_head_get**](RepoApi.md#repos_owner_repo_compare_base_head_get) | **GET** /repos/{owner}/{repo}/compare/{base}...{head} | Commits 对比
[**repos_owner_repo_contents_path_get**](RepoApi.md#repos_owner_repo_contents_path_get) | **GET** /repos/{owner}/{repo}/contents(/{path}) | 获取仓库具体路径下的内容
[**repos_owner_repo_contents_path_post**](RepoApi.md#repos_owner_repo_contents_path_post) | **POST** /repos/{owner}/{repo}/contents/{path} | 新建文件
[**repos_owner_repo_contributors_get**](RepoApi.md#repos_owner_repo_contributors_get) | **GET** /repos/{owner}/{repo}/contributors | 获取仓库贡献者
[**repos_owner_repo_events_get**](RepoApi.md#repos_owner_repo_events_get) | **GET** /repos/{owner}/{repo}/events | 列出仓库的所有动态
[**repos_owner_repo_forks_get**](RepoApi.md#repos_owner_repo_forks_get) | **GET** /repos/{owner}/{repo}/forks | 查看仓库的Forks
[**repos_owner_repo_get**](RepoApi.md#repos_owner_repo_get) | **GET** /repos/{owner}/{repo} | 获取用户的某个仓库
[**repos_owner_repo_git_blobs_sha_get**](RepoApi.md#repos_owner_repo_git_blobs_sha_get) | **GET** /repos/{owner}/{repo}/git/blobs/{sha} | 获取文件Blob
[**repos_owner_repo_git_gitee_metrics_get**](RepoApi.md#repos_owner_repo_git_gitee_metrics_get) | **GET** /repos/{owner}/{repo}/git/gitee_metrics | 获取 Gitee 指数
[**repos_owner_repo_git_trees_sha_get**](RepoApi.md#repos_owner_repo_git_trees_sha_get) | **GET** /repos/{owner}/{repo}/git/trees/{sha} | 获取目录Tree
[**repos_owner_repo_keys_available_get**](RepoApi.md#repos_owner_repo_keys_available_get) | **GET** /repos/{owner}/{repo}/keys/available | 获取仓库可部署的公钥
[**repos_owner_repo_keys_enable_id_put**](RepoApi.md#repos_owner_repo_keys_enable_id_put) | **PUT** /repos/{owner}/{repo}/keys/enable/{id} | 启用仓库公钥
[**repos_owner_repo_keys_get**](RepoApi.md#repos_owner_repo_keys_get) | **GET** /repos/{owner}/{repo}/keys | 获取仓库已部署的公钥
[**repos_owner_repo_keys_id_get**](RepoApi.md#repos_owner_repo_keys_id_get) | **GET** /repos/{owner}/{repo}/keys/{id} | 获取仓库的单个公钥
[**repos_owner_repo_labels_get**](RepoApi.md#repos_owner_repo_labels_get) | **GET** /repos/{owner}/{repo}/labels | 获取仓库所有任务标签
[**repos_owner_repo_labels_name_get**](RepoApi.md#repos_owner_repo_labels_name_get) | **GET** /repos/{owner}/{repo}/labels/{name} | 根据标签名称获取单个标签
[**repos_owner_repo_labels_original_name_patch**](RepoApi.md#repos_owner_repo_labels_original_name_patch) | **PATCH** /repos/{owner}/{repo}/labels/{original_name} | 更新一个仓库任务标签
[**repos_owner_repo_license_get**](RepoApi.md#repos_owner_repo_license_get) | **GET** /repos/{owner}/{repo}/license | 获取一个仓库使用的开源许可协议
[**repos_owner_repo_milestones_get**](RepoApi.md#repos_owner_repo_milestones_get) | **GET** /repos/{owner}/{repo}/milestones | 获取仓库所有里程碑
[**repos_owner_repo_milestones_number_get**](RepoApi.md#repos_owner_repo_milestones_number_get) | **GET** /repos/{owner}/{repo}/milestones/{number} | 获取仓库单个里程碑
[**repos_owner_repo_open_post**](RepoApi.md#repos_owner_repo_open_post) | **POST** /repos/{owner}/{repo}/open | 开通Gitee Go
[**repos_owner_repo_pages_builds_post**](RepoApi.md#repos_owner_repo_pages_builds_post) | **POST** /repos/{owner}/{repo}/pages/builds | 请求建立Pages
[**repos_owner_repo_pages_get**](RepoApi.md#repos_owner_repo_pages_get) | **GET** /repos/{owner}/{repo}/pages | 获取Pages信息
[**repos_owner_repo_project_labels_get**](RepoApi.md#repos_owner_repo_project_labels_get) | **GET** /repos/{owner}/{repo}/project_labels | 获取仓库所有标签
[**repos_owner_repo_pulls_get**](RepoApi.md#repos_owner_repo_pulls_get) | **GET** /repos/{owner}/{repo}/pulls | 获取Pull Request列表
[**repos_owner_repo_pulls_number_assignees_post**](RepoApi.md#repos_owner_repo_pulls_number_assignees_post) | **POST** /repos/{owner}/{repo}/pulls/{number}/assignees | 指派用户审查 Pull Request
[**repos_owner_repo_pulls_number_commits_get**](RepoApi.md#repos_owner_repo_pulls_number_commits_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/commits | 获取某Pull Request的所有Commit信息。最多显示250条Commit
[**repos_owner_repo_pulls_number_files_get**](RepoApi.md#repos_owner_repo_pulls_number_files_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/files | Pull Request Commit文件列表。最多显示300条diff
[**repos_owner_repo_pulls_number_get**](RepoApi.md#repos_owner_repo_pulls_number_get) | **GET** /repos/{owner}/{repo}/pulls/{number} | 获取单个Pull Request
[**repos_owner_repo_pulls_number_labels_get**](RepoApi.md#repos_owner_repo_pulls_number_labels_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/labels | 获取某个 Pull Request 的所有标签
[**repos_owner_repo_pulls_number_labels_name_delete**](RepoApi.md#repos_owner_repo_pulls_number_labels_name_delete) | **DELETE** /repos/{owner}/{repo}/pulls/{number}/labels/{name} | 删除 Pull Request 标签
[**repos_owner_repo_pulls_number_merge_get**](RepoApi.md#repos_owner_repo_pulls_number_merge_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/merge | 判断Pull Request是否已经合并
[**repos_owner_repo_pulls_number_operate_logs_get**](RepoApi.md#repos_owner_repo_pulls_number_operate_logs_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/operate_logs | 获取某个Pull Request的操作日志
[**repos_owner_repo_pulls_number_review_post**](RepoApi.md#repos_owner_repo_pulls_number_review_post) | **POST** /repos/{owner}/{repo}/pulls/{number}/review | 处理 Pull Request 审查
[**repos_owner_repo_pulls_number_test_post**](RepoApi.md#repos_owner_repo_pulls_number_test_post) | **POST** /repos/{owner}/{repo}/pulls/{number}/test | 处理 Pull Request 测试
[**repos_owner_repo_pulls_number_testers_post**](RepoApi.md#repos_owner_repo_pulls_number_testers_post) | **POST** /repos/{owner}/{repo}/pulls/{number}/testers | 指派用户测试 Pull Request
[**repos_owner_repo_push_config_get**](RepoApi.md#repos_owner_repo_push_config_get) | **GET** /repos/{owner}/{repo}/push_config | 获取仓库推送规则设置
[**repos_owner_repo_raw_path_get**](RepoApi.md#repos_owner_repo_raw_path_get) | **GET** /repos/{owner}/{repo}/raw/{path} | 获取 raw 文件（100MB 以内）
[**repos_owner_repo_readme_get**](RepoApi.md#repos_owner_repo_readme_get) | **GET** /repos/{owner}/{repo}/readme | 获取仓库README
[**repos_owner_repo_reviewer_put**](RepoApi.md#repos_owner_repo_reviewer_put) | **PUT** /repos/{owner}/{repo}/reviewer | 修改代码审查设置
[**repos_owner_repo_stargazers_get**](RepoApi.md#repos_owner_repo_stargazers_get) | **GET** /repos/{owner}/{repo}/stargazers | 列出 star 了仓库的用户
[**repos_owner_repo_subscribers_get**](RepoApi.md#repos_owner_repo_subscribers_get) | **GET** /repos/{owner}/{repo}/subscribers | 列出 watch 了仓库的用户
[**repos_owner_repo_tags_get**](RepoApi.md#repos_owner_repo_tags_get) | **GET** /repos/{owner}/{repo}/tags | 列出仓库所有的tags
[**repos_owner_repo_tarball_get**](RepoApi.md#repos_owner_repo_tarball_get) | **GET** /repos/{owner}/{repo}/tarball | 下载仓库 tar.gz
[**repos_owner_repo_traffic_data_post**](RepoApi.md#repos_owner_repo_traffic_data_post) | **POST** /repos/{owner}/{repo}/traffic-data | 获取最近30天的七日以内访问量
[**repos_owner_repo_zipball_get**](RepoApi.md#repos_owner_repo_zipball_get) | **GET** /repos/{owner}/{repo}/zipball | 下载仓库 zip
[**user_repos_get**](RepoApi.md#user_repos_get) | **GET** /user/repos | 列出授权用户的所有仓库
[**users_username_repos_get**](RepoApi.md#users_username_repos_get) | **GET** /users/{username}/repos | 获取某个用户的公开仓库

# **networks_owner_repo_events_get**
> InlineResponse20012 networks_owner_repo_events_get(owner, repo, access_token=access_token, prev_id=prev_id, limit=limit)

列出仓库的所有公开动态

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出仓库的所有公开动态
    api_response = api_instance.networks_owner_repo_events_get(owner, repo, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->networks_owner_repo_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_baidu_statistic_key_get**
> repos_owner_repo_baidu_statistic_key_get(owner, repo, access_token=access_token)

获取仓库的百度统计 key

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的百度统计 key
    api_instance.repos_owner_repo_baidu_statistic_key_get(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_baidu_statistic_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_blame_path_get**
> InlineResponse20021 repos_owner_repo_blame_path_get(owner, repo, path, access_token=access_token, ref=ref)

Blame

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径（1 MB 以内的文件文件）
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag 或 commit。默认: 仓库的默认分支（通常是 master） (optional)

try:
    # Blame
    api_response = api_instance.repos_owner_repo_blame_path_get(owner, repo, path, access_token=access_token, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_blame_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径（1 MB 以内的文件文件） | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag 或 commit。默认: 仓库的默认分支（通常是 master） | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_branches_branch_get**
> InlineResponse20024 repos_owner_repo_branches_branch_get(owner, repo, branch, access_token=access_token)

获取单个分支

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
branch = 'branch_example' # str | 分支名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单个分支
    api_response = api_instance.repos_owner_repo_branches_branch_get(owner, repo, branch, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_branches_branch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **branch** | **str**| 分支名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_branches_branch_protection_put**
> InlineResponse20024 repos_owner_repo_branches_branch_protection_put(owner, repo, branch, body=body)

设置分支保护

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
branch = 'branch_example' # str | 分支名称
body = pygitee.BranchProtectionBody() # BranchProtectionBody |  (optional)

try:
    # 设置分支保护
    api_response = api_instance.repos_owner_repo_branches_branch_protection_put(owner, repo, branch, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_branches_branch_protection_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **branch** | **str**| 分支名称 | 
 **body** | [**BranchProtectionBody**](BranchProtectionBody.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_branches_get**
> InlineResponse20022 repos_owner_repo_branches_get(owner, repo, access_token=access_token)

获取所有分支

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取所有分支
    api_response = api_instance.repos_owner_repo_branches_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_branches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_branches_setting_new_put**
> InlineResponse20023 repos_owner_repo_branches_setting_new_put(owner, repo, body=body)

新建保护分支规则

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.SettingNewBody() # SettingNewBody |  (optional)

try:
    # 新建保护分支规则
    api_response = api_instance.repos_owner_repo_branches_setting_new_put(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_branches_setting_new_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**SettingNewBody**](SettingNewBody.md)|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_branches_wildcard_setting_put**
> InlineResponse20023 repos_owner_repo_branches_wildcard_setting_put(owner, repo, wildcard, body=body)

更新保护分支规则

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
wildcard = 'wildcard_example' # str | 分支/通配符
body = pygitee.WildcardSettingBody() # WildcardSettingBody |  (optional)

try:
    # 更新保护分支规则
    api_response = api_instance.repos_owner_repo_branches_wildcard_setting_put(owner, repo, wildcard, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_branches_wildcard_setting_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **wildcard** | **str**| 分支/通配符 | 
 **body** | [**WildcardSettingBody**](WildcardSettingBody.md)|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_clear_put**
> repos_owner_repo_clear_put(owner, repo, body=body)

清空一个仓库

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.RepoClearBody() # RepoClearBody |  (optional)

try:
    # 清空一个仓库
    api_instance.repos_owner_repo_clear_put(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_clear_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**RepoClearBody**](RepoClearBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_collaborators_get**
> InlineResponse20025 repos_owner_repo_collaborators_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库的所有成员

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取仓库的所有成员
    api_response = api_instance.repos_owner_repo_collaborators_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_collaborators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_collaborators_username_get**
> repos_owner_repo_collaborators_username_get(owner, repo, username, access_token=access_token)

判断用户是否为仓库成员

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 判断用户是否为仓库成员
    api_instance.repos_owner_repo_collaborators_username_get(owner, repo, username, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_collaborators_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_collaborators_username_permission_get**
> InlineResponse20026 repos_owner_repo_collaborators_username_permission_get(owner, repo, username, access_token=access_token)

查看仓库成员的权限

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 查看仓库成员的权限
    api_response = api_instance.repos_owner_repo_collaborators_username_permission_get(owner, repo, username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_collaborators_username_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_commits_get**
> InlineResponse20027 repos_owner_repo_commits_get(owner, repo, access_token=access_token, sha=sha, path=path, author=author, since=since, until=until, page=page, per_page=per_page)

仓库的所有提交

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sha = 'sha_example' # str | 提交起始的SHA值或者分支名. 默认: 仓库的默认分支 (optional)
path = 'path_example' # str | 包含该文件的提交 (optional)
author = 'author_example' # str | 提交作者的邮箱或个人空间地址(username/login) (optional)
since = 'since_example' # str | 提交的起始时间，时间格式为 ISO 8601 (optional)
until = 'until_example' # str | 提交的最后时间，时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 仓库的所有提交
    api_response = api_instance.repos_owner_repo_commits_get(owner, repo, access_token=access_token, sha=sha, path=path, author=author, since=since, until=until, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_commits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sha** | **str**| 提交起始的SHA值或者分支名. 默认: 仓库的默认分支 | [optional] 
 **path** | **str**| 包含该文件的提交 | [optional] 
 **author** | **str**| 提交作者的邮箱或个人空间地址(username/login) | [optional] 
 **since** | **str**| 提交的起始时间，时间格式为 ISO 8601 | [optional] 
 **until** | **str**| 提交的最后时间，时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_commits_sha_get**
> InlineResponse20028 repos_owner_repo_commits_sha_get(owner, repo, sha, access_token=access_token)

仓库的某个提交

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 提交的SHA值或者分支名
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 仓库的某个提交
    api_response = api_instance.repos_owner_repo_commits_sha_get(owner, repo, sha, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_commits_sha_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 提交的SHA值或者分支名 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_compare_base_head_get**
> InlineResponse20029 repos_owner_repo_compare_base_head_get(owner, repo, base, head, access_token=access_token, straight=straight, suffix=suffix)

Commits 对比

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
base = 'base_example' # str | 对比的起点。Commit SHA、分支名或标签名
head = 'head_example' # str | 对比的终点。Commit SHA、分支名或标签名
access_token = 'access_token_example' # str | 用户授权码 (optional)
straight = true # bool | 是否直对比。默认 false (optional)
suffix = 'suffix_example' # str | 按照文件后缀过滤文件，如 `.txt`。只影响 `files` (optional)

try:
    # Commits 对比
    api_response = api_instance.repos_owner_repo_compare_base_head_get(owner, repo, base, head, access_token=access_token, straight=straight, suffix=suffix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_compare_base_head_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **base** | **str**| 对比的起点。Commit SHA、分支名或标签名 | 
 **head** | **str**| 对比的终点。Commit SHA、分支名或标签名 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **straight** | **bool**| 是否直对比。默认 false | [optional] 
 **suffix** | **str**| 按照文件后缀过滤文件，如 &#x60;.txt&#x60;。只影响 &#x60;files&#x60; | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_contents_path_get**
> InlineResponse20030 repos_owner_repo_contents_path_get(owner, repo, path, access_token=access_token, ref=ref)

获取仓库具体路径下的内容

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag或commit。默认: 仓库的默认分支(通常是master) (optional)

try:
    # 获取仓库具体路径下的内容
    api_response = api_instance.repos_owner_repo_contents_path_get(owner, repo, path, access_token=access_token, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_contents_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag或commit。默认: 仓库的默认分支(通常是master) | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_contents_path_post**
> InlineResponse20031 repos_owner_repo_contents_path_post(owner, repo, path, body=body)

新建文件

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
body = pygitee.ContentsPathBody() # ContentsPathBody |  (optional)

try:
    # 新建文件
    api_response = api_instance.repos_owner_repo_contents_path_post(owner, repo, path, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_contents_path_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **body** | [**ContentsPathBody**](ContentsPathBody.md)|  | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_contributors_get**
> InlineResponse20032 repos_owner_repo_contributors_get(owner, repo, access_token=access_token, type=type)

获取仓库贡献者

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'type_example' # str | 贡献者类型 (optional)

try:
    # 获取仓库贡献者
    api_response = api_instance.repos_owner_repo_contributors_get(owner, repo, access_token=access_token, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_contributors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 贡献者类型 | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_events_get**
> InlineResponse20012 repos_owner_repo_events_get(owner, repo, access_token=access_token, prev_id=prev_id, limit=limit)

列出仓库的所有动态

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出仓库的所有动态
    api_response = api_instance.repos_owner_repo_events_get(owner, repo, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_forks_get**
> InlineResponse2007 repos_owner_repo_forks_get(owner, repo, access_token=access_token, sort=sort, page=page, per_page=per_page)

查看仓库的Forks

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'sort_example' # str | 排序方式: fork的时间(newest, oldest)，star的人数(stargazers) (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 查看仓库的Forks
    api_response = api_instance.repos_owner_repo_forks_get(owner, repo, access_token=access_token, sort=sort, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_forks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 排序方式: fork的时间(newest, oldest)，star的人数(stargazers) | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_get**
> InlineResponse2007 repos_owner_repo_get(owner, repo, access_token=access_token)

获取用户的某个仓库

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取用户的某个仓库
    api_response = api_instance.repos_owner_repo_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_git_blobs_sha_get**
> InlineResponse20033 repos_owner_repo_git_blobs_sha_get(owner, repo, sha, access_token=access_token)

获取文件Blob

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取文件Blob
    api_response = api_instance.repos_owner_repo_git_blobs_sha_get(owner, repo, sha, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_git_blobs_sha_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_git_gitee_metrics_get**
> InlineResponse20034 repos_owner_repo_git_gitee_metrics_get(owner, repo, access_token=access_token)

获取 Gitee 指数

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取 Gitee 指数
    api_response = api_instance.repos_owner_repo_git_gitee_metrics_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_git_gitee_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_git_trees_sha_get**
> InlineResponse20035 repos_owner_repo_git_trees_sha_get(owner, repo, sha, access_token=access_token, recursive=recursive)

获取目录Tree

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 可以是分支名(如master)、Commit或者目录Tree的SHA值
access_token = 'access_token_example' # str | 用户授权码 (optional)
recursive = 56 # int | 赋值为1递归获取目录 (optional)

try:
    # 获取目录Tree
    api_response = api_instance.repos_owner_repo_git_trees_sha_get(owner, repo, sha, access_token=access_token, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_git_trees_sha_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 可以是分支名(如master)、Commit或者目录Tree的SHA值 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **recursive** | **int**| 赋值为1递归获取目录 | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_keys_available_get**
> InlineResponse20038 repos_owner_repo_keys_available_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库可部署的公钥

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取仓库可部署的公钥
    api_response = api_instance.repos_owner_repo_keys_available_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_keys_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_keys_enable_id_put**
> repos_owner_repo_keys_enable_id_put(owner, repo, id, body=body)

启用仓库公钥

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 公钥 ID
body = pygitee.EnableIdBody() # EnableIdBody |  (optional)

try:
    # 启用仓库公钥
    api_instance.repos_owner_repo_keys_enable_id_put(owner, repo, id, body=body)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_keys_enable_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 公钥 ID | 
 **body** | [**EnableIdBody**](EnableIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_keys_get**
> InlineResponse20037 repos_owner_repo_keys_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取仓库已部署的公钥

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取仓库已部署的公钥
    api_response = api_instance.repos_owner_repo_keys_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_keys_id_get**
> InlineResponse20037 repos_owner_repo_keys_id_get(owner, repo, id, access_token=access_token)

获取仓库的单个公钥

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的单个公钥
    api_response = api_instance.repos_owner_repo_keys_id_get(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_keys_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_labels_get**
> InlineResponse2005 repos_owner_repo_labels_get(owner, repo, access_token=access_token)

获取仓库所有任务标签

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库所有任务标签
    api_response = api_instance.repos_owner_repo_labels_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_labels_name_get**
> InlineResponse2005 repos_owner_repo_labels_name_get(owner, repo, name, access_token=access_token)

根据标签名称获取单个标签

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 根据标签名称获取单个标签
    api_response = api_instance.repos_owner_repo_labels_name_get(owner, repo, name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_labels_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_labels_original_name_patch**
> InlineResponse2005 repos_owner_repo_labels_original_name_patch(owner, repo, original_name, body=body)

更新一个仓库任务标签

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
original_name = 'original_name_example' # str | 标签原有名称
body = pygitee.LabelsOriginalNameBody() # LabelsOriginalNameBody |  (optional)

try:
    # 更新一个仓库任务标签
    api_response = api_instance.repos_owner_repo_labels_original_name_patch(owner, repo, original_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_labels_original_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **original_name** | **str**| 标签原有名称 | 
 **body** | [**LabelsOriginalNameBody**](LabelsOriginalNameBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_license_get**
> repos_owner_repo_license_get(owner, repo, access_token=access_token)

获取一个仓库使用的开源许可协议

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个仓库使用的开源许可协议
    api_instance.repos_owner_repo_license_get(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_license_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_milestones_get**
> InlineResponse20039 repos_owner_repo_milestones_get(owner, repo, access_token=access_token, state=state, sort=sort, direction=direction, page=page, per_page=per_page)

获取仓库所有里程碑

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'state_example' # str | 里程碑状态: open, closed, all。默认: open (optional)
sort = 'sort_example' # str | 排序方式: due_on (optional)
direction = 'direction_example' # str | 升序(asc)或是降序(desc)。默认: asc (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取仓库所有里程碑
    api_response = api_instance.repos_owner_repo_milestones_get(owner, repo, access_token=access_token, state=state, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_milestones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| 里程碑状态: open, closed, all。默认: open | [optional] 
 **sort** | **str**| 排序方式: due_on | [optional] 
 **direction** | **str**| 升序(asc)或是降序(desc)。默认: asc | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_milestones_number_get**
> InlineResponse20039 repos_owner_repo_milestones_number_get(owner, repo, number, access_token=access_token)

获取仓库单个里程碑

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 里程碑序号(id)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库单个里程碑
    api_response = api_instance.repos_owner_repo_milestones_number_get(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_milestones_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 里程碑序号(id) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_open_post**
> repos_owner_repo_open_post(owner, repo, body=body)

开通Gitee Go

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库path
body = pygitee.RepoOpenBody() # RepoOpenBody |  (optional)

try:
    # 开通Gitee Go
    api_instance.repos_owner_repo_open_post(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_open_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库path | 
 **body** | [**RepoOpenBody**](RepoOpenBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pages_builds_post**
> repos_owner_repo_pages_builds_post(owner, repo, body=body)

请求建立Pages

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.PagesBuildsBody() # PagesBuildsBody |  (optional)

try:
    # 请求建立Pages
    api_instance.repos_owner_repo_pages_builds_post(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pages_builds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**PagesBuildsBody**](PagesBuildsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pages_get**
> repos_owner_repo_pages_get(owner, repo, access_token=access_token)

获取Pages信息

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取Pages信息
    api_instance.repos_owner_repo_pages_get(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_project_labels_get**
> InlineResponse20040 repos_owner_repo_project_labels_get(owner, repo, access_token=access_token)

获取仓库所有标签

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库所有标签
    api_response = api_instance.repos_owner_repo_project_labels_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_project_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_get**
> InlineResponse2001 repos_owner_repo_pulls_get(owner, repo, access_token=access_token, state=state, head=head, base=base, sort=sort, since=since, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)

获取Pull Request列表

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'state_example' # str | 可选。Pull Request 状态 (optional)
head = 'head_example' # str | 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch (optional)
base = 'base_example' # str | 可选。Pull Request 提交目标分支的名称。 (optional)
sort = 'sort_example' # str | 可选。排序字段，默认按创建时间 (optional)
since = 'since_example' # str | 可选。起始的更新时间，要求时间格式为 ISO 8601 (optional)
direction = 'direction_example' # str | 可选。升序/降序 (optional)
milestone_number = 56 # int | 可选。里程碑序号(id) (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取Pull Request列表
    api_response = api_instance.repos_owner_repo_pulls_get(owner, repo, access_token=access_token, state=state, head=head, base=base, sort=sort, since=since, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| 可选。Pull Request 状态 | [optional] 
 **head** | **str**| 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch | [optional] 
 **base** | **str**| 可选。Pull Request 提交目标分支的名称。 | [optional] 
 **sort** | **str**| 可选。排序字段，默认按创建时间 | [optional] 
 **since** | **str**| 可选。起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **direction** | **str**| 可选。升序/降序 | [optional] 
 **milestone_number** | **int**| 可选。里程碑序号(id) | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_assignees_post**
> InlineResponse2001 repos_owner_repo_pulls_number_assignees_post(owner, repo, number, body=body)

指派用户审查 Pull Request

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = pygitee.NumberAssigneesBody() # NumberAssigneesBody |  (optional)

try:
    # 指派用户审查 Pull Request
    api_response = api_instance.repos_owner_repo_pulls_number_assignees_post(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_assignees_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**NumberAssigneesBody**](NumberAssigneesBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_commits_get**
> InlineResponse20042 repos_owner_repo_pulls_number_commits_get(owner, repo, number, access_token=access_token)

获取某Pull Request的所有Commit信息。最多显示250条Commit

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取某Pull Request的所有Commit信息。最多显示250条Commit
    api_response = api_instance.repos_owner_repo_pulls_number_commits_get(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_commits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_files_get**
> InlineResponse20043 repos_owner_repo_pulls_number_files_get(owner, repo, number, access_token=access_token)

Pull Request Commit文件列表。最多显示300条diff

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # Pull Request Commit文件列表。最多显示300条diff
    api_response = api_instance.repos_owner_repo_pulls_number_files_get(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_get**
> InlineResponse2001 repos_owner_repo_pulls_number_get(owner, repo, number, access_token=access_token)

获取单个Pull Request

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单个Pull Request
    api_response = api_instance.repos_owner_repo_pulls_number_get(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_labels_get**
> InlineResponse2005 repos_owner_repo_pulls_number_labels_get(owner, repo, number, access_token=access_token, page=page, per_page=per_page)

获取某个 Pull Request 的所有标签

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取某个 Pull Request 的所有标签
    api_response = api_instance.repos_owner_repo_pulls_number_labels_get(owner, repo, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_labels_name_delete**
> repos_owner_repo_pulls_number_labels_name_delete(owner, repo, number, name, access_token=access_token)

删除 Pull Request 标签

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
name = 'name_example' # str | 标签名称(批量删除用英文逗号分隔，如: bug,feature)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除 Pull Request 标签
    api_instance.repos_owner_repo_pulls_number_labels_name_delete(owner, repo, number, name, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_labels_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **name** | **str**| 标签名称(批量删除用英文逗号分隔，如: bug,feature) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_merge_get**
> repos_owner_repo_pulls_number_merge_get(owner, repo, number, access_token=access_token)

判断Pull Request是否已经合并

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 判断Pull Request是否已经合并
    api_instance.repos_owner_repo_pulls_number_merge_get(owner, repo, number, access_token=access_token)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_merge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_operate_logs_get**
> InlineResponse20020 repos_owner_repo_pulls_number_operate_logs_get(owner, repo, number, access_token=access_token, sort=sort)

获取某个Pull Request的操作日志

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'sort_example' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional)

try:
    # 获取某个Pull Request的操作日志
    api_response = api_instance.repos_owner_repo_pulls_number_operate_logs_get(owner, repo, number, access_token=access_token, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_operate_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_review_post**
> repos_owner_repo_pulls_number_review_post(owner, repo, number, body=body)

处理 Pull Request 审查

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = pygitee.NumberReviewBody() # NumberReviewBody |  (optional)

try:
    # 处理 Pull Request 审查
    api_instance.repos_owner_repo_pulls_number_review_post(owner, repo, number, body=body)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_review_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**NumberReviewBody**](NumberReviewBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_test_post**
> repos_owner_repo_pulls_number_test_post(owner, repo, number, body=body)

处理 Pull Request 测试

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = pygitee.NumberTestBody() # NumberTestBody |  (optional)

try:
    # 处理 Pull Request 测试
    api_instance.repos_owner_repo_pulls_number_test_post(owner, repo, number, body=body)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**NumberTestBody**](NumberTestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_testers_post**
> InlineResponse2001 repos_owner_repo_pulls_number_testers_post(owner, repo, number, body=body)

指派用户测试 Pull Request

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = pygitee.NumberTestersBody() # NumberTestersBody |  (optional)

try:
    # 指派用户测试 Pull Request
    api_response = api_instance.repos_owner_repo_pulls_number_testers_post(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_pulls_number_testers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**NumberTestersBody**](NumberTestersBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_push_config_get**
> InlineResponse20044 repos_owner_repo_push_config_get(owner, repo, access_token=access_token)

获取仓库推送规则设置

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库推送规则设置
    api_response = api_instance.repos_owner_repo_push_config_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_push_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_raw_path_get**
> repos_owner_repo_raw_path_get(owner, repo, path, access_token=access_token, ref=ref)

获取 raw 文件（100MB 以内）

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
path = 'path_example' # str | 文件的路径
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag 或 commit。默认: 仓库的默认分支（通常是 master） (optional)

try:
    # 获取 raw 文件（100MB 以内）
    api_instance.repos_owner_repo_raw_path_get(owner, repo, path, access_token=access_token, ref=ref)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_raw_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **path** | **str**| 文件的路径 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag 或 commit。默认: 仓库的默认分支（通常是 master） | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_readme_get**
> InlineResponse20030 repos_owner_repo_readme_get(owner, repo, access_token=access_token, ref=ref)

获取仓库README

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag或commit。默认: 仓库的默认分支(通常是master) (optional)

try:
    # 获取仓库README
    api_response = api_instance.repos_owner_repo_readme_get(owner, repo, access_token=access_token, ref=ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_readme_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag或commit。默认: 仓库的默认分支(通常是master) | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_reviewer_put**
> InlineResponse20032 repos_owner_repo_reviewer_put(owner, repo, body=body)

修改代码审查设置

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.RepoReviewerBody() # RepoReviewerBody |  (optional)

try:
    # 修改代码审查设置
    api_response = api_instance.repos_owner_repo_reviewer_put(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_reviewer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**RepoReviewerBody**](RepoReviewerBody.md)|  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_stargazers_get**
> InlineResponse20046 repos_owner_repo_stargazers_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出 star 了仓库的用户

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出 star 了仓库的用户
    api_response = api_instance.repos_owner_repo_stargazers_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_stargazers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_subscribers_get**
> InlineResponse20047 repos_owner_repo_subscribers_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出 watch 了仓库的用户

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出 watch 了仓库的用户
    api_response = api_instance.repos_owner_repo_subscribers_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_subscribers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_tags_get**
> InlineResponse20048 repos_owner_repo_tags_get(owner, repo, access_token=access_token)

列出仓库所有的tags

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出仓库所有的tags
    api_response = api_instance.repos_owner_repo_tags_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_tarball_get**
> repos_owner_repo_tarball_get(owner, repo, access_token=access_token, ref=ref)

下载仓库 tar.gz

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag或commit。默认: 仓库的默认分支(通常是master) (optional)

try:
    # 下载仓库 tar.gz
    api_instance.repos_owner_repo_tarball_get(owner, repo, access_token=access_token, ref=ref)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_tarball_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag或commit。默认: 仓库的默认分支(通常是master) | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_traffic_data_post**
> InlineResponse20049 repos_owner_repo_traffic_data_post(owner, repo, body=body)

获取最近30天的七日以内访问量

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.RepoTrafficdataBody() # RepoTrafficdataBody |  (optional)

try:
    # 获取最近30天的七日以内访问量
    api_response = api_instance.repos_owner_repo_traffic_data_post(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_traffic_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**RepoTrafficdataBody**](RepoTrafficdataBody.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_zipball_get**
> repos_owner_repo_zipball_get(owner, repo, access_token=access_token, ref=ref)

下载仓库 zip

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
ref = 'ref_example' # str | 分支、tag或commit。默认: 仓库的默认分支(通常是master) (optional)

try:
    # 下载仓库 zip
    api_instance.repos_owner_repo_zipball_get(owner, repo, access_token=access_token, ref=ref)
except ApiException as e:
    print("Exception when calling RepoApi->repos_owner_repo_zipball_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **ref** | **str**| 分支、tag或commit。默认: 仓库的默认分支(通常是master) | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_repos_get**
> InlineResponse2007 user_repos_get(access_token=access_token, visibility=visibility, affiliation=affiliation, type=type, sort=sort, direction=direction, q=q, page=page, per_page=per_page)

列出授权用户的所有仓库

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
visibility = 'visibility_example' # str | 公开(public)、私有(private)或者所有(all)，默认: 所有(all) (optional)
affiliation = 'affiliation_example' # str | owner(授权用户拥有的仓库)、collaborator(授权用户为仓库成员)、organization_member(授权用户为仓库所在组织并有访问仓库权限)、enterprise_member(授权用户所在企业并有访问仓库权限)、admin(所有有权限的，包括所管理的组织中所有仓库、所管理的企业的所有仓库)。                    可以用逗号分隔符组合。如: owner, organization_member 或 owner, collaborator, organization_member (optional)
type = 'type_example' # str | 筛选用户仓库: 其创建(owner)、个人(personal)、其为成员(member)、公开(public)、私有(private)，不能与 visibility 或 affiliation 参数一并使用，否则会报 422 错误 (optional)
sort = 'sort_example' # str | 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name (optional)
direction = 'direction_example' # str | 如果sort参数为full_name，用升序(asc)。否则降序(desc) (optional)
q = 'q_example' # str | 搜索关键字 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户的所有仓库
    api_response = api_instance.user_repos_get(access_token=access_token, visibility=visibility, affiliation=affiliation, type=type, sort=sort, direction=direction, q=q, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->user_repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **visibility** | **str**| 公开(public)、私有(private)或者所有(all)，默认: 所有(all) | [optional] 
 **affiliation** | **str**| owner(授权用户拥有的仓库)、collaborator(授权用户为仓库成员)、organization_member(授权用户为仓库所在组织并有访问仓库权限)、enterprise_member(授权用户所在企业并有访问仓库权限)、admin(所有有权限的，包括所管理的组织中所有仓库、所管理的企业的所有仓库)。                    可以用逗号分隔符组合。如: owner, organization_member 或 owner, collaborator, organization_member | [optional] 
 **type** | **str**| 筛选用户仓库: 其创建(owner)、个人(personal)、其为成员(member)、公开(public)、私有(private)，不能与 visibility 或 affiliation 参数一并使用，否则会报 422 错误 | [optional] 
 **sort** | **str**| 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name | [optional] 
 **direction** | **str**| 如果sort参数为full_name，用升序(asc)。否则降序(desc) | [optional] 
 **q** | **str**| 搜索关键字 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_repos_get**
> InlineResponse2007 users_username_repos_get(username, access_token=access_token, type=type, sort=sort, direction=direction, page=page, per_page=per_page)

获取某个用户的公开仓库

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
api_instance = pygitee.RepoApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'type_example' # str | 用户创建的仓库(owner)，用户个人仓库(personal)，用户为仓库成员(member)，所有(all)。默认: 所有(all) (optional)
sort = 'sort_example' # str | 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name (optional)
direction = 'direction_example' # str | 如果sort参数为full_name，用升序(asc)。否则降序(desc) (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取某个用户的公开仓库
    api_response = api_instance.users_username_repos_get(username, access_token=access_token, type=type, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->users_username_repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 用户创建的仓库(owner)，用户个人仓库(personal)，用户为仓库成员(member)，所有(all)。默认: 所有(all) | [optional] 
 **sort** | **str**| 排序方式: 创建时间(created)，更新时间(updated)，最后推送时间(pushed)，仓库所属与名称(full_name)。默认: full_name | [optional] 
 **direction** | **str**| 如果sort参数为full_name，用升序(asc)。否则降序(desc) | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

