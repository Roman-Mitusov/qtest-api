# swagger_client.ToscaApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify_test_event_import**](ToscaApi.md#notify_test_event_import) | **POST** /api/v3/projects/{projectId}/tosca/import/test-event | Import Tosca TestEvent objects


# **notify_test_event_import**
> QueueProcessingResponse notify_test_event_import(project_id, body)

Import Tosca TestEvent objects

To export TestEvent objects from Tosca to qTest

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
api_instance = swagger_client.ToscaApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = [swagger_client.ToscaTestCycleResource()] # list[ToscaTestCycleResource] | An array of hierarchy Tosca objects  <em>toscaUniqueId (required):</em> Unique ID of the Tosca object  <em>name (required):</em> Name of the Tosca object  <em>description:</em> Description of the Tosca object  <em>toscaObjectType (required):</em> Type of the Tosca object: TestEvent, ExecutionList (contained inTestEvent), ExecutionEntry Folder(contained in Execution List). Object is TestEvent type is always on the root of body array and doesn't contain ExecutionEntry objects   <em>toscaNodePath (required):</em> Node path of the Tosca object  <em>testCycles:</em> The array of TestEvent or ExecutionList or ExecutionEntry Folder objects  <em>testRuns:</em> The array of ExecutionEntry objects in testCycle property  <em>associatedToscaTestCase:</em> Testcase object that associated with testRun object

try:
    # Import Tosca TestEvent objects
    api_response = api_instance.notify_test_event_import(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToscaApi->notify_test_event_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**list[ToscaTestCycleResource]**](ToscaTestCycleResource.md)| An array of hierarchy Tosca objects  &lt;em&gt;toscaUniqueId (required):&lt;/em&gt; Unique ID of the Tosca object  &lt;em&gt;name (required):&lt;/em&gt; Name of the Tosca object  &lt;em&gt;description:&lt;/em&gt; Description of the Tosca object  &lt;em&gt;toscaObjectType (required):&lt;/em&gt; Type of the Tosca object: TestEvent, ExecutionList (contained inTestEvent), ExecutionEntry Folder(contained in Execution List). Object is TestEvent type is always on the root of body array and doesn&#39;t contain ExecutionEntry objects   &lt;em&gt;toscaNodePath (required):&lt;/em&gt; Node path of the Tosca object  &lt;em&gt;testCycles:&lt;/em&gt; The array of TestEvent or ExecutionList or ExecutionEntry Folder objects  &lt;em&gt;testRuns:&lt;/em&gt; The array of ExecutionEntry objects in testCycle property  &lt;em&gt;associatedToscaTestCase:&lt;/em&gt; Testcase object that associated with testRun object | 

### Return type

[**QueueProcessingResponse**](QueueProcessingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

