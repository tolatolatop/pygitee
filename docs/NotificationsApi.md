# pygitee.NotificationsApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_count_get**](NotificationsApi.md#notifications_count_get) | **GET** /notifications/count | 获取授权用户的通知数
[**notifications_messages_get**](NotificationsApi.md#notifications_messages_get) | **GET** /notifications/messages | 列出授权用户的所有私信
[**notifications_messages_id_get**](NotificationsApi.md#notifications_messages_id_get) | **GET** /notifications/messages/{id} | 获取一条私信
[**notifications_messages_id_patch**](NotificationsApi.md#notifications_messages_id_patch) | **PATCH** /notifications/messages/{id} | 标记一条私信为已读
[**notifications_messages_post**](NotificationsApi.md#notifications_messages_post) | **POST** /notifications/messages | 发送私信给指定用户
[**notifications_messages_put**](NotificationsApi.md#notifications_messages_put) | **PUT** /notifications/messages | 标记所有私信为已读
[**notifications_threads_get**](NotificationsApi.md#notifications_threads_get) | **GET** /notifications/threads | 列出授权用户的所有通知
[**notifications_threads_id_get**](NotificationsApi.md#notifications_threads_id_get) | **GET** /notifications/threads/{id} | 获取一条通知
[**notifications_threads_id_patch**](NotificationsApi.md#notifications_threads_id_patch) | **PATCH** /notifications/threads/{id} | 标记一条通知为已读
[**notifications_threads_put**](NotificationsApi.md#notifications_threads_put) | **PUT** /notifications/threads | 标记所有通知为已读
[**repos_owner_repo_notifications_get**](NotificationsApi.md#repos_owner_repo_notifications_get) | **GET** /repos/{owner}/{repo}/notifications | 列出一个仓库里的通知
[**repos_owner_repo_notifications_put**](NotificationsApi.md#repos_owner_repo_notifications_put) | **PUT** /repos/{owner}/{repo}/notifications | 标记一个仓库里的通知为已读

# **notifications_count_get**
> InlineResponse20014 notifications_count_get(access_token=access_token, unread=unread)

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

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_get**
> InlineResponse20015 notifications_messages_get(access_token=access_token, unread=unread, since=since, before=before, ids=ids, page=page, per_page=per_page)

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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_id_get**
> InlineResponse20016 notifications_messages_id_get(id, access_token=access_token)

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

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_id_patch**
> notifications_messages_id_patch(id, body=body)

标记一条私信为已读

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
body = pygitee.MessagesIdBody() # MessagesIdBody |  (optional)

try:
    # 标记一条私信为已读
    api_instance.notifications_messages_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_messages_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 私信的 ID | 
 **body** | [**MessagesIdBody**](MessagesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_post**
> InlineResponse20016 notifications_messages_post(body=body)

发送私信给指定用户

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
body = pygitee.NotificationsMessagesBody1() # NotificationsMessagesBody1 |  (optional)

try:
    # 发送私信给指定用户
    api_response = api_instance.notifications_messages_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationsMessagesBody1**](NotificationsMessagesBody1.md)|  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_messages_put**
> notifications_messages_put(body=body)

标记所有私信为已读

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
body = pygitee.NotificationsMessagesBody() # NotificationsMessagesBody |  (optional)

try:
    # 标记所有私信为已读
    api_instance.notifications_messages_put(body=body)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_messages_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationsMessagesBody**](NotificationsMessagesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_threads_get**
> InlineResponse20015 notifications_threads_get(access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)

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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_threads_id_get**
> InlineResponse20017 notifications_threads_id_get(id, access_token=access_token)

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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_threads_id_patch**
> notifications_threads_id_patch(id, body=body)

标记一条通知为已读

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
body = pygitee.ThreadsIdBody() # ThreadsIdBody |  (optional)

try:
    # 标记一条通知为已读
    api_instance.notifications_threads_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_threads_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 通知的 ID | 
 **body** | [**ThreadsIdBody**](ThreadsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_threads_put**
> notifications_threads_put(body=body)

标记所有通知为已读

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
body = pygitee.NotificationsThreadsBody() # NotificationsThreadsBody |  (optional)

try:
    # 标记所有通知为已读
    api_instance.notifications_threads_put(body=body)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_threads_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationsThreadsBody**](NotificationsThreadsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_notifications_get**
> InlineResponse20015 repos_owner_repo_notifications_get(owner, repo, access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)

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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_owner_repo_notifications_put**
> repos_owner_repo_notifications_put(owner, repo, body=body)

标记一个仓库里的通知为已读

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
body = pygitee.RepoNotificationsBody() # RepoNotificationsBody |  (optional)

try:
    # 标记一个仓库里的通知为已读
    api_instance.repos_owner_repo_notifications_put(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling NotificationsApi->repos_owner_repo_notifications_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**RepoNotificationsBody**](RepoNotificationsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

