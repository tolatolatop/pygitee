# pygitee.NotificationsApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_count_get**](NotificationsApi.md#notifications_count_get) | **GET** /notifications/count | 获取授权用户的通知数
[**notifications_messages_get**](NotificationsApi.md#notifications_messages_get) | **GET** /notifications/messages | 列出授权用户的所有私信
[**notifications_messages_id_get**](NotificationsApi.md#notifications_messages_id_get) | **GET** /notifications/messages/{id} | 获取一条私信
[**notifications_threads_get**](NotificationsApi.md#notifications_threads_get) | **GET** /notifications/threads | 列出授权用户的所有通知
[**notifications_threads_id_get**](NotificationsApi.md#notifications_threads_id_get) | **GET** /notifications/threads/{id} | 获取一条通知
[**repos_owner_repo_notifications_get**](NotificationsApi.md#repos_owner_repo_notifications_get) | **GET** /repos/{owner}/{repo}/notifications | 列出一个仓库里的通知

# **notifications_count_get**
> InlineResponse20013 notifications_count_get(access_token=access_token, unread=unread)

获取授权用户的通知数

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
api_instance = pygitee.NotificationsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)

try:
    # 获取授权用户的通知数
    api_response = api_instance.notifications_count_get(access_token=access_token, unread=unread)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只获取未读消息，默认：否 | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_get**
> InlineResponse20014 notifications_messages_get(access_token=access_token, unread=unread, since=since, before=before, ids=ids, page=page, per_page=per_page)

列出授权用户的所有私信

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
api_instance = pygitee.NotificationsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只显示未读私信，默认：否 (optional)
since = 'since_example' # str | 只获取在给定时间后更新的私信，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的私信，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组私信 ID，以 , 分隔 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户的所有私信
    api_response = api_instance.notifications_messages_get(access_token=access_token, unread=unread, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只显示未读私信，默认：否 | [optional] 
 **since** | **str**| 只获取在给定时间后更新的私信，要求时间格式为 ISO 8601 | [optional] 
 **before** | **str**| 只获取在给定时间前更新的私信，要求时间格式为 ISO 8601 | [optional] 
 **ids** | **str**| 指定一组私信 ID，以 , 分隔 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_id_get**
> InlineResponse20015 notifications_messages_id_get(id, access_token=access_token)

获取一条私信

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
api_instance = pygitee.NotificationsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 私信的 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一条私信
    api_response = api_instance.notifications_messages_id_get(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_messages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 私信的 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_threads_get**
> InlineResponse20014 notifications_threads_get(access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)

列出授权用户的所有通知

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
api_instance = pygitee.NotificationsApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)
participating = true # bool | 是否只获取自己直接参与的消息，默认：否 (optional)
type = 'type_example' # str | 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 (optional)
since = 'since_example' # str | 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组通知 ID，以 , 分隔 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出授权用户的所有通知
    api_response = api_instance.notifications_threads_get(access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_threads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只获取未读消息，默认：否 | [optional] 
 **participating** | **bool**| 是否只获取自己直接参与的消息，默认：否 | [optional] 
 **type** | **str**| 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 | [optional] 
 **since** | **str**| 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **before** | **str**| 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **ids** | **str**| 指定一组通知 ID，以 , 分隔 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_threads_id_get**
> InlineResponse20016 notifications_threads_id_get(id, access_token=access_token)

获取一条通知

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
api_instance = pygitee.NotificationsApi(pygitee.ApiClient(configuration))
id = 'id_example' # str | 通知的 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一条通知
    api_response = api_instance.notifications_threads_id_get(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_threads_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 通知的 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_notifications_get**
> InlineResponse20014 repos_owner_repo_notifications_get(owner, repo, access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)

列出一个仓库里的通知

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
api_instance = pygitee.NotificationsApi(pygitee.ApiClient(configuration))
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)
participating = true # bool | 是否只获取自己直接参与的消息，默认：否 (optional)
type = 'type_example' # str | 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 (optional)
since = 'since_example' # str | 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组通知 ID，以 , 分隔 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出一个仓库里的通知
    api_response = api_instance.repos_owner_repo_notifications_get(owner, repo, access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->repos_owner_repo_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只获取未读消息，默认：否 | [optional] 
 **participating** | **bool**| 是否只获取自己直接参与的消息，默认：否 | [optional] 
 **type** | **str**| 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 | [optional] 
 **since** | **str**| 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **before** | **str**| 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **ids** | **str**| 指定一组通知 ID，以 , 分隔 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

