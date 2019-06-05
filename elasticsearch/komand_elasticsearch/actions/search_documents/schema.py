# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    _INDEX = "_index"
    _TYPE = "_type"
    QUERY = "query"
    ROUTING = "routing"
    

class Output:
    _SHARDS = "_shards"
    HITS = "hits"
    TIMED_OUT = "timed_out"
    TOOK = "took"
    

class SearchDocumentsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_index": {
      "type": "string",
      "title": "Index",
      "description": "Document Index",
      "order": 1
    },
    "_type": {
      "type": "string",
      "title": "Type",
      "description": "Document Type",
      "order": 2
    },
    "query": {
      "type": "object",
      "title": "Query",
      "description": "JSON Query DSL",
      "order": 4
    },
    "routing": {
      "type": "string",
      "title": "Routing",
      "description": "Optional Shards to Search",
      "order": 3
    }
  },
  "required": [
    "_index"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchDocumentsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_shards": {
      "$ref": "#/definitions/_shards",
      "title": "Shards",
      "description": "Information About Replication Process",
      "order": 3
    },
    "hits": {
      "$ref": "#/definitions/hits",
      "title": "Hits",
      "description": "Information About Hits",
      "order": 4
    },
    "timed_out": {
      "type": "boolean",
      "title": "Timed out",
      "description": "Timed Out Flag",
      "order": 2
    },
    "took": {
      "type": "integer",
      "title": "Took",
      "description": "Duration in Milliseconds",
      "order": 1
    }
  },
  "definitions": {
    "_shards": {
      "type": "object",
      "title": "_shards",
      "properties": {
        "failed": {
          "type": "integer",
          "title": "Failed",
          "description": "Number of Failed Shards",
          "order": 3
        },
        "successful": {
          "type": "integer",
          "title": "Successful",
          "description": "Number of Successful Shards",
          "order": 2
        },
        "total": {
          "type": "integer",
          "title": "Total",
          "description": "Number of Total Shards",
          "order": 1
        }
      }
    },
    "hit": {
      "type": "object",
      "title": "hit",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "Document ID",
          "order": 3
        },
        "_index": {
          "type": "string",
          "title": "Index",
          "description": "Document Index",
          "order": 1
        },
        "_score": {
          "type": "number",
          "title": "Score",
          "description": "Relevance Score",
          "order": 5
        },
        "_source": {
          "type": "object",
          "title": "Source",
          "description": "Content of Document",
          "order": 6
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Document Type",
          "order": 2
        },
        "_version": {
          "type": "integer",
          "title": "Version",
          "description": "Document Version",
          "order": 4
        }
      }
    },
    "hits": {
      "type": "object",
      "title": "hits",
      "properties": {
        "hits": {
          "type": "array",
          "title": "Hits",
          "description": "Array of Hits",
          "items": {
            "$ref": "#/definitions/hit"
          },
          "order": 3
        },
        "max_score": {
          "type": "number",
          "title": "Max Score",
          "description": "Maximum Relevance Score",
          "order": 2
        },
        "total": {
          "type": "integer",
          "title": "Total",
          "description": "Number of Total Hits",
          "order": 1
        }
      },
      "definitions": {
        "hit": {
          "type": "object",
          "title": "hit",
          "properties": {
            "_id": {
              "type": "string",
              "title": "ID",
              "description": "Document ID",
              "order": 3
            },
            "_index": {
              "type": "string",
              "title": "Index",
              "description": "Document Index",
              "order": 1
            },
            "_score": {
              "type": "number",
              "title": "Score",
              "description": "Relevance Score",
              "order": 5
            },
            "_source": {
              "type": "object",
              "title": "Source",
              "description": "Content of Document",
              "order": 6
            },
            "_type": {
              "type": "string",
              "title": "Type",
              "description": "Document Type",
              "order": 2
            },
            "_version": {
              "type": "integer",
              "title": "Version",
              "description": "Document Version",
              "order": 4
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