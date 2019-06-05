# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    pass

class Output:
    INCIDENTS = "incidents"
    

class ListIncidentsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListIncidentsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidents": {
      "type": "array",
      "title": "Incidents",
      "description": "List of all incidents",
      "items": {
        "$ref": "#/definitions/incident"
      },
      "order": 1
    }
  },
  "required": [
    "incidents"
  ],
  "definitions": {
    "incident": {
      "type": "object",
      "title": "incident",
      "properties": {
        "assets": {
          "type": "array",
          "title": "Assets",
          "description": "Assets",
          "items": {
            "$ref": "#/definitions/samanage_id"
          },
          "order": 13
        },
        "assignee": {
          "$ref": "#/definitions/samanage_email",
          "title": "Assignee",
          "description": "Assignee",
          "order": 10
        },
        "category": {
          "$ref": "#/definitions/samanage_name",
          "title": "Category",
          "description": "Category",
          "order": 6
        },
        "changes": {
          "type": "array",
          "title": "Changes",
          "description": "Changes",
          "items": {
            "$ref": "#/definitions/samanage_number"
          },
          "order": 12
        },
        "configuration_items": {
          "type": "array",
          "title": "Configuration Items",
          "description": "Configuration items",
          "items": {
            "$ref": "#/definitions/samanage_id"
          },
          "order": 15
        },
        "custom_fields_values": {
          "type": "array",
          "title": "Custom Fields Values",
          "description": "Custom fields values",
          "items": {
            "$ref": "#/definitions/samanage_field"
          },
          "order": 18
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 5
        },
        "due_at": {
          "type": "string",
          "title": "Due At",
          "description": "Due at",
          "order": 9
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "incidents": {
          "type": "array",
          "title": "Incidents",
          "description": "Incidents",
          "items": {
            "$ref": "#/definitions/samanage_number"
          },
          "order": 16
        },
        "mobiles": {
          "type": "array",
          "title": "Mobiles",
          "description": "Mobiles",
          "items": {
            "$ref": "#/definitions/samanage_id"
          },
          "order": 14
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority",
          "order": 4
        },
        "problem": {
          "$ref": "#/definitions/samanage_problem",
          "title": "Problem",
          "description": "Problem",
          "order": 11
        },
        "requester": {
          "$ref": "#/definitions/samanage_email",
          "title": "Requester",
          "description": "Requester",
          "order": 8
        },
        "solutions": {
          "type": "array",
          "title": "Solutions",
          "description": "Solutions",
          "items": {
            "$ref": "#/definitions/samanage_number"
          },
          "order": 17
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 3
        },
        "subcategory": {
          "$ref": "#/definitions/samanage_name",
          "title": "Subcategory",
          "description": "Subcategory",
          "order": 7
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "$ref": "#/definitions/samanage_tag"
          },
          "order": 19
        }
      },
      "definitions": {
        "samanage_email": {
          "type": "object",
          "title": "samanage_email",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "Email",
              "order": 1
            }
          }
        },
        "samanage_field": {
          "type": "object",
          "title": "samanage_field",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 2
            }
          }
        },
        "samanage_id": {
          "type": "object",
          "title": "samanage_id",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 1
            }
          }
        },
        "samanage_name": {
          "type": "object",
          "title": "samanage_name",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            }
          }
        },
        "samanage_number": {
          "type": "object",
          "title": "samanage_number",
          "properties": {
            "number": {
              "type": "string",
              "title": "Number",
              "description": "Number",
              "order": 1
            }
          }
        },
        "samanage_problem": {
          "type": "object",
          "title": "samanage_problem",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "number": {
              "type": "string",
              "title": "Number",
              "description": "Number",
              "order": 1
            }
          }
        },
        "samanage_tag": {
          "type": "object",
          "title": "samanage_tag",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "tagging_count": {
              "type": "integer",
              "title": "Tagging Count",
              "description": "Tagging count",
              "order": 1
            }
          }
        }
      }
    },
    "samanage_email": {
      "type": "object",
      "title": "samanage_email",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 1
        }
      }
    },
    "samanage_field": {
      "type": "object",
      "title": "samanage_field",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "samanage_id": {
      "type": "object",
      "title": "samanage_id",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        }
      }
    },
    "samanage_name": {
      "type": "object",
      "title": "samanage_name",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        }
      }
    },
    "samanage_number": {
      "type": "object",
      "title": "samanage_number",
      "properties": {
        "number": {
          "type": "string",
          "title": "Number",
          "description": "Number",
          "order": 1
        }
      }
    },
    "samanage_problem": {
      "type": "object",
      "title": "samanage_problem",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "number": {
          "type": "string",
          "title": "Number",
          "description": "Number",
          "order": 1
        }
      }
    },
    "samanage_tag": {
      "type": "object",
      "title": "samanage_tag",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "tagging_count": {
          "type": "integer",
          "title": "Tagging Count",
          "description": "Tagging count",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)