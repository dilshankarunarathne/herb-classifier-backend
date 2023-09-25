---
title: Herb Classifier API v1.2
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<h1 id="fastapi">Herb Classifier API v1.2</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

- OAuth2 authentication. 

    - Flow: Bear Token

    - Token URL = [http://127.0.0.1:8000/auth/login](http://127.0.0.1:8000/auth/login)


<h1 id="fastapi-auth">/auth</h1>

## Register User

<a id="opIdregister_user_api_auth_register_post"></a>

> Code samples

Curl
```shell
# You can also use wget
curl -X POST /api/auth/register \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json'

```

HTTP
```http
POST /api/auth/register HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

JavaScript
```javascript
const inputBody = '{
  "username": "string",
  "email": "string",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json'
};

fetch('/api/auth/register',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

Ruby 
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/auth/register',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

r = requests.post('/api/auth/register', headers = headers)

print(r.json())

```

PHP
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/auth/register', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

Java
```java
URL obj = new URL("/api/auth/register");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

Go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/auth/register", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/auth/register`

*Register User*

The endpoint for registering a new user

Args:
    username (str): the username of the user
    email (str): the email of the user
    password (str): the password of the user
    is_admin (bool): whether the user is an admin

Returns:
    (UserInDB) The user that was registered

Raises:
    HTTPException: if the username already exists

> Body parameter

```yaml
username: string
email: string
password: string

```

<h3 id="register_user_api_auth_register_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|is_admin|query|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="register_user_api_auth_register_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="register_user_api_auth_register_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## User Login 

<a id="opIdlogin_for_access_token_api_auth_login_post"></a>

> Code samples

Curl
```shell
# You can also use wget
curl -X POST /api/auth/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json'

```

HTTP
```http
POST /api/auth/login HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

JavaScript
```javascript
const inputBody = '{
  "grant_type": "string",
  "username": "string",
  "password": "string",
  "scope": "",
  "client_id": "string",
  "client_secret": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json'
};

