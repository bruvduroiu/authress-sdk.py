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
from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from authress.models.connection_data import ConnectionData
from authress.models.connection_default_connection_properties import ConnectionDefaultConnectionProperties

class Connection(BaseModel):
    """
    Connection
    """
    type: Optional[StrictStr] = 'OAUTH2'
    connection_id: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="connectionId")
    authentication_url: Optional[constr(strict=True, max_length=128, min_length=1)] = Field(None, alias="authenticationUrl")
    token_url: Optional[constr(strict=True, max_length=128, min_length=1)] = Field(None, alias="tokenUrl")
    issuer_url: Optional[constr(strict=True, max_length=128, min_length=1)] = Field(None, alias="issuerUrl")
    provider_certificate: Optional[constr(strict=True, max_length=4096, min_length=1)] = Field(None, alias="providerCertificate")
    client_id: Optional[constr(strict=True, max_length=128, min_length=1)] = Field(None, alias="clientId")
    client_secret: Optional[constr(strict=True, max_length=128, min_length=1)] = Field(None, alias="clientSecret")
    data: Optional[ConnectionData] = None
    default_connection_properties: Optional[ConnectionDefaultConnectionProperties] = Field(None, alias="defaultConnectionProperties")
    created_time: Optional[datetime] = Field(None, alias="createdTime")
    tags: Optional[Dict[str, constr(strict=True, max_length=128)]] = Field(None, description="The tags associated with this resource, this property is an map. { key1: value1, key2: value2 }")
    __properties = ["type", "connectionId", "authenticationUrl", "tokenUrl", "issuerUrl", "providerCertificate", "clientId", "clientSecret", "data", "defaultConnectionProperties", "createdTime", "tags"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('OAUTH2', 'SAML2', 'WebAuthN'):
            raise ValueError("must be one of enum values ('OAUTH2', 'SAML2', 'WebAuthN')")
        return value

    @validator('connection_id')
    def connection_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9-_.:]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9-_.:]+$/")
        return value

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
    def from_json(cls, json_str: str) -> Connection:
        """Create an instance of Connection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_time",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_connection_properties
        if self.default_connection_properties:
            _dict['defaultConnectionProperties'] = self.default_connection_properties.to_dict()
        # set to None if connection_id (nullable) is None
        # and __fields_set__ contains the field
        if self.connection_id is None and "connection_id" in self.__fields_set__:
            _dict['connectionId'] = None

        # set to None if token_url (nullable) is None
        # and __fields_set__ contains the field
        if self.token_url is None and "token_url" in self.__fields_set__:
            _dict['tokenUrl'] = None

        # set to None if issuer_url (nullable) is None
        # and __fields_set__ contains the field
        if self.issuer_url is None and "issuer_url" in self.__fields_set__:
            _dict['issuerUrl'] = None

        # set to None if provider_certificate (nullable) is None
        # and __fields_set__ contains the field
        if self.provider_certificate is None and "provider_certificate" in self.__fields_set__:
            _dict['providerCertificate'] = None

        # set to None if client_id (nullable) is None
        # and __fields_set__ contains the field
        if self.client_id is None and "client_id" in self.__fields_set__:
            _dict['clientId'] = None

        # set to None if client_secret (nullable) is None
        # and __fields_set__ contains the field
        if self.client_secret is None and "client_secret" in self.__fields_set__:
            _dict['clientSecret'] = None

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        # set to None if default_connection_properties (nullable) is None
        # and __fields_set__ contains the field
        if self.default_connection_properties is None and "default_connection_properties" in self.__fields_set__:
            _dict['defaultConnectionProperties'] = None

        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Connection:
        """Create an instance of Connection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Connection.parse_obj(obj)

        _obj = Connection.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'OAUTH2',
            "connection_id": obj.get("connectionId"),
            "authentication_url": obj.get("authenticationUrl"),
            "token_url": obj.get("tokenUrl"),
            "issuer_url": obj.get("issuerUrl"),
            "provider_certificate": obj.get("providerCertificate"),
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret"),
            "data": ConnectionData.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "default_connection_properties": ConnectionDefaultConnectionProperties.from_dict(obj.get("defaultConnectionProperties")) if obj.get("defaultConnectionProperties") is not None else None,
            "created_time": obj.get("createdTime"),
            "tags": obj.get("tags")
        })
        return _obj


