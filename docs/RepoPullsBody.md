# RepoPullsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**assignees** | **str** | 可选。审查人员username，可多个，半角逗号分隔，如：(username1,username2), 注意: 当仓库代码审查设置中已设置【指派审查人员】则此选项无效 | [optional] 
**assignees_number** | **int** | 可选。最少审查人数 | [optional] 
**base** | **str** | 必填。Pull Request 提交目标分支的名称 | 
**body** | **str** | 可选。Pull Request 内容 | [optional] 
**close_related_issue** | **bool** | 可选，合并后是否关闭关联的 Issue，默认根据仓库配置设置 | [optional] 
**draft** | **bool** | 是否设置为草稿 | [optional] 
**head** | **str** | 必填。Pull Request 提交的源分支。格式：branch 或者：username:branch | 
**issue** | **str** | 可选。Pull Request的标题和内容可以根据指定的Issue Id自动填充 | [optional] 
**labels** | **str** | 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance | [optional] 
**milestone_number** | **int** | 可选。里程碑序号(id) | [optional] 
**prune_source_branch** | **bool** | 可选。合并PR后是否删除源分支，默认false（不删除） | [optional] 
**ref_pull_request_numbers** | **str** | 可选。依赖的当前仓库下的PR编号，置空则清空依赖的PR。如：17,18,19 | [optional] 
**squash** | **bool** | 接受 Pull Request 时使用扁平化（Squash）合并 | [optional] 
**testers** | **str** | 可选。测试人员username，可多个，半角逗号分隔，如：(username1,username2), 注意: 当仓库代码审查设置中已设置【指派测试人员】则此选项无效 | [optional] 
**testers_number** | **int** | 可选。最少测试人数 | [optional] 
**title** | **str** | 必填。Pull Request 标题 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

