# SearchUserResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to resource | [optional] 
**id** | **int** | ID of the User | [optional] 
**username** | **str** | Login username of the User | [optional] 
**email** | **str** | Contact email of the User | [optional] 
**password** | **str** |  | [optional] 
**first_name** | **str** | First name of the User | [optional] 
**last_name** | **str** | Last name of the User | [optional] 
**status** | **int** | Status of the User | [optional] 
**avatar** | **str** | Avatar URL of the User | [optional] 
**ldap_username** | **str** | LDAP username | [optional] 
**user_group_ids** | **list[int]** |  | [optional] 
**send_activation_email** | **bool** |  | [optional] [default to False]
**external_auth_config_id** | **int** |  | [optional] 
**external_user_name** | **str** |  | [optional] 
**include_default_groups** | **bool** |  | [optional] [default to False]
**assigned_projects** | **list[int]** | Arrays of Project that user assigned to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


