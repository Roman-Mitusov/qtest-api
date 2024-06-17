# swagger_client.SearchApi

All URIs are relative to *https://apitryout.qtestnet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_histories**](SearchApi.md#query_histories) | **POST** /api/v3/projects/{projectId}/histories | Queries objects&#39; histories
[**search_artifact**](SearchApi.md#search_artifact) | **POST** /api/v3/projects/{projectId}/search | Queries objects
[**search_comment_with_query**](SearchApi.md#search_comment_with_query) | **POST** /api/v3/projects/{projectId}/comments | Queries Comments


# **query_histories**
> ArtifactHistoryResource query_histories(project_id, body, page_size=page_size, page=page)

Queries objects' histories

To query histories of Requirements, Test Cases, Test Runs and <em>internal</em> Defects  <strong>qTest Manager version:</strong> 7.6+

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.HistoryQueryParams() # HistoryQueryParams | <em>object_type (required):</em> valid values include <em>requirements</em>, <em>test-cases</em>, <em>test-runs</em>, or <em>defects</em>  <em>fields:</em> specify which object fields you want to include in the response. If you omit it or specify an asterisk (*), all fields are included  <em>object_query:</em> specify a structured query to search for qTest objects. <br/>Refer to attribute <em>query</em> in the Request Body of <em>Queries Objects</em> API  <em>query:</em> specify a structured query to retrieve histories of objects specified in attribute <em>object_query</em> above. You can use operators <em>and</em> and <em>or</em> to combine multiple criteria. Only these 2 criteria are supported:  <br/>i) <em>created:</em> it can be used for querying by updated date of the object. Its values need to be in ISO Date format. Applicable operator include: =, <>, &lt;= and >=  <br/>ii) <em>author:</em> it can be used for querying by ID of the users who made the update. Applicable operators include: = and <>
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)

try:
    # Queries objects' histories
    api_response = api_instance.query_histories(project_id, body, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->query_histories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**HistoryQueryParams**](HistoryQueryParams.md)| &lt;em&gt;object_type (required):&lt;/em&gt; valid values include &lt;em&gt;requirements&lt;/em&gt;, &lt;em&gt;test-cases&lt;/em&gt;, &lt;em&gt;test-runs&lt;/em&gt;, or &lt;em&gt;defects&lt;/em&gt;  &lt;em&gt;fields:&lt;/em&gt; specify which object fields you want to include in the response. If you omit it or specify an asterisk (*), all fields are included  &lt;em&gt;object_query:&lt;/em&gt; specify a structured query to search for qTest objects. &lt;br/&gt;Refer to attribute &lt;em&gt;query&lt;/em&gt; in the Request Body of &lt;em&gt;Queries Objects&lt;/em&gt; API  &lt;em&gt;query:&lt;/em&gt; specify a structured query to retrieve histories of objects specified in attribute &lt;em&gt;object_query&lt;/em&gt; above. You can use operators &lt;em&gt;and&lt;/em&gt; and &lt;em&gt;or&lt;/em&gt; to combine multiple criteria. Only these 2 criteria are supported:  &lt;br/&gt;i) &lt;em&gt;created:&lt;/em&gt; it can be used for querying by updated date of the object. Its values need to be in ISO Date format. Applicable operator include: &#x3D;, &lt;&gt;, &amp;lt;&#x3D; and &gt;&#x3D;  &lt;br/&gt;ii) &lt;em&gt;author:&lt;/em&gt; it can be used for querying by ID of the users who made the update. Applicable operators include: &#x3D; and &lt;&gt; | 
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]

### Return type

