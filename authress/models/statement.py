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
    from pydantic.v1 import BaseModel, Field, conlist, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, conlist, constr, validator
from authress.models.linked_group import LinkedGroup
from authress.models.resource import Resource
from authress.models.user import User

class Statement(BaseModel):
    """
    Statement
    """
    roles: conlist(constr(strict=True, max_length=64, min_length=1), min_items=1) = Field(...)
    resources: conlist(Resource, min_items=1) = Field(...)
    users: Optional[conlist(User)] = Field(None, description="The list of users this statement applies to. Users and groups can be set at either the statement level or the record level, but not both.")
    groups: Optional[conlist(LinkedGroup)] = Field(None, description="The list of groups this statement applies to. Users in these groups will be receive access to the resources listed. Users and groups can be set at either the statement level or the record level, but not both.")
    __properties = ["roles", "resources", "users", "groups"]

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
    def from_json(cls, json_str: str) -> Statement:
        """Create an instance of Statement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Statement:
        """Create an instance of Statement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Statement.parse_obj(obj)

        _obj = Statement.parse_obj({
            "roles": obj.get("roles"),
            "resources": [Resource.from_dict(_item) for _item in obj.get("resources")] if obj.get("resources") is not None else None,
            "users": [User.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None,
            "groups": [LinkedGroup.from_dict(_item) for _item in obj.get("groups")] if obj.get("groups") is not None else None
        })
        return _obj


