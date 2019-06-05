# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    DESCRIPTION = "description"
    ERROR = "error"
    INSTALLATION_DATE = "installation_date"
    MAX_AGENTS = "max_agents"
    OPENSSL_SUPPORT = "openssl_support"
    PATH = "path"
    RULESET_VERSION = "ruleset_version"
    TYPE = "type"
    TZ_NAME = "tz_name"
    TZ_OFFSET = "tz_offset"
    VERSION = "version"
    

class ManagerInfoInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ManagerInfoOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description",
      "order": 9
    },
    "error": {
      "type": "integer",
      "title": "Error Code",
      "description": "Error Code",
      "order": 11
    },
    "installation_date": {
      "type": "string",
      "title": "Installation Date",
      "description": "Installation date",
      "order": 5
    },
    "max_agents": {
      "type": "string",
      "title": "Max Agents",
      "description": "Max agents",
      "order": 7
    },
    "openssl_support": {
      "type": "string",
      "title": "OpenSSL Support",
      "description": "OpenSSL support",
      "order": 1
    },
    "path": {
      "type": "string",
      "title": "Path",
      "description": "Path",
      "order": 8
    },
    "ruleset_version": {
      "type": "string",
      "title": "Ruleset Version",
      "description": "Ruleset version",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type",
      "order": 10
    },
    "tz_name": {
      "type": "string",
      "title": "TZ Name",
      "description": "TZ name",
      "order": 3
    },
    "tz_offset": {
      "type": "string",
      "title": "TZ Offset",
      "description": "TZ Offset",
      "order": 4
    },
    "version": {
      "type": "string",
      "title": "Version",
      "description": "Version",
      "order": 6
    }
  },
  "required": [
    "tz_name",
    "tz_offset",
    "version",
    "max_agents",
    "description",
    "type",
    "openssl_support",
    "ruleset_version",
    "installation_date",
    "error"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)