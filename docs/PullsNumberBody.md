# PullsNumberBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**assignees_number** | **int** | 可选。最少审查人数 | [optional] 
**body** | **str** | 可选。Pull Request 内容 | [optional] 
**draft** | **bool** | 是否设置为草稿 | [optional] 
**labels** | **str** | 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance | [optional] 
**milestone_number** | **int** | 可选。里程碑序号(id) | [optional] 
**ref_pull_request_numbers** | **str** | 可选。依赖的当前仓库下的PR编号，置空则清空依赖的PR。如：17,18,19 | [optional] 
**squash** | **bool** | 接受 Pull Request 时使用扁平化（Squash）合并 | [optional] 
**state** | **str** | 可选。Pull Request 状态 | [optional] 
**testers_number** | **int** | 可选。最少测试人数 | [optional] 
**title** | **str** | 可选。Pull Request 标题 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

