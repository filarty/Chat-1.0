import json


class Protocol:
    @staticmethod
    def message(user: str, message: str) -> json:
        return json.dumps([{"send": {"user": user, "message": message}}])

    @staticmethod
    def decode_json(message: json) -> json:
        return json.loads(message)

    @staticmethod
    def update_json(info: dict, obj: json, key: str) -> json:
        file = json.loads(obj)[0]
        if key in file:
            file[key].update(info)
        else:
            file.update(info)
        return json.dumps([file])

    @staticmethod
    def add_user(users: list[str]) -> json:
        return json.dumps([{"add": users}])


    @staticmethod
    def login(name: str) -> json:
        return json.dumps({"login": name})