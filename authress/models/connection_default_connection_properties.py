# coding: utf-8

"""
    Authress

    <p> <h2>Introduction</h2> <p>Welcome to the Authress Authorization API. <br>The Authress REST API provides the operations and resources necessary to create records, assign permissions, and verify any user in your platform.</p> <p><ul>   <li>Manage multitenant platforms and create user tenants for SSO connections.</li>   <li>Create records to assign roles and resources to grant access for users.</li>   <li>Check user access control by calling the authorization API at the right time.</li>   <li>Configure service clients to securely access services in your platform.</li> </ul></p> <p>For more in-depth scenarios check out the <a href=\"https://authress.io/knowledge-base\" target=\"_blank\">Authress knowledge base</a>.</p> </p>

    The version of the OpenAPI document: v1
    Contact: support@authress.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
try:
    from pydantic.v1 import BaseModel, Field, constr
except ImportError:
    from pydantic import BaseModel, Field, constr

class ConnectionDefaultConnectionProperties(BaseModel):
    """
    ConnectionDefaultConnectionProperties
    """
    scope: Optional[constr(strict=True, max_length=384)] = Field(default='profile email openid', description="Default OAuth scopes to use for every request (leave blank to remove scopes).")
    additional_properties: Dict[str, Any] = {}
    __properties = ["scope"]

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
    def from_json(cls, json_str: str) -> ConnectionDefaultConnectionProperties:
        """Create an instance of ConnectionDefaultConnectionProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectionDefaultConnectionProperties:
        """Create an instance of ConnectionDefaultConnectionProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectionDefaultConnectionProperties.parse_obj(obj)

        _obj = ConnectionDefaultConnectionProperties.parse_obj({
            "scope": obj.get("scope") if obj.get("scope") is not None else 'profile email openid'
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


