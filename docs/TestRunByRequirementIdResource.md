# TestRunByRequirementIdResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** |  | [optional] 
**parent_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**pid** | **str** |  | [optional] 
**test_run_name** | **str** |  | [optional] 
**automation** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**creator_id** | **int** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**status** | **str** | Latest test-run status | [optional] 
**execution_type** | **str** | Test-run type (e.g., functional, etc.) | [optional] 
**env** | **str** | Test-run environment | [optional] 
**test_case_id** | **int** |  | [optional] 
**test_case_version_id** | **int** |  | [optional] 
**test_case_version** | **str** |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**latest_test_log** | [**ShortTestLogResource**](ShortTestLogResource.md) |  | [optional] 
**test_case** | [**TestCaseWithNoCustomFieldResource**](TestCaseWithNoCustomFieldResource.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


