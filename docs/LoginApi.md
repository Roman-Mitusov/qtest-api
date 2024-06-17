# swagger_client.LoginApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_access_token**](LoginApi.md#post_access_token) | **POST** /oauth/token | Log in
[**token_status**](LoginApi.md#token_status) | **GET** /oauth/status | Gets status of access token


# **post_access_token**
> OAuthResponse post_access_token(grant_type=grant_type, username=username, password=password, refresh_token=refresh_token, authorization=authorization)

Log in

To authenticate the API client against qTest Manager and acquire authorized access token.    Note: Please choose parameter <em>content-type=application/x-www-form-urlencoded</em>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
grant_type = 'password' # str | Use <em>grant_type=password</em> or <em>grant_type=refresh_token</em> to refresh access token (optional) (default to password)
username = 'username_example' # str | Your qTest Manager username (optional)
password = 'password_example' # str | Your qTest Manager password (optional)
refresh_token = 'refresh_token_example' # str | qTest refresh token to refresh access token associate with provided refresh token (optional)
authorization = 'authorization_example' # str | Basic + [base64 string of \"<strong>your qTest site name and colon</strong>\"]  or Basic cXRlc3QtYXBpOg== [base64 string of \"<strong>qtest-api:</strong>\"] to use refresh token (grant_type = refresh_token)  Example: qTest Manager site is: apitryout.qtestnet.com then site name is: apitryout + ':', then Authorization is: Basic YXBpdHJ5b3V0Og== (optional)

try:
    # Log in
    api_response = api_instance.post_access_token(grant_type=grant_type, username=username, password=password, refresh_token=refresh_token, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->post_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Use &lt;em&gt;grant_type&#x3D;password&lt;/em&gt; or &lt;em&gt;grant_type&#x3D;refresh_token&lt;/em&gt; to refresh access token | [optional] [default to password]
 **username** | **str**| Your qTest Manager username | [optional] 
 **password** | **str**| Your qTest Manager password | [optional] 
 **refresh_token** | **str**| qTest refresh token to refresh access token associate with provided refresh token | [optional] 
 **authorization** | **str**| Basic + [base64 string of \&quot;&lt;strong&gt;your qTest site name and colon&lt;/strong&gt;\&quot;]  or Basic cXRlc3QtYXBpOg&#x3D;&#x3D; [base64 string of \&quot;&lt;strong&gt;qtest-api:&lt;/strong&gt;\&quot;] to use refresh token (grant_type &#x3D; refresh_token)  Example: qTest Manager site is: apitryout.qtestnet.com then site name is: apitryout + &#39;:&#39;, then Authorization is: Basic YXBpdHJ5b3V0Og&#x3D;&#x3D; | [optional] 

### Return type

[**OAuthResponse**](OAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_status**
> OAuthTokenStatusVM token_status(authorization=authorization)

Gets status of access token

Gets status of access token

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
api_instance = swagger_client.LoginApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | The qTest access token you want to check (optional)

try:
    # Gets status of access token
    api_response = api_instance.token_status(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->token_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| The qTest access token you want to check | [optional] 

### Return type

[**OAuthTokenStatusVM**](OAuthTokenStatusVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

