Scope of Lecture:

1. The HTTP Protocol – Basic Concepts
2. HTTP Developer Tools
3. HTML Forms
# Forms can specify the HTTP method for sending the form data

  3.1. HTML Forms: Method GET
  NOTE: Form data is in the URL

index.html content:
<!doctype html>
<html>
<body>
  <form method="get">
    Name: <input type="text" name="name">
    <br /><br />
    <input type="submit" value="Submit">
  </form>
</body>
</html>

  3.2. HTML Forms: Method POST
  NOTE: The HTTP request body holds the submitted form data

index.html content:
<!doctype html>
<html>
<body>
  <form method="post">
    Name: <input type="text" name="name">
    <br /><br />
    <input type="submit" value="Submit">
  </form>
</body>
</html>

POST /index.html HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 10
name=Peter

  3.3. URL Encoded Form Data – Example
  NOTE: File upload fields are not supported (unless multipart encoding is set)

index.html content:
<!doctype html>
<html>
<body>
  <form method="post">
    Name: <input type="text" name="name"/> <br/>
    Age: <input type="password" name="age"/> <br/>
    <input type="submit" />
  </form>
</body>
</html>

POST /index.html HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 23
name=Maria+Smith&age=19 # <--- URL-encoded form data

4. HTTP Request
  4.1. HTTP Request Methods:
  NOTE: CRUD == the four main functions of persistent storage

GET - Retrieve a resource
POST - Create / store a resource
PUT - Update (replace) a resource
DELETE - Delete (remove) a resource
PATCH - Update resource partially (modify)
HEAD - Retrieve the resource's headers
CONNECT
OPTIONS
TRAACE

5. HTTP Response
  5.1. HTTP Response Status Codes

Status Code Action Description:
200 - OK - Successfully retrieved resource
201 - Created - A new resource was created
204 - No Content - Request has nothing to return
301 / 302 - Moved - Moved to another location (redirect)
400 - Bad Request - Invalid request / syntax error
401 / 403 - Unauthorized - Authentication failed / Access denied
404 - Not Found - Invalid resource was requested
409 - Conflict - Conflict was detected, e.g. duplicated email
500 / 503 - Server Error - Internal server error / Service unavailable 

6. URLs and URL Structure

Example: http://mysite.com:8080/demo/index.php?id=27&lang=en#lectures
       Protocol    Host    Port     Path       Query string  Fragment

Uniform Resource Locator (URL)
- Network protocol (http, ftp, https...) – HTTP in most cases
- Host or IP address (softuni.org, gmail.com, 127.0.0.1, web)
- Port (the default port is 80) – integer in the range [0…65535]
- Path (/forum, /path/index.php)
- Query string (?id=27&lang=en)
- Fragment (#slides) – navigate to some section in the page


7. Summary

- HyperText Transfer Protocol
  - Text-based client-server protocol for the Internet
  - Works with message pairs
    * Request: method + headers + body
    * Response: status + headers + body
- The URL parts: protocol, host, port, path, query string and fragment