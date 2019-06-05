# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    COMMENT = "comment"
    MACHINE_ID = "machine_id"
    SHA1 = "sha1"
    

class Output:
    STOP_AND_QUARANTINE_RESPONSE = "stop_and_quarantine_response"
    

class StopAndQuarantineFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment to associate with the stop and quarantine action",
      "order": 2
    },
    "machine_id": {
      "type": "string",
      "title": "Machine ID",
      "description": "Machine ID",
      "order": 1
    },
    "sha1": {
      "type": "string",
      "title": "Sha1",
      "description": "Sha1 of the file to stop and quarantine on the machine",
      "order": 3
    }
  },
  "required": [
    "machine_id",
    "comment",
    "sha1"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StopAndQuarantineFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "stop_and_quarantine_response": {
      "$ref": "#/definitions/stop_and_quarantine_response",
      "title": "Stop and Quarantine Response",
      "description": "A response that includes the result of the action, and supplemental information about the action taken",
      "order": 1
    }
  },
  "required": [
    "stop_and_quarantine_response"
  ],
  "definitions": {
    "relatedFileInfo": {
      "type": "object",
      "title": "relatedFileInfo",
      "properties": {
        "fileIdentifier": {
          "type": "string",
          "title": "File Identifier",
          "description": "File identifier",
          "order": 1
        },
        "fileIdentifierType": {
          "type": "string",
          "title": "File Identifier Type",
          "description": "File identifier type",
          "order": 2
        }
      }
    },
    "stop_and_quarantine_response": {
      "type": "object",
      "title": "stop_and_quarantine_response",
      "properties": {
        "@odata.context": {
          "type": "string",
          "title": "@Odata.Context",
          "description": "@odata.context",
          "order": 5
        },
        "creationDateTimeUtc": {
          "type": "string",
          "title": "Creation Date Time UTC",
          "description": "Creation date time utc",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 9
        },
        "lastUpdateTimeUtc": {
          "type": "string",
          "title": "Last Update Time UTC",
          "description": "Last update time UTC",
          "order": 4
        },
        "machineId": {
          "type": "string",
          "title": "Machine ID",
          "description": "Machine ID",
          "order": 3
        },
        "relatedFileInfo": {
          "$ref": "#/definitions/relatedFileInfo",
          "title": "Related File Info",
          "description": "Related File Info",
          "order": 7
        },
        "requestor": {
          "type": "string",
          "title": "Requestor",
          "description": "Requestor",
          "order": 6
        },
        "requestorComment": {
          "type": "string",
          "title": "Requestor Comment",
          "description": "Requestor comment",
          "order": 10
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 8
        }
      },
      "definitions": {
        "relatedFileInfo": {
          "type": "object",
          "title": "relatedFileInfo",
          "properties": {
            "fileIdentifier": {
              "type": "string",
              "title": "File Identifier",
              "description": "File identifier",
              "order": 1
            },
            "fileIdentifierType": {
              "type": "string",
              "title": "File Identifier Type",
              "description": "File identifier type",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)