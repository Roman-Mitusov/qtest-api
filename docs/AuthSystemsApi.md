# swagger_client.AuthSystemsApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all**](AuthSystemsApi.md#get_all) | **GET** /api/v3/auth-systems | Get multiple Authentication Systems
[**get_all_ldap_users**](AuthSystemsApi.md#get_all_ldap_users) | **GET** /api/v3/auth-systems/ldap/{ldapAuthConfigId}/users | Get all LDAP users of an authentication LDAP config
[**import_l_dap_users**](AuthSystemsApi.md#import_l_dap_users) | **POST** /api/v3/auth-systems/ldap/{ldapAuthConfigId}/import | Associate Manager users with LDAP users


# **get_all**
> AuthSystemResponse get_all()

Get multiple Authentication Systems

To get multiple Authentication Systems

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
api_instance = swagger_client.AuthSystemsApi(swagger_client.ApiClient(configuration))

try:
    # Get multiple Authentication Systems
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSystemsApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthSystemResponse**](AuthSystemResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ldap_users**
> LDAPUsersResponse get_all_ldap_users(ldap_auth_config_id, page_size=page_size, page=page)

Get all LDAP users of an authentication LDAP config

Get all LDAP users of an authentication LDAP config with pagination supported. Users are mapped with qTest users won't be returned.  If <strong>pageSize</strong> and <strong>page</strong> is omitted, all users will be returned without any default paging data.

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
api_instance = swagger_client.AuthSystemsApi(swagger_client.ApiClient(configuration))
ldap_auth_config_id = 789 # int | Id of the Authentication config
page_size = 100 # int | Number of of item count per page. If this <strong>pageSize</strong> and <strong>page</strong> is omitted, all users will be returned without any default paging data. (optional) (default to 100)
page = 1 # int | Page number that you want to get the result. If this <strong>pageSize</strong> and <strong>page</strong> is omitted, all users will be returned without any default paging data. (optional) (default to 1)

try:
    # Get all LDAP users of an authentication LDAP config
    api_response = api_instance.get_all_ldap_users(ldap_auth_config_id, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSystemsApi->get_all_ldap_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_auth_config_id** | **int**| Id of the Authentication config | 
 **page_size** | **int**| Number of of item count per page. If this &lt;strong&gt;pageSize&lt;/strong&gt; and &lt;strong&gt;page&lt;/strong&gt; is omitted, all users will be returned without any default paging data. | [optional] [default to 100]
 **page** | **int**| Page number that you want to get the result. If this &lt;strong&gt;pageSize&lt;/strong&gt; and &lt;strong&gt;page&lt;/strong&gt; is omitted, all users will be returned without any default paging data. | [optional] [default to 1]

### Return type

[**LDAPUsersResponse**](LDAPUsersResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_l_dap_users**
> ResponseWrapper import_l_dap_users(ldap_auth_config_id, body, merge_user=merge_user)

Associate Manager users with LDAP users

Associate Manager users with LDAP users authentication LDAP config

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
api_instance = swagger_client.AuthSystemsApi(swagger_client.ApiClient(configuration))
ldap_auth_config_id = 789 # int | Id of the Authentication config
body = [swagger_client.LdapUserResource()] # list[LdapUserResource] | 
merge_user = true # bool | Option to merge LDAP account to qTest account if qTest email already exists in qTest (support true/false value, <strong>default = false</strong>) (optional)

try:
    # Associate Manager users with LDAP users
    api_response = api_instance.import_l_dap_users(ldap_auth_config_id, body, merge_user=merge_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSystemsApi->import_l_dap_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_auth_config_id** | **int**| Id of the Authentication config | 
 **body** | [**list[LdapUserResource]**](LdapUserResource.md)|  | 
 **merge_user** | **bool**| Option to merge LDAP account to qTest account if qTest email already exists in qTest (support true/false value, &lt;strong&gt;default &#x3D; false&lt;/strong&gt;) | [optional] 

### Return type

[**ResponseWrapper**](ResponseWrapper.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

