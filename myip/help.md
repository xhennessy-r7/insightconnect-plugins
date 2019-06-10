
# MyIP

## About

[MyIP](https://www.myip.com) is a free service which returns your public routable IP address.
This plugin utilizes the [MyIP API](https://www.myip.com/api-docs/).

## Actions

### IP Address Lookup

This action is used to obtain your public routable IP address.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cc|string|True|Country code e.g. US|
|ip|string|True|The public routable IP address|
|country|string|True|Country name|

Example output:

```

{
  "ip": "50.82.223.224",
  "country": "United States",
  "cc": "US"
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin

## Workflows

Examples:

* Network

## References

* [MyIP](https://www.myip.com)
* [MyIP API](https://www.myip.com/api-docs/)
