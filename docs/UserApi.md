# pygitee.UserApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_followers_get**](UserApi.md#user_followers_get) | **GET** /user/followers | 列出授权用户的关注者
[**user_following_get**](UserApi.md#user_following_get) | **GET** /user/following | 列出授权用户正关注的用户
[**user_following_username_delete**](UserApi.md#user_following_username_delete) | **DELETE** /user/following/{username} | 取消关注一个用户
[**user_following_username_get**](UserApi.md#user_following_username_get) | **GET** /user/following/{username} | 检查授权用户是否关注了一个用户
[**user_following_username_put**](UserApi.md#user_following_username_put) | **PUT** /user/following/{username} | 关注一个用户
[**user_get**](UserApi.md#user_get) | **GET** /user | 获取授权用户的资料
[**user_keys_get**](UserApi.md#user_keys_get) | **GET** /user/keys | 列出授权用户的所有公钥
[**user_keys_id_delete**](UserApi.md#user_keys_id_delete) | **DELETE** /user/keys/{id} | 删除一个公钥
[**user_keys_id_get**](UserApi.md#user_keys_id_get) | **GET** /user/keys/{id} | 获取一个公钥
[**user_keys_post**](UserApi.md#user_keys_post) | **POST** /user/keys | 添加一个公钥
[**user_namespace_get**](UserApi.md#user_namespace_get) | **GET** /user/namespace | 获取授权用户的一个 Namespace
[**user_namespaces_get**](UserApi.md#user_namespaces_get) | **GET** /user/namespaces | 列出授权用户所有的 Namespace
[**user_patch**](UserApi.md#user_patch) | **PATCH** /user | 更新授权用户的资料
[**user_starred_get**](UserApi.md#user_starred_get) | **GET** /user/starred | 列出授权用户 star 了的仓库
[**user_starred_owner_repo_delete**](UserApi.md#user_starred_owner_repo_delete) | **DELETE** /user/starred/{owner}/{repo} | 取消 star 一个仓库
[**user_starred_owner_repo_get**](UserApi.md#user_starred_owner_repo_get) | **GET** /user/starred/{owner}/{repo} | 检查授权用户是否 star 了一个仓库
[**user_starred_owner_repo_put**](UserApi.md#user_starred_owner_repo_put) | **PUT** /user/starred/{owner}/{repo} | star 一个仓库
[**user_subscriptions_get**](UserApi.md#user_subscriptions_get) | **GET** /user/subscriptions | 列出授权用户 watch 了的仓库
[**user_subscriptions_owner_repo_delete**](UserApi.md#user_subscriptions_owner_repo_delete) | **DELETE** /user/subscriptions/{owner}/{repo} | 取消 watch 一个仓库
[**user_subscriptions_owner_repo_get**](UserApi.md#user_subscriptions_owner_repo_get) | **GET** /user/subscriptions/{owner}/{repo} | 检查授权用户是否 watch 了一个仓库
[**user_subscriptions_owner_repo_put**](UserApi.md#user_subscriptions_owner_repo_put) | **PUT** /user/subscriptions/{owner}/{repo} | watch 一个仓库
[**users_organization_post**](UserApi.md#users_organization_post) | **POST** /users/organization | 创建组织
[**users_username_events_get**](UserApi.md#users_username_events_get) | **GET** /users/{username}/events | 列出用户的动态
[**users_username_events_public_get**](UserApi.md#users_username_events_public_get) | **GET** /users/{username}/events/public | 列出用户的公开动态
[**users_username_followers_get**](UserApi.md#users_username_followers_get) | **GET** /users/{username}/followers | 列出指定用户的关注者
[**users_username_following_get**](UserApi.md#users_username_following_get) | **GET** /users/{username}/following | 列出指定用户正在关注的用户
[**users_username_following_target_user_get**](UserApi.md#users_username_following_target_user_get) | **GET** /users/{username}/following/{target_user} | 检查指定用户是否关注目标用户
[**users_username_get**](UserApi.md#users_username_get) | **GET** /users/{username} | 获取一个用户
[**users_username_keys_get**](UserApi.md#users_username_keys_get) | **GET** /users/{username}/keys | 列出指定用户的所有公钥
[**users_username_received_events_get**](UserApi.md#users_username_received_events_get) | **GET** /users/{username}/received_events | 列出一个用户收到的动态
[**users_username_received_events_public_get**](UserApi.md#users_username_received_events_public_get) | **GET** /users/{username}/received_events/public | 列出一个用户收到的公开动态
[**users_username_starred_get**](UserApi.md#users_username_starred_get) | **GET** /users/{username}/starred | 列出用户 star 了的仓库
[**users_username_subscriptions_get**](UserApi.md#users_username_subscriptions_get) | **GET** /users/{username}/subscriptions | 列出用户 watch 了的仓库

# **user_followers_get**
> InlineResponse20021 user_followers_get(access_token=access_token, page=page, per_page=per_page)

列出授权用户的关注者

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户的关注者
    api_response = api_instance.user_followers_get(access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_followers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_following_get**
> InlineResponse20021 user_following_get(access_token=access_token, page=page, per_page=per_page)

列出授权用户正关注的用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户正关注的用户
    api_response = api_instance.user_following_get(access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_following_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_following_username_delete**
> user_following_username_delete(username, access_token=access_token)

取消关注一个用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消关注一个用户
    api_instance.user_following_username_delete(username, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_following_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **user_following_username_get**
> user_following_username_get(username, access_token=access_token)

检查授权用户是否关注了一个用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否关注了一个用户
    api_instance.user_following_username_get(username, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_following_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **user_following_username_put**
> user_following_username_put(username, body=body)

关注一个用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
body = pygitee.FollowingUsernameBody() # FollowingUsernameBody |  (optional)

try:
    # 关注一个用户
    api_instance.user_following_username_put(username, body=body)
except ApiException as e:
    print("Exception when calling UserApi->user_following_username_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **body** | [**FollowingUsernameBody**](FollowingUsernameBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> InlineResponse20054 user_get(access_token=access_token)

获取授权用户的资料

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户的资料
    api_response = api_instance.user_get(access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_keys_get**
> InlineResponse20040 user_keys_get(access_token=access_token, page=page, per_page=per_page)

列出授权用户的所有公钥

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户的所有公钥
    api_response = api_instance.user_keys_get(access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_keys_id_delete**
> user_keys_id_delete(id, access_token=access_token)

删除一个公钥

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除一个公钥
    api_instance.user_keys_id_delete(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_keys_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_keys_id_get**
> InlineResponse20040 user_keys_id_get(id, access_token=access_token)

获取一个公钥

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
id = 56 # int | 公钥 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个公钥
    api_response = api_instance.user_keys_id_get(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_keys_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 公钥 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_keys_post**
> InlineResponse20040 user_keys_post(body=body)

添加一个公钥

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
body = pygitee.UserKeysBody() # UserKeysBody |  (optional)

try:
    # 添加一个公钥
    api_response = api_instance.user_keys_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserKeysBody**](UserKeysBody.md)|  | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_namespace_get**
> InlineResponse20055 user_namespace_get(path, access_token=access_token)

获取授权用户的一个 Namespace

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
path = 'path_example' # str | Namespace path
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户的一个 Namespace
    api_response = api_instance.user_namespace_get(path, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_namespace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Namespace path | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_namespaces_get**
> InlineResponse20055 user_namespaces_get(access_token=access_token, mode=mode)

列出授权用户所有的 Namespace

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
mode = 'mode_example' # str | 参与方式: project(所有参与仓库的namepsce)、intrant(所加入的namespace)、all(包含前两者)，默认(intrant) (optional)

try:
    # 列出授权用户所有的 Namespace
    api_response = api_instance.user_namespaces_get(access_token=access_token, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_namespaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **mode** | **str**| 参与方式: project(所有参与仓库的namepsce)、intrant(所加入的namespace)、all(包含前两者)，默认(intrant) | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_patch**
> InlineResponse20053 user_patch(body=body)

更新授权用户的资料

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
body = pygitee.UserBody() # UserBody |  (optional)

try:
    # 更新授权用户的资料
    api_response = api_instance.user_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserBody**](UserBody.md)|  | [optional] 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_starred_get**
> InlineResponse2007 user_starred_get(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)

列出授权用户 star 了的仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'sort_example' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional)
direction = 'direction_example' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户 star 了的仓库
    api_response = api_instance.user_starred_get(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_starred_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] 
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] 
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

# **user_starred_owner_repo_delete**
> user_starred_owner_repo_delete(owner, repo, access_token=access_token)

取消 star 一个仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消 star 一个仓库
    api_instance.user_starred_owner_repo_delete(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_starred_owner_repo_delete: %s\n" % e)
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

# **user_starred_owner_repo_get**
> user_starred_owner_repo_get(owner, repo, access_token=access_token)

检查授权用户是否 star 了一个仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否 star 了一个仓库
    api_instance.user_starred_owner_repo_get(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_starred_owner_repo_get: %s\n" % e)
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

# **user_starred_owner_repo_put**
> user_starred_owner_repo_put(owner, repo, body=body)

star 一个仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.OwnerRepoBody1() # OwnerRepoBody1 |  (optional)

try:
    # star 一个仓库
    api_instance.user_starred_owner_repo_put(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling UserApi->user_starred_owner_repo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**OwnerRepoBody1**](OwnerRepoBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_subscriptions_get**
> InlineResponse2007 user_subscriptions_get(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)

列出授权用户 watch 了的仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'sort_example' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional)
direction = 'direction_example' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户 watch 了的仓库
    api_response = api_instance.user_subscriptions_get(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] 
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] 
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

# **user_subscriptions_owner_repo_delete**
> user_subscriptions_owner_repo_delete(owner, repo, access_token=access_token)

取消 watch 一个仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消 watch 一个仓库
    api_instance.user_subscriptions_owner_repo_delete(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_subscriptions_owner_repo_delete: %s\n" % e)
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

# **user_subscriptions_owner_repo_get**
> user_subscriptions_owner_repo_get(owner, repo, access_token=access_token)

检查授权用户是否 watch 了一个仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否 watch 了一个仓库
    api_instance.user_subscriptions_owner_repo_get(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->user_subscriptions_owner_repo_get: %s\n" % e)
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

# **user_subscriptions_owner_repo_put**
> user_subscriptions_owner_repo_put(owner, repo, body=body)

watch 一个仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = pygitee.OwnerRepoBody2() # OwnerRepoBody2 |  (optional)

try:
    # watch 一个仓库
    api_instance.user_subscriptions_owner_repo_put(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling UserApi->user_subscriptions_owner_repo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**OwnerRepoBody2**](OwnerRepoBody2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_organization_post**
> InlineResponse20018 users_organization_post(body=body)

创建组织

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
body = pygitee.UsersOrganizationBody() # UsersOrganizationBody |  (optional)

try:
    # 创建组织
    api_response = api_instance.users_organization_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_organization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersOrganizationBody**](UsersOrganizationBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_events_get**
> InlineResponse20013 users_username_events_get(username, access_token=access_token, prev_id=prev_id, limit=limit)

列出用户的动态

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出用户的动态
    api_response = api_instance.users_username_events_get(username, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_events_public_get**
> InlineResponse20013 users_username_events_public_get(username, access_token=access_token, prev_id=prev_id, limit=limit)

列出用户的公开动态

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出用户的公开动态
    api_response = api_instance.users_username_events_public_get(username, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_events_public_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_followers_get**
> InlineResponse20021 users_username_followers_get(username, access_token=access_token, page=page, per_page=per_page)

列出指定用户的关注者

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出指定用户的关注者
    api_response = api_instance.users_username_followers_get(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_followers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_following_get**
> InlineResponse20021 users_username_following_get(username, access_token=access_token, page=page, per_page=per_page)

列出指定用户正在关注的用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出指定用户正在关注的用户
    api_response = api_instance.users_username_following_get(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_following_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_following_target_user_get**
> users_username_following_target_user_get(username, target_user, access_token=access_token)

检查指定用户是否关注目标用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
target_user = 'target_user_example' # str | 目标用户的用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查指定用户是否关注目标用户
    api_instance.users_username_following_target_user_get(username, target_user, access_token=access_token)
except ApiException as e:
    print("Exception when calling UserApi->users_username_following_target_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **target_user** | **str**| 目标用户的用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_get**
> InlineResponse20056 users_username_get(username, access_token=access_token)

获取一个用户

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个用户
    api_response = api_instance.users_username_get(username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_keys_get**
> InlineResponse20041 users_username_keys_get(username, access_token=access_token, page=page, per_page=per_page)

列出指定用户的所有公钥

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出指定用户的所有公钥
    api_response = api_instance.users_username_keys_get(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_received_events_get**
> InlineResponse20013 users_username_received_events_get(username, access_token=access_token, prev_id=prev_id, limit=limit)

列出一个用户收到的动态

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出一个用户收到的动态
    api_response = api_instance.users_username_received_events_get(username, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_received_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_received_events_public_get**
> InlineResponse20013 users_username_received_events_public_get(username, access_token=access_token, prev_id=prev_id, limit=limit)

列出一个用户收到的公开动态

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出一个用户收到的公开动态
    api_response = api_instance.users_username_received_events_public_get(username, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_received_events_public_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_starred_get**
> InlineResponse2007 users_username_starred_get(username, access_token=access_token, prev_id=prev_id, limit=limit, sort=sort, direction=direction)

列出用户 star 了的仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)
sort = 'sort_example' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional)
direction = 'direction_example' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional)

try:
    # 列出用户 star 了的仓库
    api_response = api_instance.users_username_starred_get(username, access_token=access_token, prev_id=prev_id, limit=limit, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_starred_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] 
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_subscriptions_get**
> InlineResponse2007 users_username_subscriptions_get(username, access_token=access_token, prev_id=prev_id, limit=limit, sort=sort, direction=direction)

列出用户 watch 了的仓库

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
api_instance = pygitee.UserApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)
sort = 'sort_example' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional)
direction = 'direction_example' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional)

try:
    # 列出用户 watch 了的仓库
    api_response = api_instance.users_username_subscriptions_get(username, access_token=access_token, prev_id=prev_id, limit=limit, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_username_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **prev_id** | **int**| 滚动列表的最后一条记录的id | [optional] 
 **limit** | **int**| 滚动列表每页的数量，最大为 100 | [optional] 
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] 
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

