# coding: utf-8

"""
    JumpCloud Directory API

    Allow cusotmers to manage the JumpCloud Directory objects, groupings and mappings.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PoliciesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete(self, id, **kwargs):
        """
        Deletes a Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy object. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_with_http_info(id, **kwargs)
            return data

    def delete_with_http_info(self, id, **kwargs):
        """
        Deletes a Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy object. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")


        collection_formats = {}

        resource_path = '/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def policies_get(self, id, **kwargs):
        """
        Gets a specific Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policies_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy object. (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.policies_get_with_http_info(id, **kwargs)
        else:
            (data) = self.policies_get_with_http_info(id, **kwargs)
            return data

    def policies_get_with_http_info(self, id, **kwargs):
        """
        Gets a specific Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policies_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy object. (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `policies_get`")


        collection_formats = {}

        resource_path = '/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def policies_list(self, **kwargs):
        """
        Lists all the policies.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policies_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param str filter: 
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.policies_list_with_http_info(**kwargs)
        else:
            (data) = self.policies_list_with_http_info(**kwargs)
            return data

    def policies_list_with_http_info(self, **kwargs):
        """
        Lists all the policies.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policies_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param str filter: 
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'skip', 'sort', 'fields', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policies_list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/policies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'skip' in params:
            query_params['skip'] = params['skip']
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'filter' in params:
            query_params['filter'] = params['filter']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Policy]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def policies_post(self, body, **kwargs):
        """
        Create a new Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policies_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Policy body: (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.policies_post_with_http_info(body, **kwargs)
        else:
            (data) = self.policies_post_with_http_info(body, **kwargs)
            return data

    def policies_post_with_http_info(self, body, **kwargs):
        """
        Create a new Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policies_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Policy body: (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policies_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `policies_post`")


        collection_formats = {}

        resource_path = '/policies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def policytemplates_id_get(self, id, **kwargs):
        """
        Get a specific Policy Template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policytemplates_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy Template. (required)
        :return: PolicyTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.policytemplates_id_get_with_http_info(id, **kwargs)
        else:
            (data) = self.policytemplates_id_get_with_http_info(id, **kwargs)
            return data

    def policytemplates_id_get_with_http_info(self, id, **kwargs):
        """
        Get a specific Policy Template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policytemplates_id_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy Template. (required)
        :return: PolicyTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policytemplates_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `policytemplates_id_get`")


        collection_formats = {}

        resource_path = '/policytemplates/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PolicyTemplate',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def policytemplates_list(self, **kwargs):
        """
        Lists all of the policy templates.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policytemplates_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param str filter: 
        :return: list[PolicyTemplate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.policytemplates_list_with_http_info(**kwargs)
        else:
            (data) = self.policytemplates_list_with_http_info(**kwargs)
            return data

    def policytemplates_list_with_http_info(self, **kwargs):
        """
        Lists all of the policy templates.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policytemplates_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param str filter: 
        :return: list[PolicyTemplate]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'skip', 'sort', 'fields', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policytemplates_list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/policytemplates'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'skip' in params:
            query_params['skip'] = params['skip']
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'filter' in params:
            query_params['filter'] = params['filter']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[PolicyTemplate]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, id, body, **kwargs):
        """
        Update an existing Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy object. (required)
        :param Policy body: (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(id, body, **kwargs)
        else:
            (data) = self.update_with_http_info(id, body, **kwargs)
            return data

    def update_with_http_info(self, id, body, **kwargs):
        """
        Update an existing Policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ObjectID of the Policy object. (required)
        :param Policy body: (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update`")


        collection_formats = {}

        resource_path = '/policies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Policy',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)