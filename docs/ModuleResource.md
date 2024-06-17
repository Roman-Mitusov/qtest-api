# ModuleResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** | ID of the Module | [optional] 
**name** | **str** | Name of the Module | [optional] 
**order** | **int** | Display order of the Module | [optional] 
**pid** | **str** | PID of the Module | [optional] 
**created_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**parent_id** | **int** | Parent Module of the Module | [optional] 
**description** | **str** | Description of the Module | [optional] 
**shared** | **bool** | Is shared or not | [optional] [default to False]
**projects_shared_to** | **list[int]** |  | [optional] 
**children** | [**list[ModuleResource]**](ModuleResource.md) | Arrays of child module | [optional] 
**recursive** | **bool** |  | [optional] [default to False]
**tosca_guid** | **str** | Tosca folder GUID. Use for creating Module and link with Tosca folder. | [optional] 
**tosca_node_path** | **str** | Tosca folder node path. Use for creating Module and link with Tosca folder. | [optional] 
**tosca_state** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


