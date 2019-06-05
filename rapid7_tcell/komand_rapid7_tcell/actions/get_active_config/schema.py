# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    APP_ID = "app_id"
    

class Output:
    CONFIG = "config"
    

class GetActiveConfigInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App ID",
      "order": 1
    }
  },
  "required": [
    "app_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetActiveConfigOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "config": {
      "type": "object",
      "title": "Configuration",
      "description": "The latest configuration data",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)