# pygitee.EnterpriseApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprises_enterprise_get**](EnterpriseApi.md#enterprises_enterprise_get) | **GET** /enterprises/{enterprise} | 获取一个企业
[**enterprises_enterprise_labels_get**](EnterpriseApi.md#enterprises_enterprise_labels_get) | **GET** /enterprises/{enterprise}/labels | 获取企业所有标签
[**enterprises_enterprise_labels_name_get**](EnterpriseApi.md#enterprises_enterprise_labels_name_get) | **GET** /enterprises/{enterprise}/labels/{name} | 获取企业某个标签
[**enterprises_enterprise_members_get**](EnterpriseApi.md#enterprises_enterprise_members_get) | **GET** /enterprises/{enterprise}/members | 列出企业的所有成员
[**enterprises_enterprise_members_username_get**](EnterpriseApi.md#enterprises_enterprise_members_username_get) | **GET** /enterprises/{enterprise}/members/{username} | 获取企业的一个成员
[**enterprises_enterprise_repos_get**](EnterpriseApi.md#enterprises_enterprise_repos_get) | **GET** /enterprises/{enterprise}/repos | 获取企业的所有仓库
[**user_enterprises_get**](EnterpriseApi.md#user_enterprises_get) | **GET** /user/enterprises | 列出授权用户所属的企业

# **enterprises_enterprise_get**
> InlineResponse2002 enterprises_enterprise_get(enterprise, access_token=access_token)

获取一个企业

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个企业
    api_response = api_instance.enterprises_enterprise_get(enterprise, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->enterprises_enterprise_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_labels_get**
> InlineResponse2005 enterprises_enterprise_labels_get(enterprise, access_token=access_token)

获取企业所有标签

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业所有标签
    api_response = api_instance.enterprises_enterprise_labels_get(enterprise, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->enterprises_enterprise_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_labels_name_get**
> InlineResponse2005 enterprises_enterprise_labels_name_get(enterprise, name, access_token=access_token)

获取企业某个标签

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业某个标签
    api_response = api_instance.enterprises_enterprise_labels_name_get(enterprise, name, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->enterprises_enterprise_labels_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_members_get**
> InlineResponse2006 enterprises_enterprise_members_get(enterprise, access_token=access_token, role=role, page=page, per_page=per_page)

列出企业的所有成员

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
role = 'role_example' # str | 根据角色筛选成员 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 列出企业的所有成员
    api_response = api_instance.enterprises_enterprise_members_get(enterprise, access_token=access_token, role=role, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->enterprises_enterprise_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **role** | **str**| 根据角色筛选成员 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_members_username_get**
> InlineResponse2006 enterprises_enterprise_members_username_get(enterprise, username, access_token=access_token)

获取企业的一个成员

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业的一个成员
    api_response = api_instance.enterprises_enterprise_members_username_get(enterprise, username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->enterprises_enterprise_members_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_repos_get**
> InlineResponse2007 enterprises_enterprise_repos_get(enterprise, access_token=access_token, type=type, direct=direct, page=page, per_page=per_page)

获取企业的所有仓库

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
type = 'type_example' # str | 筛选仓库的类型，可以是 all, public, internal, private。默认: all (optional)
direct = true # bool | 只获取直属仓库，默认: false (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 获取企业的所有仓库
    api_response = api_instance.enterprises_enterprise_repos_get(enterprise, access_token=access_token, type=type, direct=direct, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->enterprises_enterprise_repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **type** | **str**| 筛选仓库的类型，可以是 all, public, internal, private。默认: all | [optional] 
 **direct** | **bool**| 只获取直属仓库，默认: false | [optional] 
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

# **user_enterprises_get**
> InlineResponse2002 user_enterprises_get(access_token=access_token, page=page, per_page=per_page, admin=admin)

列出授权用户所属的企业

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
api_instance = pygitee.EnterpriseApi(pygitee.ApiClient(configuration))
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
admin = true # bool | 只列出授权用户管理的企业 (optional)

try:
    # 列出授权用户所属的企业
    api_response = api_instance.user_enterprises_get(access_token=access_token, page=page, per_page=per_page, admin=admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->user_enterprises_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **admin** | **bool**| 只列出授权用户管理的企业 | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

