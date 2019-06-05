# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_VERSION = "api_version"
    CREDENTIALS = "credentials"
    URL = "url"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_version": {
      "type": "string",
      "title": "API Version",
      "description": "Version of the API",
      "default": "2.7",
      "enum": [
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
        "1.8",
        "1.9",
        "2.0",
        "2.1",
        "2.2",
        "2.3",
        "2.4",
        "2.5",
        "2.6",
        "2.7"
      ],
      "order": 3
    },
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Infoblox username and password",
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "The URL of a running Infoblox instance (e.g. https://192.168.1.2 or https://example.infoblox.com)",
      "order": 1
    }
  },
  "required": [
    "url",
    "credentials",
    "api_version"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)