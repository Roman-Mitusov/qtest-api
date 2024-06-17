# swagger_client.SiteTemplatesApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_projects**](SiteTemplatesApi.md#add_projects) | **POST** /api/v3/site-templates/{templateId}/projects | Apply template to existing projects.
[**get_all_site_templates**](SiteTemplatesApi.md#get_all_site_templates) | **GET** /api/v3/site-templates | Get all site-templates
[**remove_project_templates**](SiteTemplatesApi.md#remove_project_templates) | **DELETE** /api/v3/site-templates/{templateId}/projects | Remove projects from a site template.


# **add_projects**
> list[ProjectResource] add_projects(template_id, body)

Apply template to existing projects.

To apply template to existing projects.

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
api_instance = swagger_client.SiteTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 789 # int | Template id which you want to apply to existing projects.
body = swagger_client.ApplyTemplateQueryObject() # ApplyTemplateQueryObject | <em>project_ids:</em>List of Project IDs  <em>create_new_site_field_values:</em> Option to allow user to decide if they want to create new values to the site fields or keep the value private to the project when there are \"unique values in project fields that do not exist in site fields\" (default: true).

try:
    # Apply template to existing projects.
    api_response = api_instance.add_projects(template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplatesApi->add_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template id which you want to apply to existing projects. | 
 **body** | [**ApplyTemplateQueryObject**](ApplyTemplateQueryObject.md)| &lt;em&gt;project_ids:&lt;/em&gt;List of Project IDs  &lt;em&gt;create_new_site_field_values:&lt;/em&gt; Option to allow user to decide if they want to create new values to the site fields or keep the value private to the project when there are \&quot;unique values in project fields that do not exist in site fields\&quot; (default: true). | 

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_site_templates**
> list[SiteTemplateResponse] get_all_site_templates()

Get all site-templates

To retrieve all site-templates

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
api_instance = swagger_client.SiteTemplatesApi(swagger_client.ApiClient(configuration))

try:
    # Get all site-templates
    api_response = api_instance.get_all_site_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplatesApi->get_all_site_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SiteTemplateResponse]**](SiteTemplateResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_templates**
> list[ProjectResource] remove_project_templates(template_id, body)

Remove projects from a site template.

To remove projects from a site template.

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
api_instance = swagger_client.SiteTemplatesApi(swagger_client.ApiClient(configuration))
template_id = 789 # int | Template id which you want to detach it's projects. If <strong>0</strong> (unassigned template id) is placing here, remove all site templates associated to provided project ids list.
body = [swagger_client.list[int]()] # list[int] | Array of project ids that you want to detach from site template.

try:
    # Remove projects from a site template.
    api_response = api_instance.remove_project_templates(template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplatesApi->remove_project_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template id which you want to detach it&#39;s projects. If &lt;strong&gt;0&lt;/strong&gt; (unassigned template id) is placing here, remove all site templates associated to provided project ids list. | 
 **body** | **list[int]**| Array of project ids that you want to detach from site template. | 

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

