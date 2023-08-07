# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import authress
from authress.models.user_token import UserToken  # noqa: E501
from authress.rest import ApiException

class TestUserToken(unittest.TestCase):
    """UserToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserToken`
        """
        model = authress.models.user_token.UserToken()  # noqa: E501
        if include_optional :
            return UserToken(
                account = authress.models.permission_collection_account.PermissionCollection_account(
                    account_id = '', ), 
                user_id = None, 
                token_id = '', 
                token = '', 
                links = authress.models.account_links.Account_links(
                    self = authress.models.link.Link(
                        href = '', 
                        rel = '', ), )
            )
        else :
            return UserToken(
                user_id = None,
                token_id = '',
                token = '',
        )
        """

    def testUserToken(self):
        """Test UserToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()