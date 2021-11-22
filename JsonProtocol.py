import json


class Protocol:
    @staticmethod
    def message(user: str, message: str) -> json:
        return json.dumps([{"send": {"user": user, "message": message}}])

    @staticmethod
    def decode_json(message: json):
        return json.loads(message)