fetch('/api/auth/login',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

Ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/auth/login',
  params: {
  }, headers: headers

p JSON.parse(result)

```

Python
```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

r = requests.post('/api/auth/login', headers = headers)

print(r.json())

```

PHP
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/auth/login', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

Java
```java
URL obj = new URL("/api/auth/login");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

Go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/auth/login", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/auth/login`

*Login For Access Token*

The endpoint for logging in a user

Args:
    form_data (OAuth2PasswordRequestForm): the form data for the user

Returns:
    (dict) The access token for the user

Raises:
    HTTPException: if the username or password is incorrect

> Body parameter

```yaml
grant_type: string
username: string
password: string
scope: ""
client_id: string
client_secret: string

```

<h3 id="login_for_access_token_api_auth_login_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|


> Example responses

> 200 Response

```json
token: <Bearer Token>
```

<h3 id="login_for_access_token_api_auth_login_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="login_for_access_token_api_auth_login_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## User Logout

<a id="opIdlogout_api_auth_logout_post"></a>

> Code samples

Curl
```shell
# You can also use wget
curl -X POST /api/auth/logout \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

HTTP
```http
POST /api/auth/logout HTTP/1.1

Accept: application/json

```

JavaScript
```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/api/auth/logout',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

Ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/api/auth/logout',
  params: {
  }, headers: headers

p JSON.parse(result)

```

Python
```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/api/auth/logout', headers = headers)

print(r.json())

```

PHP
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/auth/logout', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

Java
```java
URL obj = new URL("/api/auth/logout");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

Go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/auth/logout", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/auth/logout`

*Logout*

The endpoint for logging out a user

Args:
    token (oauth2 bearer token): the token for the user

Returns:
    (dict) The message for logging out

> Example responses

> 200 Response

```json
message: Logged out successfully
```

<h3 id="logout_api_auth_logout_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|

<h3 id="logout_api_auth_logout_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

<h1 id="fastapi-herb">/herb</h1>

## Search Herb by Disease

<a id="opIdsearch_herb_by_disease_api_herb_search_herbs_post"></a>

> Code samples

Curl
```shell
# You can also use wget
curl -X POST /api/herb/search-herbs \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

HTTP
```http
POST /api/herb/search-herbs HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

JavaScript
```javascript
const inputBody = '{
  "disease": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/api/herb/search-herbs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

Ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/api/herb/search-herbs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

Python
```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/api/herb/search-herbs', headers = headers)

print(r.json())

```

PHP
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/herb/search-herbs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

Java
```java
URL obj = new URL("/api/herb/search-herbs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

Go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/herb/search-herbs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/herb/search-herbs`

*Search Herb By Disease*

The endpoint for searching a herb by disease

Args:
    disease (str): the disease to search for
    token (oauth2 bearer token): the token for the user

Returns:
    (str) The herb for the disease

> Body parameter

```yaml
disease: string

```

<h3 id="search_herb_by_disease_api_herb_search_herbs_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|


> Example responses

> 200 Response

```json
{HERB1, HERB2}
```

<h3 id="search_herb_by_disease_api_herb_search_herbs_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="search_herb_by_disease_api_herb_search_herbs_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## Search Herb by Disease

<a id="opIdsearch_herb_by_disease_api_herb_search_diseases_post"></a>

> Code samples

Curl
```shell
# You can also use wget
curl -X POST /api/herb/search-diseases \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

HTTP
```http
POST /api/herb/search-diseases HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

JavaScript
```javascript
const inputBody = '{
  "herb": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/api/herb/search-diseases',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

Ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/api/herb/search-diseases',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/api/herb/search-diseases', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/herb/search-diseases', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/herb/search-diseases");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/herb/search-diseases", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/herb/search-diseases`

*Search Herb By Disease*

The endpoint for searching a disease by herb

Args:
    herb (str): the herb to search for
    token (oauth2 bearer token): the token for the user

Returns:
    (str) The disease for the herb

> Body parameter

```yaml
herb: string

```

<h3 id="search_herb_by_disease_api_herb_search_diseases_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_search_herb_by_disease_api_herb_search_diseases_post](#schemabody_search_herb_by_disease_api_herb_search_diseases_post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="search_herb_by_disease_api_herb_search_diseases_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="search_herb_by_disease_api_herb_search_diseases_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

<h1 id="fastapi-disease">disease</h1>

## search_disease_api_disease_search_post

<a id="opIdsearch_disease_api_disease_search_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/disease/search \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```http
POST /api/disease/search HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

```javascript
const inputBody = '{
  "disease": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/api/disease/search',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/api/disease/search',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/api/disease/search', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/disease/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/disease/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/disease/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/disease/search`

*Search Disease*

The endpoint for searching a disease

Args:
    disease (str): the disease to search for
    token (oauth2 bearer token): the token for the user

Returns:
    (str) The disease details

Raises:
    HTTPException: if the user is not logged in

> Body parameter

```yaml
disease: string

```

<h3 id="search_disease_api_disease_search_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_search_disease_api_disease_search_post](#schemabody_search_disease_api_disease_search_post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="search_disease_api_disease_search_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="search_disease_api_disease_search_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

<h1 id="fastapi-location">location</h1>

## get_location_for_herb_api_location_get_location_post

<a id="opIdget_location_for_herb_api_location_get_location_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/location/get-location \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```http
POST /api/location/get-location HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

```javascript
const inputBody = '{
  "herb": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/api/location/get-location',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/api/location/get-location',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/api/location/get-location', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/location/get-location', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/location/get-location");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/location/get-location", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/location/get-location`

*Get Location For Herb*

The endpoint for getting location for a herb
Args:
    herb (str): the herb to search for
    token (oauth2 bearer token): the token for the user

Returns:
    (str) The location for the herb

Raises:
    HTTPException: if the user is not logged in

> Body parameter

```yaml
herb: string

```

<h3 id="get_location_for_herb_api_location_get_location_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_get_location_for_herb_api_location_get_location_post](#schemabody_get_location_for_herb_api_location_get_location_post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_location_for_herb_api_location_get_location_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_location_for_herb_api_location_get_location_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

## add_new_location_api_location_add_location_post

<a id="opIdadd_new_location_api_location_add_location_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/location/add-location \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```http
POST /api/location/add-location HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

```javascript
const inputBody = '{
  "lon": 0,
  "lat": 0,
  "herb": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/api/location/add-location',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/api/location/add-location',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/api/location/add-location', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/location/add-location', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/location/add-location");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/location/add-location", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/location/add-location`

*Add New Location*

The endpoint for adding a new location for a herb 
Args:
    lon (float): the longitude of the location
    lat (float): the latitude of the location
    herb (str): the herb to add the location for
    token (oauth2 bearer token): the token for the user

Returns:
    (str) A message indicating the success of the operation

Raises:
    HTTPException: if the user is not logged in

> Body parameter

```yaml
lon: 0
lat: 0
herb: string

```

<h3 id="add_new_location_api_location_add_location_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_add_new_location_api_location_add_location_post](#schemabody_add_new_location_api_location_add_location_post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="add_new_location_api_location_add_location_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The requested page was not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="add_new_location_api_location_add_location_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

# Schemas

<h2 id="tocS_Body_add_new_location_api_location_add_location_post">Body_add_new_location_api_location_add_location_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_add_new_location_api_location_add_location_post"></a>
<a id="schema_Body_add_new_location_api_location_add_location_post"></a>
<a id="tocSbody_add_new_location_api_location_add_location_post"></a>
<a id="tocsbody_add_new_location_api_location_add_location_post"></a>

```json
{
  "lon": 0,
  "lat": 0,
  "herb": "string"
}

```

Body_add_new_location_api_location_add_location_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lon|number|true|none|none|
|lat|number|true|none|none|
|herb|string|true|none|none|

<h2 id="tocS_Body_get_location_for_herb_api_location_get_location_post">Body_get_location_for_herb_api_location_get_location_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_get_location_for_herb_api_location_get_location_post"></a>
<a id="schema_Body_get_location_for_herb_api_location_get_location_post"></a>
<a id="tocSbody_get_location_for_herb_api_location_get_location_post"></a>
<a id="tocsbody_get_location_for_herb_api_location_get_location_post"></a>

```json
{
  "herb": "string"
}

```

Body_get_location_for_herb_api_location_get_location_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|herb|string|true|none|none|

<h2 id="tocS_Body_login_for_access_token_api_auth_login_post">Body_login_for_access_token_api_auth_login_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_login_for_access_token_api_auth_login_post"></a>
<a id="schema_Body_login_for_access_token_api_auth_login_post"></a>
<a id="tocSbody_login_for_access_token_api_auth_login_post"></a>
<a id="tocsbody_login_for_access_token_api_auth_login_post"></a>

```json
{
  "grant_type": "string",
  "username": "string",
  "password": "string",
  "scope": "",
  "client_id": "string",
  "client_secret": "string"
}

```

Body_login_for_access_token_api_auth_login_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|grant_type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|none|none|
|password|string|true|none|none|
|scope|string|false|none|none|
|client_id|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|client_secret|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_Body_register_user_api_auth_register_post">Body_register_user_api_auth_register_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_register_user_api_auth_register_post"></a>
<a id="schema_Body_register_user_api_auth_register_post"></a>
<a id="tocSbody_register_user_api_auth_register_post"></a>
<a id="tocsbody_register_user_api_auth_register_post"></a>

```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}

```

Body_register_user_api_auth_register_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|none|none|
|email|string|true|none|none|
|password|string|true|none|none|

<h2 id="tocS_Body_search_disease_api_disease_search_post">Body_search_disease_api_disease_search_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_search_disease_api_disease_search_post"></a>
<a id="schema_Body_search_disease_api_disease_search_post"></a>
<a id="tocSbody_search_disease_api_disease_search_post"></a>
<a id="tocsbody_search_disease_api_disease_search_post"></a>

```json
{
  "disease": "string"
}

```

Body_search_disease_api_disease_search_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease|string|true|none|none|

<h2 id="tocS_Body_search_herb_by_disease_api_herb_search_diseases_post">Body_search_herb_by_disease_api_herb_search_diseases_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_search_herb_by_disease_api_herb_search_diseases_post"></a>
<a id="schema_Body_search_herb_by_disease_api_herb_search_diseases_post"></a>
<a id="tocSbody_search_herb_by_disease_api_herb_search_diseases_post"></a>
<a id="tocsbody_search_herb_by_disease_api_herb_search_diseases_post"></a>

```json
{
  "herb": "string"
}

```

Body_search_herb_by_disease_api_herb_search_diseases_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|herb|string|true|none|none|

<h2 id="tocS_Body_search_herb_by_disease_api_herb_search_herbs_post">Body_search_herb_by_disease_api_herb_search_herbs_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_search_herb_by_disease_api_herb_search_herbs_post"></a>
<a id="schema_Body_search_herb_by_disease_api_herb_search_herbs_post"></a>
<a id="tocSbody_search_herb_by_disease_api_herb_search_herbs_post"></a>
<a id="tocsbody_search_herb_by_disease_api_herb_search_herbs_post"></a>

```json
{
  "disease": "string"
}

```

Body_search_herb_by_disease_api_herb_search_herbs_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|disease|string|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

