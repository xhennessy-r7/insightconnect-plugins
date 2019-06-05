# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Post time-series data that can be graphed on Datadog's dashboards"


class Input:
    SERIES = "series"
    

class Output:
    RESOURCE = "resource"
    STATUS = "status"
    

class PostMetricsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "series": {
      "type": "array",
      "title": "Metric Series",
      "description": "Pass a JSON array of the following timeseries format body https://docs.datadoghq.com/api/?lang=bash#post-timeseries-points",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "required": [
    "series"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PostMetricsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resource": {
      "$ref": "#/definitions/resource",
      "title": "Resource",
      "description": "Resource",
      "order": 1
    },
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status code",
      "order": 2
    }
  },
  "definitions": {
    "resource": {
      "type": "object",
      "title": "resource",
      "properties": {
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status message",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)