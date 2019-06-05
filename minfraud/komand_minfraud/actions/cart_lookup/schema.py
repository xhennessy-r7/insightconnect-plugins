# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESS = "address"
    ITEM_CATEGORY = "item_category"
    ITEM_ID = "item_id"
    PRICE = "price"
    QUANTITY = "quantity"
    

class Output:
    RISK_SCORE = "risk_score"
    

class CartLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "item_category": {
      "type": "string",
      "title": "Item Category",
      "description": "Category of the item",
      "order": 2
    },
    "item_id": {
      "type": "string",
      "title": "Item ID",
      "description": "Internal ID for the item",
      "order": 3
    },
    "price": {
      "type": "string",
      "title": "Item Price",
      "description": "Item price",
      "order": 5
    },
    "quantity": {
      "type": "integer",
      "title": "Item Quantity",
      "description": "Item quantity",
      "order": 4
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CartLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)