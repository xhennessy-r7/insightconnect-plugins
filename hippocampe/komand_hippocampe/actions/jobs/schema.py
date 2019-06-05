# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    JOBS = "jobs"
    

class JobsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class JobsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "jobs": {
      "type": "array",
      "title": "Jobs",
      "description": "List of all jobs, with their reports",
      "items": {
        "$ref": "#/definitions/job"
      },
      "order": 1
    }
  },
  "required": [
    "jobs"
  ],
  "definitions": {
    "job": {
      "type": "object",
      "title": "job",
      "properties": {
        "duration": {
          "type": "number",
          "title": "Duration",
          "description": "Duration of the indexation (in minutes)",
          "order": 2
        },
        "endTime": {
          "type": "string",
          "title": "End Time",
          "displayType": "date",
          "description": "End time",
          "format": "date-time",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "reports": {
          "type": "array",
          "title": "Reports",
          "description": "Reports per configuration file",
          "items": {
            "$ref": "#/definitions/report"
          },
          "order": 6
        },
        "startTime": {
          "type": "string",
          "title": "Start Time",
          "displayType": "date",
          "description": "Start time",
          "format": "date-time",
          "order": 4
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the job (ongoing, done, failed)",
          "order": 3
        }
      },
      "definitions": {
        "report": {
          "type": "object",
          "title": "report",
          "properties": {
            "activated": {
              "type": "boolean",
              "title": "Activated",
              "description": "Is the source activated (only activated sources are queried)",
              "order": 2
            },
            "error": {
              "type": "array",
              "title": "Error",
              "description": "List of exception names (in case of failure)",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "filename": {
              "type": "string",
              "title": "Filename",
              "description": "Name of the configuration file",
              "order": 1
            },
            "link": {
              "type": "string",
              "title": "Link",
              "description": "URL of the source",
              "order": 4
            },
            "nbFailed": {
              "type": "integer",
              "title": "Failed",
              "description": "Number of feed lines that failed indexation",
              "order": 5
            },
            "nbIndex": {
              "type": "integer",
              "title": "Indexed",
              "description": "Number of elements successfully indexed",
              "order": 6
            },
            "nbNew": {
              "type": "integer",
              "title": "New",
              "description": "Number of elements not known before",
              "order": 7
            },
            "nbUpdate": {
              "type": "integer",
              "title": "Update",
              "description": "Number of elements successfully updated",
              "order": 8
            }
          }
        }
      }
    },
    "report": {
      "type": "object",
      "title": "report",
      "properties": {
        "activated": {
          "type": "boolean",
          "title": "Activated",
          "description": "Is the source activated (only activated sources are queried)",
          "order": 2
        },
        "error": {
          "type": "array",
          "title": "Error",
          "description": "List of exception names (in case of failure)",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of the configuration file",
          "order": 1
        },
        "link": {
          "type": "string",
          "title": "Link",
          "description": "URL of the source",
          "order": 4
        },
        "nbFailed": {
          "type": "integer",
          "title": "Failed",
          "description": "Number of feed lines that failed indexation",
          "order": 5
        },
        "nbIndex": {
          "type": "integer",
          "title": "Indexed",
          "description": "Number of elements successfully indexed",
          "order": 6
        },
        "nbNew": {
          "type": "integer",
          "title": "New",
          "description": "Number of elements not known before",
          "order": 7
        },
        "nbUpdate": {
          "type": "integer",
          "title": "Update",
          "description": "Number of elements successfully updated",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)