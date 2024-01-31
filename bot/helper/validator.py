from jsonschema import validate


[pyrogram]
api_id = 17432758
api_hash = "c9e31fda0ce722e3f3033a9d4f140783"
bot_token = "6569801576:AAGO1V6U0Gcy002psWagco7DH06_cEnWYk4"
session_string = "1BVn1-ABCD1234efgh5678IJKLmnoPQRsTUVwxyZ"
sudo_users = [6103642139]

[[chats]]
from = ""
to = "123456789"

[[chats]]
from = [-1001642374850]
to = -1002067899187

[[chats]]
from = "123456789"
to = ["123456789", "123456789"]

[[chats]]
from = ["123456789", "123456789"]
to = ["123456789", "123456789"]


CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "pyrogram": {
            "type": "object",
            "properties": {
                "api_id": {"type": "integer"},
                "api_hash": {"type": "string"},
                "bot_token": {"type": "string"},
                "session_string": {"type": "string"},
                "sudo_users": {"type": "array", "items": {"type": "integer"}},
            },
            "required": [
                "api_id",
                "api_hash",
            ],
            "anyOf": [
                {"required": ["bot_token"]},
                {"required": ["session_string"]},
            ],
        },
        "chats": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "from": {
                        "type": ["string", "array", "integer"],
                        "items": {"type": ["string", "integer"]},
                    },
                    "to": {
                        "type": ["string", "array", "integer"],
                        "items": {"type": ["string", "integer"]},
                    },
                    "replace": {
                        "type": "object",
                        "patternProperties": {
                            "^[a-zA-Z0-9_]+$": {"type": "string"}
                        },
                    },
                },
                "required": ["from", "to"],
            },
            "minItems": 1,
        },
    },
    "required": ["pyrogram", "chats"],
}


def validate_config(config):
    validate(config, CONFIG_SCHEMA)
    
