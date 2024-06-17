# swagger_client.IntegrationSettingsApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_connection**](IntegrationSettingsApi.md#add_new_connection) | **POST** /api/v3/projects/{projectId}/settings/integration/connections | Add a new Jira connection
[**add_new_defect_mapping**](IntegrationSettingsApi.md#add_new_defect_mapping) | **POST** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/defect/mappings | Add a defect mapping to a Jira connection
[**add_new_release_mapping**](IntegrationSettingsApi.md#add_new_release_mapping) | **POST** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/release/mappings | Add a new Jira release mapping to a Jira connection
[**add_new_requirement_mapping**](IntegrationSettingsApi.md#add_new_requirement_mapping) | **POST** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/requirement/mappings | Add a requirement mapping to a Jira connection
[**configure_populating_jira_unlinked_defects**](IntegrationSettingsApi.md#configure_populating_jira_unlinked_defects) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/defect | Enable or disable populating Jira Unlinked Defects of a Jira connection
[**configure_release_mapping**](IntegrationSettingsApi.md#configure_release_mapping) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/release/mappings | Update a Release Mapping of a Jira connection
[**configure_requirement_mapping**](IntegrationSettingsApi.md#configure_requirement_mapping) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/requirement/mappings | Update a requirement mapping of a Jira connection
[**delete_connection**](IntegrationSettingsApi.md#delete_connection) | **DELETE** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId} | Delete a Jira connection
[**get_authorize_url**](IntegrationSettingsApi.md#get_authorize_url) | **GET** /api/v3/projects/{projectId}/settings/integration/connections/oauthAuthorizeURL | OAuth Authorize URL
[**get_connections**](IntegrationSettingsApi.md#get_connections) | **GET** /api/v3/projects/{projectId}/settings/integration/connections | Get all Jira connections of a project
[**get_defect_mappings**](IntegrationSettingsApi.md#get_defect_mappings) | **GET** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/defect/mappings | Get Jira defect mappings of a Jira connection
[**get_release_mappings**](IntegrationSettingsApi.md#get_release_mappings) | **GET** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/release/mappings | Get Jira release mappings of a Jira connection
[**refresh_field_settings**](IntegrationSettingsApi.md#refresh_field_settings) | **POST** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/refreshFieldSettings | Trigger retrieving latest field settings from a JIRA connection
[**remove_mapping**](IntegrationSettingsApi.md#remove_mapping) | **DELETE** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/{artifact}/mappings | Remove a Mapping of a Jira connection
[**retrieve_all_requirement_mappings_of_connection**](IntegrationSettingsApi.md#retrieve_all_requirement_mappings_of_connection) | **GET** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/requirement/mappings | Get requirement mappings of a Jira connection
[**toggle_release_integration**](IntegrationSettingsApi.md#toggle_release_integration) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/release | Enable or disable Release Integration feature of a Jira connection
[**toggle_requirement_integration**](IntegrationSettingsApi.md#toggle_requirement_integration) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/requirement | Enable or disable a Requirement Integration feature of a Jira connection
[**trigger_retrieving_data_for_connection**](IntegrationSettingsApi.md#trigger_retrieving_data_for_connection) | **GET** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/retrieve | Trigger data retrieval from an integrated Jira system
[**trigger_retrieving_defect_data_for_connection**](IntegrationSettingsApi.md#trigger_retrieving_defect_data_for_connection) | **POST** /api/v3/projects/{projectId}/settings/jira-integration/defect/retrieve | Trigger defect retrieval from an integrated Jira system
[**update_defect_mapping**](IntegrationSettingsApi.md#update_defect_mapping) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId}/defect/mappings | Update a defect mapping of Jira connection
[**update_integration_connection_status**](IntegrationSettingsApi.md#update_integration_connection_status) | **PUT** /api/v3/projects/{projectId}/settings/integration/connections/{connectionId} | Activate or deactivate a Jira connection


# **add_new_connection**
> NewIntegrationConnectionInfo add_new_connection(project_id, body)

Add a new Jira connection

Add a new Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.IntegrationConnection() # IntegrationConnection | <em>external_system (required):</em> Input <em>Jira</em>  <em>connection_name (required):</em> Name of connection  <em>server_url (required):</em> your Jira server URL  <em>web_url:</em> Your Jira web URL (for Jira server only)  <em>authentication_type (required):</em> Input <em>Token</em> if you are using password or API token, or <em>OAuth</em> if you are using Jira OAuth for authentication  <em>username:</em> If <em>authentication_type=Token</em>, then input your Jira username. If <em>authentication_type=OAuth</em>, then input <em>apikey</em>  <em>password:</em> Input your Jira password or API token (only required if <em>authentication_type=Token</em>)  <em>jiraToken, jiraSecret</em> and <em>jiraVerifier</em> these are required if authentication_type=Oauth. You will need to use our API to <em>Get OAuth Authorize URL</em> described below to retrieve values for these fields.

try:
    # Add a new Jira connection
    api_response = api_instance.add_new_connection(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->add_new_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**IntegrationConnection**](IntegrationConnection.md)| &lt;em&gt;external_system (required):&lt;/em&gt; Input &lt;em&gt;Jira&lt;/em&gt;  &lt;em&gt;connection_name (required):&lt;/em&gt; Name of connection  &lt;em&gt;server_url (required):&lt;/em&gt; your Jira server URL  &lt;em&gt;web_url:&lt;/em&gt; Your Jira web URL (for Jira server only)  &lt;em&gt;authentication_type (required):&lt;/em&gt; Input &lt;em&gt;Token&lt;/em&gt; if you are using password or API token, or &lt;em&gt;OAuth&lt;/em&gt; if you are using Jira OAuth for authentication  &lt;em&gt;username:&lt;/em&gt; If &lt;em&gt;authentication_type&#x3D;Token&lt;/em&gt;, then input your Jira username. If &lt;em&gt;authentication_type&#x3D;OAuth&lt;/em&gt;, then input &lt;em&gt;apikey&lt;/em&gt;  &lt;em&gt;password:&lt;/em&gt; Input your Jira password or API token (only required if &lt;em&gt;authentication_type&#x3D;Token&lt;/em&gt;)  &lt;em&gt;jiraToken, jiraSecret&lt;/em&gt; and &lt;em&gt;jiraVerifier&lt;/em&gt; these are required if authentication_type&#x3D;Oauth. You will need to use our API to &lt;em&gt;Get OAuth Authorize URL&lt;/em&gt; described below to retrieve values for these fields. | 

### Return type

[**NewIntegrationConnectionInfo**](NewIntegrationConnectionInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_defect_mapping**
> IntegrationAutoFillMappingVM add_new_defect_mapping(project_id, connection_id, external_project_id, external_issue_type_id)

Add a defect mapping to a Jira connection

Add a defect mapping to a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project. Use this to retrieve mappings with this Jira project only
external_issue_type_id = 'external_issue_type_id_example' # str | ID of a Jira issue type. Use this to retrieve mappings with this Jira issue type only

try:
    # Add a defect mapping to a Jira connection
    api_response = api_instance.add_new_defect_mapping(project_id, connection_id, external_project_id, external_issue_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->add_new_defect_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project. Use this to retrieve mappings with this Jira project only | 
 **external_issue_type_id** | **str**| ID of a Jira issue type. Use this to retrieve mappings with this Jira issue type only | 

### Return type

[**IntegrationAutoFillMappingVM**](IntegrationAutoFillMappingVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_release_mapping**
> IntegrationReleaseMappingResponse add_new_release_mapping(project_id, connection_id, external_project_id, external_issue_type_id)

Add a new Jira release mapping to a Jira connection

Add a new Jira release mapping to a Jira connection.   <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project. You will need to make API calls to Jira to get its project IDs
external_issue_type_id = 'external_issue_type_id_example' # str | valid values include: fixVersions, Sprint (<strong>case-sensitive</strong>)

try:
    # Add a new Jira release mapping to a Jira connection
    api_response = api_instance.add_new_release_mapping(project_id, connection_id, external_project_id, external_issue_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->add_new_release_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project. You will need to make API calls to Jira to get its project IDs | 
 **external_issue_type_id** | **str**| valid values include: fixVersions, Sprint (&lt;strong&gt;case-sensitive&lt;/strong&gt;) | 

### Return type

[**IntegrationReleaseMappingResponse**](IntegrationReleaseMappingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_requirement_mapping**
> RequirementMapping add_new_requirement_mapping(project_id, connection_id, external_project_id, external_issue_type_id)

Add a requirement mapping to a Jira connection

Add a requirement mapping to a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project. You will need to make API calls to Jira to retrieve its project IDs
external_issue_type_id = 'external_issue_type_id_example' # str | ID of a Jira issue type. You will need to make API calls to Jira to retrieve its issue type IDs

try:
    # Add a requirement mapping to a Jira connection
    api_response = api_instance.add_new_requirement_mapping(project_id, connection_id, external_project_id, external_issue_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->add_new_requirement_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project. You will need to make API calls to Jira to retrieve its project IDs | 
 **external_issue_type_id** | **str**| ID of a Jira issue type. You will need to make API calls to Jira to retrieve its issue type IDs | 

### Return type

[**RequirementMapping**](RequirementMapping.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_populating_jira_unlinked_defects**
> configure_populating_jira_unlinked_defects(project_id, connection_id, store_unlinked_defects=store_unlinked_defects)

Enable or disable populating Jira Unlinked Defects of a Jira connection

Enable or disable populating Jira Unlinked Defects of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
store_unlinked_defects = 'store_unlinked_defects_example' # str | Input <em>true</em> to populate unlinked Jira Defects, or <em>false</em> to disable this feature (optional)

try:
    # Enable or disable populating Jira Unlinked Defects of a Jira connection
    api_instance.configure_populating_jira_unlinked_defects(project_id, connection_id, store_unlinked_defects=store_unlinked_defects)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->configure_populating_jira_unlinked_defects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **store_unlinked_defects** | **str**| Input &lt;em&gt;true&lt;/em&gt; to populate unlinked Jira Defects, or &lt;em&gt;false&lt;/em&gt; to disable this feature | [optional] 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_release_mapping**
> IntegrationReleaseMappingResponse configure_release_mapping(project_id, connection_id, external_project_id, external_issue_type_id, body)

Update a Release Mapping of a Jira connection

To configure a Release Mapping of a Jira connection.   <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project
external_issue_type_id = 'external_issue_type_id_example' # str | valid values include: fixVersions, Sprint (<strong>case-sensitive</strong>)   externalProjectId and externalIssueTypeId are used to identify a release mapping and cannot be modified
body = swagger_client.IntegrationReleaseConfigurationVM() # IntegrationReleaseConfigurationVM | <em>data_retrieval_options:</em> If <em>externalIssueTypeId=fixVersions</em>, valid values include: <strong>released, unreleased</strong>. If <em>externalIssueTypeId=fixVersions</em>, valid values include: <strong>active, future, completed</strong>  <em>auto_update_release_scope:</em> Select to automatically update scope of imported Releases in qTest. Valid values include: <b>True, False</b>

try:
    # Update a Release Mapping of a Jira connection
    api_response = api_instance.configure_release_mapping(project_id, connection_id, external_project_id, external_issue_type_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->configure_release_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project | 
 **external_issue_type_id** | **str**| valid values include: fixVersions, Sprint (&lt;strong&gt;case-sensitive&lt;/strong&gt;)   externalProjectId and externalIssueTypeId are used to identify a release mapping and cannot be modified | 
 **body** | [**IntegrationReleaseConfigurationVM**](IntegrationReleaseConfigurationVM.md)| &lt;em&gt;data_retrieval_options:&lt;/em&gt; If &lt;em&gt;externalIssueTypeId&#x3D;fixVersions&lt;/em&gt;, valid values include: &lt;strong&gt;released, unreleased&lt;/strong&gt;. If &lt;em&gt;externalIssueTypeId&#x3D;fixVersions&lt;/em&gt;, valid values include: &lt;strong&gt;active, future, completed&lt;/strong&gt;  &lt;em&gt;auto_update_release_scope:&lt;/em&gt; Select to automatically update scope of imported Releases in qTest. Valid values include: &lt;b&gt;True, False&lt;/b&gt; | 

### Return type

[**IntegrationReleaseMappingResponse**](IntegrationReleaseMappingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_requirement_mapping**
> RequirementMapping configure_requirement_mapping(project_id, connection_id, external_project_id, external_issue_type_id, body)

Update a requirement mapping of a Jira connection

To configure a requirement mapping of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project
external_issue_type_id = 'external_issue_type_id_example' # str | ID of a Jira issue type   externalProjectId and externalIssueTypeId are used to identify a release mapping and cannot be modified
body = swagger_client.RequirementMapping() # RequirementMapping | <em>external_filter:</em> ID of a Jira filter whose Jira issues will be imported to qTest as Requirements.  <em>external_field_1_id</em> and <em>external_field_2_id:</em> <strong>Jira keys</strong> of 2 Jira fields that are used to organize imported Requirements  <em>active_external_fields:</em> <em>Jira keys</em> of Jira fields that will show up in qTest requirement page (Jira read-only properties panel). You can specify a list of Jira fields, <em>separated by comma without a following space</em>

try:
    # Update a requirement mapping of a Jira connection
    api_response = api_instance.configure_requirement_mapping(project_id, connection_id, external_project_id, external_issue_type_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->configure_requirement_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project | 
 **external_issue_type_id** | **str**| ID of a Jira issue type   externalProjectId and externalIssueTypeId are used to identify a release mapping and cannot be modified | 
 **body** | [**RequirementMapping**](RequirementMapping.md)| &lt;em&gt;external_filter:&lt;/em&gt; ID of a Jira filter whose Jira issues will be imported to qTest as Requirements.  &lt;em&gt;external_field_1_id&lt;/em&gt; and &lt;em&gt;external_field_2_id:&lt;/em&gt; &lt;strong&gt;Jira keys&lt;/strong&gt; of 2 Jira fields that are used to organize imported Requirements  &lt;em&gt;active_external_fields:&lt;/em&gt; &lt;em&gt;Jira keys&lt;/em&gt; of Jira fields that will show up in qTest requirement page (Jira read-only properties panel). You can specify a list of Jira fields, &lt;em&gt;separated by comma without a following space&lt;/em&gt; | 

### Return type

[**RequirementMapping**](RequirementMapping.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(project_id, connection_id)

Delete a Jira connection

Delete a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection

try:
    # Delete a Jira connection
    api_instance.delete_connection(project_id, connection_id)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorize_url**
> TokenSecretVerifierHolder get_authorize_url(project_id, server_url)

OAuth Authorize URL

OAuth Authorize URL (for Jira Server or DC only).  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | this must be 0 (zero)
server_url = 'server_url_example' # str | your Jira's Server URL

try:
    # OAuth Authorize URL
    api_response = api_instance.get_authorize_url(project_id, server_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->get_authorize_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| this must be 0 (zero) | 
 **server_url** | **str**| your Jira&#39;s Server URL | 

### Return type

[**TokenSecretVerifierHolder**](TokenSecretVerifierHolder.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> IntegrationConnectionVM get_connections(project_id)

Get all Jira connections of a project

Get all Jira connections of a project  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project

try:
    # Get all Jira connections of a project
    api_response = api_instance.get_connections(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->get_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**IntegrationConnectionVM**](IntegrationConnectionVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_defect_mappings**
> IntegrationAutoFillMappingVM get_defect_mappings(project_id, connection_id, external_project_id=external_project_id, external_issue_type_id=external_issue_type_id)

Get Jira defect mappings of a Jira connection

Get Jira defect mappings of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project. Use this to retrieve mappings with this Jira project only (optional)
external_issue_type_id = 'external_issue_type_id_example' # str | ID of a Jira issue type. Use this to retrieve mappings with this Jira issue type (optional)

try:
    # Get Jira defect mappings of a Jira connection
    api_response = api_instance.get_defect_mappings(project_id, connection_id, external_project_id=external_project_id, external_issue_type_id=external_issue_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->get_defect_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project. Use this to retrieve mappings with this Jira project only | [optional] 
 **external_issue_type_id** | **str**| ID of a Jira issue type. Use this to retrieve mappings with this Jira issue type | [optional] 

### Return type

[**IntegrationAutoFillMappingVM**](IntegrationAutoFillMappingVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_mappings**
> list[IntegrationReleaseMappingResponse] get_release_mappings(project_id, connection_id, external_project_id=external_project_id, external_issue_type_id=external_issue_type_id)

Get Jira release mappings of a Jira connection

Get Jira release mappings of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project. Use this to retrieve mappings with this Jira project only (optional)
external_issue_type_id = 'external_issue_type_id_example' # str | Valid values include: fixVersions, Sprint (<strong>case-sensitive</strong>) (optional)

try:
    # Get Jira release mappings of a Jira connection
    api_response = api_instance.get_release_mappings(project_id, connection_id, external_project_id=external_project_id, external_issue_type_id=external_issue_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->get_release_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project. Use this to retrieve mappings with this Jira project only | [optional] 
 **external_issue_type_id** | **str**| Valid values include: fixVersions, Sprint (&lt;strong&gt;case-sensitive&lt;/strong&gt;) | [optional] 

### Return type

[**list[IntegrationReleaseMappingResponse]**](IntegrationReleaseMappingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_field_settings**
> list[IntegrationFieldMapVM] refresh_field_settings(project_id, connection_id, artifact, mapping_id=mapping_id)

Trigger retrieving latest field settings from a JIRA connection

Trigger retrieving the latest Defects/Requirements field settings from Jira  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
artifact = 'artifact_example' # str | Single value. Valid values include: <b>Defects, Requirements</b>
mapping_id = 789 # int | ID of the mapping. Only required if <em>artifact=Requirements<em> (optional)

try:
    # Trigger retrieving latest field settings from a JIRA connection
    api_response = api_instance.refresh_field_settings(project_id, connection_id, artifact, mapping_id=mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->refresh_field_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **artifact** | **str**| Single value. Valid values include: &lt;b&gt;Defects, Requirements&lt;/b&gt; | 
 **mapping_id** | **int**| ID of the mapping. Only required if &lt;em&gt;artifact&#x3D;Requirements&lt;em&gt; | [optional] 

### Return type

[**list[IntegrationFieldMapVM]**](IntegrationFieldMapVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mapping**
> remove_mapping(project_id, connection_id, artifact, external_project_id, external_issue_type_id)

Remove a Mapping of a Jira connection

Remove a Mapping of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
artifact = 'artifact_example' # str | Valid values can be: <b>Defect, Requirement, Release</b>
external_project_id = 'external_project_id_example' # str | ID of a Jira project
external_issue_type_id = 'external_issue_type_id_example' # str | ID of a Jira issue type.    externalProjectId and externalIssueTypeId are used to identify a mapping

try:
    # Remove a Mapping of a Jira connection
    api_instance.remove_mapping(project_id, connection_id, artifact, external_project_id, external_issue_type_id)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->remove_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **artifact** | **str**| Valid values can be: &lt;b&gt;Defect, Requirement, Release&lt;/b&gt; | 
 **external_project_id** | **str**| ID of a Jira project | 
 **external_issue_type_id** | **str**| ID of a Jira issue type.    externalProjectId and externalIssueTypeId are used to identify a mapping | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_requirement_mappings_of_connection**
> list[RequirementMapping] retrieve_all_requirement_mappings_of_connection(project_id, connection_id, external_project_id=external_project_id, external_issue_type_id=external_issue_type_id)

Get requirement mappings of a Jira connection

Get requirement mappings of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of the Jira project. You will need to make API calls to Jira to get its project IDs (optional)
external_issue_type_id = 'external_issue_type_id_example' # str | ID of the Jira issue type. You will need to make API calls to Jira to get its issue type IDs (optional)

try:
    # Get requirement mappings of a Jira connection
    api_response = api_instance.retrieve_all_requirement_mappings_of_connection(project_id, connection_id, external_project_id=external_project_id, external_issue_type_id=external_issue_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->retrieve_all_requirement_mappings_of_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of the Jira project. You will need to make API calls to Jira to get its project IDs | [optional] 
 **external_issue_type_id** | **str**| ID of the Jira issue type. You will need to make API calls to Jira to get its issue type IDs | [optional] 

### Return type

[**list[RequirementMapping]**](RequirementMapping.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_release_integration**
> toggle_release_integration(project_id, connection_id, active=active, auto_filter_test_run=auto_filter_test_run, merge_duplicated_fix_versions=merge_duplicated_fix_versions)

Enable or disable Release Integration feature of a Jira connection

Enable or disable Release Integration feature  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
active = 'active_example' # str | Input <em>true</em> to enable Release integration, or <em>false</em> to disable it (optional)
auto_filter_test_run = 'auto_filter_test_run_example' # str | select or deselect the checkbox <em>Auto-filter Test Runs on Jira iframe to match Fix Version/Sprint of Jira issue</em>. Valid values include: <b>True, False</b> (optional)
merge_duplicated_fix_versions = 'merge_duplicated_fix_versions_example' # str | select or deselect the checkbox Merge all Jira Fix versions with existing qTest Releases that have the same name into a single Release and link to all Jira projects. Valid values include: <b>True, False</b> (optional)

try:
    # Enable or disable Release Integration feature of a Jira connection
    api_instance.toggle_release_integration(project_id, connection_id, active=active, auto_filter_test_run=auto_filter_test_run, merge_duplicated_fix_versions=merge_duplicated_fix_versions)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->toggle_release_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **active** | **str**| Input &lt;em&gt;true&lt;/em&gt; to enable Release integration, or &lt;em&gt;false&lt;/em&gt; to disable it | [optional] 
 **auto_filter_test_run** | **str**| select or deselect the checkbox &lt;em&gt;Auto-filter Test Runs on Jira iframe to match Fix Version/Sprint of Jira issue&lt;/em&gt;. Valid values include: &lt;b&gt;True, False&lt;/b&gt; | [optional] 
 **merge_duplicated_fix_versions** | **str**| select or deselect the checkbox Merge all Jira Fix versions with existing qTest Releases that have the same name into a single Release and link to all Jira projects. Valid values include: &lt;b&gt;True, False&lt;/b&gt; | [optional] 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_requirement_integration**
> toggle_requirement_integration(project_id, connection_id, active=active)

Enable or disable a Requirement Integration feature of a Jira connection

Enable or disable a Requirement Integration feature of a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
active = 'active_example' # str | Input <em>true</em> to enable the feature, or <em>false</em> to disable it (optional)

try:
    # Enable or disable a Requirement Integration feature of a Jira connection
    api_instance.toggle_requirement_integration(project_id, connection_id, active=active)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->toggle_requirement_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **active** | **str**| Input &lt;em&gt;true&lt;/em&gt; to enable the feature, or &lt;em&gt;false&lt;/em&gt; to disable it | [optional] 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_retrieving_data_for_connection**
> QueueProcessingResponseFetchDataVM trigger_retrieving_data_for_connection(project_id, connection_id, artifact)

Trigger data retrieval from an integrated Jira system

Trigger data retrieval from an integrated Jira system  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
artifact = 'artifact_example' # str | Valid values include: <b>Defects, Requirements, Releases</b>

try:
    # Trigger data retrieval from an integrated Jira system
    api_response = api_instance.trigger_retrieving_data_for_connection(project_id, connection_id, artifact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->trigger_retrieving_data_for_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **artifact** | **str**| Valid values include: &lt;b&gt;Defects, Requirements, Releases&lt;/b&gt; | 

### Return type

[**QueueProcessingResponseFetchDataVM**](QueueProcessingResponseFetchDataVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_retrieving_defect_data_for_connection**
> QueueProcessingResponse trigger_retrieving_defect_data_for_connection(project_id, body)

Trigger defect retrieval from an integrated Jira system



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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = [swagger_client.list[str]()] # list[str] | PID of Jira defects

try:
    # Trigger defect retrieval from an integrated Jira system
    api_response = api_instance.trigger_retrieving_defect_data_for_connection(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->trigger_retrieving_defect_data_for_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | **list[str]**| PID of Jira defects | 

### Return type

[**QueueProcessingResponse**](QueueProcessingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_defect_mapping**
> IntegrationAutoFillMappingVM update_defect_mapping(project_id, connection_id, external_project_id, external_issue_type_id, body)

Update a defect mapping of Jira connection

Update a defect mapping of Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
external_project_id = 'external_project_id_example' # str | ID of a Jira project
external_issue_type_id = 'external_issue_type_id_example' # str | ID of the Jira issue type   externalProjectId and externalIssueTypeId are used to identify a defect mapping and cannot be modified
body = swagger_client.IntegrationAutoFillMappingVM() # IntegrationAutoFillMappingVM | <em>sendAttachmentToJira:</em> send test log and test step log attachments to linked Jira Defects. Valid values include: <b>True, False</b>  <em>configures:</em> Auto filling configuration for Defect submission to Jira. This is an array of JSON objects each of which consists of a Jira field Id (<em>externalFieldId</em>) and qTest fields (<em>qTestFieldIds</em>) to be auto filled to the Jira field<ul><li>You can only config auto fill for Jira text typed fields</li><li>You can auto fill multiple qTest fields to one Jira fields. Use <strong>comma without a following space</strong> to separate the fields</li><li>These following qTest fields can be configured to be auto filled to Jira fields (use these field names exactly as mentioned below instead of their IDs in qTestFieldIds): <em>Assigned To, Description, Environment, Execution Type, Planned End, Planned Start, Submitter, Target Release/Build, Test Case Version, Test Data Source, Name, Precondition, Test Case Description, Session URL, Session Description, Session Environment, Test Run URL</em></li></ul>

try:
    # Update a defect mapping of Jira connection
    api_response = api_instance.update_defect_mapping(project_id, connection_id, external_project_id, external_issue_type_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->update_defect_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **external_project_id** | **str**| ID of a Jira project | 
 **external_issue_type_id** | **str**| ID of the Jira issue type   externalProjectId and externalIssueTypeId are used to identify a defect mapping and cannot be modified | 
 **body** | [**IntegrationAutoFillMappingVM**](IntegrationAutoFillMappingVM.md)| &lt;em&gt;sendAttachmentToJira:&lt;/em&gt; send test log and test step log attachments to linked Jira Defects. Valid values include: &lt;b&gt;True, False&lt;/b&gt;  &lt;em&gt;configures:&lt;/em&gt; Auto filling configuration for Defect submission to Jira. This is an array of JSON objects each of which consists of a Jira field Id (&lt;em&gt;externalFieldId&lt;/em&gt;) and qTest fields (&lt;em&gt;qTestFieldIds&lt;/em&gt;) to be auto filled to the Jira field&lt;ul&gt;&lt;li&gt;You can only config auto fill for Jira text typed fields&lt;/li&gt;&lt;li&gt;You can auto fill multiple qTest fields to one Jira fields. Use &lt;strong&gt;comma without a following space&lt;/strong&gt; to separate the fields&lt;/li&gt;&lt;li&gt;These following qTest fields can be configured to be auto filled to Jira fields (use these field names exactly as mentioned below instead of their IDs in qTestFieldIds): &lt;em&gt;Assigned To, Description, Environment, Execution Type, Planned End, Planned Start, Submitter, Target Release/Build, Test Case Version, Test Data Source, Name, Precondition, Test Case Description, Session URL, Session Description, Session Environment, Test Run URL&lt;/em&gt;&lt;/li&gt;&lt;/ul&gt; | 

### Return type

[**IntegrationAutoFillMappingVM**](IntegrationAutoFillMappingVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_connection_status**
> update_integration_connection_status(project_id, connection_id, active)

Activate or deactivate a Jira connection

Activate or deactivate a Jira connection  <strong>qTest Manager version:</strong> 9.7+

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
api_instance = swagger_client.IntegrationSettingsApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
connection_id = 789 # int | ID of the Jira connection
active = 'active_example' # str | Input <em>true</em> to activate a connection, or <em>false</em> to deactivate it

try:
    # Activate or deactivate a Jira connection
    api_instance.update_integration_connection_status(project_id, connection_id, active)
except ApiException as e:
    print("Exception when calling IntegrationSettingsApi->update_integration_connection_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **connection_id** | **int**| ID of the Jira connection | 
 **active** | **str**| Input &lt;em&gt;true&lt;/em&gt; to activate a connection, or &lt;em&gt;false&lt;/em&gt; to deactivate it | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

