# AutomationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_suite_model** | [**TestSuite**](TestSuite.md) |  | [optional] 
**parent_module_model** | [**ProjectModule**](ProjectModule.md) |  | [optional] 
**parent_test_cycle_model** | [**TestCycle**](TestCycle.md) |  | [optional] 
**skip_creating_automation_module** | **bool** |  | [optional] [default to False]
**should_check_unlink_requirement** | **bool** |  | [optional] [default to False]
**test_suite** | **str** | ID or PID of Test Suite | [optional] 
**parent_module** | **str** | ID or PID of Module | [optional] 
**test_logs** | [**list[AutomationTestLogResource]**](AutomationTestLogResource.md) | Array of Test Log | 
**execution_date** | **datetime** | Execution Date | [optional] 
**test_cycle** | **str** | ID or PID of Test Cycle | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


