# coding: utf-8

# flake8: noqa
"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from authress.models.access_record import AccessRecord
from authress.models.access_record_account import AccessRecordAccount
from authress.models.access_record_collection import AccessRecordCollection
from authress.models.access_request import AccessRequest
from authress.models.access_request_collection import AccessRequestCollection
from authress.models.access_request_response import AccessRequestResponse
from authress.models.access_template import AccessTemplate
from authress.models.account import Account
from authress.models.account_collection import AccountCollection
from authress.models.account_links import AccountLinks
from authress.models.application_delegation import ApplicationDelegation
from authress.models.claim_request import ClaimRequest
from authress.models.client import Client
from authress.models.client_access_key import ClientAccessKey
from authress.models.client_collection import ClientCollection
from authress.models.client_options import ClientOptions
from authress.models.client_rate_limit import ClientRateLimit
from authress.models.collection_links import CollectionLinks
from authress.models.connection import Connection
from authress.models.connection_collection import ConnectionCollection
from authress.models.connection_conditions import ConnectionConditions
from authress.models.connection_data import ConnectionData
from authress.models.connection_default_connection_properties import ConnectionDefaultConnectionProperties
from authress.models.connection_linking_configuration import ConnectionLinkingConfiguration
from authress.models.connection_user_data_configuration import ConnectionUserDataConfiguration
from authress.models.extension import Extension
from authress.models.extension_application import ExtensionApplication
from authress.models.extension_client import ExtensionClient
from authress.models.extension_collection import ExtensionCollection
from authress.models.group import Group
from authress.models.group_collection import GroupCollection
from authress.models.identity import Identity
from authress.models.identity_collection import IdentityCollection
from authress.models.identity_request import IdentityRequest
from authress.models.invite import Invite
from authress.models.invite_statement import InviteStatement
from authress.models.link import Link
from authress.models.linked_group import LinkedGroup
from authress.models.links import Links
from authress.models.o_auth_authorize_response import OAuthAuthorizeResponse
from authress.models.o_auth_token_request import OAuthTokenRequest
from authress.models.o_auth_token_response import OAuthTokenResponse
from authress.models.pagination import Pagination
from authress.models.pagination_next import PaginationNext
from authress.models.permission_collection import PermissionCollection
from authress.models.permission_collection_account import PermissionCollectionAccount
from authress.models.permission_object import PermissionObject
from authress.models.permissioned_resource import PermissionedResource
from authress.models.permissioned_resource_collection import PermissionedResourceCollection
from authress.models.resource import Resource
from authress.models.resource_permission import ResourcePermission
from authress.models.resource_users_collection import ResourceUsersCollection
from authress.models.role import Role
from authress.models.role_collection import RoleCollection
from authress.models.statement import Statement
from authress.models.tenant import Tenant
from authress.models.tenant_collection import TenantCollection
from authress.models.tenant_connection import TenantConnection
from authress.models.tenant_data import TenantData
from authress.models.tenant_domain import TenantDomain
from authress.models.tenant_user import TenantUser
from authress.models.token_request import TokenRequest
from authress.models.user import User
from authress.models.user_connection_credentials import UserConnectionCredentials
from authress.models.user_identity import UserIdentity
from authress.models.user_identity_collection import UserIdentityCollection
from authress.models.user_resources_collection import UserResourcesCollection
from authress.models.user_role import UserRole
from authress.models.user_role_collection import UserRoleCollection
from authress.models.user_token import UserToken
