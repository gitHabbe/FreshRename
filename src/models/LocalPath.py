import json


class LocalPath:
    filePath = "./private/cache.json"

    def __init__(self):
        self.__jsonData = self.readPath()

    def readPath(self):
        with open(self.filePath, "r") as f:
            __jsonData = json.load(f)
        return __jsonData

    def path(self) -> str:
        cachedPath = self.__jsonData["last_path"]
        return cachedPath

    def savePath(self, path: str) -> str:
        self.__jsonData["last_path"] = path
        with open(self.filePath, "w") as f:
            json.dump(self.__jsonData, f)
        return path
