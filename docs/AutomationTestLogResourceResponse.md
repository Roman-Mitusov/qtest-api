# AutomationTestLogResourceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** |  | [optional] 
**test_case_version_id** | **int** |  | [optional] 
**exe_start_date** | **datetime** |  | 
**exe_end_date** | **datetime** |  | 
**note** | **str** |  | [optional] 
**attachments** | [**list[AttachmentResource]**](AttachmentResource.md) |  | [optional] 
**name** | **str** |  | [optional] 
**planned_exe_time** | **int** |  | [optional] 
**actual_exe_time** | **int** |  | [optional] 
**build_number** | **str** |  | [optional] 
**build_url** | **str** |  | [optional] 
**properties** | [**list[PropertyResource]**](PropertyResource.md) |  | [optional] 
**automation_content** | **str** |  | [optional] 
**linked_defects** | [**AutomationLinkedDefectResponse**](AutomationLinkedDefectResponse.md) |  | [optional] 
**system_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**test_step_logs** | [**list[AutomationTestStepLog]**](AutomationTestStepLog.md) |  | [optional] 
**testcase_properties** | [**list[PropertyResource]**](PropertyResource.md) |  | [optional] 
**module_names** | **list[str]** |  | [optional] 
**agent_ids** | **list[int]** |  | [optional] 
**defect_pids** | **list[str]** | Defect pids | [optional] 
**tosca_guid** | **str** |  | [optional] 
**tosca_node_path** | **str** |  | [optional] 
**tosca_state** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


