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

from datetime import datetime
from typing import List
try:
    from pydantic.v1 import BaseModel, Field, conlist
except ImportError:
    from pydantic import BaseModel, Field, conlist
from authress.models.statement import Statement

class TokenRequest(BaseModel):
    """
    TokenRequest
    """
    statements: conlist(Statement, min_items=1) = Field(..., description="A list of statements which match roles to resources. The token will have all statements apply to it.")
    expires: datetime = Field(..., description="The ISO8601 datetime when the token will expire. Default is 24 hours from now.")
    __properties = ["statements", "expires"]

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
    def from_json(cls, json_str: str) -> TokenRequest:
        """Create an instance of TokenRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in statements (list)
        _items = []
        if self.statements:
            for _item in self.statements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['statements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TokenRequest:
        """Create an instance of TokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TokenRequest.parse_obj(obj)

        _obj = TokenRequest.parse_obj({
            "statements": [Statement.from_dict(_item) for _item in obj.get("statements")] if obj.get("statements") is not None else None,
            "expires": obj.get("expires")
        })
        return _obj


