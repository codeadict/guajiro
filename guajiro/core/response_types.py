import json
import enum

#TODO: Define XML and YAML response

class ResponseType(enum.Enum):

    TEXT = {
        "headers": {
            "Content-Type": "text/plain",
        },
    }

    HTML = {
        "headers": {
            "Content-Type": "text/html",
        }
    }

    JSON = {
        "handler": json.dumps,
        "headers": {
            "Content-Type": "application/json"
        },
    }