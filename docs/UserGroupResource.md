# UserGroupResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Name of UserGroup | [optional] 
**description** | **str** | Description of UserGroup | [optional] 
**total_user** | **int** | The total user of UserGroup | [optional] 
**is_system** | **bool** |  | [optional] [default to False]
**is_default** | **bool** | Set this UserGroup as default group for new user | [optional] [default to False]
**authorities** | [**list[AuthorityVM]**](AuthorityVM.md) |  | [optional] 
**users** | [**list[UserInfoVM]**](UserInfoVM.md) |  | [optional] 
**user_ids** | **list[int]** | List of userId will be assign to this group after created | [optional] 
**authority_names** | **list[str]** | List of authorities for this UserGroup. Values can be: [ ROLE_ADMINCONFIGURATION, ROLE_ADMININFORMATION, ROLE_INSIGHTSEDITOR, ROLE_INSIGHTSEDITOR, ROLE_LAUNCHACCESS, ROLE_PROFILEADMIN, ROLE_PROFILEVIEWER, ROLE_PROJECTARCHIVER, ROLE_PROJECTCREATOR, ROLE_PROJECTUPDATER, ROLE_PROJECTVIEWER, ROLE_PULSEACCESS, ROLE_SITELEVELFIELD, ROLE_USERADMIN, ROLE_USERGROUPMANAGER, ROLE_ANALYTICSVIEWER ] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


