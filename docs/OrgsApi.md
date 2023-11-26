# pygitee.OrgsApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_org_events_get**](OrgsApi.md#orgs_org_events_get) | **GET** /orgs/{org}/events | 列出组织的公开动态
[**orgs_org_followers_get**](OrgsApi.md#orgs_org_followers_get) | **GET** /orgs/{org}/followers | 列出指定组织的所有关注者
[**orgs_org_get**](OrgsApi.md#orgs_org_get) | **GET** /orgs/{org} | 获取一个组织
[**orgs_org_members_get**](OrgsApi.md#orgs_org_members_get) | **GET** /orgs/{org}/members | 列出一个组织的所有成员
[**orgs_org_memberships_username_delete**](OrgsApi.md#orgs_org_memberships_username_delete) | **DELETE** /orgs/{org}/memberships/{username} | 移除授权用户所管理组织中的成员
[**orgs_org_repos_get**](OrgsApi.md#orgs_org_repos_get) | **GET** /orgs/{org}/repos | 获取一个组织的仓库
[**user_memberships_orgs_get**](OrgsApi.md#user_memberships_orgs_get) | **GET** /user/memberships/orgs | 列出授权用户在所属组织的成员资料
[**user_memberships_orgs_org_get**](OrgsApi.md#user_memberships_orgs_org_get) | **GET** /user/memberships/orgs/{org} | 获取授权用户在一个组织的成员资料
[**user_orgs_get**](OrgsApi.md#user_orgs_get) | **GET** /user/orgs | 列出授权用户所属的组织
[**users_username_events_orgs_org_get**](OrgsApi.md#users_username_events_orgs_org_get) | **GET** /users/{username}/events/orgs/{org} | 列出用户所属组织的动态
[**users_username_orgs_get**](OrgsApi.md#users_username_orgs_get) | **GET** /users/{username}/orgs | 列出用户所属的组织

# **orgs_org_events_get**
> InlineResponse20012 orgs_org_events_get(org, access_token=access_token, prev_id=prev_id, limit=limit)

列出组织的公开动态

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出组织的公开动态
    api_response = api_instance.orgs_org_events_get(org, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->orgs_org_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
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

# **orgs_org_followers_get**
> InlineResponse20018 orgs_org_followers_get(org, access_token=access_token, page=page, per_page=per_page)

列出指定组织的所有关注者

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出指定组织的所有关注者
    api_response = api_instance.orgs_org_followers_get(org, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->orgs_org_followers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_get**
> InlineResponse20017 orgs_org_get(org, access_token=access_token)

获取一个组织

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个组织
    api_response = api_instance.orgs_org_get(org, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->orgs_org_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_members_get**
> InlineResponse20019 orgs_org_members_get(org, access_token=access_token, page=page, per_page=per_page, role=role)

列出一个组织的所有成员

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
role = 'role_example' # str | 根据角色筛选成员 (optional)

try:
    # 列出一个组织的所有成员
    api_response = api_instance.orgs_org_members_get(org, access_token=access_token, page=page, per_page=per_page, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->orgs_org_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **role** | **str**| 根据角色筛选成员 | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_org_memberships_username_delete**
> orgs_org_memberships_username_delete(org, username, access_token=access_token)

移除授权用户所管理组织中的成员

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 移除授权用户所管理组织中的成员
    api_instance.orgs_org_memberships_username_delete(org, username, access_token=access_token)
except ApiException as e:
    print("Exception when calling OrgsApi->orgs_org_memberships_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
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

# **orgs_org_repos_get**
> InlineResponse2007 orgs_org_repos_get(org, access_token=access_token, type=type, page=page, per_page=per_page)

获取一个组织的仓库

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'type_example' # str | 筛选仓库的类型，可以是 all, public, private。默认: all (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取一个组织的仓库
    api_response = api_instance.orgs_org_repos_get(org, access_token=access_token, type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->orgs_org_repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 筛选仓库的类型，可以是 all, public, private。默认: all | [optional] 
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

# **user_memberships_orgs_get**
> InlineResponse20052 user_memberships_orgs_get(access_token=access_token, active=active, page=page, per_page=per_page)

列出授权用户在所属组织的成员资料

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
active = true # bool | 根据成员是否已激活进行筛选资料，缺省返回所有资料 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户在所属组织的成员资料
    api_response = api_instance.user_memberships_orgs_get(access_token=access_token, active=active, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->user_memberships_orgs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **active** | **bool**| 根据成员是否已激活进行筛选资料，缺省返回所有资料 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_memberships_orgs_org_get**
> InlineResponse20052 user_memberships_orgs_org_get(org, access_token=access_token)

获取授权用户在一个组织的成员资料

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户在一个组织的成员资料
    api_response = api_instance.user_memberships_orgs_org_get(org, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->user_memberships_orgs_org_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_orgs_get**
> InlineResponse20017 user_orgs_get(access_token=access_token, page=page, per_page=per_page, admin=admin)

列出授权用户所属的组织

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
admin = true # bool | 只列出授权用户管理的组织 (optional)

try:
    # 列出授权用户所属的组织
    api_response = api_instance.user_orgs_get(access_token=access_token, page=page, per_page=per_page, admin=admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->user_orgs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **admin** | **bool**| 只列出授权用户管理的组织 | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_events_orgs_org_get**
> InlineResponse20012 users_username_events_orgs_org_get(username, org, access_token=access_token, prev_id=prev_id, limit=limit)

列出用户所属组织的动态

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
prev_id = 56 # int | 滚动列表的最后一条记录的id (optional)
limit = 56 # int | 滚动列表每页的数量，最大为 100 (optional)

try:
    # 列出用户所属组织的动态
    api_response = api_instance.users_username_events_orgs_org_get(username, org, access_token=access_token, prev_id=prev_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->users_username_events_orgs_org_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **org** | **str**| 组织的路径(path/login) | 
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

# **users_username_orgs_get**
> InlineResponse20017 users_username_orgs_get(username, access_token=access_token, page=page, per_page=per_page)

列出用户所属的组织

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
api_instance = pygitee.OrgsApi(pygitee.ApiClient(configuration))
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出用户所属的组织
    api_response = api_instance.users_username_orgs_get(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->users_username_orgs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

