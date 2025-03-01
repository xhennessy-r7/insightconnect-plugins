# Viper

## About

[Viper](https://viper.li/en/latest/) is a binary analysis and management framework. Viper's fundamental objective is to provide a solution to easily organize your collection of malware and exploit samples as well as your collection of scripts you created, or found over time to facilitate your daily research. Think of it as a Metasploit for malware researchers: it provides a terminal interface that you can use to store, search and analyze arbitrary files.

This plugin utilizes the [Viper API](https://viper.li/en/latest/usage/web.html#api)

## Actions

### Create Note

This action is used to create a note for malware.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|string|None|True|Note body|None|
|malware_sha256|string|None|True|Malware SHA256|None|
|project_name|string|None|True|Project name|None|
|title|string|None|True|Note title|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|note|Note|True|New note|

Example output:

```
{
  "note": {
      "id": 2,
      "project_name": "test",
      "malware_sha256": "31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347",
      "title": "new title",
      "body": "body"
  }
}
```

### Create New Project

This action is used to create a new project with a given name.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|New project|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|project|Project|True|Project|

Example output:

```
{
  "project": {
      "name": "test"
  }
}
```

### Delete Analysis

This action is used to delete an analysis by ID and malware SHA256 hash.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Analysis ID|None|
|malware_sha256|string|None|True|Malware SHA256 hash|None|
|project_name|string|None|True|Project name|None|

### Delete Malware

This action is used to delete malware by SHA256 hash.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_name|string|None|True|Project name|None|
|sha256|string|None|True|Malware SHA256|None|

### Delete Note

This action is used to delete a note by ID and malware SHA256 hash.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Note ID|None|
|malware_sha256|string|None|True|Malware SHA256|None|
|project_name|string|None|True|Project name|None|

### Delete Tag

This action is used to delete a tag by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID|None|
|project_name|string|None|True|Project name|None|

### Download Malware

This action is used to download a malware instance as a raw file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compressor|string|None|False|Compressor class|None|
|malware_sha256|string|None|True|Malware SHA256|None|
|password|password|None|False|Password|None|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|raw|file|True|Raw file|

Example output:

```
{
  "raw": {
      "file": {
          "filename": "filename v2",
          "content": "ZmlsZW5hbWUgdjE="
      }
  }
}
```

### Project Analysis

This action is used to get a single analysis for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Analysis ID|None|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analyses|Analysis|True|Project analysis|

Example output:

```
{
  "analyses": {
      "id": 1,
      "project_name": "test",
      "malware_sha256": null,
      "cmd_line": "yara scan -t",
      "stored_at": "2019-06-23 00:01:41.833881",
      "results": "[{\"type\": \"info\", \"data\": \"Scanning filename v2 (31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347)\"}]"
  }
}
```

### Project Malware

This action is used to get a single malware for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_name|string|None|True|Project name|None|
|sha256|string|None|True|SHA256 hash|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|malware|Malware|True|Project malware|

Example output:

```
{
  "malware": {
      "project_name": "test",
      "id": 1,
      "name": "filename v2",
      "crc32": "B9C5D962",
      "md5": "a1a43a5ee95a91291ff582c7f9ffe24d",
      "sha1": "653a6ef54169396c505123c2882cadea31ccf8e3",
      "sha256": "31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347",
      "sha512": "2275c38346dfa962a71e2ccf8c3bb143d509873d77b8049860aa3621814e0d109bab335929f63eb30ccbce0a0987d04e44a2ecea785d1257f3f5235b729c2af4",
      "size": 11,
      "ssdeep": "3:xipU:xkU",
      "type": "ASCII text, with no line terminators",
      "mime": "text/plain",
      "created_at": "2019-06-23 00:00:18.052132"
  }
}
```

### Project Note

This action is used to get a single note for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Note ID|None|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|note|Note|True|Project note|

Example output:

```
{
  "note": {
      "id": 1,
      "project_name": "test",
      "malware_sha256": null,
      "title": "new title",
      "body": "body"
  }
}
```

### Project by Name

This action gets a single project by a given name.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|project|Project|True|Project|

Example output:

```
{
  "project": {
      "name": "test"
  }
}
```

### Project Tag

This action is used to get a single tag for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|None|None|
|project_name|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tag|Tag|True|Project tag|

Example output:

```
{
  "tag": {
      "project_name": "test",
      "id": 1,
      "tag": "tag1 tag2"
  }
}
```

### Project Analyses

This action is used to list analyses for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analyses|[]Analysis|True|List of analyses|

Example output:

```
{
  "analyses": [
      {
          "id": 1,
          "project_name": "test",
          "malware_sha256": null,
          "cmd_line": "yara scan -t",
          "stored_at": "2019-06-23 00:01:41.833881",
          "results": "[{\"type\": \"info\", \"data\": \"Scanning filename v2 (31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347)\"}]"
      },
      {
          "id": 2,
          "project_name": "test",
          "malware_sha256": null,
          "cmd_line": "triage",
          "stored_at": "2019-06-23 00:01:41.850765",
          "results": "[]"
      }
  ]
}
```

### Available Compressors

This action is used to list available archive compressors.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|compressors|[]Archive|True|Archive compressor|

Example output:

```
{
  "compressors": [
      {
          "cls_name": "SevenZipSystemCompressor",
          "title": "7-Zip (System)",
          "extensions": [
              "7z"
          ],
          "password": true
      },
      {
          "cls_name": "ZipCompressor",
          "title": "Zip",
          "extensions": [
              "zip"
          ],
          "password": false
      }
  ]
}
```

### Available Extractors

This action is used to list available archive extractors.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|extractors|[]Archive|True|Archive extractor|

Example output:

```
{
  "extractors": [
      {
          "cls_name": "BZ2Extractor",
          "title": "BZip2",
          "extensions": [
              "bz2"
          ],
          "password": false
      },
      {
          "cls_name": "GZipExtractor",
          "title": "GZip",
          "extensions": [
              "gz"
          ],
          "password": false
      },
      {
          "cls_name": "RarExtractor",
          "title": "Rar",
          "extensions": [
              "rar"
          ],
          "password": true
      },
      {
          "cls_name": "SevenZipSystemExtractor",
          "title": "7-Zip (System)",
          "extensions": [
              "7z"
          ],
          "password": true
      },
      {
          "cls_name": "TarExtractor",
          "title": "Tar",
          "extensions": [
              "tar",
              "tar.gz",
              "tar.bz2"
          ],
          "password": false
      },
      {
          "cls_name": "ZipExtractor",
          "title": "Zip",
          "extensions": [
              "zip"
          ],
          "password": true
      }
  ]
}
```

### Available Modules

This action is used to list available modules.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|modules|[]Module|True|Available modules|

Example output:

```
{
  "modules": [
      {
          "name": "apk",
          "description": "Parse Android Applications"
      },
      {
          "name": "cuckoo",
          "description": "Submit the file to Cuckoo Sandbox"
      },
      {
          "name": "debup",
          "description": "Parse McAfee BUP Files"
      }
  ]
}
```

### Existing Projects

This action is used to list existing projects.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|projects|[]Project|True|Available projects|

Example output:

```
{
  "projects": [
      {
          "name": "default"
      },
      {
          "name": "test"
      }
  ]
}
```

### Malwares

This action is used to list malware for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|malware|[]Malware|True|List of malware|

Example output:

```
{
  "malware": [
      {
          "project_name": "test",
          "id": 1,
          "name": "filename v2",
          "crc32": "B9C5D962",
          "md5": "a1a43a5ee95a91291ff582c7f9ffe24d",
          "sha1": "653a6ef54169396c505123c2882cadea31ccf8e3",
          "sha256": "31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347",
          "sha512": "2275c38346dfa962a71e2ccf8c3bb143d509873d77b8049860aa3621814e0d109bab335929f63eb30ccbce0a0987d04e44a2ecea785d1257f3f5235b729c2af4",
          "size": 11,
          "ssdeep": "3:xipU:xkU",
          "type": "ASCII text, with no line terminators",
          "mime": "text/plain",
          "created_at": "2019-06-23 00:00:18.052132"
      }
  ]
}
```

### Project Notes

This action is used to list notes for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|notes|[]Note|True|List of notes|

Example output:

```
{
  "notes": [
      {
          "id": 1,
          "project_name": "test",
          "malware_sha256": null,
          "title": "new title",
          "body": "body"
      }
  ]
}
```

### Project Tags

This action is used to list tags for this project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_name|string|None|True|Project name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tags|[]Tag|True|Project tags|

Example output:

```
{
  "tags": [
      {
          "project_name": "test",
          "id": 1,
          "tag": "tag1 tag2"
      }
  ]
}
```

### Update Note

This action is used to update a note for malware.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|string|None|True|Note body|None|
|id|integer|None|True|Note ID|None|
|malware_sha256|string|None|True|Malware SHA256|None|
|project_name|string|None|True|Project name|None|
|title|string|None|True|Note title|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|note|Note|True|Updated note|

Example output:

```
{
  "note": {
      "id": 1,
      "project_name": "test",
      "malware_sha256": "31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347",
      "title": "new title",
      "body": "body"
  }
}
```

### Upload File

This action is used to upload a file and create new malware.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|extractor|string|None|False|Extractor name|None|
|file|file|None|True|File for upload|None|
|file_name|string|None|False|File name|None|
|note_body|string|None|False|Note body|None|
|note_title|string|None|False|Note title|None|
|password|string|None|False|Archive password|None|
|project_name|string|None|True|Project name|None|
|store_archive|boolean|None|False|Store archive, true or false|None|
|tags|[]string|None|False|Tags|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|malware|[]Malware|True|New malware|

Example output:

```
{
  "malware": [
      {
          "project_name": "test",
          "id": 1,
          "name": "filename v2",
          "crc32": "B9C5D962",
          "md5": "a1a43a5ee95a91291ff582c7f9ffe24d",
          "sha1": "653a6ef54169396c505123c2882cadea31ccf8e3",
          "sha256": "31246673091f2674b28b06917d868bca638ad3585126a54c7e9d56cb9007c347",
          "sha512": "2275c38346dfa962a71e2ccf8c3bb143d509873d77b8049860aa3621814e0d109bab335929f63eb30ccbce0a0987d04e44a2ecea785d1257f3f5235b729c2af4",
          "size": 11,
          "ssdeep": "3:xipU:xkU",
          "type": "ASCII text, with no line terminators",
          "mime": "text/plain",
          "created_at": "2019-06-23 00:00:18.052132"
      }
  ]
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|credential_secret_key|None|True|Token to authenticate to Viper API|None|
|url|string|None|True|API URL to Viper server e.g. http://example.com:8080/api/v3/|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Binary analysis

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 2.0.0 - Update plugin to use the Viper v3 API

## References

* [Viper](https://viper.li/en/latest/)
* [Viper API](https://viper.li/en/latest/usage/web.html#api)

## Custom Output Types

### Archive

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cls_name|string|True|Compressor class name|
|extensions|[]string|True|Which extension are connected to archive?|
|password|boolean|True|Is password required on archive?|
|title|string|True|Title of compressed file|

### Module

|Name|Type|Required|Description|
|----|----|--------|-----------|
|description|string|False|Description of module|
|name|string|False|Title of module|

### Project

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|False|Project name|

### Analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cmd_line|string|False|Command for running analysis|
|id|integer|False|ID of analysis|
|results|string|False|Result of analysis|
|stored_at|string|False|Datetime when analysis was created|

### Note

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body|string|False|Note description|
|id|integer|False|Note ID|
|title|string|False|Note title|

### Tag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Tag ID|
|tag|string|False|Tag name|

### Malware

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysis_set|[]Analysis|False|Analysis connected with malware|
|crc32|string|False|CRC32 hash|
|created_at|string|False|Date when the file was created|
|id|integer|False|Malware ID|
|md5|string|False|MD5 hash|
|mime|string|False|MIME type|
|name|string|False|Malware name|
|note_set|[]Note|False|Notes added to malware|
|parent|string|False|Parent file name|
|parent_id|string|False|ID of parent file|
|sha1|string|False|SHA1 hash|
|sha256|string|False|SHA256 hash|
|sha512|string|False|SHA512 hash|
|size|integer|False|Size of malware file in bytes|
|ssdeep|string|False|Ssdeep|
|tag_set|[]Tag|False|Tags added to malware|
|type|string|False|Malware type|
