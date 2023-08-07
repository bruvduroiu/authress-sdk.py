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

import authress
from authress.api.users_api import UsersApi  # noqa: E501
from authress.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = authress.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete a user  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Retrieve a user  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
