# pygitee.GistsApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gists_get**](GistsApi.md#gists_get) | **GET** /gists | 获取代码片段
[**gists_id_commits_get**](GistsApi.md#gists_id_commits_get) | **GET** /gists/{id}/commits | 获取代码片段的commit
[**gists_id_delete**](GistsApi.md#gists_id_delete) | **DELETE** /gists/{id} | 删除指定代码片段
[**gists_id_forks_get**](GistsApi.md#gists_id_forks_get) | **GET** /gists/{id}/forks | 获取 Fork 了指定代码片段的列表
[**gists_id_forks_post**](GistsApi.md#gists_id_forks_post) | **POST** /gists/{id}/forks | Fork代码片段
[**gists_id_get**](GistsApi.md#gists_id_get) | **GET** /gists/{id} | 获取单条代码片段
[**gists_id_patch**](GistsApi.md#gists_id_patch) | **PATCH** /gists/{id} | 修改代码片段
[**gists_id_star_delete**](GistsApi.md#gists_id_star_delete) | **DELETE** /gists/{id}/star | 取消Star代码片段
[**gists_id_star_get**](GistsApi.md#gists_id_star_get) | **GET** /gists/{id}/star | 判断代码片段是否已Star
[**gists_id_star_put**](GistsApi.md#gists_id_star_put) | **PUT** /gists/{id}/star | Star代码片段
[**gists_post**](GistsApi.md#gists_post) | **POST** /gists | 创建代码片段
[**gists_starred_get**](GistsApi.md#gists_starred_get) | **GET** /gists/starred | 获取用户Star的代码片段

# **gists_get**
> InlineResponse2009 gists_get(access_token=access_token, since=since, page=page, per_page=per_page)

获取代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取代码片段
    api_response = api_instance.gists_get(access_token=access_token, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_commits_get**
> InlineResponse20010 gists_id_commits_get(id, access_token=access_token)

获取代码片段的commit

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取代码片段的commit
    api_response = api_instance.gists_id_commits_get(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_commits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_delete**
> gists_id_delete(id, access_token=access_token)

删除指定代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除指定代码片段
    api_instance.gists_id_delete(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_forks_get**
> InlineResponse20012 gists_id_forks_get(id, access_token=access_token, page=page, per_page=per_page)

获取 Fork 了指定代码片段的列表

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取 Fork 了指定代码片段的列表
    api_response = api_instance.gists_id_forks_get(id, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_forks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_forks_post**
> gists_id_forks_post(id, body=body)

Fork代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
body = pygitee.IdForksBody() # IdForksBody |  (optional)

try:
    # Fork代码片段
    api_instance.gists_id_forks_post(id, body=body)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_forks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **body** | [**IdForksBody**](IdForksBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_get**
> InlineResponse20010 gists_id_get(id, access_token=access_token)

获取单条代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单条代码片段
    api_response = api_instance.gists_id_get(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_patch**
> InlineResponse20010 gists_id_patch(id, body=body)

修改代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
body = pygitee.GistsIdBody() # GistsIdBody |  (optional)

try:
    # 修改代码片段
    api_response = api_instance.gists_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **body** | [**GistsIdBody**](GistsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_star_delete**
> gists_id_star_delete(id, access_token=access_token)

取消Star代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消Star代码片段
    api_instance.gists_id_star_delete(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_star_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_star_get**
> gists_id_star_get(id, access_token=access_token)

判断代码片段是否已Star

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 判断代码片段是否已Star
    api_instance.gists_id_star_get(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_star_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_id_star_put**
> gists_id_star_put(id, body=body)

Star代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 代码片段的ID
body = pygitee.IdStarBody() # IdStarBody |  (optional)

try:
    # Star代码片段
    api_instance.gists_id_star_put(id, body=body)
except ApiException as e:
    print("Exception when calling GistsApi->gists_id_star_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 代码片段的ID | 
 **body** | [**IdStarBody**](IdStarBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_post**
> InlineResponse20010 gists_post(body=body)

创建代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
body = pygitee.GistsBody() # GistsBody |  (optional)

try:
    # 创建代码片段
    api_response = api_instance.gists_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GistsBody**](GistsBody.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_starred_get**
> InlineResponse2009 gists_starred_get(access_token=access_token, since=since, page=page, per_page=per_page)

获取用户Star的代码片段

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
api_instance = pygitee.GistsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取用户Star的代码片段
    api_response = api_instance.gists_starred_get(access_token=access_token, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GistsApi->gists_starred_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

