# swagger_client.GroupsApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_user_group**](GroupsApi.md#create_custom_user_group) | **POST** /api/v3/groups | Create custom UserGroup
[**get_all_user_groups**](GroupsApi.md#get_all_user_groups) | **GET** /api/v3/groups | Get multiple UserGroups


# **create_custom_user_group**
> UserGroupResource create_custom_user_group(body)

Create custom UserGroup

To create new custom UserGroup

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserGroupResource() # UserGroupResource | <em>name (required):</em> Name of UserGroup  <em>description:</em> Description of UserGroup  <em>is_default:</em> Set this UserGroup as default group for new user  <em>user_ids:</em> List of userId will be assign to this group after created  <em>authority_names:</em> List of authorities for this UserGroup. Values can be: [ ROLE_ADMINCONFIGURATION, ROLE_ADMININFORMATION, ROLE_INSIGHTSEDITOR, ROLE_INSIGHTSEDITOR, ROLE_LAUNCHACCESS, ROLE_PROFILEADMIN, ROLE_PROFILEVIEWER, ROLE_PROJECTARCHIVER, ROLE_PROJECTCREATOR, ROLE_PROJECTUPDATER, ROLE_PROJECTVIEWER, ROLE_PULSEACCESS, ROLE_SITELEVELFIELD, ROLE_USERADMIN, ROLE_USERGROUPMANAGER, ROLE_ANALYTICSVIEWER ]

try:
    # Create custom UserGroup
    api_response = api_instance.create_custom_user_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_custom_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupResource**](UserGroupResource.md)| &lt;em&gt;name (required):&lt;/em&gt; Name of UserGroup  &lt;em&gt;description:&lt;/em&gt; Description of UserGroup  &lt;em&gt;is_default:&lt;/em&gt; Set this UserGroup as default group for new user  &lt;em&gt;user_ids:&lt;/em&gt; List of userId will be assign to this group after created  &lt;em&gt;authority_names:&lt;/em&gt; List of authorities for this UserGroup. Values can be: [ ROLE_ADMINCONFIGURATION, ROLE_ADMININFORMATION, ROLE_INSIGHTSEDITOR, ROLE_INSIGHTSEDITOR, ROLE_LAUNCHACCESS, ROLE_PROFILEADMIN, ROLE_PROFILEVIEWER, ROLE_PROJECTARCHIVER, ROLE_PROJECTCREATOR, ROLE_PROJECTUPDATER, ROLE_PROJECTVIEWER, ROLE_PULSEACCESS, ROLE_SITELEVELFIELD, ROLE_USERADMIN, ROLE_USERGROUPMANAGER, ROLE_ANALYTICSVIEWER ] | 

### Return type

[**UserGroupResource**](UserGroupResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_groups**
> list[UserGroupResource] get_all_user_groups()

Get multiple UserGroups

To get multiple UserGroups

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))

try:
    # Get multiple UserGroups
    api_response = api_instance.get_all_user_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_all_user_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserGroupResource]**](UserGroupResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

