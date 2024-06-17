# swagger_client.UserApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_to_project**](UserApi.md#assign_to_project) | **POST** /api/v3/users/{userId}/projects | Assigns a User to a Project
[**assign_users_to_project**](UserApi.md#assign_users_to_project) | **POST** /api/v3/users/projects | Assigns multiple Users to a Project
[**create_user**](UserApi.md#create_user) | **POST** /api/v3/users | Invites a User
[**find_by_user_name_or_email**](UserApi.md#find_by_user_name_or_email) | **GET** /api/v3/users/search | Queries Users by Username
[**find_users_by_projects_name**](UserApi.md#find_users_by_projects_name) | **GET** /api/v3/search/user | Queries Users by Project Name
[**get_avatar**](UserApi.md#get_avatar) | **GET** /api/v3/users/{userId}/avatar | Gets a User&#39;s Avatar
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /api/v3/users/{userId} | Gets a User
[**reevaluate_token**](UserApi.md#reevaluate_token) | **GET** /api/v3/re-evaluation | Gets current user&#39;s information
[**remove_association_users_and_projects**](UserApi.md#remove_association_users_and_projects) | **PUT** /api/v3/users/projects | Remove association between users and projects
[**update_user**](UserApi.md#update_user) | **PUT** /api/v3/users/{userId} | Update user&#39;s information


# **assign_to_project**
> AssignedProject assign_to_project(user_id, body)

Assigns a User to a Project

To assign a User to a Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | ID of the user.
body = swagger_client.AssignedProject() # AssignedProject | The project ID and the assigned user profile in the project. If the profile is not provided, profile Developer is used by default

try:
    # Assigns a User to a Project
    api_response = api_instance.assign_to_project(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->assign_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 
 **body** | [**AssignedProject**](AssignedProject.md)| The project ID and the assigned user profile in the project. If the profile is not provided, profile Developer is used by default | 

### Return type

[**AssignedProject**](AssignedProject.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_users_to_project**
> AssignedUsersProject assign_users_to_project(body)

Assigns multiple Users to a Project

To assign a list of Users to a Project  <strong>qTest Manager version:</strong> 4+

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.AssignedUsersProject() # AssignedUsersProject | ID of the Project and an array of assigned Users' IDs. If the profile is not provided, Developer profile is used by default

try:
    # Assigns multiple Users to a Project
    api_response = api_instance.assign_users_to_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->assign_users_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignedUsersProject**](AssignedUsersProject.md)| ID of the Project and an array of assigned Users&#39; IDs. If the profile is not provided, Developer profile is used by default | 

### Return type

[**AssignedUsersProject**](AssignedUsersProject.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserResource create_user(body)

Invites a User

To invite a user to your qTest Manager instance and activate the account. If the password is omitted, the default \"<em>admin123</em>\" will be used  <strong>qTest Manager version:</strong> 4+

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserResource() # UserResource | Invited user's information  <em>username (require)</em>: email of new user  <em>email</em>: recovery email of new user  <em>password</em>: password of new user. If the password is omitted, the default \"admin123\" will be used  <em>first_name (require)</em>: First name of new user  <em>last_name (require)</em>: Last name of new user  <em>user_group_ids</em>: List usergroup ids will be assigned for new user.  <em>send_activation_email</em>: activation email will be ignored if this is set to <strong>false</strong>. Default value is <strong>false</strong>  <em>external_auth_config_id</em>: auto assign this new user with External Authentication system by this providing config id here. If this value is provided, <em>\"external_user_name\"</em> need to have value, or it will failed to create.  <em>external_user_name</em>: external username that will be assigned to newly created qTest user   <em>include_default_groups</em>:Include default groups or not. Default value is <strong>false</strong>

try:
    # Invites a User
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserResource**](UserResource.md)| Invited user&#39;s information  &lt;em&gt;username (require)&lt;/em&gt;: email of new user  &lt;em&gt;email&lt;/em&gt;: recovery email of new user  &lt;em&gt;password&lt;/em&gt;: password of new user. If the password is omitted, the default \&quot;admin123\&quot; will be used  &lt;em&gt;first_name (require)&lt;/em&gt;: First name of new user  &lt;em&gt;last_name (require)&lt;/em&gt;: Last name of new user  &lt;em&gt;user_group_ids&lt;/em&gt;: List usergroup ids will be assigned for new user.  &lt;em&gt;send_activation_email&lt;/em&gt;: activation email will be ignored if this is set to &lt;strong&gt;false&lt;/strong&gt;. Default value is &lt;strong&gt;false&lt;/strong&gt;  &lt;em&gt;external_auth_config_id&lt;/em&gt;: auto assign this new user with External Authentication system by this providing config id here. If this value is provided, &lt;em&gt;\&quot;external_user_name\&quot;&lt;/em&gt; need to have value, or it will failed to create.  &lt;em&gt;external_user_name&lt;/em&gt;: external username that will be assigned to newly created qTest user   &lt;em&gt;include_default_groups&lt;/em&gt;:Include default groups or not. Default value is &lt;strong&gt;false&lt;/strong&gt; | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_user_name_or_email**
> SearchUserResourceExtensionResponse find_by_user_name_or_email(username=username, include_inactive_users=include_inactive_users, pagination=pagination, auth_system_config_ids=auth_system_config_ids, page=page, page_size=page_size)

Queries Users by Username

To query for users by their username  <strong>qTest Manager version:</strong> 8.4.2+

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | API will return users which have been added to projects whose names contain the text specified in this parameter.  Login names of users should be provided for this query, but they vary based on the source of the user.  - qTest Login Email - for users created directly on qTest  - LDAP or SSO username or external username - for users created from LDAP or SSO (optional)
include_inactive_users = true # bool | <em>includeInactiveUsers=false</em> - default value. Inactive users are excluded from the response  <em>includeInactiveUsers=true</em> - inactive users are included in the response (optional)
pagination = true # bool | <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated (optional)
auth_system_config_ids = [56] # list[int] | LDAP Configuration Ids (optional)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 100) in this parameter. (optional) (default to 100)

try:
    # Queries Users by Username
    api_response = api_instance.find_by_user_name_or_email(username=username, include_inactive_users=include_inactive_users, pagination=pagination, auth_system_config_ids=auth_system_config_ids, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->find_by_user_name_or_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| API will return users which have been added to projects whose names contain the text specified in this parameter.  Login names of users should be provided for this query, but they vary based on the source of the user.  - qTest Login Email - for users created directly on qTest  - LDAP or SSO username or external username - for users created from LDAP or SSO | [optional] 
 **include_inactive_users** | **bool**| &lt;em&gt;includeInactiveUsers&#x3D;false&lt;/em&gt; - default value. Inactive users are excluded from the response  &lt;em&gt;includeInactiveUsers&#x3D;true&lt;/em&gt; - inactive users are included in the response | [optional] 
 **pagination** | **bool**| &lt;em&gt;pagination&#x3D;true&lt;/em&gt; - default value. The result is paginated  &lt;em&gt;pagination&#x3D;false&lt;/em&gt; - the result is not paginated | [optional] 
 **auth_system_config_ids** | [**list[int]**](int.md)| LDAP Configuration Ids | [optional] 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 100) in this parameter. | [optional] [default to 100]

### Return type

[**SearchUserResourceExtensionResponse**](SearchUserResourceExtensionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_users_by_projects_name**
> SearchUserResponse find_users_by_projects_name(project_name=project_name, inactive=inactive, pagination=pagination, page=page, page_size=page_size)

Queries Users by Project Name

To query for users by names of their assigned projects  - Admin users with <em>Manage Client Users</em> permission can query users in any projects  - For other users: the API only returns users within projects to which the requesting user is assigned

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
project_name = 'project_name_example' # str | Name of the project whose users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Project name is case sensitive (optional)
inactive = true # bool | <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - include inactive users (optional) (default to true)
pagination = true # bool | <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated (optional) (default to true)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Queries Users by Project Name
    api_response = api_instance.find_users_by_projects_name(project_name=project_name, inactive=inactive, pagination=pagination, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->find_users_by_projects_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Name of the project whose users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  &lt;strong&gt;IMPORTANT:&lt;/strong&gt; Project name is case sensitive | [optional] 
 **inactive** | **bool**| &lt;em&gt;inactive&#x3D;false&lt;/em&gt; - default value. Inactive users are excluded from the response  &lt;em&gt;inactive&#x3D;true&lt;/em&gt; - include inactive users | [optional] [default to true]
 **pagination** | **bool**| &lt;em&gt;pagination&#x3D;true&lt;/em&gt; - default value. The result is paginated  &lt;em&gt;pagination&#x3D;false&lt;/em&gt; - the result is not paginated | [optional] [default to true]
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**SearchUserResponse**](SearchUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar**
> OutputStream get_avatar(user_id)

Gets a User's Avatar

To retrieve a User's Avatar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | ID of the user.

try:
    # Gets a User's Avatar
    api_response = api_instance.get_avatar(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 

### Return type

[**OutputStream**](OutputStream.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserResource get_user_by_id(user_id)

Gets a User

To retrieve a User's information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | ID of the user.

try:
    # Gets a User
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reevaluate_token**
> LoggedUser reevaluate_token(include_inaccessible_apps=include_inaccessible_apps)

Gets current user's information

To retrieve your information such as username, email, first name, and last name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
include_inaccessible_apps = true # bool |  (optional)

try:
    # Gets current user's information
    api_response = api_instance.reevaluate_token(include_inaccessible_apps=include_inaccessible_apps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reevaluate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inaccessible_apps** | **bool**|  | [optional] 

### Return type

[**LoggedUser**](LoggedUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_association_users_and_projects**
> Message remove_association_users_and_projects(body)

Remove association between users and projects

To remove association between users and projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ProjectWithUserIdsObject()] # list[ProjectWithUserIdsObject] | An array of pairs project_id and user_ids   <em>project_id:</em> ID of the project  <em>user_ids: </em> List of User IDs which are being removed from the project

try:
    # Remove association between users and projects
    api_response = api_instance.remove_association_users_and_projects(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_association_users_and_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ProjectWithUserIdsObject]**](ProjectWithUserIdsObject.md)| An array of pairs project_id and user_ids   &lt;em&gt;project_id:&lt;/em&gt; ID of the project  &lt;em&gt;user_ids: &lt;/em&gt; List of User IDs which are being removed from the project | 

### Return type

[**Message**](Message.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserResource update_user(user_id, body)

Update user's information

To update information of a user, like : recovery email, password, status...

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | ID of the user.
body = swagger_client.UserUpdateResource() # UserUpdateResource | Update user's information  <em>email</em>: New recovery email of user  <em>password</em>: New password of user. Password have to map with password policy of current user's client  <em>first_name</em>: New first name of user  <em>last_name</em>: New last name of user  <em>user_group_ids</em>: List usergroup ids will be assigned for user (old usergroup ids will be replaced).  <em>external_auth_config_id</em>: New user's external authenticate id,it will auto assign this user with External Authentication system by this providing config id here. If this value is provided, <em>\"external_user_name\"</em> need to have value, or it will failed to update. For internal authentication system input : <strong>-1</strong>  <em>external_user_name</em>: external username that will be assigned to user (if LDAP external is specified, \"first_name\" and \"last_name\" will be fetch from LDAP system).  <em>status</em>: New status id of user. Status id must be <strong>1</strong> for Active or <strong>3</strong> for Inactive status.

try:
    # Update user's information
    api_response = api_instance.update_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 
 **body** | [**UserUpdateResource**](UserUpdateResource.md)| Update user&#39;s information  &lt;em&gt;email&lt;/em&gt;: New recovery email of user  &lt;em&gt;password&lt;/em&gt;: New password of user. Password have to map with password policy of current user&#39;s client  &lt;em&gt;first_name&lt;/em&gt;: New first name of user  &lt;em&gt;last_name&lt;/em&gt;: New last name of user  &lt;em&gt;user_group_ids&lt;/em&gt;: List usergroup ids will be assigned for user (old usergroup ids will be replaced).  &lt;em&gt;external_auth_config_id&lt;/em&gt;: New user&#39;s external authenticate id,it will auto assign this user with External Authentication system by this providing config id here. If this value is provided, &lt;em&gt;\&quot;external_user_name\&quot;&lt;/em&gt; need to have value, or it will failed to update. For internal authentication system input : &lt;strong&gt;-1&lt;/strong&gt;  &lt;em&gt;external_user_name&lt;/em&gt;: external username that will be assigned to user (if LDAP external is specified, \&quot;first_name\&quot; and \&quot;last_name\&quot; will be fetch from LDAP system).  &lt;em&gt;status&lt;/em&gt;: New status id of user. Status id must be &lt;strong&gt;1&lt;/strong&gt; for Active or &lt;strong&gt;3&lt;/strong&gt; for Inactive status. | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

