# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FIRST_TIME = "first_time"
    RESULT_UNIT = "result_unit"
    SECOND_TIME = "second_time"
    

class Output:
    DIFFERENCE = "difference"
    TIME_UNIT = "time_unit"
    

class TimeElapsedInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "first_time": {
      "type": "string",
      "title": "First Date",
      "displayType": "date",
      "description": "First date",
      "format": "date-time",
      "order": 1
    },
    "result_unit": {
      "type": "string",
      "title": "Result Unit",
      "description": "Time unit of measurement for result",
      "enum": [
        "Years",
        "Months",
        "Days",
        "Hours",
        "Minutes",
        "Seconds"
      ],
      "order": 3
    },
    "second_time": {
      "type": "string",
      "title": "Second Date",
      "displayType": "date",
      "description": "Second date",
      "format": "date-time",
      "order": 2
    }
  },
  "required": [
    "first_time",
    "second_time",
    "result_unit"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TimeElapsedOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "difference": {
      "type": "integer",
      "title": "Difference",
      "description": "Quantity of time difference",
      "order": 1
    },
    "time_unit": {
      "type": "string",
      "title": "Unit of Time",
      "description": "Time unit of measurement",
      "order": 2
    }
  },
  "required": [
    "time_unit",
    "difference"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)