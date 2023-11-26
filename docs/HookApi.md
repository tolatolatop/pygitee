# pygitee.HookApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repos_owner_repo_hooks_get**](HookApi.md#repos_owner_repo_hooks_get) | **GET** /repos/{owner}/{repo}/hooks | 列出仓库的WebHooks
[**repos_owner_repo_hooks_id_get**](HookApi.md#repos_owner_repo_hooks_id_get) | **GET** /repos/{owner}/{repo}/hooks/{id} | 获取仓库单个WebHook
[**repos_owner_repo_hooks_id_tests_post**](HookApi.md#repos_owner_repo_hooks_id_tests_post) | **POST** /repos/{owner}/{repo}/hooks/{id}/tests | 测试WebHook是否发送成功

# **repos_owner_repo_hooks_get**
> InlineResponse20036 repos_owner_repo_hooks_get(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出仓库的WebHooks

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
api_instance = pygitee.HookApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出仓库的WebHooks
    api_response = api_instance.repos_owner_repo_hooks_get(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->repos_owner_repo_hooks_get: %s\n" % e)
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

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_hooks_id_get**
> InlineResponse20036 repos_owner_repo_hooks_id_get(owner, repo, id, access_token=access_token)

获取仓库单个WebHook

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
api_instance = pygitee.HookApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库单个WebHook
    api_response = api_instance.repos_owner_repo_hooks_id_get(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->repos_owner_repo_hooks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_hooks_id_tests_post**
> repos_owner_repo_hooks_id_tests_post(owner, repo, id, body=body)

测试WebHook是否发送成功

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
api_instance = pygitee.HookApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | Webhook的ID
body = pygitee.IdTestsBody() # IdTestsBody |  (optional)

try:
    # 测试WebHook是否发送成功
    api_instance.repos_owner_repo_hooks_id_tests_post(owner, repo, id, body=body)
except ApiException as e:
    print("Exception when calling HookApi->repos_owner_repo_hooks_id_tests_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| Webhook的ID | 
 **body** | [**IdTestsBody**](IdTestsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

