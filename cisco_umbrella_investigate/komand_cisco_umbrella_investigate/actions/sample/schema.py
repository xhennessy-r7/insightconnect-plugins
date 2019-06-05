# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HASH = "hash"
    LIMIT = "limit"
    OFFSET = "offset"
    

class Output:
    SAMPLE = "sample"
    

class SampleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "Search sample by hash (SHA-256, SHA-1 or MD5)",
      "order": 1
    },
    "limit": {
      "type": "string",
      "title": "Limit",
      "description": "Default of 10, can be extended for a larger data set",
      "order": 2
    },
    "offset": {
      "type": "string",
      "title": "Offset",
      "description": "The offset of the individual entities in the query’s response, used for pagination",
      "order": 3
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SampleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sample": {
      "$ref": "#/definitions/sample_info",
      "title": "Sample",
      "description": "Sample",
      "order": 1
    }
  },
  "definitions": {
    "sample_info": {
      "type": "object",
      "title": "sample_info",
      "properties": {
        "avresults": {
          "type": "array",
          "title": "AV Results",
          "description": "AntiVirus results according to ClamAV. A sample can have more than one signature if it is possibly detected under more than one family of malware. A sample may also have no signatures associated",
          "order": 10
        },
        "firstSeen": {
          "type": "number",
          "title": "FirstSeen",
          "description": "The epoch time stamp for when this sample was first seen by Threat Grid",
          "order": 7
        },
        "lastSeen": {
          "type": "number",
          "title": "LastSeen",
          "description": "The epoch time stamp for when this sample was last seen by Threat Grid. The lastSeen and firstSeen will often be the same if the sample is more recent",
          "order": 8
        },
        "magicType": {
          "type": "string",
          "title": "MagicType",
          "description": "A ‘magic type’ is better understood as a file type. Specifically, it is the output of the Linux “file” utility",
          "order": 4
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "The MD5 checksum of the sample, as above, can be searched in /sample/ endpoint",
          "order": 3
        },
        "sha1": {
          "type": "string",
          "title": "SHA1",
          "description": "The SHA1 checksum of the sample. As above, can be searched in /sample/ endpoint",
          "order": 2
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "The SHA256 checksum of the sample. This checksum is important if you’d like to find out more about this sample in the /sample/ endpoint",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the sample in bytes",
          "order": 6
        },
        "threatScore": {
          "type": "integer",
          "title": "ThreatScore",
          "description": "A threatScore is a measure of the amount of system weakening, obfuscation, persistence, modification, data exfiltration, and other behaviors which may be a threat to the host system’s integrity",
          "order": 5
        },
        "visible": {
          "type": "boolean",
          "title": "Visible",
          "description": "Boolean, either true or false. For internal Umbrella use only, please ignore",
          "order": 9
        }
      },
      "required": [
        "sha256",
        "md5",
        "size",
        "avresults",
        "sha1",
        "magicType",
        "threatScore",
        "firstSeen",
        "lastSeen",
        "visible"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)