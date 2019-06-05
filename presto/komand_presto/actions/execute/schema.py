# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    OPERATION = "operation"
    PARAMETERS = "parameters"
    

class Output:
    ROWS = "rows"
    

class ExecuteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "operation": {
      "type": "string",
      "title": "Operation",
      "description": "Query or command to execute",
      "order": 1
    },
    "parameters": {
      "type": "string",
      "title": "Parameters",
      "description": "Reserved for future use. Parameters which safely will be passed to operation string",
      "order": 2
    }
  },
  "required": [
    "operation"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ExecuteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "rows": {
      "type": "array",
      "title": "Rows",
      "description": "Rows as sequence of sequences",
      "items": {
        "$ref": "#/definitions/row"
      },
      "order": 1
    }
  },
  "definitions": {
    "row": {
      "type": "object",
      "title": "row",
      "properties": {
        "row": {
          "type": "array",
          "title": "Row",
          "description": "Row field list",
          "items": {
            "type": "string"
          },
          "order": 1
        }
      },
      "required": [
        "row"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)