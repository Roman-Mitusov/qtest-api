# swagger_client.TestRunApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_run_comment**](TestRunApi.md#add_test_run_comment) | **POST** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments | Adds a Comment to a Test Run
[**add_test_run_with_parameters**](TestRunApi.md#add_test_run_with_parameters) | **POST** /api/v3/projects/{projectId}/test-runs/assign-parameter-values/manually | Create multiple Test Runs with Parameter values manual
[**add_test_run_with_parameters_dataset**](TestRunApi.md#add_test_run_with_parameters_dataset) | **POST** /api/v3/projects/{projectId}/test-runs/assign-parameter-values/dataset | Create multiple Test Runs with Parameter values from dataset.
[**add_test_run_with_parameters_randomize**](TestRunApi.md#add_test_run_with_parameters_randomize) | **POST** /api/v3/projects/{projectId}/test-runs/assign-parameter-values/randomize | Create multiple Test Runs with Parameter values random from selection combine type.
[**create_test_run**](TestRunApi.md#create_test_run) | **POST** /api/v3/projects/{projectId}/test-runs | Creates a Test Run
[**delete_comment_by_id**](TestRunApi.md#delete_comment_by_id) | **DELETE** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments/{commentId} | Deletes a Comment of a Test Run
[**delete_test_run_by_id**](TestRunApi.md#delete_test_run_by_id) | **DELETE** /api/v3/projects/{projectId}/test-runs/{testRunId} | Deletes a Test Run
[**get_of**](TestRunApi.md#get_of) | **GET** /api/v3/projects/{projectId}/test-runs | Gets multiple Test Runs
[**get_status_valuable**](TestRunApi.md#get_status_valuable) | **GET** /api/v3/projects/{projectId}/test-runs/execution-statuses | Gets Test Run statuses
[**get_subhierachy**](TestRunApi.md#get_subhierachy) | **GET** /api/v3/projects/{projectId}/test-runs/subhierarchy | Gets a Sub Hierarchy
[**get_test_run_by_id**](TestRunApi.md#get_test_run_by_id) | **GET** /api/v3/projects/{projectId}/test-runs/{testRunId} | Gets a Test Run
[**get_test_run_comment_by_id**](TestRunApi.md#get_test_run_comment_by_id) | **GET** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments/{commentId} | Gets a Comment from a Test Run
[**get_test_run_comments**](TestRunApi.md#get_test_run_comments) | **GET** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments | Gets all Comments of a Test Run
[**update_comment_by_id**](TestRunApi.md#update_comment_by_id) | **PUT** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments/{commentId} | Updates a Comment of a Test Run
[**update_test_run_by_id**](TestRunApi.md#update_test_run_by_id) | **PUT** /api/v3/projects/{projectId}/test-runs/{testRunId} | Updates a Test Run


# **add_test_run_comment**
> CommentResource add_test_run_comment(project_id, id_or_key, body)

Adds a Comment to a Test Run

To add a Comment to a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | The PID or ID of the Test Run.
body = swagger_client.CommentResource() # CommentResource | The Comment's content

try:
    # Adds a Comment to a Test Run
    api_response = api_instance.add_test_run_comment(project_id, id_or_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->add_test_run_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| The PID or ID of the Test Run. | 
 **body** | [**CommentResource**](CommentResource.md)| The Comment&#39;s content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_test_run_with_parameters**
> QueueProcessingResponseTestRunDataVM add_test_run_with_parameters(project_id, body, parent_id=parent_id, parent_type=parent_type)

Create multiple Test Runs with Parameter values manual

To create multiple Test Runs with parameter values under root or a container (Release, Test Cycle or Test Suite). Maximum number of test runs can be created is 100.

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.TestRunWithParameterCreateManualResource() # TestRunWithParameterCreateManualResource | The Test Run's properties, its associated Test Case and list of Test runs   <em>name (optional):</em> All test runs will be created with the same name if provided. If not provided, test run name = test case name + [increased number, starting from 1]   <em>properties (optional):</em> All test runs will be created with the same property list if provided. If not provided, default property values will be used.   <strong>test_case attributes:</strong>  <em>id (required):</em> id of testcase   <em>test_case_version_id (optional):</em> Version ID of Testcase. If not specify, latest value will be used. For shared test case, only accept approved version   <em>test_runs (required):</em> list of test runs will be created by this API. For each test run, it will have list of test steps (by providing test step id) and their parameter values for each step e.g.(\"description_parameter_values\", and \"expected_parameter_values\").   <strong>You no need to specify <em>combined_type</em> and <em>number_of_combinations</em> in this api.<strong>
parent_id = 789 # int | ID of the container  Input 0 (zero) to get Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em>, and <em>test-suite</em> (optional)

try:
    # Create multiple Test Runs with Parameter values manual
    api_response = api_instance.add_test_run_with_parameters(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->add_test_run_with_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestRunWithParameterCreateManualResource**](TestRunWithParameterCreateManualResource.md)| The Test Run&#39;s properties, its associated Test Case and list of Test runs   &lt;em&gt;name (optional):&lt;/em&gt; All test runs will be created with the same name if provided. If not provided, test run name &#x3D; test case name + [increased number, starting from 1]   &lt;em&gt;properties (optional):&lt;/em&gt; All test runs will be created with the same property list if provided. If not provided, default property values will be used.   &lt;strong&gt;test_case attributes:&lt;/strong&gt;  &lt;em&gt;id (required):&lt;/em&gt; id of testcase   &lt;em&gt;test_case_version_id (optional):&lt;/em&gt; Version ID of Testcase. If not specify, latest value will be used. For shared test case, only accept approved version   &lt;em&gt;test_runs (required):&lt;/em&gt; list of test runs will be created by this API. For each test run, it will have list of test steps (by providing test step id) and their parameter values for each step e.g.(\&quot;description_parameter_values\&quot;, and \&quot;expected_parameter_values\&quot;).   &lt;strong&gt;You no need to specify &lt;em&gt;combined_type&lt;/em&gt; and &lt;em&gt;number_of_combinations&lt;/em&gt; in this api.&lt;strong&gt; | 
 **parent_id** | **int**| ID of the container  Input 0 (zero) to get Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt;, and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**QueueProcessingResponseTestRunDataVM**](QueueProcessingResponseTestRunDataVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_test_run_with_parameters_dataset**
> QueueProcessingResponseTestRunDataVM add_test_run_with_parameters_dataset(project_id, body, parent_id=parent_id, parent_type=parent_type)

Create multiple Test Runs with Parameter values from dataset.

To create multiple Test Runs with parameter values under root or a container (Release, Test Cycle or Test Suite). Number of test runs can be created depend on number_of_rows property and it should not more than 100.

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.TestRunWithParameterCreateByDatasetResource() # TestRunWithParameterCreateByDatasetResource | The Test Run's properties, its associated Test Case and specific data set   <em>name (optional):</em> All test runs will be created with the same name if provided. If not provided, test run name = test case name + [increased number, starting from 1]   <em>properties (optional):</em> All test runs will be created with the same property list if provided. If not provided, default property values will be used.   <strong>test_case attributes:</strong>  <em>id (required):</em> id of testcase   <em>test_case_version_id (optional):</em> Version ID of Testcase. If not specify, latest value will be used. For shared test case, only accept approved version   <em>dataset_id:</em> Dataset id use for generate test runs. Dataset must be active and contains all parameters inside all test case steps. Dataset has at least 1 data row.   <em>from_row:</em> Must be less or equal max rows in dataset.   <em>number_of_rows:</em> number of test run can be create must be less or equal ((max rows - from_row) +1) and must be less than <em>100</em>.
parent_id = 789 # int | ID of the container  Input 0 (zero) to get Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em>, and <em>test-suite</em> (optional)

try:
    # Create multiple Test Runs with Parameter values from dataset.
    api_response = api_instance.add_test_run_with_parameters_dataset(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->add_test_run_with_parameters_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestRunWithParameterCreateByDatasetResource**](TestRunWithParameterCreateByDatasetResource.md)| The Test Run&#39;s properties, its associated Test Case and specific data set   &lt;em&gt;name (optional):&lt;/em&gt; All test runs will be created with the same name if provided. If not provided, test run name &#x3D; test case name + [increased number, starting from 1]   &lt;em&gt;properties (optional):&lt;/em&gt; All test runs will be created with the same property list if provided. If not provided, default property values will be used.   &lt;strong&gt;test_case attributes:&lt;/strong&gt;  &lt;em&gt;id (required):&lt;/em&gt; id of testcase   &lt;em&gt;test_case_version_id (optional):&lt;/em&gt; Version ID of Testcase. If not specify, latest value will be used. For shared test case, only accept approved version   &lt;em&gt;dataset_id:&lt;/em&gt; Dataset id use for generate test runs. Dataset must be active and contains all parameters inside all test case steps. Dataset has at least 1 data row.   &lt;em&gt;from_row:&lt;/em&gt; Must be less or equal max rows in dataset.   &lt;em&gt;number_of_rows:&lt;/em&gt; number of test run can be create must be less or equal ((max rows - from_row) +1) and must be less than &lt;em&gt;100&lt;/em&gt;. | 
 **parent_id** | **int**| ID of the container  Input 0 (zero) to get Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt;, and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**QueueProcessingResponseTestRunDataVM**](QueueProcessingResponseTestRunDataVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_test_run_with_parameters_randomize**
> QueueProcessingResponseTestRunDataVM add_test_run_with_parameters_randomize(project_id, body, parent_id=parent_id, parent_type=parent_type)

Create multiple Test Runs with Parameter values random from selection combine type.

To create multiple Test Runs with parameter values under root or a container (Release, Test Cycle or Test Suite). Maximum number of test runs can be created depend on combine type.

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.TestRunWithParameterCreateRandomResource() # TestRunWithParameterCreateRandomResource | The Test Run's properties, its associated Test Case and combine type, number of combination   <em>name (optional):</em> All test runs will be created with the same name if provided. If not provided, test run name = test case name + [increased number, starting from 1]   <em>properties (optional):</em> All test runs will be created with the same property list if provided. If not provided, default property values will be used.   <strong>test_case attributes:</strong>  <em>id (required):</em> id of testcase   <em>test_case_version_id (optional):</em> Version ID of Testcase. If not specify, latest value will be used. For shared test case, only accept approved version   <em>combined_type:</em> combine type for generate test runs with random test run value. Values can specify for this property are: <strong>1</strong> (for unique_value ) OR <strong>0</strong> (for unique_data ).   <em>number_of_combinations:</em> number of test run can be create must be less or equal max possible created combinations based on selected combination_type and must less than <em>100</em>.
parent_id = 789 # int | ID of the container  Input 0 (zero) to get Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em>, and <em>test-suite</em> (optional)

try:
    # Create multiple Test Runs with Parameter values random from selection combine type.
    api_response = api_instance.add_test_run_with_parameters_randomize(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->add_test_run_with_parameters_randomize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestRunWithParameterCreateRandomResource**](TestRunWithParameterCreateRandomResource.md)| The Test Run&#39;s properties, its associated Test Case and combine type, number of combination   &lt;em&gt;name (optional):&lt;/em&gt; All test runs will be created with the same name if provided. If not provided, test run name &#x3D; test case name + [increased number, starting from 1]   &lt;em&gt;properties (optional):&lt;/em&gt; All test runs will be created with the same property list if provided. If not provided, default property values will be used.   &lt;strong&gt;test_case attributes:&lt;/strong&gt;  &lt;em&gt;id (required):&lt;/em&gt; id of testcase   &lt;em&gt;test_case_version_id (optional):&lt;/em&gt; Version ID of Testcase. If not specify, latest value will be used. For shared test case, only accept approved version   &lt;em&gt;combined_type:&lt;/em&gt; combine type for generate test runs with random test run value. Values can specify for this property are: &lt;strong&gt;1&lt;/strong&gt; (for unique_value ) OR &lt;strong&gt;0&lt;/strong&gt; (for unique_data ).   &lt;em&gt;number_of_combinations:&lt;/em&gt; number of test run can be create must be less or equal max possible created combinations based on selected combination_type and must less than &lt;em&gt;100&lt;/em&gt;. | 
 **parent_id** | **int**| ID of the container  Input 0 (zero) to get Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt;, and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**QueueProcessingResponseTestRunDataVM**](QueueProcessingResponseTestRunDataVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_run**
> GetMultipleTestRunsResource create_test_run(project_id, body, parent_id=parent_id, parent_type=parent_type)

Creates a Test Run

To create a Test Run under root or a container (Release, Test Cycle or Test Suite)  <strong>qTest Manager version:</strong> 6+You can optionally specify a parent in the request parameter to create its test runs.  The associated Test Case is specified in the request body

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.GetMultipleTestRunsResource() # GetMultipleTestRunsResource | The Test Run's properties and its associated Test Case
parent_id = 789 # int | ID of the container  Input 0 (zero) to get Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em>, and <em>test-suite</em> (optional)

try:
    # Creates a Test Run
    api_response = api_instance.create_test_run(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->create_test_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**GetMultipleTestRunsResource**](GetMultipleTestRunsResource.md)| The Test Run&#39;s properties and its associated Test Case | 
 **parent_id** | **int**| ID of the container  Input 0 (zero) to get Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt;, and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**GetMultipleTestRunsResource**](GetMultipleTestRunsResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_by_id**
> object delete_comment_by_id(project_id, id_or_key, comment_id)

Deletes a Comment of a Test Run

To delete a Comment of a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run.
comment_id = 789 # int | ID of the comment which you want to delete.

try:
    # Deletes a Comment of a Test Run
    api_response = api_instance.delete_comment_by_id(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->delete_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run. | 
 **comment_id** | **int**| ID of the comment which you want to delete. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_run_by_id**
> Message delete_test_run_by_id(project_id, test_run_id)

Deletes a Test Run

To delete a Test Run  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run

try:
    # Deletes a Test Run
    api_response = api_instance.delete_test_run_by_id(project_id, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->delete_test_run_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run | 

### Return type

[**Message**](Message.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_of**
> GetMultipleTestRunListResource get_of(project_id, parent_id=parent_id, parent_type=parent_type, expand=expand, include_tosca_properties=include_tosca_properties, page=page, page_size=page_size)

Gets multiple Test Runs

To retrieve all Test Runs under root or under a container (Release, Test Cycle or Test Suite)  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
parent_id = 789 # int | ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to retrieve Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em> and <em>test-suite</em> (optional)
expand = 'expand_example' # str | Specify <em>expand=descendants</em> to include all Test Runs which are directly or indirectly under the container (optional)
include_tosca_properties = true # bool | By default, Tosca properties of Test Run (imported from Tosca) are not included in the response. Specify includeToscaProperties=true to include them.   <em>(tosca_guid, tosca_node_path, tosca_workspace_url, tosca_testevent_guid)</em> (optional)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Gets multiple Test Runs
    api_response = api_instance.get_of(project_id, parent_id=parent_id, parent_type=parent_type, expand=expand, include_tosca_properties=include_tosca_properties, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->get_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_id** | **int**| ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to retrieve Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 
 **expand** | **str**| Specify &lt;em&gt;expand&#x3D;descendants&lt;/em&gt; to include all Test Runs which are directly or indirectly under the container | [optional] 
 **include_tosca_properties** | **bool**| By default, Tosca properties of Test Run (imported from Tosca) are not included in the response. Specify includeToscaProperties&#x3D;true to include them.   &lt;em&gt;(tosca_guid, tosca_node_path, tosca_workspace_url, tosca_testevent_guid)&lt;/em&gt; | [optional] 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**GetMultipleTestRunListResource**](GetMultipleTestRunListResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_valuable**
> list[StatusResource] get_status_valuable(project_id)

Gets Test Run statuses

Gets Test Run statuses

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project

try:
    # Gets Test Run statuses
    api_response = api_instance.get_status_valuable(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->get_status_valuable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**list[StatusResource]**](StatusResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subhierachy**
> AutomationObjectTree get_subhierachy(project_id, parent_type=parent_type, parent_id=parent_id)

Gets a Sub Hierarchy

To retrieve a Sub Hierarchy of a container (root, release, test-cycle)   <strong>qTest Manager version:</strong> 9.3.4+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
parent_type = 'parent_type_example' # str | parentType (optional)
parent_id = 789 # int | parentId (optional)

try:
    # Gets a Sub Hierarchy
    api_response = api_instance.get_subhierachy(project_id, parent_type=parent_type, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->get_subhierachy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_type** | **str**| parentType | [optional] 
 **parent_id** | **int**| parentId | [optional] 

### Return type

[**AutomationObjectTree**](AutomationObjectTree.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run_by_id**
> TestRunWithCustomFieldResource get_test_run_by_id(project_id, test_run_id, expand=expand, include_tosca_properties=include_tosca_properties)

Gets a Test Run

To retrieve a Test Run  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run.
expand = 'expand_example' # str | Valid values include:   i)<em>testcase</em> - to expand the associated Test Case in the response;   ii) <em>testcase.teststep</em> - to expand the associated Test Case and its Test Steps in the response (optional)
include_tosca_properties = true # bool | By default, Tosca properties of Test Run (imported from Tosca) are not included in the response. Specify includeToscaProperties=true to include them.   <em>(tosca_guid, tosca_node_path, tosca_workspace_url, tosca_testevent_guid)</em> (optional)

try:
    # Gets a Test Run
    api_response = api_instance.get_test_run_by_id(project_id, test_run_id, expand=expand, include_tosca_properties=include_tosca_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->get_test_run_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run. | 
 **expand** | **str**| Valid values include:   i)&lt;em&gt;testcase&lt;/em&gt; - to expand the associated Test Case in the response;   ii) &lt;em&gt;testcase.teststep&lt;/em&gt; - to expand the associated Test Case and its Test Steps in the response | [optional] 
 **include_tosca_properties** | **bool**| By default, Tosca properties of Test Run (imported from Tosca) are not included in the response. Specify includeToscaProperties&#x3D;true to include them.   &lt;em&gt;(tosca_guid, tosca_node_path, tosca_workspace_url, tosca_testevent_guid)&lt;/em&gt; | [optional] 

### Return type

[**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run_comment_by_id**
> CommentResource get_test_run_comment_by_id(project_id, id_or_key, comment_id)

Gets a Comment from a Test Run

To retrieve a specific Comment from a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run.
comment_id = 789 # int | ID of the Comment

try:
    # Gets a Comment from a Test Run
    api_response = api_instance.get_test_run_comment_by_id(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->get_test_run_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run. | 
 **comment_id** | **int**| ID of the Comment | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run_comments**
> PagedResourceCommentResource get_test_run_comments(project_id, id_or_key)

Gets all Comments of a Test Run

To retrieve all Comments of a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run

try:
    # Gets all Comments of a Test Run
    api_response = api_instance.get_test_run_comments(project_id, id_or_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->get_test_run_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run | 

### Return type

[**PagedResourceCommentResource**](PagedResourceCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment_by_id**
> CommentResource update_comment_by_id(project_id, id_or_key, comment_id, body)

Updates a Comment of a Test Run

To update a Comment of a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run
comment_id = 789 # int | ID of the comment which you want to update.
body = swagger_client.CommentResource() # CommentResource | The Comment's updated content

try:
    # Updates a Comment of a Test Run
    api_response = api_instance.update_comment_by_id(project_id, id_or_key, comment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->update_comment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run | 
 **comment_id** | **int**| ID of the comment which you want to update. | 
 **body** | [**CommentResource**](CommentResource.md)| The Comment&#39;s updated content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_run_by_id**
> TestRunWithCustomFieldResource update_test_run_by_id(project_id, test_run_id, body, parent_id=parent_id, parent_type=parent_type)

Updates a Test Run

To update a Test Run or move it to another container  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run.
body = swagger_client.TestRunWithCustomFieldResource() # TestRunWithCustomFieldResource | The Test Run's updated properties
parent_id = 789 # int | ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to move the test run to under root  <strong>Important:</strong> If you use the request parameters, the request body will be ignored. That means the test run is being moved but it will not be updated with the properties specify in the request body (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em> and <em>test-suite</em> (optional)

try:
    # Updates a Test Run
    api_response = api_instance.update_test_run_by_id(project_id, test_run_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->update_test_run_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run. | 
 **body** | [**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)| The Test Run&#39;s updated properties | 
 **parent_id** | **int**| ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to move the test run to under root  &lt;strong&gt;Important:&lt;/strong&gt; If you use the request parameters, the request body will be ignored. That means the test run is being moved but it will not be updated with the properties specify in the request body | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

