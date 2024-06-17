# swagger_client.RequirementApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_requirement_comment**](RequirementApi.md#add_requirement_comment) | **POST** /api/v3/projects/{projectId}/requirements/{idOrKey}/comments | Adds a Comment to a Requirement
[**create_requirement**](RequirementApi.md#create_requirement) | **POST** /api/v3/projects/{projectId}/requirements | Creates a Requirement
[**delete_requirement_by_id**](RequirementApi.md#delete_requirement_by_id) | **DELETE** /api/v3/projects/{projectId}/requirements/{requirementId} | Deletes a Requirement
[**delete_requirement_comment_by_id**](RequirementApi.md#delete_requirement_comment_by_id) | **DELETE** /api/v3/projects/{projectId}/requirements/{idOrKey}/comments/{commentId} | Deletes a Comment of a Requirement
[**get_all_requirement_comments**](RequirementApi.md#get_all_requirement_comments) | **GET** /api/v3/projects/{projectId}/requirements/{idOrKey}/comments | Gets all Comments of a Requirement
[**get_public_traceability_matrix_report**](RequirementApi.md#get_public_traceability_matrix_report) | **GET** /api/v3/projects/{projectId}/requirements/trace-matrix-report | Gets Requirement Traceability Matrix Report
[**get_requirement**](RequirementApi.md#get_requirement) | **GET** /api/v3/projects/{projectId}/requirements/{requirementId} | Gets a Requirement
[**get_requirement_comment_by_id**](RequirementApi.md#get_requirement_comment_by_id) | **GET** /api/v3/projects/{projectId}/requirements/{idOrKey}/comments/{commentId} | Gets a Comment of a Requirement
[**get_requirements**](RequirementApi.md#get_requirements) | **GET** /api/v3/projects/{projectId}/requirements | Gets multiple Requirements
[**get_test_runs_by_requirment_id**](RequirementApi.md#get_test_runs_by_requirment_id) | **GET** /api/v3/projects/{projectId}/requirements/{requirementId}/test-runs | To get all test runs associated to requirement
[**update_requirement**](RequirementApi.md#update_requirement) | **PUT** /api/v3/projects/{projectId}/requirements/{requirementId} | Updates a Requirement
[**update_requirement_comment_by_id**](RequirementApi.md#update_requirement_comment_by_id) | **PUT** /api/v3/projects/{projectId}/requirements/{idOrKey}/comments/{commentId} | Updates a Comment of a Requirement


# **add_requirement_comment**
> CommentResource add_requirement_comment(project_id, id_or_key, body)

Adds a Comment to a Requirement

To add a comment to a Requirement  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Requirement.
body = swagger_client.CommentResource() # CommentResource | The comment's properties and its content

try:
    # Adds a Comment to a Requirement
    api_response = api_instance.add_requirement_comment(project_id, id_or_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->add_requirement_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Requirement. | 
 **body** | [**CommentResource**](CommentResource.md)| The comment&#39;s properties and its content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_requirement**
> RequirementResource create_requirement(project_id, body, parent_id=parent_id)

Creates a Requirement

To create a new Requirement  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.RequirementResource() # RequirementResource | <p><em>name *:</em> Requirement name</p><p><em>properties:</em> An array of field-value pairs</p>
parent_id = 789 # int | ID of the parent Module under which the Requirement will be located (optional)

try:
    # Creates a Requirement
    api_response = api_instance.create_requirement(project_id, body, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->create_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**RequirementResource**](RequirementResource.md)| &lt;p&gt;&lt;em&gt;name *:&lt;/em&gt; Requirement name&lt;/p&gt;&lt;p&gt;&lt;em&gt;properties:&lt;/em&gt; An array of field-value pairs&lt;/p&gt; | 
 **parent_id** | **int**| ID of the parent Module under which the Requirement will be located | [optional] 

### Return type

[**RequirementResource**](RequirementResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_requirement_by_id**
> object delete_requirement_by_id(project_id, requirement_id)

Deletes a Requirement

To delete a Requirement  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
requirement_id = 789 # int | ID of the Requirement which needs to be deleted.

try:
    # Deletes a Requirement
    api_response = api_instance.delete_requirement_by_id(project_id, requirement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->delete_requirement_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **requirement_id** | **int**| ID of the Requirement which needs to be deleted. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_requirement_comment_by_id**
> object delete_requirement_comment_by_id(project_id, id_or_key, comment_id)

Deletes a Comment of a Requirement

To delete a comment of a Requirement  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Requirement whose comment you want to delete
comment_id = 789 # int | The comment's ID

try:
    # Deletes a Comment of a Requirement
    api_response = api_instance.delete_requirement_comment_by_id(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->delete_requirement_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Requirement whose comment you want to delete | 
 **comment_id** | **int**| The comment&#39;s ID | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_requirement_comments**
> PagedResourceCommentResource get_all_requirement_comments(project_id, id_or_key)

Gets all Comments of a Requirement

To retrieve all comments of a Requirement  <strong>qTest Manager version:</strong> 7.6+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Requirement whose comments you want to retrieve

try:
    # Gets all Comments of a Requirement
    api_response = api_instance.get_all_requirement_comments(project_id, id_or_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->get_all_requirement_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Requirement whose comments you want to retrieve | 

### Return type

[**PagedResourceCommentResource**](PagedResourceCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_traceability_matrix_report**
> list[TraceabilityRequirement] get_public_traceability_matrix_report(project_id, page=page, size=size, field_ids=field_ids)

Gets Requirement Traceability Matrix Report

To retrieve a report of Requirements with their covering Test Cases

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve requirements. (optional) (default to 1)
size = 20 # int | The result is paginated. By default, the number of requirements in each page is 20.  You can specify your custom number in this parameter and the maximum number is 999. (optional) (default to 20)
field_ids = 'field_ids_example' # str | ID(s) of requirement fields (system or custom fields) which you would like to retrieve.  They are separated by commas. (optional)

try:
    # Gets Requirement Traceability Matrix Report
    api_response = api_instance.get_public_traceability_matrix_report(project_id, page=page, size=size, field_ids=field_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->get_public_traceability_matrix_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve requirements. | [optional] [default to 1]
 **size** | **int**| The result is paginated. By default, the number of requirements in each page is 20.  You can specify your custom number in this parameter and the maximum number is 999. | [optional] [default to 20]
 **field_ids** | **str**| ID(s) of requirement fields (system or custom fields) which you would like to retrieve.  They are separated by commas. | [optional] 

### Return type

[**list[TraceabilityRequirement]**](TraceabilityRequirement.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requirement**
> RequirementResource get_requirement(project_id, requirement_id, include_external_properties=include_external_properties)

Gets a Requirement

To retrieve a Requirement  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
requirement_id = 789 # int | ID of the Requirement which you want to retrieve.
include_external_properties = true # bool | By default, Requirement external properties are not included in the response. Specify includeExternalProperties=true to include them. (optional)

try:
    # Gets a Requirement
    api_response = api_instance.get_requirement(project_id, requirement_id, include_external_properties=include_external_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->get_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **requirement_id** | **int**| ID of the Requirement which you want to retrieve. | 
 **include_external_properties** | **bool**| By default, Requirement external properties are not included in the response. Specify includeExternalProperties&#x3D;true to include them. | [optional] 

### Return type

[**RequirementResource**](RequirementResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requirement_comment_by_id**
> CommentResource get_requirement_comment_by_id(project_id, id_or_key, comment_id)

Gets a Comment of a Requirement

To retrieve a comment of a Requirement  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Requirement whose comment you want to delete
comment_id = 789 # int | The comment's ID

try:
    # Gets a Comment of a Requirement
    api_response = api_instance.get_requirement_comment_by_id(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->get_requirement_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Requirement whose comment you want to delete | 
 **comment_id** | **int**| The comment&#39;s ID | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requirements**
> list[RequirementResource] get_requirements(project_id, parent_id=parent_id, page=page, size=size, include_external_properties=include_external_properties)

Gets multiple Requirements

To retrieve all Requirements or Requirements under a specific Module

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
parent_id = 789 # int | Specify the parent Module's ID to retrieve all of its Requirements which are located directly under the parent Module (optional)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve requirements. (optional) (default to 1)
size = 56 # int | The result is paginated. By the default, the number of requirements in each page is 20.  You can specify your custom number in this parameter. (optional)
include_external_properties = true # bool | By default, Requirement external properties are not included in the response. Specify includeExternalProperties=true to include them. (optional)

try:
    # Gets multiple Requirements
    api_response = api_instance.get_requirements(project_id, parent_id=parent_id, page=page, size=size, include_external_properties=include_external_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->get_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_id** | **int**| Specify the parent Module&#39;s ID to retrieve all of its Requirements which are located directly under the parent Module | [optional] 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve requirements. | [optional] [default to 1]
 **size** | **int**| The result is paginated. By the default, the number of requirements in each page is 20.  You can specify your custom number in this parameter. | [optional] 
 **include_external_properties** | **bool**| By default, Requirement external properties are not included in the response. Specify includeExternalProperties&#x3D;true to include them. | [optional] 

### Return type

[**list[RequirementResource]**](RequirementResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_runs_by_requirment_id**
> TestRunByRequirementIdListResource get_test_runs_by_requirment_id(project_id, requirement_id, page=page, page_size=page_size, include_latest_log=include_latest_log, expand=expand)

To get all test runs associated to requirement



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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
requirement_id = 789 # int | requirementId
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)
include_latest_log = true # bool | Include latest test log (default is false) (optional)
expand = 'expand_example' # str | Valid values: default is none.    1) testcase - to expand the associated Test Case in the response;    2) testcase.teststep - to expand the associated Test Case and its Test Steps in the response (optional)

try:
    # To get all test runs associated to requirement
    api_response = api_instance.get_test_runs_by_requirment_id(project_id, requirement_id, page=page, page_size=page_size, include_latest_log=include_latest_log, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->get_test_runs_by_requirment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **requirement_id** | **int**| requirementId | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]
 **include_latest_log** | **bool**| Include latest test log (default is false) | [optional] 
 **expand** | **str**| Valid values: default is none.    1) testcase - to expand the associated Test Case in the response;    2) testcase.teststep - to expand the associated Test Case and its Test Steps in the response | [optional] 

### Return type

[**TestRunByRequirementIdListResource**](TestRunByRequirementIdListResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_requirement**
> RequirementResource update_requirement(project_id, requirement_id, body, parent_id=parent_id)

Updates a Requirement

To update properties of an Requirement or to move it to other parent Module

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
requirement_id = 789 # int | ID of the Requirement which needs to be updated.
body = swagger_client.RequirementResource() # RequirementResource | <strong>name: *</strong> Requirement name.  <strong>properties:</strong> An array of field-value pairs
parent_id = 789 # int | ID of the parent Module to which the Requirement will be moved to (optional)

try:
    # Updates a Requirement
    api_response = api_instance.update_requirement(project_id, requirement_id, body, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->update_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **requirement_id** | **int**| ID of the Requirement which needs to be updated. | 
 **body** | [**RequirementResource**](RequirementResource.md)| &lt;strong&gt;name: *&lt;/strong&gt; Requirement name.  &lt;strong&gt;properties:&lt;/strong&gt; An array of field-value pairs | 
 **parent_id** | **int**| ID of the parent Module to which the Requirement will be moved to | [optional] 

### Return type

[**RequirementResource**](RequirementResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_requirement_comment_by_id**
> CommentResource update_requirement_comment_by_id(project_id, id_or_key, comment_id, body)

Updates a Comment of a Requirement

To modify a comment of a Requirement  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.RequirementApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Requirement whose comment you want to update
comment_id = 789 # int | The comment's ID
body = swagger_client.CommentResource() # CommentResource | The comment's updated content

try:
    # Updates a Comment of a Requirement
    api_response = api_instance.update_requirement_comment_by_id(project_id, id_or_key, comment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequirementApi->update_requirement_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Requirement whose comment you want to update | 
 **comment_id** | **int**| The comment&#39;s ID | 
 **body** | [**CommentResource**](CommentResource.md)| The comment&#39;s updated content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