[**ArtifactHistoryResource**](ArtifactHistoryResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_artifact**
> PagedResource search_artifact(project_id, body, append_test_steps=append_test_steps, include_external_properties=include_external_properties, page_size=page_size, page=page)

Queries objects

This API mimics the Data Query function of qTest Manager web app. It provides the capability to query Requirements, Test Cases, Test Runs and <em>internal</em> Defects

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.ArtifactSearchParams() # ArtifactSearchParams | <em>object_type (required):</em> Its value can be <em>releases</em>, <em>requirements</em>, <em>test-cases</em>, <em>test-runs</em>, <em>test-suites</em>, <em>test-cycles</em>, <em>test-logs</em>, <em>builds</em>, or <em>defects</em>.  <em>fields:</em> specify which object fields you want to include in the response. If you omit it or specify an asterisk (*), all fields are included.  <em>query:</em> specify a structured query to search for qTest Manager objects. Basically, you can use the Query Summary text as in qTest web app for this attribute.  <strong>IMPORTANT:</strong> When using Query Summary to specify the query, you will need to modify the Query Summary in some special cases as below:  - If there are spaces in the criteria name, put it between '  ' (single quotation marks).  - There need to be spaces between a criteria, an operator, and a value.  - You can use field name or field ID in the query.  - For the fields with datetime as the data type, convert the values to ISO Date Time format.  - Operator \"IN\" for fields with datetime as the data type will search for the values within this range: inputted date time &lt;= value &lt;= (inputted date time + 23h59m59s).  - <em>Affected Release/Build:</em> You can use either Affected Release or Affected Build as criteria in a query. This criterion can be used only for <em>defects</em>.  - <em>Target Release/Build:</em> You can use either Target Release or Target Build as criteria in a query. This criterion can be used for <em>requirements</em>, <em>test-runs</em>, <em>defects</em>, <em>test-logs</em>, and <em>test-cycles</em>. Release Id should be passed as Negative value.  - <em>Fixed Release/Build:</em> You can use either Fixed Release or Fixed Build as criteria in a query. This criterion can be used only for <em>defects</em>.  - <em>Subscribers</em>: Use user ID instead of username in the query for this criteria.  - You need to use id or pid for the following fields when using them in a query: Affected Release, Affected Build, Target Release, Target Build, Fixed Release, and Fixed Build.  - Use <em>~</em> for operator <em>contains</em>, and <em>!~</em> for operator <em>not contains</em>. Eg: instead of <em>Name contains \"login\"</em>, use <em>Name ~ \"login\"</em>  - Use operator <em>is not empty</em> in the following way: <strong>is 'not empty'</strong>. Eg: \"Name is 'not empty'\"  - For builds and test-cycles, you can use the following additional criterion: <em>Created Date</em> and <em>Last Modified Date</em> in a query. Eg: 'Created Date' > '2021-05-07T03:15:37.652Z'  - For test-logs, you can use the following additional criterion: <em>Execution Start Date</em> and <em>Execution End Date</em> in a query. Eg: 'Execution Start Date' > '2021-05-07T03:15:37.652Z'
append_test_steps = true # bool |  (optional)
include_external_properties = true # bool | By default, Requirement external properties are not included in the response. Specify includeExternalProperties=true to include them. (optional)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)

try:
    # Queries objects
    api_response = api_instance.search_artifact(project_id, body, append_test_steps=append_test_steps, include_external_properties=include_external_properties, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**ArtifactSearchParams**](ArtifactSearchParams.md)| &lt;em&gt;object_type (required):&lt;/em&gt; Its value can be &lt;em&gt;releases&lt;/em&gt;, &lt;em&gt;requirements&lt;/em&gt;, &lt;em&gt;test-cases&lt;/em&gt;, &lt;em&gt;test-runs&lt;/em&gt;, &lt;em&gt;test-suites&lt;/em&gt;, &lt;em&gt;test-cycles&lt;/em&gt;, &lt;em&gt;test-logs&lt;/em&gt;, &lt;em&gt;builds&lt;/em&gt;, or &lt;em&gt;defects&lt;/em&gt;.  &lt;em&gt;fields:&lt;/em&gt; specify which object fields you want to include in the response. If you omit it or specify an asterisk (*), all fields are included.  &lt;em&gt;query:&lt;/em&gt; specify a structured query to search for qTest Manager objects. Basically, you can use the Query Summary text as in qTest web app for this attribute.  &lt;strong&gt;IMPORTANT:&lt;/strong&gt; When using Query Summary to specify the query, you will need to modify the Query Summary in some special cases as below:  - If there are spaces in the criteria name, put it between &#39;  &#39; (single quotation marks).  - There need to be spaces between a criteria, an operator, and a value.  - You can use field name or field ID in the query.  - For the fields with datetime as the data type, convert the values to ISO Date Time format.  - Operator \&quot;IN\&quot; for fields with datetime as the data type will search for the values within this range: inputted date time &amp;lt;&#x3D; value &amp;lt;&#x3D; (inputted date time + 23h59m59s).  - &lt;em&gt;Affected Release/Build:&lt;/em&gt; You can use either Affected Release or Affected Build as criteria in a query. This criterion can be used only for &lt;em&gt;defects&lt;/em&gt;.  - &lt;em&gt;Target Release/Build:&lt;/em&gt; You can use either Target Release or Target Build as criteria in a query. This criterion can be used for &lt;em&gt;requirements&lt;/em&gt;, &lt;em&gt;test-runs&lt;/em&gt;, &lt;em&gt;defects&lt;/em&gt;, &lt;em&gt;test-logs&lt;/em&gt;, and &lt;em&gt;test-cycles&lt;/em&gt;. Release Id should be passed as Negative value.  - &lt;em&gt;Fixed Release/Build:&lt;/em&gt; You can use either Fixed Release or Fixed Build as criteria in a query. This criterion can be used only for &lt;em&gt;defects&lt;/em&gt;.  - &lt;em&gt;Subscribers&lt;/em&gt;: Use user ID instead of username in the query for this criteria.  - You need to use id or pid for the following fields when using them in a query: Affected Release, Affected Build, Target Release, Target Build, Fixed Release, and Fixed Build.  - Use &lt;em&gt;~&lt;/em&gt; for operator &lt;em&gt;contains&lt;/em&gt;, and &lt;em&gt;!~&lt;/em&gt; for operator &lt;em&gt;not contains&lt;/em&gt;. Eg: instead of &lt;em&gt;Name contains \&quot;login\&quot;&lt;/em&gt;, use &lt;em&gt;Name ~ \&quot;login\&quot;&lt;/em&gt;  - Use operator &lt;em&gt;is not empty&lt;/em&gt; in the following way: &lt;strong&gt;is &#39;not empty&#39;&lt;/strong&gt;. Eg: \&quot;Name is &#39;not empty&#39;\&quot;  - For builds and test-cycles, you can use the following additional criterion: &lt;em&gt;Created Date&lt;/em&gt; and &lt;em&gt;Last Modified Date&lt;/em&gt; in a query. Eg: &#39;Created Date&#39; &gt; &#39;2021-05-07T03:15:37.652Z&#39;  - For test-logs, you can use the following additional criterion: &lt;em&gt;Execution Start Date&lt;/em&gt; and &lt;em&gt;Execution End Date&lt;/em&gt; in a query. Eg: &#39;Execution Start Date&#39; &gt; &#39;2021-05-07T03:15:37.652Z&#39; | 
 **append_test_steps** | **bool**|  | [optional] 
 **include_external_properties** | **bool**| By default, Requirement external properties are not included in the response. Specify includeExternalProperties&#x3D;true to include them. | [optional] 
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

# **search_comment_with_query**
> QueryCommentResource search_comment_with_query(project_id, body, page=page, page_size=page_size)

Queries Comments

To search for comments  <strong>qTest Manager version:</strong> 7.6+

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | ID of the project
body = swagger_client.CommentQueryParams() # CommentQueryParams | <em>object_type (required):</em> valid values include requirements, test-cases, test-runs and defects  <em>object:</em> ID of the object from which you want to retrieve comments  <em>authors:</em> ID of the user who made the comments  <em>start:</em> This value needs to be in ISO Date format  <em>end:</em> This value needs to be in ISO Date format
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try:
    # Queries Comments
    api_response = api_instance.search_comment_with_query(project_id, body, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_comment_with_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**CommentQueryParams**](CommentQueryParams.md)| &lt;em&gt;object_type (required):&lt;/em&gt; valid values include requirements, test-cases, test-runs and defects  &lt;em&gt;object:&lt;/em&gt; ID of the object from which you want to retrieve comments  &lt;em&gt;authors:&lt;/em&gt; ID of the user who made the comments  &lt;em&gt;start:&lt;/em&gt; This value needs to be in ISO Date format  &lt;em&gt;end:&lt;/em&gt; This value needs to be in ISO Date format | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**QueryCommentResource**](QueryCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

