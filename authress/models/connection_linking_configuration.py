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


from typing import Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictStr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, validator

class ConnectionLinkingConfiguration(BaseModel):
    """
    Linking configuration enables users to connect identities from different connections together, so that they can log in with either connection.  # noqa: E501
    """
    type: Optional[StrictStr] = Field(default=None, description="Specify the type of linking supported by this connection. The default configuration is DISABLED, meaning that users cannot link their identity from one connection to another connection. Both connections must allow for linking for a link to be successful. By default linking is disabled because it comes with security implications, users can potentially use linking through malicious connections to steal identities from other users.<br><ul><li>EXPLICIT - Users can use the linking API to link accounts.</li><li>AUTOMATIC - When a user signs up with a new account, if the verified email address matches an existing account, the two accounts will be automatically linked.</li><li>Set to <code>null</code> or leave unspecified to disable identity linking.</li></ul>")
    __properties = ["type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('null', 'EXPLICIT', 'AUTOMATIC'):
            raise ValueError("must be one of enum values ('null', 'EXPLICIT', 'AUTOMATIC')")
        return value

    class Config:
        """Pydantic configuration"""
        extra = 'forbid'
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConnectionLinkingConfiguration:
        """Create an instance of ConnectionLinkingConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectionLinkingConfiguration:
        """Create an instance of ConnectionLinkingConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectionLinkingConfiguration.parse_obj(obj)

        _obj = ConnectionLinkingConfiguration.parse_obj({
            "type": obj.get("type")
        })
        return _obj


