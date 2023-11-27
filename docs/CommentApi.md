# pygitee.CommentApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprises_enterprise_issues_number_comments_get**](CommentApi.md#enterprises_enterprise_issues_number_comments_get) | **GET** /enterprises/{enterprise}/issues/{number}/comments | 获取企业某个Issue所有评论
[**enterprises_enterprise_week_reports_id_comment_post**](CommentApi.md#enterprises_enterprise_week_reports_id_comment_post) | **POST** /enterprises/{enterprise}/week_reports/{id}/comment | 评论周报
[**enterprises_enterprise_week_reports_id_comments_get**](CommentApi.md#enterprises_enterprise_week_reports_id_comments_get) | **GET** /enterprises/{enterprise}/week_reports/{id}/comments | 某个周报评论列表
[**enterprises_enterprise_week_reports_report_id_comments_id_delete**](CommentApi.md#enterprises_enterprise_week_reports_report_id_comments_id_delete) | **DELETE** /enterprises/{enterprise}/week_reports/{report_id}/comments/{id} | 删除周报某个评论
[**gists_gist_id_comments_get**](CommentApi.md#gists_gist_id_comments_get) | **GET** /gists/{gist_id}/comments | 获取代码片段的评论
[**gists_gist_id_comments_id_delete**](CommentApi.md#gists_gist_id_comments_id_delete) | **DELETE** /gists/{gist_id}/comments/{id} | 删除代码片段的评论
[**gists_gist_id_comments_id_get**](CommentApi.md#gists_gist_id_comments_id_get) | **GET** /gists/{gist_id}/comments/{id} | 获取单条代码片段的评论
[**gists_gist_id_comments_id_patch**](CommentApi.md#gists_gist_id_comments_id_patch) | **PATCH** /gists/{gist_id}/comments/{id} | 修改代码片段的评论
[**gists_gist_id_comments_post**](CommentApi.md#gists_gist_id_comments_post) | **POST** /gists/{gist_id}/comments | 增加代码片段的评论
[**repos_owner_repo_comments_get**](CommentApi.md#repos_owner_repo_comments_get) | **GET** /repos/{owner}/{repo}/comments | 获取仓库的Commit评论
[**repos_owner_repo_comments_id_delete**](CommentApi.md#repos_owner_repo_comments_id_delete) | **DELETE** /repos/{owner}/{repo}/comments/{id} | 删除Commit评论
[**repos_owner_repo_comments_id_get**](CommentApi.md#repos_owner_repo_comments_id_get) | **GET** /repos/{owner}/{repo}/comments/{id} | 获取仓库的某条Commit评论
[**repos_owner_repo_comments_id_patch**](CommentApi.md#repos_owner_repo_comments_id_patch) | **PATCH** /repos/{owner}/{repo}/comments/{id} | 更新Commit评论
[**repos_owner_repo_commits_ref_comments_get**](CommentApi.md#repos_owner_repo_commits_ref_comments_get) | **GET** /repos/{owner}/{repo}/commits/{ref}/comments | 获取单个Commit的评论
[**repos_owner_repo_commits_sha_comments_post**](CommentApi.md#repos_owner_repo_commits_sha_comments_post) | **POST** /repos/{owner}/{repo}/commits/{sha}/comments | 创建Commit评论
[**repos_owner_repo_issues_comments_get**](CommentApi.md#repos_owner_repo_issues_comments_get) | **GET** /repos/{owner}/{repo}/issues/comments | 获取仓库所有Issue的评论
[**repos_owner_repo_issues_comments_id_delete**](CommentApi.md#repos_owner_repo_issues_comments_id_delete) | **DELETE** /repos/{owner}/{repo}/issues/comments/{id} | 删除Issue某条评论
[**repos_owner_repo_issues_comments_id_get**](CommentApi.md#repos_owner_repo_issues_comments_id_get) | **GET** /repos/{owner}/{repo}/issues/comments/{id} | 获取仓库Issue某条评论
[**repos_owner_repo_issues_comments_id_patch**](CommentApi.md#repos_owner_repo_issues_comments_id_patch) | **PATCH** /repos/{owner}/{repo}/issues/comments/{id} | 更新Issue某条评论
[**repos_owner_repo_issues_number_comments_get**](CommentApi.md#repos_owner_repo_issues_number_comments_get) | **GET** /repos/{owner}/{repo}/issues/{number}/comments | 获取仓库某个Issue所有的评论
[**repos_owner_repo_issues_number_comments_post**](CommentApi.md#repos_owner_repo_issues_number_comments_post) | **POST** /repos/{owner}/{repo}/issues/{number}/comments | 创建某个Issue评论
[**repos_owner_repo_pulls_comments_id_delete**](CommentApi.md#repos_owner_repo_pulls_comments_id_delete) | **DELETE** /repos/{owner}/{repo}/pulls/comments/{id} | 删除评论
[**repos_owner_repo_pulls_comments_id_get**](CommentApi.md#repos_owner_repo_pulls_comments_id_get) | **GET** /repos/{owner}/{repo}/pulls/comments/{id} | 获取Pull Request的某个评论
[**repos_owner_repo_pulls_comments_id_patch**](CommentApi.md#repos_owner_repo_pulls_comments_id_patch) | **PATCH** /repos/{owner}/{repo}/pulls/comments/{id} | 编辑评论
[**repos_owner_repo_pulls_number_comments_get**](CommentApi.md#repos_owner_repo_pulls_number_comments_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/comments | 获取某个Pull Request的所有评论
[**repos_owner_repo_pulls_number_comments_post**](CommentApi.md#repos_owner_repo_pulls_number_comments_post) | **POST** /repos/{owner}/{repo}/pulls/{number}/comments | 提交Pull Request评论

# **enterprises_enterprise_issues_number_comments_get**
> InlineResponse2004 enterprises_enterprise_issues_number_comments_get(enterprise, number, access_token=access_token, page=page, per_page=per_page)

获取企业某个Issue所有评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取企业某个Issue所有评论
    api_response = api_instance.enterprises_enterprise_issues_number_comments_get(enterprise, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->enterprises_enterprise_issues_number_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_reports_id_comment_post**
> InlineResponse2004 enterprises_enterprise_week_reports_id_comment_post(enterprise, id, body=body)

评论周报

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID
body = pygitee.IdCommentBody() # IdCommentBody |  (optional)

try:
    # 评论周报
    api_response = api_instance.enterprises_enterprise_week_reports_id_comment_post(enterprise, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->enterprises_enterprise_week_reports_id_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 
 **body** | [**IdCommentBody**](IdCommentBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_reports_id_comments_get**
> InlineResponse2004 enterprises_enterprise_week_reports_id_comments_get(enterprise, id, access_token=access_token, page=page, per_page=per_page)

某个周报评论列表

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 某个周报评论列表
    api_response = api_instance.enterprises_enterprise_week_reports_id_comments_get(enterprise, id, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->enterprises_enterprise_week_reports_id_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_reports_report_id_comments_id_delete**
> enterprises_enterprise_week_reports_report_id_comments_id_delete(enterprise, report_id, id, access_token=access_token)

删除周报某个评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
report_id = 56 # int | 周报ID
id = 56 # int | 评论ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除周报某个评论
    api_instance.enterprises_enterprise_week_reports_report_id_comments_id_delete(enterprise, report_id, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling CommentApi->enterprises_enterprise_week_reports_report_id_comments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **report_id** | **int**| 周报ID | 
 **id** | **int**| 评论ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_gist_id_comments_get**
> InlineResponse20011 gists_gist_id_comments_get(gist_id, access_token=access_token, page=page, per_page=per_page)

获取代码片段的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
gist_id = 'gist_id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取代码片段的评论
    api_response = api_instance.gists_gist_id_comments_get(gist_id, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->gists_gist_id_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_gist_id_comments_id_delete**
> gists_gist_id_comments_id_delete(gist_id, id, access_token=access_token)

删除代码片段的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
gist_id = 'gist_id_example' # str | 代码片段的ID
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除代码片段的评论
    api_instance.gists_gist_id_comments_id_delete(gist_id, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling CommentApi->gists_gist_id_comments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_gist_id_comments_id_get**
> InlineResponse20011 gists_gist_id_comments_id_get(gist_id, id, access_token=access_token)

获取单条代码片段的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
gist_id = 'gist_id_example' # str | 代码片段的ID
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单条代码片段的评论
    api_response = api_instance.gists_gist_id_comments_id_get(gist_id, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->gists_gist_id_comments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_gist_id_comments_id_patch**
> InlineResponse20011 gists_gist_id_comments_id_patch(gist_id, id, body=body)

修改代码片段的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
gist_id = 'gist_id_example' # str | 代码片段的ID
id = 56 # int | 评论的ID
body = pygitee.CommentsIdBody() # CommentsIdBody |  (optional)

try:
    # 修改代码片段的评论
    api_response = api_instance.gists_gist_id_comments_id_patch(gist_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->gists_gist_id_comments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **id** | **int**| 评论的ID | 
 **body** | [**CommentsIdBody**](CommentsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_gist_id_comments_post**
> InlineResponse20011 gists_gist_id_comments_post(gist_id, body=body)

增加代码片段的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
gist_id = 'gist_id_example' # str | 代码片段的ID
body = pygitee.GistIdCommentsBody() # GistIdCommentsBody |  (optional)

try:
    # 增加代码片段的评论
    api_response = api_instance.gists_gist_id_comments_post(gist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->gists_gist_id_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| 代码片段的ID | 
 **body** | [**GistIdCommentsBody**](GistIdCommentsBody.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_comments_get**
> list[Comment] repos_owner_repo_comments_get(owner, repo, access_token=access_token, page=page, per_page=per_page, order=order)

获取仓库的Commit评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
order = 'order_example' # str | 排序顺序: asc(default),desc (optional)

try:
    # 获取仓库的Commit评论
    api_response = api_instance.repos_owner_repo_comments_get(owner, repo, access_token=access_token, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **order** | **str**| 排序顺序: asc(default),desc | [optional] 

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_comments_id_delete**
> repos_owner_repo_comments_id_delete(owner, repo, id, access_token=access_token)

删除Commit评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Commit评论
    api_instance.repos_owner_repo_comments_id_delete(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_comments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_comments_id_get**
> InlineResponse2004 repos_owner_repo_comments_id_get(owner, repo, id, access_token=access_token)

获取仓库的某条Commit评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的某条Commit评论
    api_response = api_instance.repos_owner_repo_comments_id_get(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_comments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_comments_id_patch**
> InlineResponse2004 repos_owner_repo_comments_id_patch(owner, repo, id, body=body)

更新Commit评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
body = pygitee.CommentsIdBody1() # CommentsIdBody1 |  (optional)

try:
    # 更新Commit评论
    api_response = api_instance.repos_owner_repo_comments_id_patch(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_comments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **body** | [**CommentsIdBody1**](CommentsIdBody1.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_commits_ref_comments_get**
> InlineResponse2004 repos_owner_repo_commits_ref_comments_get(owner, repo, ref, access_token=access_token, page=page, per_page=per_page)

获取单个Commit的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
ref = 'ref_example' # str | Commit的Reference
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取单个Commit的评论
    api_response = api_instance.repos_owner_repo_commits_ref_comments_get(owner, repo, ref, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_commits_ref_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **ref** | **str**| Commit的Reference | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_commits_sha_comments_post**
> InlineResponse2004 repos_owner_repo_commits_sha_comments_post(owner, repo, sha, body=body)

创建Commit评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 评论的sha值
body = pygitee.ShaCommentsBody() # ShaCommentsBody |  (optional)

try:
    # 创建Commit评论
    api_response = api_instance.repos_owner_repo_commits_sha_comments_post(owner, repo, sha, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_commits_sha_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 评论的sha值 | 
 **body** | [**ShaCommentsBody**](ShaCommentsBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_comments_get**
> InlineResponse2004 repos_owner_repo_issues_comments_get(owner, repo, access_token=access_token, sort=sort, direction=direction, since=since, page=page, per_page=per_page)

获取仓库所有Issue的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'sort_example' # str | Either created or updated. Default: created (optional)
direction = 'direction_example' # str | Either asc or desc. Ignored without the sort parameter. (optional)
since = 'since_example' # str | Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取仓库所有Issue的评论
    api_response = api_instance.repos_owner_repo_issues_comments_get(owner, repo, access_token=access_token, sort=sort, direction=direction, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_issues_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| Either created or updated. Default: created | [optional] 
 **direction** | **str**| Either asc or desc. Ignored without the sort parameter. | [optional] 
 **since** | **str**| Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_comments_id_delete**
> repos_owner_repo_issues_comments_id_delete(owner, repo, id, access_token=access_token)

删除Issue某条评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Issue某条评论
    api_instance.repos_owner_repo_issues_comments_id_delete(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_issues_comments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_comments_id_get**
> InlineResponse2004 repos_owner_repo_issues_comments_id_get(owner, repo, id, access_token=access_token)

获取仓库Issue某条评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库Issue某条评论
    api_response = api_instance.repos_owner_repo_issues_comments_id_get(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_issues_comments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_comments_id_patch**
> InlineResponse2004 repos_owner_repo_issues_comments_id_patch(owner, repo, id, body=body)

更新Issue某条评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
body = pygitee.CommentsIdBody2() # CommentsIdBody2 |  (optional)

try:
    # 更新Issue某条评论
    api_response = api_instance.repos_owner_repo_issues_comments_id_patch(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_issues_comments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **body** | [**CommentsIdBody2**](CommentsIdBody2.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_comments_get**
> list[Comment] repos_owner_repo_issues_number_comments_get(owner, repo, number, access_token=access_token, since=since, page=page, per_page=per_page, order=order)

获取仓库某个Issue所有的评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
since = 'since_example' # str | Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
order = 'order_example' # str | 排序顺序: asc(default),desc (optional)

try:
    # 获取仓库某个Issue所有的评论
    api_response = api_instance.repos_owner_repo_issues_number_comments_get(owner, repo, number, access_token=access_token, since=since, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_issues_number_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **since** | **str**| Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **order** | **str**| 排序顺序: asc(default),desc | [optional] 

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_comments_post**
> InlineResponse2004 repos_owner_repo_issues_number_comments_post(owner, repo, number, body=body)

创建某个Issue评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = pygitee.NumberCommentsBody() # NumberCommentsBody |  (optional)

try:
    # 创建某个Issue评论
    api_response = api_instance.repos_owner_repo_issues_number_comments_post(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_issues_number_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**NumberCommentsBody**](NumberCommentsBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_comments_id_delete**
> repos_owner_repo_pulls_comments_id_delete(owner, repo, id, access_token=access_token)

删除评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除评论
    api_instance.repos_owner_repo_pulls_comments_id_delete(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_pulls_comments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_comments_id_get**
> InlineResponse20044 repos_owner_repo_pulls_comments_id_get(owner, repo, access_token=access_token)

获取Pull Request的某个评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取Pull Request的某个评论
    api_response = api_instance.repos_owner_repo_pulls_comments_id_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_pulls_comments_id_get: %s\n" % e)
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

# **repos_owner_repo_pulls_comments_id_patch**
> InlineResponse20044 repos_owner_repo_pulls_comments_id_patch(owner, repo, id, body=body)

编辑评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
body = pygitee.CommentsIdBody3() # CommentsIdBody3 |  (optional)

try:
    # 编辑评论
    api_response = api_instance.repos_owner_repo_pulls_comments_id_patch(owner, repo, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_pulls_comments_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **body** | [**CommentsIdBody3**](CommentsIdBody3.md)|  | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_comments_get**
> InlineResponse20044 repos_owner_repo_pulls_number_comments_get(owner, repo, number, access_token=access_token, page=page, per_page=per_page, direction=direction, comment_type=comment_type)

获取某个Pull Request的所有评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
direction = 'direction_example' # str | 可选。升序/降序 (optional)
comment_type = 'comment_type_example' # str | 可选。筛选评论类型。代码行评论/pr普通评论 (optional)

try:
    # 获取某个Pull Request的所有评论
    api_response = api_instance.repos_owner_repo_pulls_number_comments_get(owner, repo, number, access_token=access_token, page=page, per_page=per_page, direction=direction, comment_type=comment_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_pulls_number_comments_get: %s\n" % e)
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
 **direction** | **str**| 可选。升序/降序 | [optional] 
 **comment_type** | **str**| 可选。筛选评论类型。代码行评论/pr普通评论 | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_comments_post**
> InlineResponse20044 repos_owner_repo_pulls_number_comments_post(owner, repo, number, body=body)

提交Pull Request评论

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
api_instance = pygitee.CommentApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = pygitee.NumberCommentsBody1() # NumberCommentsBody1 |  (optional)

try:
    # 提交Pull Request评论
    api_response = api_instance.repos_owner_repo_pulls_number_comments_post(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->repos_owner_repo_pulls_number_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**NumberCommentsBody1**](NumberCommentsBody1.md)|  | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

