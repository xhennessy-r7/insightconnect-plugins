# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FILTER = "filter"
    MAXRESULTS = "maxResults"
    ORDERBY = "orderBy"
    PAGETOKEN = "pageToken"
    

class Output:
    ID = "id"
    ITEMS = "items"
    KIND = "kind"
    NEXTPAGETOKEN = "nextPageToken"
    SELFLINK = "selfLink"
    

class ListFirewallsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Sets a filter expression for filtering listed resources",
      "order": 1
    },
    "maxResults": {
      "type": "integer",
      "title": "Max Results",
      "description": "The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500",
      "order": 2
    },
    "orderBy": {
      "type": "string",
      "title": "OrderBy",
      "description": "Sorts list results by a certain order",
      "order": 3
    },
    "pageToken": {
      "type": "string",
      "title": "Page Token",
      "description": "Set pageToken to the nextPageToken returned by a previous list request to get the next page of results",
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListFirewallsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier for the resource. This identifier is defined by the server",
      "order": 2
    },
    "items": {
      "type": "array",
      "title": "Items",
      "description": "A list of firewall resources",
      "items": {
        "$ref": "#/definitions/items_firewalls"
      },
      "order": 3
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Type of resource. Always compute#firewallList for lists of firewalls",
      "order": 1
    },
    "nextPageToken": {
      "type": "string",
      "title": "Next Page Token",
      "description": "This token allows you to get the next page of results for list requests",
      "order": 5
    },
    "selfLink": {
      "type": "string",
      "title": "Self Link",
      "description": "Server-defined url for this resource",
      "order": 4
    }
  },
  "definitions": {
    "allowed": {
      "type": "object",
      "title": "allowed",
      "properties": {
        "IPProtocol": {
          "type": "string",
          "title": "IPProtocol",
          "order": 1
        },
        "ports": {
          "type": "array",
          "title": "Ports",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      }
    },
    "items_firewalls": {
      "type": "object",
      "title": "items_firewalls",
      "properties": {
        "allowed": {
          "type": "array",
          "title": "Allowed",
          "items": {
            "$ref": "#/definitions/allowed"
          },
          "order": 1
        },
        "creationTimestamp": {
          "type": "string",
          "title": "CreationTimestamp",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 4
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 6
        },
        "network": {
          "type": "string",
          "title": "Network",
          "order": 7
        },
        "selfLink": {
          "type": "string",
          "title": "SelfLink",
          "order": 8
        },
        "sourceRanges": {
          "type": "array",
          "title": "SourceRanges",
          "items": {
            "type": "string"
          },
          "order": 9
        }
      },
      "definitions": {
        "allowed": {
          "type": "object",
          "title": "allowed",
          "properties": {
            "IPProtocol": {
              "type": "string",
              "title": "IPProtocol",
              "order": 1
            },
            "ports": {
              "type": "array",
              "title": "Ports",
              "items": {
                "type": "string"
              },
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