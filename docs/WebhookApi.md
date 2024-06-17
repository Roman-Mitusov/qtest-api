# swagger_client.WebhookApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /api/v3/webhooks | Registers a webhook
[**delete_webhook_by_id**](WebhookApi.md#delete_webhook_by_id) | **DELETE** /api/v3/webhooks/{webhookId} | Deletes a webhook
[**get_all_event_names**](WebhookApi.md#get_all_event_names) | **GET** /api/v3/webhooks/events | Get list of webhook event names
[**get_all_webhooks**](WebhookApi.md#get_all_webhooks) | **GET** /api/v3/webhooks | Gets list of all registered webhooks
[**get_webhook_by_id**](WebhookApi.md#get_webhook_by_id) | **GET** /api/v3/webhooks/{webhookId} | Gets a webhook
[**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /api/v3/webhooks/{webhookId} | Updates a webhook


# **create_webhook**
> WebhookVM create_webhook(body)

Registers a webhook

To register a webhook

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookRequest() # WebhookRequest | <em>name (required):</em> name of the webhook  <em>URL (required):</em> where the callback should be sent  <em>secretkey (required):</em> secretkey is used to ensure that POST requests sent to the URL are from qTest  <em>responseType (optional):</em> content-type of the callback message. Allow values: \"text\" for <b>text/plain</b>, \"json\" for <b>application/json</b>. Default value is \"text\"  <em>events (required):</em> list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  <em>projectIds (optional):</em> list valid projectid(s) to register. Its valid values include only Active Projects

try:
    # Registers a webhook
    api_response = api_instance.create_webhook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookRequest**](WebhookRequest.md)| &lt;em&gt;name (required):&lt;/em&gt; name of the webhook  &lt;em&gt;URL (required):&lt;/em&gt; where the callback should be sent  &lt;em&gt;secretkey (required):&lt;/em&gt; secretkey is used to ensure that POST requests sent to the URL are from qTest  &lt;em&gt;responseType (optional):&lt;/em&gt; content-type of the callback message. Allow values: \&quot;text\&quot; for &lt;b&gt;text/plain&lt;/b&gt;, \&quot;json\&quot; for &lt;b&gt;application/json&lt;/b&gt;. Default value is \&quot;text\&quot;  &lt;em&gt;events (required):&lt;/em&gt; list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  &lt;em&gt;projectIds (optional):&lt;/em&gt; list valid projectid(s) to register. Its valid values include only Active Projects | 

### Return type

[**WebhookVM**](WebhookVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_by_id**
> object delete_webhook_by_id(webhook_id)

Deletes a webhook

To delete a registered webhook

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | ID of the webhook

try:
    # Deletes a webhook
    api_response = api_instance.delete_webhook_by_id(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_webhook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| ID of the webhook | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_event_names**
> list[str] get_all_event_names()

Get list of webhook event names

To retrieve list of all available event names for webhook registering

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))

try:
    # Get list of webhook event names
    api_response = api_instance.get_all_event_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_all_event_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_webhooks**
> list[WebhookVM] get_all_webhooks()

Gets list of all registered webhooks

To retrieve list of all registered webhooks

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))

try:
    # Gets list of all registered webhooks
    api_response = api_instance.get_all_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_all_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebhookVM]**](WebhookVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_by_id**
> WebhookVM get_webhook_by_id(webhook_id)

Gets a webhook

To retrieve details of a registered webhook

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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | ID of the webhook

try:
    # Gets a webhook
    api_response = api_instance.get_webhook_by_id(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| ID of the webhook | 

### Return type

[**WebhookVM**](WebhookVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookVM update_webhook(webhook_id, body)

Updates a webhook



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
api_instance = swagger_client.WebhookApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | ID of the webhook
body = swagger_client.WebhookRequest() # WebhookRequest | Update webhook's information  <em>name:</em> New name of the webhook  <em>URL:</em> New URL of the webhook  <em>secretkey:</em> New secret key of the webhook  <em>responseType:</em> New content-type of the callback message. Allow values: \"text\" for <b>text/plain</b>, \"json\" for <b>application/json</b>  <em>events (required):</em> New list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  <em>projectIds (optional):</em> list valid projectid(s) to register. Its valid values include only Active Projects

try:
    # Updates a webhook
    api_response = api_instance.update_webhook(webhook_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| ID of the webhook | 
 **body** | [**WebhookRequest**](WebhookRequest.md)| Update webhook&#39;s information  &lt;em&gt;name:&lt;/em&gt; New name of the webhook  &lt;em&gt;URL:&lt;/em&gt; New URL of the webhook  &lt;em&gt;secretkey:&lt;/em&gt; New secret key of the webhook  &lt;em&gt;responseType:&lt;/em&gt; New content-type of the callback message. Allow values: \&quot;text\&quot; for &lt;b&gt;text/plain&lt;/b&gt;, \&quot;json\&quot; for &lt;b&gt;application/json&lt;/b&gt;  &lt;em&gt;events (required):&lt;/em&gt; New list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  &lt;em&gt;projectIds (optional):&lt;/em&gt; list valid projectid(s) to register. Its valid values include only Active Projects | 

### Return type

[**WebhookVM**](WebhookVM.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

