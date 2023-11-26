# pygitee.IssueApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprises_enterprise_issues_get**](IssueApi.md#enterprises_enterprise_issues_get) | **GET** /enterprises/{enterprise}/issues | 获取某个企业的所有Issues
[**enterprises_enterprise_issues_number_get**](IssueApi.md#enterprises_enterprise_issues_number_get) | **GET** /enterprises/{enterprise}/issues/{number} | 获取企业的某个Issue
[**enterprises_enterprise_issues_number_labels_get**](IssueApi.md#enterprises_enterprise_issues_number_labels_get) | **GET** /enterprises/{enterprise}/issues/{number}/labels | 获取企业某个Issue所有标签
[**enterprises_enterprise_issues_number_patch**](IssueApi.md#enterprises_enterprise_issues_number_patch) | **PATCH** /enterprises/{enterprise}/issues/{number} | 更新企业的某个Issue
[**enterprises_enterprise_issues_number_pull_requests_get**](IssueApi.md#enterprises_enterprise_issues_number_pull_requests_get) | **GET** /enterprises/{enterprise}/issues/{number}/pull_requests | 获取企业 issue 关联的 Pull Requests
[**issues_get**](IssueApi.md#issues_get) | **GET** /issues | 获取当前授权用户的所有Issues
[**orgs_org_issues_get**](IssueApi.md#orgs_org_issues_get) | **GET** /orgs/{org}/issues | 获取当前用户某个组织的Issues
[**repos_owner_issues_number_operate_logs_get**](IssueApi.md#repos_owner_issues_number_operate_logs_get) | **GET** /repos/{owner}/issues/{number}/operate_logs | 获取某个Issue下的操作日志
[**repos_owner_issues_number_patch**](IssueApi.md#repos_owner_issues_number_patch) | **PATCH** /repos/{owner}/issues/{number} | 更新Issue
[**repos_owner_issues_number_pull_requests_get**](IssueApi.md#repos_owner_issues_number_pull_requests_get) | **GET** /repos/{owner}/issues/{number}/pull_requests | 获取 issue 关联的 Pull Requests
[**repos_owner_issues_post**](IssueApi.md#repos_owner_issues_post) | **POST** /repos/{owner}/issues | 创建Issue
[**repos_owner_repo_issues_get**](IssueApi.md#repos_owner_repo_issues_get) | **GET** /repos/{owner}/{repo}/issues | 仓库的所有Issues
[**repos_owner_repo_issues_number_get**](IssueApi.md#repos_owner_repo_issues_number_get) | **GET** /repos/{owner}/{repo}/issues/{number} | 仓库的某个Issue
[**repos_owner_repo_issues_number_labels_delete**](IssueApi.md#repos_owner_repo_issues_number_labels_delete) | **DELETE** /repos/{owner}/{repo}/issues/{number}/labels | 删除Issue所有标签
[**repos_owner_repo_issues_number_labels_get**](IssueApi.md#repos_owner_repo_issues_number_labels_get) | **GET** /repos/{owner}/{repo}/issues/{number}/labels | 获取仓库任务的所有标签
[**repos_owner_repo_issues_number_labels_name_delete**](IssueApi.md#repos_owner_repo_issues_number_labels_name_delete) | **DELETE** /repos/{owner}/{repo}/issues/{number}/labels/{name} | 删除Issue标签
[**repos_owner_repo_issues_number_labels_post**](IssueApi.md#repos_owner_repo_issues_number_labels_post) | **POST** /repos/{owner}/{repo}/issues/{number}/labels | 创建Issue标签
[**repos_owner_repo_issues_number_labels_put**](IssueApi.md#repos_owner_repo_issues_number_labels_put) | **PUT** /repos/{owner}/{repo}/issues/{number}/labels | 替换Issue所有标签
[**repos_owner_repo_pulls_number_issues_get**](IssueApi.md#repos_owner_repo_pulls_number_issues_get) | **GET** /repos/{owner}/{repo}/pulls/{number}/issues | 获取 Pull Request 关联的 issues
[**user_issues_get**](IssueApi.md#user_issues_get) | **GET** /user/issues | 获取授权用户的所有Issues

# **enterprises_enterprise_issues_get**
> InlineResponse2003 enterprises_enterprise_issues_get(enterprise, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)

获取某个企业的所有Issues

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'state_example' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'sort_example' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional)
direction = 'direction_example' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)
milestone = 'milestone_example' # str | 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 (optional)
assignee = 'assignee_example' # str | 用户的username。 none为没指派者, *为所有带有指派者的 (optional)
creator = 'creator_example' # str | 创建Issues的用户username (optional)
program = 'program_example' # str | 所属项目名称。none为没所属有项目的，*为所有带所属项目的 (optional)

try:
    # 获取某个企业的所有Issues
    api_response = api_instance.enterprises_enterprise_issues_get(enterprise, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->enterprises_enterprise_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] 
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 
 **milestone** | **str**| 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 | [optional] 
 **assignee** | **str**| 用户的username。 none为没指派者, *为所有带有指派者的 | [optional] 
 **creator** | **str**| 创建Issues的用户username | [optional] 
 **program** | **str**| 所属项目名称。none为没所属有项目的，*为所有带所属项目的 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_issues_number_get**
> InlineResponse2003 enterprises_enterprise_issues_number_get(enterprise, number, access_token=access_token)

获取企业的某个Issue

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业的某个Issue
    api_response = api_instance.enterprises_enterprise_issues_number_get(enterprise, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->enterprises_enterprise_issues_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_issues_number_labels_get**
> InlineResponse2005 enterprises_enterprise_issues_number_labels_get(enterprise, number, access_token=access_token, page=page, per_page=per_page)

获取企业某个Issue所有标签

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取企业某个Issue所有标签
    api_response = api_instance.enterprises_enterprise_issues_number_labels_get(enterprise, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->enterprises_enterprise_issues_number_labels_get: %s\n" % e)
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

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_issues_number_patch**
> InlineResponse2003 enterprises_enterprise_issues_number_patch(enterprise, number, body=body)

更新企业的某个Issue

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = pygitee.IssuesNumberBody() # IssuesNumberBody |  (optional)

try:
    # 更新企业的某个Issue
    api_response = api_instance.enterprises_enterprise_issues_number_patch(enterprise, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->enterprises_enterprise_issues_number_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**IssuesNumberBody**](IssuesNumberBody.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_issues_number_pull_requests_get**
> InlineResponse2001 enterprises_enterprise_issues_number_pull_requests_get(enterprise, number, access_token=access_token)

获取企业 issue 关联的 Pull Requests

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业 issue 关联的 Pull Requests
    api_response = api_instance.enterprises_enterprise_issues_number_pull_requests_get(enterprise, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->enterprises_enterprise_issues_number_pull_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_get**
> InlineResponse2003 issues_get(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)

获取当前授权用户的所有Issues

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
filter = 'filter_example' # str | 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned (optional)
state = 'state_example' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'sort_example' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional)
direction = 'direction_example' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)

try:
    # 获取当前授权用户的所有Issues
    api_response = api_instance.issues_get(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **filter** | **str**| 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] 
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_issues_get**
> InlineResponse2003 orgs_org_issues_get(org, access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)

获取当前用户某个组织的Issues

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
filter = 'filter_example' # str | 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned (optional)
state = 'state_example' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'sort_example' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional)
direction = 'direction_example' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)

try:
    # 获取当前用户某个组织的Issues
    api_response = api_instance.orgs_org_issues_get(org, access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->orgs_org_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **filter** | **str**| 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] 
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_issues_number_operate_logs_get**
> InlineResponse20023 repos_owner_issues_number_operate_logs_get(owner, number, access_token=access_token, repo=repo, sort=sort)

获取某个Issue下的操作日志

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
repo = 'repo_example' # str | 仓库路径(path) (optional)
sort = 'sort_example' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional)

try:
    # 获取某个Issue下的操作日志
    api_response = api_instance.repos_owner_issues_number_operate_logs_get(owner, number, access_token=access_token, repo=repo, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_issues_number_operate_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **repo** | **str**| 仓库路径(path) | [optional] 
 **sort** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_issues_number_patch**
> InlineResponse2003 repos_owner_issues_number_patch(owner, number, body=body)

更新Issue

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = pygitee.IssuesNumberBody1() # IssuesNumberBody1 |  (optional)

try:
    # 更新Issue
    api_response = api_instance.repos_owner_issues_number_patch(owner, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_issues_number_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**IssuesNumberBody1**](IssuesNumberBody1.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_issues_number_pull_requests_get**
> InlineResponse2001 repos_owner_issues_number_pull_requests_get(owner, number, access_token=access_token, repo=repo)

获取 issue 关联的 Pull Requests

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
repo = 'repo_example' # str | 仓库路径(path) (optional)

try:
    # 获取 issue 关联的 Pull Requests
    api_response = api_instance.repos_owner_issues_number_pull_requests_get(owner, number, access_token=access_token, repo=repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_issues_number_pull_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **repo** | **str**| 仓库路径(path) | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_issues_post**
> InlineResponse2003 repos_owner_issues_post(owner, body=body)

创建Issue

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
body = pygitee.OwnerIssuesBody() # OwnerIssuesBody |  (optional)

try:
    # 创建Issue
    api_response = api_instance.repos_owner_issues_post(owner, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_issues_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **body** | [**OwnerIssuesBody**](OwnerIssuesBody.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_get**
> InlineResponse2003 repos_owner_repo_issues_get(owner, repo, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)

仓库的所有Issues

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'state_example' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'sort_example' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional)
direction = 'direction_example' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)
milestone = 'milestone_example' # str | 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 (optional)
assignee = 'assignee_example' # str | 用户的username。 none为没指派者, *为所有带有指派者的 (optional)
creator = 'creator_example' # str | 创建Issues的用户username (optional)
program = 'program_example' # str | 所属项目名称。none为没有所属项目，*为所有带所属项目的 (optional)

try:
    # 仓库的所有Issues
    api_response = api_instance.repos_owner_repo_issues_get(owner, repo, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] 
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 
 **milestone** | **str**| 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 | [optional] 
 **assignee** | **str**| 用户的username。 none为没指派者, *为所有带有指派者的 | [optional] 
 **creator** | **str**| 创建Issues的用户username | [optional] 
 **program** | **str**| 所属项目名称。none为没有所属项目，*为所有带所属项目的 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_get**
> InlineResponse2003 repos_owner_repo_issues_number_get(owner, repo, number, access_token=access_token)

仓库的某个Issue

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 仓库的某个Issue
    api_response = api_instance.repos_owner_repo_issues_number_get(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_labels_delete**
> repos_owner_repo_issues_number_labels_delete(owner, repo, number, access_token=access_token)

删除Issue所有标签

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Issue所有标签
    api_instance.repos_owner_repo_issues_number_labels_delete(owner, repo, number, access_token=access_token)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_number_labels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_labels_get**
> InlineResponse2005 repos_owner_repo_issues_number_labels_get(owner, repo, number, access_token=access_token)

获取仓库任务的所有标签

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库任务的所有标签
    api_response = api_instance.repos_owner_repo_issues_number_labels_get(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_number_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_labels_name_delete**
> repos_owner_repo_issues_number_labels_name_delete(owner, repo, number, name, access_token=access_token)

删除Issue标签

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
name = 'name_example' # str | 标签名称(批量删除用英文逗号分隔，如: bug,feature)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Issue标签
    api_instance.repos_owner_repo_issues_number_labels_name_delete(owner, repo, number, name, access_token=access_token)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_number_labels_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
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

# **repos_owner_repo_issues_number_labels_post**
> InlineResponse2005 repos_owner_repo_issues_number_labels_post(owner, repo, number, body=body)

创建Issue标签

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = pygitee.NumberLabelsBody1() # NumberLabelsBody1 |  (optional)

try:
    # 创建Issue标签
    api_response = api_instance.repos_owner_repo_issues_number_labels_post(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_number_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**NumberLabelsBody1**](NumberLabelsBody1.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_issues_number_labels_put**
> InlineResponse2005 repos_owner_repo_issues_number_labels_put(owner, repo, number, body=body)

替换Issue所有标签

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
body = pygitee.NumberLabelsBody() # NumberLabelsBody |  (optional)

try:
    # 替换Issue所有标签
    api_response = api_instance.repos_owner_repo_issues_number_labels_put(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_issues_number_labels_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **body** | [**NumberLabelsBody**](NumberLabelsBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_pulls_number_issues_get**
> InlineResponse2003 repos_owner_repo_pulls_number_issues_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

获取 Pull Request 关联的 issues

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取 Pull Request 关联的 issues
    api_response = api_instance.repos_owner_repo_pulls_number_issues_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->repos_owner_repo_pulls_number_issues_get: %s\n" % e)
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

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_issues_get**
> InlineResponse2003 user_issues_get(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)

获取授权用户的所有Issues

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
api_instance = pygitee.IssueApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
filter = 'filter_example' # str | 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned (optional)
state = 'state_example' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'sort_example' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional)
direction = 'direction_example' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)

try:
    # 获取授权用户的所有Issues
    api_response = api_instance.user_issues_get(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueApi->user_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **filter** | **str**| 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] 
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

