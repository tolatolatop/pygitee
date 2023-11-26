# pygitee.WeekReportApi

All URIs are relative to *https://gitee.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprises_enterprise_users_username_week_reports_get**](WeekReportApi.md#enterprises_enterprise_users_username_week_reports_get) | **GET** /enterprises/{enterprise}/users/{username}/week_reports | 个人周报列表
[**enterprises_enterprise_week_report_id_patch**](WeekReportApi.md#enterprises_enterprise_week_report_id_patch) | **PATCH** /enterprises/{enterprise}/week_report/{id} | 编辑周报
[**enterprises_enterprise_week_report_post**](WeekReportApi.md#enterprises_enterprise_week_report_post) | **POST** /enterprises/{enterprise}/week_report | 新建周报
[**enterprises_enterprise_week_reports_get**](WeekReportApi.md#enterprises_enterprise_week_reports_get) | **GET** /enterprises/{enterprise}/week_reports | 企业成员周报列表
[**enterprises_enterprise_week_reports_id_get**](WeekReportApi.md#enterprises_enterprise_week_reports_id_get) | **GET** /enterprises/{enterprise}/week_reports/{id} | 周报详情

# **enterprises_enterprise_users_username_week_reports_get**
> InlineResponse2008 enterprises_enterprise_users_username_week_reports_get(enterprise, username, access_token=access_token, page=page, per_page=per_page)

个人周报列表

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
api_instance = pygitee.WeekReportApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)

try:
    # 个人周报列表
    api_response = api_instance.enterprises_enterprise_users_username_week_reports_get(enterprise, username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeekReportApi->enterprises_enterprise_users_username_week_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_report_id_patch**
> InlineResponse2008 enterprises_enterprise_week_report_id_patch(enterprise, id, body=body)

编辑周报

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
api_instance = pygitee.WeekReportApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID
body = pygitee.WeekReportIdBody() # WeekReportIdBody |  (optional)

try:
    # 编辑周报
    api_response = api_instance.enterprises_enterprise_week_report_id_patch(enterprise, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeekReportApi->enterprises_enterprise_week_report_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 
 **body** | [**WeekReportIdBody**](WeekReportIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_report_post**
> InlineResponse2008 enterprises_enterprise_week_report_post(enterprise, body=body)

新建周报

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
api_instance = pygitee.WeekReportApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
body = pygitee.EnterpriseWeekReportBody() # EnterpriseWeekReportBody |  (optional)

try:
    # 新建周报
    api_response = api_instance.enterprises_enterprise_week_report_post(enterprise, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeekReportApi->enterprises_enterprise_week_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **body** | [**EnterpriseWeekReportBody**](EnterpriseWeekReportBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_reports_get**
> InlineResponse2008 enterprises_enterprise_week_reports_get(enterprise, access_token=access_token, page=page, per_page=per_page, username=username, year=year, week_index=week_index, _date=_date)

企业成员周报列表

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
api_instance = pygitee.WeekReportApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 56 # int | 当前的页码 (optional)
per_page = 56 # int | 每页的数量，最大为 100 (optional)
username = 'username_example' # str | 用户名(username/login) (optional)
year = 56 # int | 周报所属年 (optional)
week_index = 56 # int | 周报所属周 (optional)
_date = '_date_example' # str | 周报日期(格式：2019-03-25) (optional)

try:
    # 企业成员周报列表
    api_response = api_instance.enterprises_enterprise_week_reports_get(enterprise, access_token=access_token, page=page, per_page=per_page, username=username, year=year, week_index=week_index, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeekReportApi->enterprises_enterprise_week_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] 
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] 
 **username** | **str**| 用户名(username/login) | [optional] 
 **year** | **int**| 周报所属年 | [optional] 
 **week_index** | **int**| 周报所属周 | [optional] 
 **_date** | **str**| 周报日期(格式：2019-03-25) | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_enterprise_week_reports_id_get**
> InlineResponse2008 enterprises_enterprise_week_reports_id_get(enterprise, id, access_token=access_token)

周报详情

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
api_instance = pygitee.WeekReportApi(pygitee.ApiClient(configuration))
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 周报详情
    api_response = api_instance.enterprises_enterprise_week_reports_id_get(enterprise, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeekReportApi->enterprises_enterprise_week_reports_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

