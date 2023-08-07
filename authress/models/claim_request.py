# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, constr

class ClaimRequest(BaseModel):
    """
    ClaimRequest
    """
    collection_resource: constr(strict=True, max_length=128, min_length=1) = Field(..., alias="collectionResource", description="The parent resource to add a sub-resource to. The resource must have a resource configuration that add the permission CLAIM for this to work.")
    resource_id: constr(strict=True, max_length=128, min_length=1) = Field(..., alias="resourceId", description="The sub-resource the user is requesting Admin ownership over.")
    __properties = ["collectionResource", "resourceId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ClaimRequest:
        """Create an instance of ClaimRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClaimRequest:
        """Create an instance of ClaimRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClaimRequest.parse_obj(obj)

        _obj = ClaimRequest.parse_obj({
            "collection_resource": obj.get("collectionResource"),
            "resource_id": obj.get("resourceId")
        })
        return _obj


