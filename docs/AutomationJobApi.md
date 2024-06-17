# swagger_client.AutomationJobApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](AutomationJobApi.md#create_schedule) | **POST** /api/v3/automation/jobs/schedule/create | Create a Schedule
[**search_automation_agents**](AutomationJobApi.md#search_automation_agents) | **POST** /api/v3/automation/automation-agents | Search automation agents


# **create_schedule**
> int create_schedule(body)

Create a Schedule

To create a new Schedule which will be executed immediately  <strong>NOTE:</strong> Try It Out function will not work for this API  <strong>qTest Manager version:</strong> 6+\"

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
api_instance = swagger_client.AutomationJobApi(swagger_client.ApiClient(configuration))
body = swagger_client.AutomationScheduleCreationAPI() # AutomationScheduleCreationAPI | 

try:
    # Create a Schedule
    api_response = api_instance.create_schedule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationJobApi->create_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomationScheduleCreationAPI**](AutomationScheduleCreationAPI.md)|  | 

### Return type

**int**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_automation_agents**
> PagedResource search_automation_agents(body, page_size=page_size, page=page)

Search automation agents

To search automation agents in projects that user is assigned to   <em>fields:</em> specify which property of Automation Agent you want to include in the response. If you omit it or specify an asterisk (*), all of following fields are included: id, name, project_id, host_id, framework, active, configuration   <em>query:</em> specify a structured query (criteria, operator and value) with one or multiple clauses to search for Automation Agents. Following are supporting criteria  | Criteria | Operators | Value | |-----|-----|-------| | name, framework   |  <>, ~, is empty, =, !~, is not empty   | string     |  |host_name | <>, ~, =, !~ | string |  | id, project_id, host_id | <>, >, <, <=, >=, =| id   | active | = | active, inactive  

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
api_instance = swagger_client.AutomationJobApi(swagger_client.ApiClient(configuration))
body = swagger_client.AutomationArtifactSearchParams() # AutomationArtifactSearchParams | 
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)

try:
    # Search automation agents
    api_response = api_instance.search_automation_agents(body, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationJobApi->search_automation_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomationArtifactSearchParams**](AutomationArtifactSearchParams.md)|  | 
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]

### Return type

[**PagedResource**](PagedResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

