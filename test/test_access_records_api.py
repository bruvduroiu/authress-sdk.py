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
from authress.api.access_records_api import AccessRecordsApi  # noqa: E501
from authress.rest import ApiException


class TestAccessRecordsApi(unittest.TestCase):
    """AccessRecordsApi unit test stubs"""

    def setUp(self):
        self.api = authress.api.access_records_api.AccessRecordsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_claim(self):
        """Test case for create_claim

        Create resource Claim  # noqa: E501
        """
        pass

    def test_create_record(self):
        """Test case for create_record

        Create access record  # noqa: E501
        """
        pass

    def test_create_request(self):
        """Test case for create_request

        Create access request  # noqa: E501
        """
        pass

    def test_delete_record(self):
        """Test case for delete_record

        Deletes access record  # noqa: E501
        """
        pass

    def test_delete_request(self):
        """Test case for delete_request

        Deletes access request  # noqa: E501
        """
        pass

    def test_get_record(self):
        """Test case for get_record

        Retrieve access record  # noqa: E501
        """
        pass

    def test_get_records(self):
        """Test case for get_records

        List access records  # noqa: E501
        """
        pass

    def test_get_request(self):
        """Test case for get_request

        Retrieve access request  # noqa: E501
        """
        pass

    def test_get_requests(self):
        """Test case for get_requests

        List access requests  # noqa: E501
        """
        pass

    def test_respond_to_access_request(self):
        """Test case for respond_to_access_request

        Approve or deny access request  # noqa: E501
        """
        pass

    def test_update_record(self):
        """Test case for update_record

        Update access record  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
