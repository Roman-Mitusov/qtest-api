# swagger_client.TestCaseApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_case_comment**](TestCaseApi.md#add_test_case_comment) | **POST** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments | Adds a Comment to a Test Case
[**add_test_step**](TestCaseApi.md#add_test_step) | **POST** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps | Creates a Test Step
[**approve_test_case**](TestCaseApi.md#approve_test_case) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId}/approve | Approves a Test Case
[**approve_test_case_by_vera**](TestCaseApi.md#approve_test_case_by_vera) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId}/vera/approve | test-case.vera.approve
[**create_test_case**](TestCaseApi.md#create_test_case) | **POST** /api/v3/projects/{projectId}/test-cases | Creates a Test Case
[**delete_test_case**](TestCaseApi.md#delete_test_case) | **DELETE** /api/v3/projects/{projectId}/test-cases/{testCaseId} | Deletes a Test Case
[**delete_test_case_comment**](TestCaseApi.md#delete_test_case_comment) | **DELETE** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments/{commentId} | Deletes a Comment of a Test Case
[**delete_test_step**](TestCaseApi.md#delete_test_step) | **DELETE** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps/{stepId} | Deletes a Test Step
[**get_test_case**](TestCaseApi.md#get_test_case) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseIdOrPid} | Gets a Test Case
[**get_test_case_comment_by_id**](TestCaseApi.md#get_test_case_comment_by_id) | **GET** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments/{commentId} | Gets a Comment of a Test Case
[**get_test_case_comments**](TestCaseApi.md#get_test_case_comments) | **GET** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments | Gets all Comments of a Test Case
[**get_test_case_version_by_id**](TestCaseApi.md#get_test_case_version_by_id) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/versions/{versionId} | Gets a version of a Test Case
[**get_test_cases**](TestCaseApi.md#get_test_cases) | **GET** /api/v3/projects/{projectId}/test-cases | Gets multiple Test Cases
[**get_test_step**](TestCaseApi.md#get_test_step) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps/{stepId} | Gets a Test Step
[**get_test_steps**](TestCaseApi.md#get_test_steps) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps | Gets Test Steps of a Test Case
[**get_test_steps_by_version**](TestCaseApi.md#get_test_steps_by_version) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/versions/{versionId}/test-steps | Gets Test Steps of a Test Case version
[**get_test_steps_by_version_id**](TestCaseApi.md#get_test_steps_by_version_id) | **GET** /api/v4/projects/{projectId}/test-cases/{testCaseId}/versions/{versionId}/test-steps | Gets Test Steps of a Test Case version
[**get_test_steps_of_test_case**](TestCaseApi.md#get_test_steps_of_test_case) | **GET** /api/v4/projects/{projectId}/test-cases/{testCaseId}/test-steps | Gets Test Steps of a Test Case
[**get_versions**](TestCaseApi.md#get_versions) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/versions | Gets all versions of a Test Case
[**update_multiple_test_cases**](TestCaseApi.md#update_multiple_test_cases) | **PUT** /api/v3/projects/{projectId}/test-cases/update/testcases | Updates multiple test cases
[**update_test_case**](TestCaseApi.md#update_test_case) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId} | Updates a Test Case
[**update_test_case_comment**](TestCaseApi.md#update_test_case_comment) | **PUT** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments/{commentId} | Updates a Comment of a Test Case
[**update_test_step**](TestCaseApi.md#update_test_step) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps/{stepId} | Update a Test Step


# **add_test_case_comment**
> CommentResource add_test_case_comment(project_id, id_or_key, body)

Adds a Comment to a Test Case

To add a Comment to a Test Case  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
body = swagger_client.CommentResource() # CommentResource | The comment's properties and its content

try:
    # Adds a Comment to a Test Case
    api_response = api_instance.add_test_case_comment(project_id, id_or_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->add_test_case_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **body** | [**CommentResource**](CommentResource.md)| The comment&#39;s properties and its content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_test_step**
> TestStepResource add_test_step(project_id, test_case_id, body, show_param_identifier=show_param_identifier)

Creates a Test Step

To add a Test Step to a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
body = swagger_client.TestStepResource() # TestStepResource | Given resource will add or create a test step and its CustomField columns details.  Support create test step with Parameters by inputting parameters identifier in teststep's <em>description</em> with sample like below. Parameters will be automatically added to current project.  &nbsp;&nbsp;&nbsp;&nbsp;    { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      \"description\": \"Description [~param1] with [~param2].\" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ... &nbsp;&nbsp;&nbsp;&nbsp;    {
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Creates a Test Step
    api_response = api_instance.add_test_step(project_id, test_case_id, body, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->add_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **body** | [**TestStepResource**](TestStepResource.md)| Given resource will add or create a test step and its CustomField columns details.  Support create test step with Parameters by inputting parameters identifier in teststep&#39;s &lt;em&gt;description&lt;/em&gt; with sample like below. Parameters will be automatically added to current project.  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      \&quot;description\&quot;: \&quot;Description [~param1] with [~param2].\&quot; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      ... &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestStepResource**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_test_case**
> TestCaseWithCustomFieldResource approve_test_case(project_id, test_case_id)

Approves a Test Case

To approve a Test Case  <strong>qTest Manager version:</strong> 7.4+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case

try:
    # Approves a Test Case
    api_response = api_instance.approve_test_case(project_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->approve_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_test_case_by_vera**
> TestCaseWithCustomFieldResource approve_test_case_by_vera(project_id, test_case_id)

test-case.vera.approve



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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case

try:
    # test-case.vera.approve
    api_response = api_instance.approve_test_case_by_vera(project_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->approve_test_case_by_vera: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_case**
> TestCaseWithCustomFieldResource create_test_case(project_id, body, agent_id=agent_id, show_param_identifier=show_param_identifier)

Creates a Test Case

To create a Test Case  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.TestCaseWithCustomFieldResource() # TestCaseWithCustomFieldResource | Test Case properties, Test Steps along with custom field information(if any), Attachments and other information to create a Test Case.  If <em>parent_id</em> is omitted, the Test Case will be created under \"Created via API\" Module.  <em>tosca_guid</em>: GUID of Tosca test case. Use for creating Tosca Test Case.  <em>tosca_node_path</em>: Node Path of Tosca test case. Use for creating Tosca Test Case.  <em>tosca_guid</em> and <em>tosca_node_path</em> are optional but must be specified in pair  Support create test case with Parameters by inputting parameters identifier in teststep's <em>description</em> with sample like below. Parameters will be automatically added to current project.  &nbsp;&nbsp;&nbsp;&nbsp;    { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      \"description\": \"Description [~param1] with [~param2].\" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ... &nbsp;&nbsp;&nbsp;&nbsp;    {
agent_id = 'agent_id_example' # str |  (optional)
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Creates a Test Case
    api_response = api_instance.create_test_case(project_id, body, agent_id=agent_id, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->create_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)| Test Case properties, Test Steps along with custom field information(if any), Attachments and other information to create a Test Case.  If &lt;em&gt;parent_id&lt;/em&gt; is omitted, the Test Case will be created under \&quot;Created via API\&quot; Module.  &lt;em&gt;tosca_guid&lt;/em&gt;: GUID of Tosca test case. Use for creating Tosca Test Case.  &lt;em&gt;tosca_node_path&lt;/em&gt;: Node Path of Tosca test case. Use for creating Tosca Test Case.  &lt;em&gt;tosca_guid&lt;/em&gt; and &lt;em&gt;tosca_node_path&lt;/em&gt; are optional but must be specified in pair  Support create test case with Parameters by inputting parameters identifier in teststep&#39;s &lt;em&gt;description&lt;/em&gt; with sample like below. Parameters will be automatically added to current project.  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      \&quot;description\&quot;: \&quot;Description [~param1] with [~param2].\&quot; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      ... &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { | 
 **agent_id** | **str**|  | [optional] 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_case**
> delete_test_case(project_id, test_case_id)

Deletes a Test Case

To delete Test Case  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case which needs to be deleted.

try:
    # Deletes a Test Case
    api_instance.delete_test_case(project_id, test_case_id)
except ApiException as e:
    print("Exception when calling TestCaseApi->delete_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case which needs to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_case_comment**
> delete_test_case_comment(project_id, id_or_key, comment_id)

Deletes a Comment of a Test Case

To delete a comment of a Test Case  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
comment_id = 789 # int | ID of the comment.

try:
    # Deletes a Comment of a Test Case
    api_instance.delete_test_case_comment(project_id, id_or_key, comment_id)
except ApiException as e:
    print("Exception when calling TestCaseApi->delete_test_case_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **comment_id** | **int**| ID of the comment. | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_step**
> delete_test_step(project_id, test_case_id, step_id, update_version=update_version)

Deletes a Test Step

To delete a test step of a Test Case  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
step_id = 789 # int | ID of the Test Step
update_version = true # bool | If specified updateVersion=true, then the test case version will be updated when the test step is deleted. (optional)

try:
    # Deletes a Test Step
    api_instance.delete_test_step(project_id, test_case_id, step_id, update_version=update_version)
except ApiException as e:
    print("Exception when calling TestCaseApi->delete_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **step_id** | **int**| ID of the Test Step | 
 **update_version** | **bool**| If specified updateVersion&#x3D;true, then the test case version will be updated when the test step is deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case**
> TestCaseWithCustomFieldResource get_test_case(project_id, test_case_id_or_pid, version_id=version_id, expand=expand, show_param_identifier=show_param_identifier)

Gets a Test Case

To retrieve a Test Case  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id_or_pid = 'test_case_id_or_pid_example' # str | ID of the Test Case Or Pid of the test case
version_id = 789 # int | ID of the Test Case version (optional)
expand = 'expand_example' # str | By default, Test Steps are excluded from the response. Specify <em>expand=teststep</em> to include Test Steps (optional)
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets a Test Case
    api_response = api_instance.get_test_case(project_id, test_case_id_or_pid, version_id=version_id, expand=expand, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id_or_pid** | **str**| ID of the Test Case Or Pid of the test case | 
 **version_id** | **int**| ID of the Test Case version | [optional] 
 **expand** | **str**| By default, Test Steps are excluded from the response. Specify &lt;em&gt;expand&#x3D;teststep&lt;/em&gt; to include Test Steps | [optional] 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case_comment_by_id**
> CommentResource get_test_case_comment_by_id(project_id, id_or_key, comment_id)

Gets a Comment of a Test Case

To retrieve a comment of a Test Case  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
comment_id = 789 # int | ID of the comment.

try:
    # Gets a Comment of a Test Case
    api_response = api_instance.get_test_case_comment_by_id(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_case_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **comment_id** | **int**| ID of the comment. | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case_comments**
> PagedResourceCommentResource get_test_case_comments(project_id, id_or_key, page=page, page_size=page_size)

Gets all Comments of a Test Case

To retrieve all comments of a Test Case  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case whose comments you want to retrieve
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Gets all Comments of a Test Case
    api_response = api_instance.get_test_case_comments(project_id, id_or_key, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_case_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case whose comments you want to retrieve | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**PagedResourceCommentResource**](PagedResourceCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case_version_by_id**
> TestCaseWithCustomFieldResource get_test_case_version_by_id(project_id, test_case_id, version_id, show_param_identifier=show_param_identifier)

Gets a version of a Test Case

To retrieve a specific version of a Test Case  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
version_id = 789 # int | ID of the Test Case version
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets a version of a Test Case
    api_response = api_instance.get_test_case_version_by_id(project_id, test_case_id, version_id, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_case_version_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **version_id** | **int**| ID of the Test Case version | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_cases**
> list[TestCaseWithCustomFieldResource] get_test_cases(project_id, page, size, parent_id=parent_id, expand_props=expand_props, expand_steps=expand_steps, show_param_identifier=show_param_identifier)

Gets multiple Test Cases

To retrieve all Test Cases or Test Cases which are located directly under a Module

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
page = 1 # int | By default the first page is returned. However, you can specify any page number to retrieve test cases. (default to 1)
size = 20 # int | The result is paginated. By the default, the number of requirements in each page is 20.  You can specify your custom number in this parameter. (default to 20)
parent_id = 789 # int | Module ID (optional)
expand_props = true # bool | By default, Test Case properties are included in the response. specify <em>expandProps=false</em> to exclude them (optional)
expand_steps = true # bool | By default, Test Steps are excluded from the response body. Input <em>expandSteps=true</em> to include Test Steps (optional)
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets multiple Test Cases
    api_response = api_instance.get_test_cases(project_id, page, size, parent_id=parent_id, expand_props=expand_props, expand_steps=expand_steps, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **page** | **int**| By default the first page is returned. However, you can specify any page number to retrieve test cases. | [default to 1]
 **size** | **int**| The result is paginated. By the default, the number of requirements in each page is 20.  You can specify your custom number in this parameter. | [default to 20]
 **parent_id** | **int**| Module ID | [optional] 
 **expand_props** | **bool**| By default, Test Case properties are included in the response. specify &lt;em&gt;expandProps&#x3D;false&lt;/em&gt; to exclude them | [optional] 
 **expand_steps** | **bool**| By default, Test Steps are excluded from the response body. Input &lt;em&gt;expandSteps&#x3D;true&lt;/em&gt; to include Test Steps | [optional] 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**list[TestCaseWithCustomFieldResource]**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_step**
> TestStepResource get_test_step(project_id, test_case_id, step_id, show_param_identifier=show_param_identifier)

Gets a Test Step

To retrieve a Test Step of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
step_id = 789 # int | ID of the test step.   The ObjectId of customFieldInfo is used as a StepId here.
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets a Test Step
    api_response = api_instance.get_test_step(project_id, test_case_id, step_id, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **step_id** | **int**| ID of the test step.   The ObjectId of customFieldInfo is used as a StepId here. | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestStepResource**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_steps**
> list[TestStepResource] get_test_steps(project_id, test_case_id, show_param_identifier=show_param_identifier)

Gets Test Steps of a Test Case

To retrieve all Test Steps of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets Test Steps of a Test Case
    api_response = api_instance.get_test_steps(project_id, test_case_id, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**list[TestStepResource]**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_steps_by_version**
> list[TestStepResource] get_test_steps_by_version(project_id, test_case_id, version_id, expand=expand, show_param_identifier=show_param_identifier)

Gets Test Steps of a Test Case version

To retrieve all Test Steps of a specific Test Case version

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
version_id = 789 # int | ID of the Test Case version
expand = 'expand_example' # str | when you Specify <em>expand=calledteststep</em>   It will include Test Steps of the called Test Cases in your response. (optional)
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets Test Steps of a Test Case version
    api_response = api_instance.get_test_steps_by_version(project_id, test_case_id, version_id, expand=expand, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_steps_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **version_id** | **int**| ID of the Test Case version | 
 **expand** | **str**| when you Specify &lt;em&gt;expand&#x3D;calledteststep&lt;/em&gt;   It will include Test Steps of the called Test Cases in your response. | [optional] 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**list[TestStepResource]**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_steps_by_version_id**
> list[TestStepResource] get_test_steps_by_version_id(project_id, test_case_id, version_id, page, size, expand=expand, show_param_identifier=show_param_identifier)

Gets Test Steps of a Test Case version

To retrieve all Test Steps of a specific Test Case version

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
version_id = 789 # int | ID of the Test Case version
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (default to 1)
size = 200 # int | size (default to 200)
expand = 'expand_example' # str | when you Specify <em>expand=calledteststep</em>   It will include Test Steps of the called Test Cases in your response. (optional)
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets Test Steps of a Test Case version
    api_response = api_instance.get_test_steps_by_version_id(project_id, test_case_id, version_id, page, size, expand=expand, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_steps_by_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **version_id** | **int**| ID of the Test Case version | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [default to 1]
 **size** | **int**| size | [default to 200]
 **expand** | **str**| when you Specify &lt;em&gt;expand&#x3D;calledteststep&lt;/em&gt;   It will include Test Steps of the called Test Cases in your response. | [optional] 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**list[TestStepResource]**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_steps_of_test_case**
> list[TestStepResource] get_test_steps_of_test_case(project_id, test_case_id, page, size, show_param_identifier=show_param_identifier)

Gets Test Steps of a Test Case

To retrieve all Test Steps of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (default to 1)
size = 200 # int | size (default to 200)
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets Test Steps of a Test Case
    api_response = api_instance.get_test_steps_of_test_case(project_id, test_case_id, page, size, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_test_steps_of_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [default to 1]
 **size** | **int**| size | [default to 200]
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**list[TestStepResource]**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> list[TestCaseWithCustomFieldResource] get_versions(project_id, test_case_id, show_param_identifier=show_param_identifier)

Gets all versions of a Test Case

Get all versions of a Test Case.  Example:  API returns all approved major test case versions and the last unapproved minor version if there is one.  <li>if version history is 1.0, 1.1, 2.0, 2.1, 2.2, 3.0, 3.1, 3.2; it will only return versions 1.0, 2.0, 3.0 and 3.2</li><li>if the version history is 1.0, 1.1, 2.0, 2.1, 2.2, 3.0; it will only return versions 1.0, 2.0, and 3.0</li><li>if the version history is 0.1, 0.2, 0.3, 0.4; it will only return version 0.4</li><strong>qTest Manager version:</strong> 7.4+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the test case
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Gets all versions of a Test Case
    api_response = api_instance.get_versions(project_id, test_case_id, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the test case | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**list[TestCaseWithCustomFieldResource]**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multiple_test_cases**
> TestCaseWithCustomFieldResource update_multiple_test_cases(project_id, body, show_param_identifier=show_param_identifier)

Updates multiple test cases

To update multiple Test Cases  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = NULL # object | Test Case properties for all the test cases, Test Steps along with custom field information(if any) to update the Test Case.  Support update test case with Parameters by inputting parameters identifier in teststep's <em>description</em> with sample like below. Parameters will be automatically added to current project.  &nbsp;&nbsp;&nbsp;&nbsp;    { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      \"description\": \"Description [~param1] with [~param2].\" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ... &nbsp;&nbsp;&nbsp;&nbsp;    {
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Updates multiple test cases
    api_response = api_instance.update_multiple_test_cases(project_id, body, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->update_multiple_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | **object**| Test Case properties for all the test cases, Test Steps along with custom field information(if any) to update the Test Case.  Support update test case with Parameters by inputting parameters identifier in teststep&#39;s &lt;em&gt;description&lt;/em&gt; with sample like below. Parameters will be automatically added to current project.  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      \&quot;description\&quot;: \&quot;Description [~param1] with [~param2].\&quot; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      ... &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_case**
> TestCaseWithCustomFieldResource update_test_case(project_id, test_case_id, body, show_param_identifier=show_param_identifier)

Updates a Test Case

To update a Test Case  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case which needs to be updated.
body = swagger_client.TestCaseWithCustomFieldResource() # TestCaseWithCustomFieldResource | Test Case properties, Test Steps along with custom field information(if any) to update the Test Case.  Support update test case with Parameters by inputting parameters identifier in teststep's <em>description</em> with sample like below. Parameters will be automatically added to current project.  &nbsp;&nbsp;&nbsp;&nbsp;    { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      \"description\": \"Description [~param1] with [~param2].\" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ... &nbsp;&nbsp;&nbsp;&nbsp;    {
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Updates a Test Case
    api_response = api_instance.update_test_case(project_id, test_case_id, body, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->update_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case which needs to be updated. | 
 **body** | [**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)| Test Case properties, Test Steps along with custom field information(if any) to update the Test Case.  Support update test case with Parameters by inputting parameters identifier in teststep&#39;s &lt;em&gt;description&lt;/em&gt; with sample like below. Parameters will be automatically added to current project.  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      \&quot;description\&quot;: \&quot;Description [~param1] with [~param2].\&quot; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      ... &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_case_comment**
> CommentResource update_test_case_comment(project_id, id_or_key, comment_id, body)

Updates a Comment of a Test Case

To modify a comment of a Test Case  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
comment_id = 789 # int | ID of the comment.
body = swagger_client.CommentResource() # CommentResource | The comment's updated content

try:
    # Updates a Comment of a Test Case
    api_response = api_instance.update_test_case_comment(project_id, id_or_key, comment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->update_test_case_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **comment_id** | **int**| ID of the comment. | 
 **body** | [**CommentResource**](CommentResource.md)| The comment&#39;s updated content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_step**
> TestStepResource update_test_step(project_id, test_case_id, step_id, body, show_param_identifier=show_param_identifier)

Update a Test Step

To update a Test Step of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestCaseApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
step_id = 789 # int | ID of the Test Step
body = swagger_client.TestStepResource() # TestStepResource | Updated content of the Test Step for test case ID or PID   This Shows the updated CustomFields id, as well as you will get the updated stepId which will be ObjectId.  Support update test step with Parameters by inputting parameters identifier in teststep's <em>description</em> with sample like below. Parameters will be automatically added to current project.  &nbsp;&nbsp;&nbsp;&nbsp;    { &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      \"description\": \"Description [~param1] with [~param2].\" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ... &nbsp;&nbsp;&nbsp;&nbsp;    {
show_param_identifier = true # bool | By default, Parameters in Test Steps are displayed in ID number mode (like \"<strong>[~123]</strong>\"). Input <strong><em>showParamIdentifier=true</em></strong> to change to Identifier text mode. Result should be like \"<strong>[~myIdentifier]</strong>\". (optional)

try:
    # Update a Test Step
    api_response = api_instance.update_test_step(project_id, test_case_id, step_id, body, show_param_identifier=show_param_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestCaseApi->update_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **step_id** | **int**| ID of the Test Step | 
 **body** | [**TestStepResource**](TestStepResource.md)| Updated content of the Test Step for test case ID or PID   This Shows the updated CustomFields id, as well as you will get the updated stepId which will be ObjectId.  Support update test step with Parameters by inputting parameters identifier in teststep&#39;s &lt;em&gt;description&lt;/em&gt; with sample like below. Parameters will be automatically added to current project.  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      \&quot;description\&quot;: \&quot;Description [~param1] with [~param2].\&quot; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;      ... &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;    { | 
 **show_param_identifier** | **bool**| By default, Parameters in Test Steps are displayed in ID number mode (like \&quot;&lt;strong&gt;[~123]&lt;/strong&gt;\&quot;). Input &lt;strong&gt;&lt;em&gt;showParamIdentifier&#x3D;true&lt;/em&gt;&lt;/strong&gt; to change to Identifier text mode. Result should be like \&quot;&lt;strong&gt;[~myIdentifier]&lt;/strong&gt;\&quot;. | [optional] 

### Return type

[**TestStepResource**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

