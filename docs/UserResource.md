# UserResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to resource | [optional] 
**id** | **int** | ID of the User | [optional] 
**username** | **str** | Login username of the User | [optional] 
**email** | **str** | Contact email of the User | [optional] 
**password** | **str** | Password of the User | [optional] 
**first_name** | **str** | First name of the User | [optional] 
**last_name** | **str** | Last name of the User | [optional] 
**status** | **int** | Status of the User | [optional] 
**avatar** | **str** |  | [optional] 
**ldap_username** | **str** | LDAP username of the User | [optional] 
**user_group_ids** | **list[int]** |  | [optional] 
**send_activation_email** | **bool** | Send activation email or not. | [optional] [default to False]
**external_auth_config_id** | **int** | External authentication system id | [optional] 
**external_user_name** | **str** | External authentication username | [optional] 
**include_default_groups** | **bool** | Include default groups or not. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


