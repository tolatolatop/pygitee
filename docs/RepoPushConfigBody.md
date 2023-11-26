# RepoPushConfigBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**author_email_suffix** | **str** | 指定邮箱域名的后缀 | [optional] 
**commit_message_regex** | **str** | 用于验证提交信息的正则表达式 | [optional] 
**except_manager** | **bool** | 仓库管理员不受上述规则限制 | [optional] 
**max_file_size** | **int** | 限制单文件大小（MB） | [optional] 
**restrict_author_email_suffix** | **bool** | 启用只允许指定邮箱域名后缀的提交 | [optional] 
**restrict_commit_message** | **bool** | 启用提交信息正则表达式校验 | [optional] 
**restrict_file_size** | **bool** | 启用限制单文件大小 | [optional] 
**restrict_push_own_commit** | **bool** | 启用只能推送自己的提交（所推送提交中的邮箱必须与推送者所设置的提交邮箱一致） | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

