# pygitee.DefaultApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emails_get**](DefaultApi.md#emails_get) | **GET** /emails | 获取授权用户的全部邮箱
[**emojis_get**](DefaultApi.md#emojis_get) | **GET** /emojis | 列出可使用的 Emoji
[**enterprise_enterprise_pull_requests_get**](DefaultApi.md#enterprise_enterprise_pull_requests_get) | **GET** /enterprise/{enterprise}/pull_requests | 企业 Pull Request 列表
[**gitignore_templates_get**](DefaultApi.md#gitignore_templates_get) | **GET** /gitignore/templates | 列出可使用的 .gitignore 模板
[**gitignore_templates_name_get**](DefaultApi.md#gitignore_templates_name_get) | **GET** /gitignore/templates/{name} | 获取一个 .gitignore 模板
[**gitignore_templates_name_raw_get**](DefaultApi.md#gitignore_templates_name_raw_get) | **GET** /gitignore/templates/{name}/raw | 获取一个 .gitignore 模板原始文件
[**licenses_get**](DefaultApi.md#licenses_get) | **GET** /licenses | 列出可使用的开源许可协议
[**licenses_license_get**](DefaultApi.md#licenses_license_get) | **GET** /licenses/{license} | 获取一个开源许可协议
[**licenses_license_raw_get**](DefaultApi.md#licenses_license_raw_get) | **GET** /licenses/{license}/raw | 获取一个开源许可协议原始文件
[**markdown_post**](DefaultApi.md#markdown_post) | **POST** /markdown | 渲染 Markdown 文本

# **emails_get**
> InlineResponse200 emails_get(access_token=access_token)

获取授权用户的全部邮箱

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户的全部邮箱
    api_response = api_instance.emails_get(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->emails_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emojis_get**
> emojis_get(access_token=access_token)

列出可使用的 Emoji

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出可使用的 Emoji
    api_instance.emojis_get(access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->emojis_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_enterprise_pull_requests_get**
> InlineResponse2001 enterprise_enterprise_pull_requests_get(enterprise, access_token=access_token, issue_number=issue_number, repo=repo, program_id=program_id, state=state, head=head, base=base, sort=sort, since=since, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)

企业 Pull Request 列表

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
issue_number = 'issue_number_example' # str | 可选。Issue 编号(区分大小写，无需添加 # 号) (optional)
repo = 'repo_example' # str | 可选。仓库路径(path) (optional)
program_id = 56 # int | 可选。项目ID (optional)
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
    # 企业 Pull Request 列表
    api_response = api_instance.enterprise_enterprise_pull_requests_get(enterprise, access_token=access_token, issue_number=issue_number, repo=repo, program_id=program_id, state=state, head=head, base=base, sort=sort, since=since, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprise_enterprise_pull_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **issue_number** | **str**| 可选。Issue 编号(区分大小写，无需添加 # 号) | [optional] 
 **repo** | **str**| 可选。仓库路径(path) | [optional] 
 **program_id** | **int**| 可选。项目ID | [optional] 
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

# **gitignore_templates_get**
> gitignore_templates_get(access_token=access_token)

列出可使用的 .gitignore 模板

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出可使用的 .gitignore 模板
    api_instance.gitignore_templates_get(access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->gitignore_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gitignore_templates_name_get**
> gitignore_templates_name_get(name, access_token=access_token)

获取一个 .gitignore 模板

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
name = 'name_example' # str | .gitignore 模板名
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个 .gitignore 模板
    api_instance.gitignore_templates_name_get(name, access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->gitignore_templates_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| .gitignore 模板名 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gitignore_templates_name_raw_get**
> gitignore_templates_name_raw_get(name, access_token=access_token)

获取一个 .gitignore 模板原始文件

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
name = 'name_example' # str | .gitignore 模板名
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个 .gitignore 模板原始文件
    api_instance.gitignore_templates_name_raw_get(name, access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->gitignore_templates_name_raw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| .gitignore 模板名 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_get**
> licenses_get(access_token=access_token)

列出可使用的开源许可协议

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 列出可使用的开源许可协议
    api_instance.licenses_get(access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->licenses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_license_get**
> licenses_license_get(license, access_token=access_token)

获取一个开源许可协议

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
license = 'license_example' # str | 协议名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个开源许可协议
    api_instance.licenses_license_get(license, access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->licenses_license_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**| 协议名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_license_raw_get**
> licenses_license_raw_get(license, access_token=access_token)

获取一个开源许可协议原始文件

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
license = 'license_example' # str | 协议名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个开源许可协议原始文件
    api_instance.licenses_license_raw_get(license, access_token=access_token)
except ApiException as e:
    print("Exception when calling DefaultApi->licenses_license_raw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**| 协议名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markdown_post**
> markdown_post(body=body)

渲染 Markdown 文本

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
api_instance = pygitee.DefaultApi(pygitee.ApiClient(configuration))
body = pygitee.MarkdownBody() # MarkdownBody |  (optional)

try:
    # 渲染 Markdown 文本
    api_instance.markdown_post(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->markdown_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkdownBody**](MarkdownBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

