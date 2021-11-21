import json


class LocalPath:
    with open("../../cache.json", "r") as f:
        __jsonData = json.load(f)

    def path(self):
        cachedPath = self.__jsonData["last_path"]
        return cachedPath

    def savePath(self, path: str):
        self.__jsonData["last_path"] = path
        with open("cache.json", "w") as f:
            json.dump(self.__jsonData, f)
        return path
