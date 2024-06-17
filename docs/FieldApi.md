# swagger_client.FieldApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](FieldApi.md#create_custom_field) | **POST** /api/v3/projects/{projectId}/settings/{objectType}/fields | Creates a Custom Field of an Object Type
[**create_custom_site_field**](FieldApi.md#create_custom_site_field) | **POST** /api/v3/fields/{objectType} | Creates a Custom Site Field of an Object Type
[**create_project_field_allowed_values**](FieldApi.md#create_project_field_allowed_values) | **POST** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId}/allowed-values | Creates allowed values of a Project Field
[**create_site_field_allowed_values**](FieldApi.md#create_site_field_allowed_values) | **POST** /api/v3/fields/{objectType}/{fieldId}/allowed-values | Creates allowed values of a Site Field
[**delete_custom_field**](FieldApi.md#delete_custom_field) | **DELETE** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId} | Deletes a Custom Field of an Object Type
[**delete_custom_site_field**](FieldApi.md#delete_custom_site_field) | **DELETE** /api/v3/fields/{objectType}/{fieldId} | Deletes a Custom Site Field of an Object Type
[**delete_project_field_value**](FieldApi.md#delete_project_field_value) | **DELETE** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId}/allowed-values/{value} | Deletes an allowed value of a Project Field
[**delete_site_field_value**](FieldApi.md#delete_site_field_value) | **DELETE** /api/v3/fields/{objectType}/{fieldId}/allowed-values/{value} | Deletes an allowed value of a Site Field
[**get_all_site_fields**](FieldApi.md#get_all_site_fields) | **GET** /api/v3/fields/{objectType} | Gets all site field of an object type
[**get_custom_field**](FieldApi.md#get_custom_field) | **GET** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId} | Gets a Custom Field of an Object Type
[**get_custom_site_field**](FieldApi.md#get_custom_site_field) | **GET** /api/v3/fields/{objectType}/{fieldId} | Gets a Custom Site Field of an Object Type
[**get_fields**](FieldApi.md#get_fields) | **GET** /api/v3/projects/{projectId}/settings/{objectType}/fields | Gets all Fields of an Object Type
[**get_project_field_allowed_values**](FieldApi.md#get_project_field_allowed_values) | **GET** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId}/allowed-values | Gets all allowed values of a Project Field
[**get_site_field_allowed_values**](FieldApi.md#get_site_field_allowed_values) | **GET** /api/v3/fields/{objectType}/{fieldId}/allowed-values | Gets all allowed values of a Site Field
[**update_custom_field**](FieldApi.md#update_custom_field) | **PUT** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId} | Updates a Custom Field of an Object Type
[**update_custom_site_field**](FieldApi.md#update_custom_site_field) | **PUT** /api/v3/fields/{objectType}/{fieldId} | Updates a Custom Site Field of an Object Type
[**update_project_field_allowed_values**](FieldApi.md#update_project_field_allowed_values) | **PUT** /api/v3/projects/{projectId}/settings/{objectType}/fields/{fieldId}/allowed-values/{value} | Updates an allowed value of a Project Field
[**update_site_field_allowed_values**](FieldApi.md#update_site_field_allowed_values) | **PUT** /api/v3/fields/{objectType}/{fieldId}/allowed-values/{value} | Updates an allowed value of a Site Field


# **create_custom_field**
> FieldResource create_custom_field(project_id, body, object_type)

Creates a Custom Field of an Object Type

To create a new custom Field for Release, Build, Requirement, Test Case, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.FieldResource() # FieldResource | The field's properties and values  <strong>data_type (required):</strong> specify the field type. Its valid values include  - 1 - Text box  - 2 - Text area  - 3 - Combo box  - 4 - Date picker  - 5 - User list  - 6 - Rich text editor  - 7 - Number  - 8 - Check box  - 9 - Date time picker  - 12 - URL  - 17 - Multiple selection combobox  In case you are creating a multiple picklist typed field (data_type's value is 8 or 17), you will need to specify <em>multiple=true</em>  In case you are creating a picklist typed field, you can specify the field's values in the <em>allowed_values</em> array
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs

try:
    # Creates a Custom Field of an Object Type
    api_response = api_instance.create_custom_field(project_id, body, object_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->create_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**FieldResource**](FieldResource.md)| The field&#39;s properties and values  &lt;strong&gt;data_type (required):&lt;/strong&gt; specify the field type. Its valid values include  - 1 - Text box  - 2 - Text area  - 3 - Combo box  - 4 - Date picker  - 5 - User list  - 6 - Rich text editor  - 7 - Number  - 8 - Check box  - 9 - Date time picker  - 12 - URL  - 17 - Multiple selection combobox  In case you are creating a multiple picklist typed field (data_type&#39;s value is 8 or 17), you will need to specify &lt;em&gt;multiple&#x3D;true&lt;/em&gt;  In case you are creating a picklist typed field, you can specify the field&#39;s values in the &lt;em&gt;allowed_values&lt;/em&gt; array | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 

### Return type

[**FieldResource**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_site_field**
> FieldResource create_custom_site_field(object_type, body)

Creates a Custom Site Field of an Object Type

To create a new Site Field for Release, Build, Requirement, Test Case, Test Step, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
body = swagger_client.FieldInputResource() # FieldInputResource | The Site field's properties and values  <strong>label (required)</strong>: specify display name of the field  <strong>data_type (required)</strong>: specify the field type. Its valid values include  - 1 - Text box  - 2 - Text area  - 3 - Combo box  - 4 - Date picker  - 5 - User list  - 6 - Rich text editor  - 7 - Number  - 8 - Check box  - 9 - Date time picker  - 12 - URL  - 17 - Multiple selection combobox  In case you are creating a multiple picklist typed field (data_type's value is 8 or 17), you will need to specify <em>multiple=true</em>  In case you are creating a picklist typed field, you can specify the field's values in the <em>allowed_values array</em>  Order is not applicable when creating new field  For Test Steps,  - You can not create more than 2 custom fields   - You can not set field as required   - Number of characters in label should be less than or equal to 16   - You can only select Rich text editor / Combo Box / User List as <em>data_type</em> 

try:
    # Creates a Custom Site Field of an Object Type
    api_response = api_instance.create_custom_site_field(object_type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->create_custom_site_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **body** | [**FieldInputResource**](FieldInputResource.md)| The Site field&#39;s properties and values  &lt;strong&gt;label (required)&lt;/strong&gt;: specify display name of the field  &lt;strong&gt;data_type (required)&lt;/strong&gt;: specify the field type. Its valid values include  - 1 - Text box  - 2 - Text area  - 3 - Combo box  - 4 - Date picker  - 5 - User list  - 6 - Rich text editor  - 7 - Number  - 8 - Check box  - 9 - Date time picker  - 12 - URL  - 17 - Multiple selection combobox  In case you are creating a multiple picklist typed field (data_type&#39;s value is 8 or 17), you will need to specify &lt;em&gt;multiple&#x3D;true&lt;/em&gt;  In case you are creating a picklist typed field, you can specify the field&#39;s values in the &lt;em&gt;allowed_values array&lt;/em&gt;  Order is not applicable when creating new field  For Test Steps,  - You can not create more than 2 custom fields   - You can not set field as required   - Number of characters in label should be less than or equal to 16   - You can only select Rich text editor / Combo Box / User List as &lt;em&gt;data_type&lt;/em&gt;  | 

### Return type

[**FieldResource**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_field_allowed_values**
> AllowedValueResponseResource create_project_field_allowed_values(project_id, object_type, field_id, body)

Creates allowed values of a Project Field

Creates maximum 100 allowed values of a Project Field with Combo box/Multi selection combo box/Check box data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
body = [swagger_client.AllowedValueResource()] # list[AllowedValueResource] | 

try:
    # Creates allowed values of a Project Field
    api_response = api_instance.create_project_field_allowed_values(project_id, object_type, field_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->create_project_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **body** | [**list[AllowedValueResource]**](AllowedValueResource.md)|  | 

### Return type

[**AllowedValueResponseResource**](AllowedValueResponseResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_field_allowed_values**
> AllowedValueResponseResource create_site_field_allowed_values(object_type, field_id, body)

Creates allowed values of a Site Field

Creates maximum 100 allowed values of a Site Field with Combo box/Multi selection combo box/Check box data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
body = [swagger_client.AllowedValueResource()] # list[AllowedValueResource] | 

try:
    # Creates allowed values of a Site Field
    api_response = api_instance.create_site_field_allowed_values(object_type, field_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->create_site_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **body** | [**list[AllowedValueResource]**](AllowedValueResource.md)|  | 

### Return type

[**AllowedValueResponseResource**](AllowedValueResponseResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> object delete_custom_field(project_id, object_type, field_id)

Deletes a Custom Field of an Object Type

To delete a custom field (at project level) for Release, Build, Requirement, Test Case, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs
field_id = 789 # int | ID of the custom field

try:
    # Deletes a Custom Field of an Object Type
    api_response = api_instance.delete_custom_field(project_id, object_type, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->delete_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the custom field | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_site_field**
> object delete_custom_site_field(object_type, field_id)

Deletes a Custom Site Field of an Object Type

To delete a custom field (at site level) for Release, Build, Requirement, Test Case, Test Step, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the custom field

try:
    # Deletes a Custom Site Field of an Object Type
    api_response = api_instance.delete_custom_site_field(object_type, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->delete_custom_site_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the custom field | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_field_value**
> object delete_project_field_value(project_id, object_type, field_id, value)

Deletes an allowed value of a Project Field

To delete an allowed value of a Field (at project level) with Combo box/Multi selection combo box/Check box data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
value = 789 # int | ID (property \"value\") of allowed value

try:
    # Deletes an allowed value of a Project Field
    api_response = api_instance.delete_project_field_value(project_id, object_type, field_id, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->delete_project_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **value** | **int**| ID (property \&quot;value\&quot;) of allowed value | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_field_value**
> object delete_site_field_value(object_type, field_id, value)

Deletes an allowed value of a Site Field

To delete an allowed value of a Site Field with Combo box/Multi selection combo box/Check box data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
value = 789 # int | ID (property \"value\") of allowed value

try:
    # Deletes an allowed value of a Site Field
    api_response = api_instance.delete_site_field_value(object_type, field_id, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->delete_site_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **value** | **int**| ID (property \&quot;value\&quot;) of allowed value | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_site_fields**
> FieldResourceSwagger get_all_site_fields(object_type, page=page, page_size=page_size)

Gets all site field of an object type

To get all fields (at site level) for Release, Build, Requirement, Test Case, Test Step, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Gets all site field of an object type
    api_response = api_instance.get_all_site_fields(object_type, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_all_site_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**FieldResourceSwagger**](FieldResourceSwagger.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> FieldResourceSwagger get_custom_field(project_id, object_type, field_id)

Gets a Custom Field of an Object Type

To get a custom field (at project level) for Release, Build, Requirement, Test Case, Test Step, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the custom field

try:
    # Gets a Custom Field of an Object Type
    api_response = api_instance.get_custom_field(project_id, object_type, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the custom field | 

### Return type

[**FieldResourceSwagger**](FieldResourceSwagger.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_site_field**
> FieldResourceSwagger get_custom_site_field(object_type, field_id)

Gets a Custom Site Field of an Object Type

To get a custom field (at site level) for Release, Build, Requirement, Test Case, Test Step, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the custom field

try:
    # Gets a Custom Site Field of an Object Type
    api_response = api_instance.get_custom_site_field(object_type, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_custom_site_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the custom field | 

### Return type

[**FieldResourceSwagger**](FieldResourceSwagger.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> list[FieldResource] get_fields(project_id, object_type, include_inactive=include_inactive)

Gets all Fields of an Object Type

To retrieve Fields of an Object Type  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
include_inactive = true # bool | By default inactive Fields are excluded from the response. Specify <em>includeInactive=true</em> to include inactive fields (optional)

try:
    # Gets all Fields of an Object Type
    api_response = api_instance.get_fields(project_id, object_type, include_inactive=include_inactive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **include_inactive** | **bool**| By default inactive Fields are excluded from the response. Specify &lt;em&gt;includeInactive&#x3D;true&lt;/em&gt; to include inactive fields | [optional] 

### Return type

[**list[FieldResource]**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_field_allowed_values**
> list[AllowedValueResource] get_project_field_allowed_values(project_id, object_type, field_id, page=page, page_size=page_size)

Gets all allowed values of a Project Field

To get all allowed values of a Project Field with Combo box/Multi selection combo box/Check box/User list data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Gets all allowed values of a Project Field
    api_response = api_instance.get_project_field_allowed_values(project_id, object_type, field_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_project_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**list[AllowedValueResource]**](AllowedValueResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_field_allowed_values**
> list[AllowedValueResource] get_site_field_allowed_values(object_type, field_id, page=page, page_size=page_size)

Gets all allowed values of a Site Field

To get all allowed values of a Site Field with Combo box/Multi selection combo box/Check box/User list data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Gets all allowed values of a Site Field
    api_response = api_instance.get_site_field_allowed_values(object_type, field_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_site_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**list[AllowedValueResource]**](AllowedValueResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> FieldResource update_custom_field(project_id, object_type, field_id, body)

Updates a Custom Field of an Object Type

To update a custom field (at project level) for Release, Build, Requirement, Test Case, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs
field_id = 789 # int | ID of the custom field
body = swagger_client.FieldInputResource() # FieldInputResource | The Field's updated properties & values  Notes:  - Not allow to update <strong>data_type</strong>  - To delete a value of a Combo box/Checkbox or Multiple selection combo box, exclude that value out of \"allowed_values\"  - To add more allowed_values for Project Field, refer [here](#/field/createProjectFieldAllowedValues)   - To update list allowed_values of Project Field, refer [here](#/field/updateProjectFieldAllowedValues)

try:
    # Updates a Custom Field of an Object Type
    api_response = api_instance.update_custom_field(project_id, object_type, field_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the custom field | 
 **body** | [**FieldInputResource**](FieldInputResource.md)| The Field&#39;s updated properties &amp; values  Notes:  - Not allow to update &lt;strong&gt;data_type&lt;/strong&gt;  - To delete a value of a Combo box/Checkbox or Multiple selection combo box, exclude that value out of \&quot;allowed_values\&quot;  - To add more allowed_values for Project Field, refer [here](#/field/createProjectFieldAllowedValues)   - To update list allowed_values of Project Field, refer [here](#/field/updateProjectFieldAllowedValues) | 

### Return type

[**FieldResource**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_site_field**
> FieldResource update_custom_site_field(object_type, field_id, body)

Updates a Custom Site Field of an Object Type

To update a custom field (at site level) for Release, Build, Requirement, Test Case, Test Step, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the custom field
body = swagger_client.FieldInputResource() # FieldInputResource | The Site Field's updated properties & values  Notes:  - Not allow to update <strong>data_type</strong>  - To delete a value of a Combo box/Checkbox or Multiple selection combo box, exclude that value out of \"allowed_values\"  - To add more allowed_values for Site Field, refer [here](#/field/createSiteFieldAllowedValues)  - To update list allowed_values of Site Field, refer [here](#/field/updateSiteFieldAllowedValues)  - Can not set field as required for test steps  - Number of characters in label should be less than or equal to 16 for test steps

try:
    # Updates a Custom Site Field of an Object Type
    api_response = api_instance.update_custom_site_field(object_type, field_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->update_custom_site_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the custom field | 
 **body** | [**FieldInputResource**](FieldInputResource.md)| The Site Field&#39;s updated properties &amp; values  Notes:  - Not allow to update &lt;strong&gt;data_type&lt;/strong&gt;  - To delete a value of a Combo box/Checkbox or Multiple selection combo box, exclude that value out of \&quot;allowed_values\&quot;  - To add more allowed_values for Site Field, refer [here](#/field/createSiteFieldAllowedValues)  - To update list allowed_values of Site Field, refer [here](#/field/updateSiteFieldAllowedValues)  - Can not set field as required for test steps  - Number of characters in label should be less than or equal to 16 for test steps | 

### Return type

[**FieldResource**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_field_allowed_values**
> object update_project_field_allowed_values(project_id, object_type, field_id, value, body)

Updates an allowed value of a Project Field

Update allowed values of a Project Field with Combo box/Multi selection combo box/Check box data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
value = 789 # int | ID (property \"value\") of allowed value
body = swagger_client.AllowedValueInputResource() # AllowedValueInputResource | 

try:
    # Updates an allowed value of a Project Field
    api_response = api_instance.update_project_field_allowed_values(project_id, object_type, field_id, value, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->update_project_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **value** | **int**| ID (property \&quot;value\&quot;) of allowed value | 
 **body** | [**AllowedValueInputResource**](AllowedValueInputResource.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_field_allowed_values**
> ResourceSupport update_site_field_allowed_values(object_type, field_id, value, body)

Updates an allowed value of a Site Field

Update allowed values of a Site Field with Combo box/Multi selection combo box/Check box data type

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
api_instance = swagger_client.FieldApi(swagger_client.ApiClient(configuration))
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs
field_id = 789 # int | ID of the field
value = 789 # int | ID (property \"value\") of allowed value
body = swagger_client.AllowedValueInputResource() # AllowedValueInputResource | 

try:
    # Updates an allowed value of a Site Field
    api_response = api_instance.update_site_field_allowed_values(object_type, field_id, value, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->update_site_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-steps, defects, test-suites and test-runs | 
 **field_id** | **int**| ID of the field | 
 **value** | **int**| ID (property \&quot;value\&quot;) of allowed value | 
 **body** | [**AllowedValueInputResource**](AllowedValueInputResource.md)|  | 

### Return type

[**ResourceSupport**](ResourceSupport.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

