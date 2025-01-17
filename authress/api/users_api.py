# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

try:
    from pydantic.v1 import validate_arguments, ValidationError
except ImportError:
    from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

try:
    from pydantic.v1 import Field, StrictStr, conint, constr
except ImportError:
    from pydantic import Field, StrictStr, conint, constr

from typing import Optional


from authress.models.user_identity import UserIdentity
from authress.models.user_identity_collection import UserIdentityCollection

from authress.http_client import HttpClient
from authress.api_response import ApiResponse
from authress.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = HttpClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def delete_user(self, user_id : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The user identifier.")], **kwargs) -> None:  # noqa: E501
        """Delete a user  # noqa: E501

        Removes the user, all access the user has been granted through Authress access records, and any related user data. This action is completed asynchronously.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user identifier. (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_user_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_user_with_http_info(user_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_user_with_http_info(self, user_id : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The user identifier.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a user  # noqa: E501

        Removes the user, all access the user has been granted through Authress access records, and any related user data. This action is completed asynchronously.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user identifier. (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'user_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_id']:
            _path_params['userId'] = _params['user_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v1/users/{userId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_user(self, user_id : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The user identifier.")], **kwargs) -> UserIdentity:  # noqa: E501
        """Retrieve a user  # noqa: E501

        Get the user data associated with a user. The data returned by this endpoint is highly variable based on the source OAuth provider. Avoid depending on undocumented properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user identifier. (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserIdentity
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_user_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_user_with_http_info(user_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_user_with_http_info(self, user_id : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The user identifier.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve a user  # noqa: E501

        Get the user data associated with a user. The data returned by this endpoint is highly variable based on the source OAuth provider. Avoid depending on undocumented properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: The user identifier. (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UserIdentity, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_id']:
            _path_params['userId'] = _params['user_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "UserIdentity",
            '401': None,
            '403': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/v1/users/{userId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_users(self, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Max number of results to return")] = None, cursor : Annotated[Optional[StrictStr], Field(description="Continuation cursor for paging")] = None, filter : Annotated[Optional[constr(strict=True, max_length=64, min_length=0)], Field(description="Filter to search users by. This is a case insensitive search through every text field.")] = None, tenant_id : Annotated[Optional[str], Field(description="Return only users that are part of the specified tenant. Users can only be part of one tenant, using this parameter will limit returned users that have logged into this tenant.")] = None, **kwargs) -> UserIdentityCollection:  # noqa: E501
        """List users  # noqa: E501

        Returns a paginated user list for the account. The data returned by this endpoint is highly variable based on the source OAuth provider. Avoid depending on undocumented properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users(limit, cursor, filter, tenant_id, async_req=True)
        >>> result = thread.get()

        :param limit: Max number of results to return
        :type limit: int
        :param cursor: Continuation cursor for paging
        :type cursor: str
        :param filter: Filter to search users by. This is a case insensitive search through every text field.
        :type filter: str
        :param tenant_id: Return only users that are part of the specified tenant. Users can only be part of one tenant, using this parameter will limit returned users that have logged into this tenant.
        :type tenant_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserIdentityCollection
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_users_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_users_with_http_info(limit, cursor, filter, tenant_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_users_with_http_info(self, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Max number of results to return")] = None, cursor : Annotated[Optional[StrictStr], Field(description="Continuation cursor for paging")] = None, filter : Annotated[Optional[constr(strict=True, max_length=64, min_length=0)], Field(description="Filter to search users by. This is a case insensitive search through every text field.")] = None, tenant_id : Annotated[Optional[constr(strict=True, max_length=64, min_length=0)], Field(description="Return only users that are part of the specified tenant. Users can only be part of one tenant, using this parameter will limit returned users that have logged into this tenant.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List users  # noqa: E501

        Returns a paginated user list for the account. The data returned by this endpoint is highly variable based on the source OAuth provider. Avoid depending on undocumented properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users_with_http_info(limit, cursor, filter, tenant_id, async_req=True)
        >>> result = thread.get()

        :param limit: Max number of results to return
        :type limit: int
        :param cursor: Continuation cursor for paging
        :type cursor: str
        :param filter: Filter to search users by. This is a case insensitive search through every text field.
        :type filter: str
        :param tenant_id: Return only users that are part of the specified tenant. Users can only be part of one tenant, using this parameter will limit returned users that have logged into this tenant.
        :type tenant_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UserIdentityCollection, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'limit',
            'cursor',
            'filter',
            'tenant_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('cursor') is not None:  # noqa: E501
            _query_params.append(('cursor', _params['cursor']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('tenant_id') is not None:  # noqa: E501
            _query_params.append(('tenantId', _params['tenant_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/links+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "UserIdentityCollection",
            '401': None,
            '403': None,
        }

        return self.api_client.call_api(
            '/v1/users', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
