# Whats this Guajiro stuff?

[![Guajiro](artwork/logo.png?raw=true)](http://github.com/codeadict/guajiro) 

**Guajiro** is a word used to designate people from countryside in Cuba.
They are usually very hardworking people with lot of culture and traditions.
What you’re more likely to see when you search “guajiro” are Cuban cowboys wearing 
hand made hat, riding horses and smoking tobaccos.

### Overview

The aim of this project is to make a insanely fast high-productivity web services
framework built with python 3 honouring this hardworking people that every day work hard 
in the land, but this time in the land of coding.

## Install

The quick way::

    pip install guajiro

## Usage
```python3
from guajiro import Service, View
from guajiro import ResponseType


class HelloResource(View):

    def get(self, request) -> ResponseType.JSON:
        return {"hello": "world"}

if __name__ == "__main__":
    service = Service()
    
    resource = HelloResource()
    resource.append_to(service)

    service.run("localhost", 3000)
```

Finally we can test by hitting our created endpoint:

```bash
$ curl -i http://localhost:3000/hello/

HTTP/1.1 200 OK
CONTENT-TYPE: application/json; charset=utf-8
CONTENT-LENGTH: 18
DATE: Sun, 20 Mar 2016 21:42:10 GMT
SERVER: Python/3.5 aiohttp/0.21.4

{"hello": "world"}
```

##Authors:

  * Dairon Medina C. (dairon.medina@gmail.com)

##Found a bug?
  Awesome, let me know! Send a pull request or a patch. Ask! I'm here to help and will respond to all filed issues.