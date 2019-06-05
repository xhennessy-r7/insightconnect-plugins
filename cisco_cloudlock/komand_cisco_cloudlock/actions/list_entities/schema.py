# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    LIMIT = "limit"
    OFFSET = "offset"
    

class Output:
    ENTITIES = "entities"
    

class ListEntitiesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of paginated results to return. Max: 100",
      "default": 20,
      "order": 2
    },
    "offset": {
      "type": "number",
      "title": "Offset",
      "description": "Pagination offset",
      "default": 0,
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListEntitiesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "entities": {
      "type": "array",
      "title": "Entities",
      "description": "Entities",
      "items": {
        "$ref": "#/definitions/entity"
      },
      "order": 1
    }
  },
  "definitions": {
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "asset_type": {
          "type": "string",
          "title": "Asset Type",
          "order": 5
        },
        "collaborators": {
          "type": "array",
          "title": "Collaborators",
          "description": "Permissions corresponding to the collaborators on an asset",
          "items": {
            "$ref": "#/definitions/permission"
          },
          "order": 15
        },
        "collaborators_count": {
          "type": "number",
          "title": "Collaborators Count",
          "description": "Total number of collaborators on an asset",
          "order": 9
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "The time at which the asset was created",
          "format": "date-time",
          "order": 13
        },
        "direct_url": {
          "type": "string",
          "title": "Direct Url",
          "description": "URL to the asset",
          "order": 14
        },
        "exposure": {
          "type": "string",
          "title": "Exposure",
          "description": "Exposure level of the document",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Unique internal identifier for the asset",
          "order": 1
        },
        "mime_type": {
          "type": "string",
          "title": "Mime Type",
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Title, name of the asset",
          "order": 10
        },
        "origin_id": {
          "type": "string",
          "title": "Origin Id",
          "description": "Unique identifier for the asset provided by the origin platform/vendor",
          "order": 3
        },
        "origin_type": {
          "type": "string",
          "title": "Origin Type",
          "description": "Equivalent to ‘vendor_type’",
          "order": 4
        },
        "owners": {
          "type": "array",
          "title": "Owners",
          "description": "Permissions corresponding to the owner(s) of the asset",
          "items": {
            "$ref": "#/definitions/permission"
          },
          "order": 6
        },
        "size": {
          "type": "string",
          "title": "Size",
          "description": "Size of the asset in bytes",
          "order": 11
        },
        "updated_at": {
          "type": "string",
          "title": "Updated At",
          "displayType": "date",
          "description": "The last time the asset has been modified",
          "format": "date-time",
          "order": 12
        },
        "vendor": {
          "$ref": "#/definitions/vendor",
          "title": "Vendor",
          "order": 2
        }
      },
      "definitions": {
        "permission": {
          "type": "object",
          "title": "permission",
          "properties": {
            "role": {
              "type": "string",
              "title": "Role",
              "description": "Role associated with the permission",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type of permission",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Email address or domain address for the permission",
              "order": 3
            }
          }
        },
        "vendor": {
          "type": "object",
          "title": "vendor",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the vendor. For example, google",
              "order": 1
            }
          }
        }
      }
    },
    "permission": {
      "type": "object",
      "title": "permission",
      "properties": {
        "role": {
          "type": "string",
          "title": "Role",
          "description": "Role associated with the permission",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of permission",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Email address or domain address for the permission",
          "order": 3
        }
      }
    },
    "vendor": {
      "type": "object",
      "title": "vendor",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the vendor. For example, google",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)