# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get users from Asana"


class Input:
    pass

class Output:
    DATA = "data"
    

class GetUsersInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUsersOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "object",
      "title": "Data",
      "description": "List of users",
      "order": 1
    }
  },
  "required": [
    "data"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)