# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SAVED_SEARCH_NAME = "saved_search_name"
    

class Output:
    SUCCESS = "success"
    

class DeleteSavedSearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "saved_search_name": {
      "type": "string",
      "title": "Saved Search Name",
      "description": "Name of the saved search to delete",
      "order": 1
    }
  },
  "required": [
    "saved_search_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteSavedSearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the deletion was successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)