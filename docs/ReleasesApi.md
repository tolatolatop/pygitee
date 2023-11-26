# pygitee.ReleasesApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repos_owner_repo_releases_get**](ReleasesApi.md#repos_owner_repo_releases_get) | **GET** /repos/{owner}/{repo}/releases | 获取仓库的所有Releases
[**repos_owner_repo_releases_id_delete**](ReleasesApi.md#repos_owner_repo_releases_id_delete) | **DELETE** /repos/{owner}/{repo}/releases/{id} | 删除仓库Release
[**repos_owner_repo_releases_id_get**](ReleasesApi.md#repos_owner_repo_releases_id_get) | **GET** /repos/{owner}/{repo}/releases/{id} | 获取仓库的单个Releases
[**repos_owner_repo_releases_id_patch**](ReleasesApi.md#repos_owner_repo_releases_id_patch) | **PATCH** /repos/{owner}/{repo}/releases/{id} | 更新仓库Release
[**repos_owner_repo_releases_latest_get**](ReleasesApi.md#repos_owner_repo_releases_latest_get) | **GET** /repos/{owner}/{repo}/releases/latest | 获取仓库的最后更新的Release
[**repos_owner_repo_releases_post**](ReleasesApi.md#repos_owner_repo_releases_post) | **POST** /repos/{owner}/{repo}/releases | 创建仓库Release
[**repos_owner_repo_releases_tags_tag_get**](ReleasesApi.md#repos_owner_repo_releases_tags_tag_get) | **GET** /repos/{owner}/{repo}/releases/tags/{tag} | 根据Tag名称获取仓库的Release

# **repos_owner_repo_releases_get**
> InlineResponse20048 repos_owner_repo_releases_get(owner, repo, access_token=access_token, page=page, per_page=per_page, direction=direction)

获取仓库的所有Releases

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
direction = 'direction_example' # str | 可选。升序/降序。不填为升序 (optional)

try:
    # 获取仓库的所有Releases
    api_response = api_instance.repos_owner_repo_releases_get(owner, repo, access_token=access_token, page=page, per_page=per_page, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **direction** | **str**| 可选。升序/降序。不填为升序 | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_releases_id_delete**
> repos_owner_repo_releases_id_delete(owner, repo, access_token=access_token)

删除仓库Release

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除仓库Release
    api_instance.repos_owner_repo_releases_id_delete(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_id_delete: %s\n" % e)
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

# **repos_owner_repo_releases_id_get**
> InlineResponse20048 repos_owner_repo_releases_id_get(owner, repo, id, access_token=access_token)

获取仓库的单个Releases

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 发行版本的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的单个Releases
    api_response = api_instance.repos_owner_repo_releases_id_get(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 发行版本的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_releases_id_patch**
> InlineResponse20048 repos_owner_repo_releases_id_patch(owner, repo, body=body)

更新仓库Release

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.ReleasesIdBody() # ReleasesIdBody |  (optional)

try:
    # 更新仓库Release
    api_response = api_instance.repos_owner_repo_releases_id_patch(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**ReleasesIdBody**](ReleasesIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_releases_latest_get**
> InlineResponse20048 repos_owner_repo_releases_latest_get(owner, repo, access_token=access_token)

获取仓库的最后更新的Release

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库的最后更新的Release
    api_response = api_instance.repos_owner_repo_releases_latest_get(owner, repo, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_latest_get: %s\n" % e)
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

# **repos_owner_repo_releases_post**
> InlineResponse20048 repos_owner_repo_releases_post(owner, repo, body=body)

创建仓库Release

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.RepoReleasesBody() # RepoReleasesBody |  (optional)

try:
    # 创建仓库Release
    api_response = api_instance.repos_owner_repo_releases_post(owner, repo, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**RepoReleasesBody**](RepoReleasesBody.md)|  | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_releases_tags_tag_get**
> InlineResponse20048 repos_owner_repo_releases_tags_tag_get(owner, repo, tag, access_token=access_token)

根据Tag名称获取仓库的Release

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
api_instance = pygitee.ReleasesApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
tag = 'tag_example' # str | Tag 名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 根据Tag名称获取仓库的Release
    api_response = api_instance.repos_owner_repo_releases_tags_tag_get(owner, repo, tag, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleasesApi->repos_owner_repo_releases_tags_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **tag** | **str**| Tag 名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

