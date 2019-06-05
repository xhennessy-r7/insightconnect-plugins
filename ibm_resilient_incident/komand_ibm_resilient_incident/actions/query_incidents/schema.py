# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ORGANIZATION_ID = "organization_id"
    QUERY = "query"
    

class Output:
    INCIDENTS = "incidents"
    

class QueryIncidentsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organization_id": {
      "type": "number",
      "title": "Organization ID",
      "description": "The organization ID",
      "order": 1
    },
    "query": {
      "type": "object",
      "title": "Query",
      "description": "Accepts a QueryDTO JSON object. Please see the QueryDTO JSON reference in your Resilient API documentation",
      "order": 2
    }
  },
  "required": [
    "organization_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryIncidentsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidents": {
      "type": "array",
      "title": "Incidents",
      "description": "Incidents",
      "items": {
        "$ref": "#/definitions/PartialIncidentDTO"
      },
      "order": 1
    }
  },
  "definitions": {
    "PartialIncidentDTO": {
      "type": "object",
      "title": "PartialIncidentDTO",
      "properties": {
        "create_date": {
          "type": "number",
          "title": "Create Date",
          "order": 5
        },
        "description": {
          "type": "string",
          "title": "Description",
          "order": 6
        },
        "discovered_date": {
          "type": "number",
          "title": "Discovered Date",
          "order": 3
        },
        "due_date": {
          "type": "number",
          "title": "Due Date",
          "order": 4
        },
        "id": {
          "type": "number",
          "title": "Id",
          "order": 1
        },
        "inc_training": {
          "type": "boolean",
          "title": "Inc Training",
          "order": 11
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "owner_id": {
          "type": "number",
          "title": "Owner Id",
          "order": 7
        },
        "phase_id": {
          "type": "number",
          "title": "Phase Id",
          "order": 8
        },
        "plan_status": {
          "type": "string",
          "title": "Plan Status",
          "order": 10
        },
        "severity_code": {
          "type": "number",
          "title": "Severity Code",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)