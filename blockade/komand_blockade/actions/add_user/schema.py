# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    USER_EMAIL = "user_email"
    USER_NAME = "user_name"
    USER_ROLE = "user_role"
    

class Output:
    API_KEY = "api_key"
    EMAIL = "email"
    MESSAGE = "message"
    NAME = "name"
    ROLE = "role"
    SUCCESS = "success"
    

class AddUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_email": {
      "type": "string",
      "title": "Email",
      "description": "Email of new user",
      "order": 1
    },
    "user_name": {
      "type": "string",
      "title": "Username",
      "description": "Name of new user",
      "order": 2
    },
    "user_role": {
      "type": "string",
      "title": "Role",
      "description": "Role of new user",
      "enum": [
        "analyst",
        "admin"
      ],
      "order": 3
    }
  },
  "required": [
    "user_email",
    "user_name",
    "user_role"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "API key",
      "order": 1
    },
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email",
      "order": 2
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 6
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name",
      "order": 3
    },
    "role": {
      "type": "string",
      "title": "Role",
      "description": "Role",
      "order": 4
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 5
    }
  },
  "required": [
    "success",
    "message"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)