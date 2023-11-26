# OwnerRepoBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**can_comment** | **bool** | 允许用户对仓库进行评论。默认： 允许(true) | [optional] 
**default_branch** | **str** | 更新默认分支 | [optional] 
**default_merge_method** | **str** | 选择默认合并 Pull Request 的方式,分别为 merge squash rebase | [optional] 
**description** | **str** | 仓库描述 | [optional] 
**has_issues** | **bool** | 允许提Issue与否。默认: 允许(true) | [optional] 
**has_wiki** | **bool** | 提供Wiki与否。默认: 提供(true) | [optional] 
**homepage** | **str** | 主页(eg: https://gitee.com) | [optional] 
**issue_comment** | **bool** | 允许对“关闭”状态的 Issue 进行评论。默认: 不允许(false) | [optional] 
**issue_template_source** | **str** | Issue 模版来源 project: 使用仓库 Issue Template 作为模版； enterprise: 使用企业工作项作为模版 | [optional] 
**lightweight_pr_enabled** | **bool** | 是否接受轻量级 pull request | [optional] 
**merge_enabled** | **bool** | 是否开启 merge 合并方式, 默认为开启 | [optional] 
**name** | **str** | 仓库名称 | 
**online_edit_enabled** | **bool** | 是否允许仓库文件在线编辑 | [optional] 
**path** | **str** | 更新仓库路径 | [optional] 
**private** | **bool** | 仓库公开或私有。 | [optional] 
**pull_requests_enabled** | **bool** | 接受 pull request，协作开发 | [optional] 
**rebase_enabled** | **bool** | 是否开启 rebase 合并方式, 默认为开启 | [optional] 
**security_hole_enabled** | **bool** | 这个Issue涉及到安全/隐私问题，提交后不公开此Issue（可见范围：仓库成员, 企业成员） | [optional] 
**squash_enabled** | **bool** | 是否开启 squash 合并方式, 默认为开启 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

