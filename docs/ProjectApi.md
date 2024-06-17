# swagger_client.ProjectApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /api/v3/projects | Creates a Project
[**get_current_profile**](ProjectApi.md#get_current_profile) | **GET** /api/v3/projects/{projectId}/user-profiles/current | Gets current user Permissions in a Project
[**get_project**](ProjectApi.md#get_project) | **GET** /api/v3/projects/{projectId} | Gets a Project
[**get_projects**](ProjectApi.md#get_projects) | **GET** /api/v3/projects | Gets multiple Projects
[**get_users**](ProjectApi.md#get_users) | **GET** /api/v3/projects/{projectId}/users | Gets all Users in a Project
[**search_projects**](ProjectApi.md#search_projects) | **POST** /api/v3/projects/search | Search for projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /api/v3/projects/{projectId} | Updates a Project


# **create_project**
> ProjectResource create_project(body)

Creates a Project

To create a new Project  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectResource() # ProjectResource | Project created properties   <em>name:</em> name of project  <em>description:</em> description of project  <em>status_id:</em> status of project  <em>start_date:</em> start date of project, eg: 2019-06-17T05:09:13.178Z  <em>end_date:</em> end date of project, eg: 2019-06-27T05:09:13.178Z  <em>admins:</em> list assigned admin of project  <em>template_id (optional):</em> valid site template id of project. After creating a project, the valid site template filed will be applied for it  <em>uuid (optional):</em> uuid of project. User can provide any string value for uuid, then they can used it for searching projects.

try:
    # Creates a Project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectResource**](ProjectResource.md)| Project created properties   &lt;em&gt;name:&lt;/em&gt; name of project  &lt;em&gt;description:&lt;/em&gt; description of project  &lt;em&gt;status_id:&lt;/em&gt; status of project  &lt;em&gt;start_date:&lt;/em&gt; start date of project, eg: 2019-06-17T05:09:13.178Z  &lt;em&gt;end_date:&lt;/em&gt; end date of project, eg: 2019-06-27T05:09:13.178Z  &lt;em&gt;admins:&lt;/em&gt; list assigned admin of project  &lt;em&gt;template_id (optional):&lt;/em&gt; valid site template id of project. After creating a project, the valid site template filed will be applied for it  &lt;em&gt;uuid (optional):&lt;/em&gt; uuid of project. User can provide any string value for uuid, then they can used it for searching projects. | 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_profile**
> UserProfile get_current_profile(project_id)

Gets current user Permissions in a Project

To retrieve your Permissions in a Project  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project

try:
    # Gets current user Permissions in a Project
    api_response = api_instance.get_current_profile(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_current_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectResource get_project(project_id, expand=expand)

Gets a Project

To retrieve a specific Project

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
expand = 'expand_example' # str | <em>expand=userprofile</em> - include the your profile and permissions within the project in the response (optional)

try:
    # Gets a Project
    api_response = api_instance.get_project(project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **expand** | **str**| &lt;em&gt;expand&#x3D;userprofile&lt;/em&gt; - include the your profile and permissions within the project in the response | [optional] 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[ProjectResource] get_projects(expand=expand, assigned=assigned, page=page, page_size=page_size)

Gets multiple Projects

To retrieve all Projects which the requested qTest  Manager account can access to  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
expand = 'expand_example' # str | <em>expand=userprofile</em> - to include your profile and permissions in each project (optional)
assigned = true # bool | <em>assigned=true</em> - default value. Only the projects which the requested user has access to  <em>assigned=false</em> - Users with admin profile can use this value to retrieve all projects, regardless of having access (optional)
page = 1 # int | By default, all projects are returned; but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Gets multiple Projects
    api_response = api_instance.get_projects(expand=expand, assigned=assigned, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| &lt;em&gt;expand&#x3D;userprofile&lt;/em&gt; - to include your profile and permissions in each project | [optional] 
 **assigned** | **bool**| &lt;em&gt;assigned&#x3D;true&lt;/em&gt; - default value. Only the projects which the requested user has access to  &lt;em&gt;assigned&#x3D;false&lt;/em&gt; - Users with admin profile can use this value to retrieve all projects, regardless of having access | [optional] 
 **page** | **int**| By default, all projects are returned; but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[UserResource] get_users(project_id, inactive=inactive)

Gets all Users in a Project

To retrieve all members in a qTest Manager Project  <strong>qTest Manager version:</strong> 8.4.2+

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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
inactive = true # bool | <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - inactive users are included in the response (optional)

try:
    # Gets all Users in a Project
    api_response = api_instance.get_users(project_id, inactive=inactive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **inactive** | **bool**| &lt;em&gt;inactive&#x3D;false&lt;/em&gt; - default value. Inactive users are excluded from the response  &lt;em&gt;inactive&#x3D;true&lt;/em&gt; - inactive users are included in the response | [optional] 

### Return type

[**list[UserResource]**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_projects**
> list[ProjectResource] search_projects(body)

Search for projects



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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectQueryParams() # ProjectQueryParams | Project search condition properties   <em>uuid:</em> list of uuid for searching

try:
    # Search for projects
    api_response = api_instance.search_projects(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->search_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectQueryParams**](ProjectQueryParams.md)| Project search condition properties   &lt;em&gt;uuid:&lt;/em&gt; list of uuid for searching | 

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectResource update_project(project_id, body)

Updates a Project



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
api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.ProjectUpdateResource() # ProjectUpdateResource | Project updated properties   <em>name (optional):</em> name of project  <em>description (optional):</em> description of project  <em>start_date (optional):</em> Start date of project, eg: 2019-06-17T05:09:13.178Z  <em>end_date (optional):</em> End date of project, eg: 2019-06-27T05:09:13.178Z  <em>admin_ids (optional):</em> list assigned admin ids of project  <em>uuid (optional):</em> uuid of project. User can provide any string value for uuid, then they can used it for searching projects.  <em>template_id (optional):</em> site template id of project. When changing site template id, the project will be removed from old site template id and the new site template will be applied to it.

try:
    # Updates a Project
    api_response = api_instance.update_project(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**ProjectUpdateResource**](ProjectUpdateResource.md)| Project updated properties   &lt;em&gt;name (optional):&lt;/em&gt; name of project  &lt;em&gt;description (optional):&lt;/em&gt; description of project  &lt;em&gt;start_date (optional):&lt;/em&gt; Start date of project, eg: 2019-06-17T05:09:13.178Z  &lt;em&gt;end_date (optional):&lt;/em&gt; End date of project, eg: 2019-06-27T05:09:13.178Z  &lt;em&gt;admin_ids (optional):&lt;/em&gt; list assigned admin ids of project  &lt;em&gt;uuid (optional):&lt;/em&gt; uuid of project. User can provide any string value for uuid, then they can used it for searching projects.  &lt;em&gt;template_id (optional):&lt;/em&gt; site template id of project. When changing site template id, the project will be removed from old site template id and the new site template will be applied to it. | 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

