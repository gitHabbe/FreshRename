import json


class LocalPath:
    file_path = "./private/cache.json"

    def __init__(self):
        self.__jsonData = self.read_path()

    def read_path(self):
        with open(self.file_path, "r") as f:
            __jsonData = json.load(f)
        return __jsonData

    def path(self) -> str:
        cached_path = self.__jsonData["last_path"]
        return cached_path

    def save_path(self, path: str) -> str:
        self.__jsonData["last_path"] = path
        with open(self.file_path, "w") as f:
            json.dump(self.__jsonData, f)
        return path
