# coding: utf-8

"""
    qTest Manager API Version 11.0.0 - 2023.6

    qTest Manager API Version 11.0.0 - 2023.6  # noqa: E501

    OpenAPI spec version: 11.0.0 - 2023.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WebhookApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_webhook(self, body, **kwargs):  # noqa: E501
        """Registers a webhook  # noqa: E501

        To register a webhook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebhookRequest body: <em>name (required):</em> name of the webhook  <em>URL (required):</em> where the callback should be sent  <em>secretkey (required):</em> secretkey is used to ensure that POST requests sent to the URL are from qTest  <em>responseType (optional):</em> content-type of the callback message. Allow values: \"text\" for <b>text/plain</b>, \"json\" for <b>application/json</b>. Default value is \"text\"  <em>events (required):</em> list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  <em>projectIds (optional):</em> list valid projectid(s) to register. Its valid values include only Active Projects (required)
        :return: WebhookVM
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_webhook_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_webhook_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_webhook_with_http_info(self, body, **kwargs):  # noqa: E501
        """Registers a webhook  # noqa: E501

        To register a webhook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebhookRequest body: <em>name (required):</em> name of the webhook  <em>URL (required):</em> where the callback should be sent  <em>secretkey (required):</em> secretkey is used to ensure that POST requests sent to the URL are from qTest  <em>responseType (optional):</em> content-type of the callback message. Allow values: \"text\" for <b>text/plain</b>, \"json\" for <b>application/json</b>. Default value is \"text\"  <em>events (required):</em> list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  <em>projectIds (optional):</em> list valid projectid(s) to register. Its valid values include only Active Projects (required)
        :return: WebhookVM
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookVM',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_webhook_by_id(self, webhook_id, **kwargs):  # noqa: E501
        """Deletes a webhook  # noqa: E501

        To delete a registered webhook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_webhook_by_id(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: ID of the webhook (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_webhook_by_id_with_http_info(webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_webhook_by_id_with_http_info(webhook_id, **kwargs)  # noqa: E501
            return data

    def delete_webhook_by_id_with_http_info(self, webhook_id, **kwargs):  # noqa: E501
        """Deletes a webhook  # noqa: E501

        To delete a registered webhook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_webhook_by_id_with_http_info(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: ID of the webhook (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhook_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_id' is set
        if self.api_client.client_side_validation and ('webhook_id' not in params or
                                                       params['webhook_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `webhook_id` when calling `delete_webhook_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/webhooks/{webhookId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_event_names(self, **kwargs):  # noqa: E501
        """Get list of webhook event names  # noqa: E501

        To retrieve list of all available event names for webhook registering  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_event_names(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_event_names_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_event_names_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_event_names_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of webhook event names  # noqa: E501

        To retrieve list of all available event names for webhook registering  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_event_names_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_event_names" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/webhooks/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_webhooks(self, **kwargs):  # noqa: E501
        """Gets list of all registered webhooks  # noqa: E501

        To retrieve list of all registered webhooks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_webhooks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[WebhookVM]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_webhooks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_webhooks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_webhooks_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of all registered webhooks  # noqa: E501

        To retrieve list of all registered webhooks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_webhooks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[WebhookVM]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_webhooks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WebhookVM]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_webhook_by_id(self, webhook_id, **kwargs):  # noqa: E501
        """Gets a webhook  # noqa: E501

        To retrieve details of a registered webhook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webhook_by_id(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: ID of the webhook (required)
        :return: WebhookVM
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_webhook_by_id_with_http_info(webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_webhook_by_id_with_http_info(webhook_id, **kwargs)  # noqa: E501
            return data

    def get_webhook_by_id_with_http_info(self, webhook_id, **kwargs):  # noqa: E501
        """Gets a webhook  # noqa: E501

        To retrieve details of a registered webhook  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webhook_by_id_with_http_info(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: ID of the webhook (required)
        :return: WebhookVM
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_id' is set
        if self.api_client.client_side_validation and ('webhook_id' not in params or
                                                       params['webhook_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `webhook_id` when calling `get_webhook_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/webhooks/{webhookId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookVM',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_webhook(self, webhook_id, body, **kwargs):  # noqa: E501
        """Updates a webhook  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_webhook(webhook_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: ID of the webhook (required)
        :param WebhookRequest body: Update webhook's information  <em>name:</em> New name of the webhook  <em>URL:</em> New URL of the webhook  <em>secretkey:</em> New secret key of the webhook  <em>responseType:</em> New content-type of the callback message. Allow values: \"text\" for <b>text/plain</b>, \"json\" for <b>application/json</b>  <em>events (required):</em> New list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  <em>projectIds (optional):</em> list valid projectid(s) to register. Its valid values include only Active Projects (required)
        :return: WebhookVM
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_webhook_with_http_info(webhook_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_webhook_with_http_info(webhook_id, body, **kwargs)  # noqa: E501
            return data

    def update_webhook_with_http_info(self, webhook_id, body, **kwargs):  # noqa: E501
        """Updates a webhook  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_webhook_with_http_info(webhook_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: ID of the webhook (required)
        :param WebhookRequest body: Update webhook's information  <em>name:</em> New name of the webhook  <em>URL:</em> New URL of the webhook  <em>secretkey:</em> New secret key of the webhook  <em>responseType:</em> New content-type of the callback message. Allow values: \"text\" for <b>text/plain</b>, \"json\" for <b>application/json</b>  <em>events (required):</em> New list event(s) to register. Its valid values include  - testcase_created  - testcase_updated  - testcase_deleted  - testcase_approved  - testrun_created  - testrun_updated  - testrun_deleted  - testlog_submitted  - testlog_modified  - project_created  - project_updated  - defect_submitted  - defect_modified  - requirement_created  - requirement_updated  - requirement_deleted  - requirement_linked  - requirement_unlinked  - defect_linked  - defect_unlinked  <em>projectIds (optional):</em> list valid projectid(s) to register. Its valid values include only Active Projects (required)
        :return: WebhookVM
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_id' is set
        if self.api_client.client_side_validation and ('webhook_id' not in params or
                                                       params['webhook_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `webhook_id` when calling `update_webhook`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/webhooks/{webhookId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookVM',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
