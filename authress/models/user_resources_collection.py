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


from typing import List, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist
from authress.models.collection_links import CollectionLinks
from authress.models.pagination import Pagination
from authress.models.permission_collection_account import PermissionCollectionAccount
from authress.models.resource import Resource

class UserResourcesCollection(BaseModel):
    """
    A collect of permissions that the user has to a resource.
    """
    account: Optional[PermissionCollectionAccount] = None
    user_id: StrictStr = Field(..., alias="userId")
    resources: Optional[conlist(Resource)] = Field(None, description="A list of the resources the user has some permission to.")
    pagination: Optional[Pagination] = None
    links: CollectionLinks = Field(...)
    __properties = ["account", "userId", "resources", "pagination", "links"]

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
    def from_json(cls, json_str: str) -> UserResourcesCollection:
        """Create an instance of UserResourcesCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserResourcesCollection:
        """Create an instance of UserResourcesCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserResourcesCollection.parse_obj(obj)

        _obj = UserResourcesCollection.parse_obj({
            "account": PermissionCollectionAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "user_id": obj.get("userId"),
            "resources": [Resource.from_dict(_item) for _item in obj.get("resources")] if obj.get("resources") is not None else None,
            "pagination": Pagination.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None,
            "links": CollectionLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None
        })
        return _obj


