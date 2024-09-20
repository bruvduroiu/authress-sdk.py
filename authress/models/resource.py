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



try:
    from pydantic.v1 import BaseModel, Field, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, constr, validator

class Resource(BaseModel):
    """
    Resource
    """
    resource_uri: constr(strict=True, max_length=512, min_length=1) = Field(default=..., alias="resourceUri", description="A resource path which can be top level, fully qualified, or end with a *. Parent resources imply permissions to sub-resources.")
    __properties = ["resourceUri"]

    @validator('resource_uri')
    def resource_uri_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^([*]|[\/]?((([a-zA-Z0-9-_.+=~|@]{1,128}|[*])(:([a-zA-Z0-9-_.+=~|@]{1,128}|[*]|))*)\/?){0,15}([\/][*]|[\/]|))$", value):
            raise ValueError(r"must validate the regular expression /^([*]|[\/]?((([a-zA-Z0-9-_.+=~|@]{1,128}|[*])(:([a-zA-Z0-9-_.+=~|@]{1,128}|[*]|))*)\/?){0,15}([\/][*]|[\/]|))$/")
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
    def from_json(cls, json_str: str) -> Resource:
        """Create an instance of Resource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Resource:
        """Create an instance of Resource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Resource.parse_obj(obj)

        _obj = Resource.parse_obj({
            "resource_uri": obj.get("resourceUri")
        })
        return _obj


