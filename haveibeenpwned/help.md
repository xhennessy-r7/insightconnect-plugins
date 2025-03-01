
# HaveIBeenPwned

## About

[Have I been pwned?](https://haveibeenpwned.com/) is a free [Creative Commons](https://creativecommons.org/licenses/by/4.0/) service that allows you to search across multiple data breaches to see if your username, email address, or password has been compromised.

This plugin utilizes the public [have I been pwned? API](https://haveibeenpwned.com/API/v3). 

## Actions

### Lookup Domain

This action is used to list domain breaches.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|False|Domain to check E.g. adobe.com, google.com etc. If left blank will return the full breach database. Warning: this is very large|None|
|include_unverified|boolean|None|False|If true will include breaches that are unverified (default - false)|None|
|truncate_response|boolean|None|False|If true only name of breach will be shown (default - true)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|Indicates whether or not a breach for the specified domain was found|
|breaches|[]domain|False|List of details for each breach found|

Example output:

```

{
  "found": true,
  "domain": [
    {
      "Title": "Adobe",
      "Name": "Adobe",
      "Domain": "adobe.com",
      "BreachDate": "2013-10-04",
      "AddedDate": "2013-12-04T00:00:00Z",
      "ModifiedDate": "2013-12-04T00:00:00Z",
      "PwnCount": 152445165,
      "Description": "In October 2013, 153 million Adobe accounts were breached with each containing an internal ID, username, email, <em>encrypted</em> password and a password hint in plain text. The password cryptography was poorly done and <a href=\"http://stricture-group.com/files/adobe-top100.txt\" target=\"_blank\" rel=\"noopener\">many were quickly resolved back to plain text</a>. The unencrypted hints also <a href=\"http://www.troyhunt.com/2013/11/adobe-credentials-and-serious.html\" target=\"_blank\" rel=\"noopener\">disclosed much about the passwords</a> adding further to the risk that hundreds of millions of Adobe customers already faced.",
      "DataClasses": [
        "Email addresses",
        "Password hints",
        "Passwords",
        "Usernames"
      ],
      "IsVerified": true,
      "IsFabricated": false,
      "IsSensitive": false,
      "IsActive": true,
      "IsRetired": false,
      "IsSpamList": false,
      "LogoType": "svg"
    }
  ]
}

```

### Lookup Password

This action is used to lookup a password in list of known breached passwords.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|password_to_check|string|None|True|Password to check E.g. 'P@ssw0rd'|None|
|original_password_is_a_hash|boolean|None|True|Whether the password itself is a sha1 hash|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|If true the password was found in the database|

Example output:

```

{
  "found": true
}

```

### Lookup User

This action is used to check an email for compromise.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|breach|string|None|False|Breach Site to check e.g. adobe.com. If blank will check all known breaches|None|
|include_unverified|boolean|None|False|If true will include breaches that are unverified (default - false)|None|
|truncate_response|boolean|None|False|If true only name of breach will be shown (default - true)|None|
|user|string|None|True|Email to check|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|Found|
|breaches|[]domain|False|List of details for each breach found|

Example output:

```

{
  "found": true,
  "breaches": [
    {
      "Title": "000webhost",
      "Name": "000webhost",
      "Domain": "000webhost.com",
      "BreachDate": "2015-03-01",
      "AddedDate": "2015-10-26T23:35:45Z",
      "ModifiedDate": "2017-12-10T21:44:27Z",
      "PwnCount": 14936670,
      "Description": "In approximately March 2015, the free web hosting provider <a href=\"http://www.troyhunt.com/2015/10/breaches-traders-plain-text-passwords.html\" target=\"_blank\" rel=\"noopener\">000webhost suffered a major data breach</a> that exposed almost 15 million customer records. The data was sold and traded before 000webhost was alerted in October. The breach included names, email addresses and plain text passwords.",
      "DataClasses": [
        "Email addresses",
        "IP addresses",
        "Names",
        "Passwords"
      ],
      "IsVerified": true,
      "IsFabricated": false,
      "IsSensitive": false,
      "IsActive": true,
      "IsRetired": false,
      "IsSpamList": false,
      "LogoType": "png"
    },
    {
      "Title": "8tracks",
      "Name": "8tracks",
      "Domain": "8tracks.com",
      "BreachDate": "2017-06-27",
      "AddedDate": "2018-02-16T07:09:30Z",
      "ModifiedDate": "2018-02-16T07:09:30Z",
      "PwnCount": 7990619,
      "Description": "In June 2017, the online playlists service known as <a href=\"https://blog.8tracks.com/2017/06/27/password-security-alert/\" target=\"_blank\" rel=\"noopener\">8Tracks suffered a data breach</a> which impacted 18 million accounts. In their disclosure, 8Tracks advised that &quot;the vector for the attack was an employee's GitHub account, which was not secured using two-factor authentication&quot;. Salted SHA-1 password hashes for users who <em>didn't</em> sign up with either Google or Facebook authentication were also included. The data was provided to HIBP by whitehat security researcher and data analyst Adam Davies and contained almost 8 million unique email addresses.",
      "DataClasses": [
        "Email addresses",
        "Passwords"
      ],
      "IsVerified": true,
      "IsFabricated": false,
      "IsSensitive": false,
      "IsActive": true,
      "IsRetired": false,
      "IsSpamList": false,
      "LogoType": "png"
    }
  ]
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Account validation
* Intelligence

## Versions

* 0.1.0 - Initial plugin
* 0.1.2 - Match schema with spec for output
* 0.1.3 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 2.0.0 - Code overhaul | Port to Python 3
* 3.0.0 - Bug fix where output schema did not match returned API data for Lookup Domain and Lookup User actions | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size
* 3.0.1 - Set user-agent string to Rapid7 InsightConnect | Implement use of Retry-After header for rate limit | Update documentation
* 4.0.0 - Support the v3 API which requires authentication

## References

* [have i been pwned?](https://haveibeenpwned.com/)
* [have i been pwned? API](https://haveibeenpwned.com/API/v3)

## Custom Output Types

### domain

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AddedDate|string|False|The date and time (precision to the minute) the breach was added to the system in ISO 8601 format|
|BreachDate|string|False|The date (with no time) the breach originally occurred on in ISO 8601 format|
|DataClasses|[]string|False|This attribute describes the nature of the data compromised in the breach and contains an alphabetically ordered string array of impacted data classes|
|Description|string|False|Contains an overview of the breach represented in HTML markup. The description may include markup such as emphasis and strong tags as well as hyperlinks|
|Domain|string|False|The domain of the primary website the breach occurred on|
|IsActive|boolean|False|Indicates if the breach investigation is ongoing.|
|IsFabricated|boolean|False|Indicates that the breach is considered fabricated. A fabricated breach is unlikely to have been hacked from the indicated website and usually contains a large amount of manufactured data. However, it still contains legitimate email addresses and asserts that the account owners were compromised in the alleged breach|
|IsRetired|boolean|False|Indicates if the breach has been retired|
|IsSensitive|boolean|False|Indicates if the breach is considered sensitive. The public API will not return any accounts for a breach flagged as sensitive|
|IsSpamList|boolean|False|Indicates if the breach is considered a spam list. This flag has no impact on any other attributes but it means that the data has not come as a result of a security compromise|
|IsVerified|boolean|False|Indicates that the breach is considered verified|
|LogoType|string|False|None|
|ModifiedDate|string|False|The date and time (precision to the minute) the breach was modified in ISO 8601 format|
|Name|string|False|A Pascal-cased name representing the breach which is unique across all other breaches|
|PwnCount|integer|False|The total number of accounts loaded into the system|
|Title|string|False|A descriptive title for the breach suitable for displaying to end users|
